import os
import shutil
from git import Repo
from urllib.parse import urlparse
from fastapi import HTTPException
import tempfile
import requests
import base64
import httpx
import time
import subprocess

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

def safe_clone_with_size_monitoring(url: str, tmp_dir: str, token: str = None, timeout: int = 300) -> bool:
    """
    Clone repository with real-time size monitoring.
    Returns True if successful, raises HTTPException if size limit exceeded.
    """
    try:
        # Prepare git command
        if token:
            url_parsed = urlparse(url)
            authenticated_url = f"https://{token}@{url_parsed.netloc}{url_parsed.path}"
        else:
            authenticated_url = url
            
        # Use git command directly for better control
        git_cmd = [
            "git", "clone", "--depth", "1", "--progress",
            authenticated_url, tmp_dir
        ]
        
        print(f"🔄 Starting monitored clone of repository...")
        
        # Start the git clone process
        process = subprocess.Popen(
            git_cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            universal_newlines=True,
            bufsize=1
        )
        
        # Monitor the process and directory size
        start_time = time.time()
        last_size_check = 0
        
        while process.poll() is None:  # While process is running
            current_time = time.time()
            
            # Check timeout
            if current_time - start_time > timeout:
                process.terminate()
                process.wait()
                raise HTTPException(status_code=408, detail=f"Repository clone timed out after {timeout} seconds")
            
            # Check size every 2 seconds
            if current_time - last_size_check > 2:
                if os.path.exists(tmp_dir):
                    current_size = get_directory_size(tmp_dir)
                    if current_size > REPO_SIZE_LIMIT:
                        # Terminate the clone process
                        process.terminate()
                        process.wait()
                        shutil.rmtree(tmp_dir, ignore_errors=True)
                        
                        size_mb = current_size / (1024 * 1024)
                        limit_mb = REPO_SIZE_LIMIT / (1024 * 1024)
                        raise HTTPException(
                            status_code=413,
                            detail=f"Repository size ({size_mb:.1f}MB) exceeds the maximum allowed size ({limit_mb:.1f}MB)"
                        )
                    
                    if current_size > 0:  # Only print if we have some data
                        print(f"📊 Clone progress: {current_size / (1024 * 1024):.1f}MB")
                
                last_size_check = current_time
            
            time.sleep(0.5)  # Small delay to prevent excessive CPU usage
        
        # Check final return code
        return_code = process.returncode
        if return_code != 0:
            raise Exception(f"Git clone failed with return code {return_code}")
        
        # Final size check
        final_size = get_directory_size(tmp_dir)
        if final_size > REPO_SIZE_LIMIT:
            size_mb = final_size / (1024 * 1024)
            limit_mb = REPO_SIZE_LIMIT / (1024 * 1024)
            raise HTTPException(
                status_code=413,
                detail=f"Repository size ({size_mb:.1f}MB) exceeds the maximum allowed size ({limit_mb:.1f}MB)"
            )
        
        print(f"✅ Clone completed successfully: {final_size / (1024 * 1024):.1f}MB")
        return True
        
    except HTTPException:
        raise
    except subprocess.TimeoutExpired:
        raise HTTPException(status_code=408, detail="Repository clone timed out")
    except Exception as e:
        raise Exception(f"Failed to clone repository: {str(e)}")

# Old API-based size checking removed due to GitHub rate limiting issues
# Now using real-time monitoring during clone process instead

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


async def clone_repo(url: str, token: str = None) -> str:
    """
    Clone repository with real-time size monitoring (no API dependency).
    """
    try:
        requests.get("https://github.com", timeout=5)
        print("Network access to GitHub is OK")
    except Exception as e:
        print(f"Network access to GitHub failed: {e}")

    tmp_dir = tempfile.mkdtemp(prefix="repo_")

    try:
        # Use our safe clone method with size monitoring
        safe_clone_with_size_monitoring(url, tmp_dir, token)
        print(f"✅ Repo cloned successfully at {tmp_dir} (shallow clone)")
        return tmp_dir
    except HTTPException:
        # Re-raise HTTP exceptions (size limit exceeded, timeout)
        shutil.rmtree(tmp_dir, ignore_errors=True)
        raise
    except Exception as e:
        shutil.rmtree(tmp_dir, ignore_errors=True)
        raise Exception(f"Failed to clone repo: {e}")
    
async def webhook_clone_repo(url: str, token: str) -> str:
    """
    Clone repository with real-time size monitoring (no API dependency).
    """
    try:
        requests.get("https://github.com", timeout=5)
        print("Network access to GitHub is OK")
    except Exception as e:
        print(f"Network access to GitHub failed: {e}")

    tmp_dir = tempfile.mkdtemp(prefix="repo_")
    
    try:
        # Use our safe clone method with size monitoring
        safe_clone_with_size_monitoring(url, tmp_dir, token)
        print(f"✅ Repo cloned successfully at {tmp_dir} (shallow clone)")
        return tmp_dir
    except HTTPException:
        # Re-raise HTTP exceptions (size limit exceeded, timeout)
        shutil.rmtree(tmp_dir, ignore_errors=True)
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
        
     
