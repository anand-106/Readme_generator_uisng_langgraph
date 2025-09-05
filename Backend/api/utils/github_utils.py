import os
import shutil
from git import Repo
from urllib.parse import urlparse
from fastapi import HTTPException
import tempfile
import requests
import base64
import httpx
import asyncio
import time
from typing import Optional

from bson import ObjectId


REPO_SIZE_LIMIT = 500 * 1024 * 1024

def get_directory_size(directory_path: str) -> int:
    """Calculate total size of directory in bytes."""
    total_size = 0
    try:
        for dirpath, dirnames, filenames in os.walk(directory_path):
            for filename in filenames:
                filepath = os.path.join(dirpath, filename)
                try:
                    if os.path.exists(filepath):
                        total_size += os.path.getsize(filepath)
                except (OSError, FileNotFoundError):
                    continue  # Skip files that can't be accessed
    except Exception as e:
        print(f"Warning: Could not calculate directory size: {e}")
        return 0
    return total_size

async def check_repo_size_with_retry(url: str, token: str = None, max_retries: int = 3) -> Optional[int]:
    """
    Check repository size with retry logic for rate limiting.
    Returns None if rate limited and should skip size check.
    """
    try:
        url_parts = url.replace("https://github.com/", "").replace(".git", "").split("/")
        if len(url_parts) < 2:
            raise HTTPException(status_code=400, detail="Invalid GitHub repository URL")
        
        owner, repo = url_parts[0], url_parts[1]
        api_url = f"https://api.github.com/repos/{owner}/{repo}"
        
        headers = {"Accept": "application/vnd.github+json"}
        if token:
            headers["Authorization"] = f"Bearer {token}"
        
        for attempt in range(max_retries):
            try:
                async with httpx.AsyncClient(timeout=10.0) as client:
                    response = await client.get(api_url, headers=headers)
                    
                    # Handle rate limiting
                    if response.status_code == 403:
                        error_data = response.json()
                        if "rate limit" in error_data.get("message", "").lower():
                            if attempt < max_retries - 1:
                                # Exponential backoff: 2, 4, 8 seconds
                                wait_time = 2 ** (attempt + 1)
                                print(f"Rate limited. Retrying in {wait_time} seconds... (attempt {attempt + 1}/{max_retries})")
                                await asyncio.sleep(wait_time)
                                continue
                            else:
                                # After all retries, return None to skip size check
                                print("⚠️ Rate limited after all retries. Skipping size check and proceeding with clone.")
                                return None
                        else:
                            raise HTTPException(status_code=403, detail=error_data.get("message", "Access forbidden"))
                    
                    if response.status_code == 404:
                        raise HTTPException(status_code=404, detail="Repository not found")
                    elif response.status_code != 200:
                        raise HTTPException(status_code=response.status_code, detail=f"Failed to fetch repository info: {response.text}")
                    
                    repo_data = response.json()
                    repo_size_kb = repo_data.get("size", 0)
                    repo_size_bytes = repo_size_kb * 1024
                    
                    if repo_size_bytes > REPO_SIZE_LIMIT:
                        size_mb = repo_size_bytes / (1024 * 1024)
                        limit_mb = REPO_SIZE_LIMIT / (1024 * 1024)
                        raise HTTPException(
                            status_code=413, 
                            detail=f"Repository size ({size_mb:.1f}MB) exceeds the maximum allowed size ({limit_mb:.1f}MB)"
                        )
                    
                    print(f"✅ Repository size check passed: {repo_size_bytes / (1024 * 1024):.1f}MB")
                    return repo_size_bytes
                    
            except httpx.TimeoutException:
                if attempt < max_retries - 1:
                    print(f"Timeout occurred. Retrying... (attempt {attempt + 1}/{max_retries})")
                    await asyncio.sleep(1)
                    continue
                else:
                    print("⚠️ Timeout after all retries. Skipping size check and proceeding with clone.")
                    return None
            except httpx.RequestError as e:
                if attempt < max_retries - 1:
                    print(f"Network error: {e}. Retrying... (attempt {attempt + 1}/{max_retries})")
                    await asyncio.sleep(1)
                    continue
                else:
                    print(f"⚠️ Network error after all retries: {e}. Skipping size check and proceeding with clone.")
                    return None
                    
    except HTTPException:
        raise
    except Exception as e:
        print(f"⚠️ Unexpected error during size check: {e}. Skipping size check and proceeding with clone.")
        return None

# Backwards compatibility wrapper
async def check_repo_size(url: str, token: str = None) -> int:
    """
    Backwards compatible wrapper that either checks size or proceeds if rate limited.
    """
    result = await check_repo_size_with_retry(url, token)
    if result is None:
        # Size check was skipped due to rate limiting - proceed with clone
        print("📋 Size check skipped due to API limitations. Repository will be cloned directly.")
        return 0  # Return 0 to indicate size check was skipped but proceed
    return result

def clean_mongo_doc(doc: dict) -> dict:
    """
    Convert MongoDB doc to safe dict (ObjectId -> str).
    """
    out = {}
    for k, v in doc.items():
        if isinstance(v, ObjectId):
            out[k] = str(v)
        else:
            out[k] = v
    return out


