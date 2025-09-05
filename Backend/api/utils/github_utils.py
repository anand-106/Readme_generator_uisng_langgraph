import os
import shutil
from git import Repo
from urllib.parse import urlparse
from fastapi import HTTPException
import tempfile
import requests
import base64
import httpx


from bson import ObjectId


REPO_SIZE_LIMIT = 500 * 1024 * 1024

async def check_repo_size(url: str, token: str = None) -> int:
   
    try:
        
        url_parts = url.replace("https://github.com/", "").replace(".git", "").split("/")
        if len(url_parts) < 2:
            raise HTTPException(status_code=400, detail="Invalid GitHub repository URL")
        
        owner, repo = url_parts[0], url_parts[1]
        api_url = f"https://api.github.com/repos/{owner}/{repo}"
        
        headers = {"Accept": "application/vnd.github+json"}
        if token:
            headers["Authorization"] = f"Bearer {token}"
        
        async with httpx.AsyncClient() as client:
            response = await client.get(api_url, headers=headers)
            
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
            
            print(f"Repository size check passed: {repo_size_bytes / (1024 * 1024):.1f}MB")
            return repo_size_bytes
            
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to check repository size: {str(e)}")

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
    # Check repository size before cloning
    await check_repo_size(url, token)

    try:
        requests.get("https://github.com", timeout=5)
        print("Network access to GitHub is OK")
    except Exception as e:
        print(f"Network access to GitHub failed: {e}")

    tmp_dir = tempfile.mkdtemp(prefix="repo_")

    try:
        Repo.clone_from(url, tmp_dir, depth=1)
        print(f"Repo cloned successfully at {tmp_dir} (shallow clone)")
        return tmp_dir
    except Exception as e:
        shutil.rmtree(tmp_dir,ignore_errors=False)
        raise Exception(f"Failed to clone repo: {e}")
    
async def webhook_clone_repo(url:str,token:str)->str:
   
    await check_repo_size(url, token)
    
    try:
        requests.get("https://github.com", timeout=5)
        print("Network access to GitHub is OK")
    except Exception as e:
        print(f"Network access to GitHub failed: {e}")

    tmp_dir = tempfile.mkdtemp(prefix="repo_")
    
    try:
        url_parsed = urlparse(url)
        
        authenticated_url = f"https://{token}@{url_parsed.netloc}{url_parsed.path}"
        
        Repo.clone_from(authenticated_url, tmp_dir, depth=1)
        
        print(f"✅ Repo cloned successfully at {tmp_dir} (shallow clone)")
        return tmp_dir
    except Exception as e:
        
        shutil.rmtree(tmp_dir,ignore_errors=True)
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
        
     