async def clone_repo(url: str, token: str = None)->str:
    # Check repository size before cloning (with rate limit handling)
    size_check_result = await check_repo_size(url, token)
    
    try:
        requests.get("https://github.com", timeout=5)
        print("Network access to GitHub is OK")
    except Exception as e:
        print(f"Network access to GitHub failed: {e}")

    tmp_dir = tempfile.mkdtemp(prefix="repo_")

    try:
        # Clone with shallow depth for efficiency
        Repo.clone_from(url, tmp_dir, depth=1)
        
        # If size check was skipped due to rate limiting, do a post-clone size check
        if size_check_result == 0:  # Size check was skipped
            repo_size = get_directory_size(tmp_dir)
            if repo_size > REPO_SIZE_LIMIT:
                shutil.rmtree(tmp_dir, ignore_errors=True)
                size_mb = repo_size / (1024 * 1024)
                limit_mb = REPO_SIZE_LIMIT / (1024 * 1024)
                raise HTTPException(
                    status_code=413,
                    detail=f"Repository size ({size_mb:.1f}MB) exceeds the maximum allowed size ({limit_mb:.1f}MB)"
                )
            print(f"✅ Post-clone size check passed: {repo_size / (1024 * 1024):.1f}MB")
        
        print(f"Repo cloned successfully at {tmp_dir} (shallow clone)")
        return tmp_dir
    except HTTPException:
        # Re-raise HTTP exceptions (size limit exceeded)
        raise
    except Exception as e:
        shutil.rmtree(tmp_dir, ignore_errors=True)
        raise Exception(f"Failed to clone repo: {e}")
    
async def webhook_clone_repo(url:str,token:str)->str:
    # Check repository size before cloning (with rate limit handling)
    size_check_result = await check_repo_size(url, token)
    
    try:
        requests.get("https://github.com", timeout=5)
        print("Network access to GitHub is OK")
    except Exception as e:
        print(f"Network access to GitHub failed: {e}")

    tmp_dir = tempfile.mkdtemp(prefix="repo_")
    
    try:
        url_parsed = urlparse(url)
        authenticated_url = f"https://{token}@{url_parsed.netloc}{url_parsed.path}"
        
        # Clone with shallow depth for efficiency
        Repo.clone_from(authenticated_url, tmp_dir, depth=1)
        
        # If size check was skipped due to rate limiting, do a post-clone size check
        if size_check_result == 0:  # Size check was skipped
            repo_size = get_directory_size(tmp_dir)
            if repo_size > REPO_SIZE_LIMIT:
                shutil.rmtree(tmp_dir, ignore_errors=True)
                size_mb = repo_size / (1024 * 1024)
                limit_mb = REPO_SIZE_LIMIT / (1024 * 1024)
                raise HTTPException(
                    status_code=413,
                    detail=f"Repository size ({size_mb:.1f}MB) exceeds the maximum allowed size ({limit_mb:.1f}MB)"
                )
            print(f"✅ Post-clone size check passed: {repo_size / (1024 * 1024):.1f}MB")
        
        print(f"✅ Repo cloned successfully at {tmp_dir} (shallow clone)")
        return tmp_dir
    except HTTPException:
        # Re-raise HTTP exceptions (size limit exceeded)
        raise
    except Exception as e:
        shutil.rmtree(tmp_dir, ignore_errors=True)
        raise Exception(f"❌ Failed to clone repo: {e}")


async def get_existing_readme_filename( repo: str, token: str) -> str:
    url = f"https://api.github.com/repos/{repo}/contents"
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json"
    }

    async with httpx.AsyncClient() as client:
        res = await client.get(url, headers=headers)
        if res.status_code != 200:
            raise Exception(f"Failed to fetch contents: {res.json()}")

        files = res.json()
        for file in files:
            if file["name"].lower() == "readme.md":
                
                return file["name"] 

    return "README.md"

async def update_github_readme(file_name:str,repo_full_name:str,readme_text:str,access_token:str):
    
    
    async with httpx.AsyncClient() as client:
    
        get_url = f'https://api.github.com/repos/{repo_full_name}/contents/{file_name}'
        
        headers = {
                "Authorization": f"Bearer {access_token}",
                "Accept": "application/vnd.github+json"
            }
        
        get_res = await client.get(get_url,headers=headers)
        
        if get_res.status_code == 200:
            sha = get_res.json()["sha"]
        
        elif get_res.status_code == 404:
            sha = None
        else:
            raise HTTPException(status_code=500,detail="failed to fetch readme.md")
        
        put_payload={
            "message":"readme update by AI",
            "content":base64.b64encode(readme_text.encode('utf-8')).decode('utf-8'),
            "branch":"main"
        }
        
        if sha:
            put_payload["sha"]=sha
        
        put_res = await client.put(get_url,headers=headers,json=put_payload)
        
        if put_res.status_code >= 400:
            raise HTTPException(status_code=put_res.status_code, detail=f"Failed to update README.md: {put_res.text}")

        return put_res.json()
        
     
