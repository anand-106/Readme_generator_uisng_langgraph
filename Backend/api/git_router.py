import httpx
import os
from pprint import pprint
from dotenv import load_dotenv
from fastapi import APIRouter, HTTPException,Request
from fastapi.responses import RedirectResponse
from .model import GithubUserResponse,WebHookRequest
from agent.agent import webhook_pipeline
from .utils.github_utils import get_existing_readme_filename,update_github_readme
from fastapi.concurrency import run_in_threadpool


git_router = APIRouter(prefix="/api/github",tags=["Github"])

load_dotenv()


@git_router.get("/auth/callback")
async def github_callback(code:str):

    GITHUB_CLIENT_ID = os.getenv("GITHUB_CLIENT_ID")
    GITHUB_CLIENT_SECRET = os.getenv("GITHUB_CLIENT_SECRET")
    # print(GITHUB_CLIENT_ID,GITHUB_CLIENT_SECRET)
    FRONTEND_URL = "http://localhost:3000/github"

    async with httpx.AsyncClient() as client:
        token_res= await client.post("https://github.com/login/oauth/access_token",
                                     headers={"Accept": "application/json"},
                                     data={
                                            "client_id": GITHUB_CLIENT_ID,
                                            "client_secret": GITHUB_CLIENT_SECRET,
                                            "code": code
                                            }
                                     )
        

        token_data = token_res.json()
        
        access_token = token_data["access_token"]

        if not access_token:
            raise HTTPException(status_code=400, detail="GitHub OAuth failed")
        
        async with httpx.AsyncClient() as client:
            user_data = await client.get("https://api.github.com/user",
            headers={"Authorization": f"Bearer {access_token}"})
            user_res=user_data.json()
            # pprint(user_data.json())
            return RedirectResponse(f'http://localhost:3000/github/{user_res["login"]}')


@git_router.get("/user",response_model=GithubUserResponse)
async def get_user_info():
    token = os.getenv("TOKEN")

    async with httpx.AsyncClient() as client:
        user_res = await client.get("https://api.github.com/user",
                                    headers={
                                        "Authorization":f"Bearer {token}",
                                        "Accept":"application/vnd.github+json"
                                    }
                                    )
        
        repo_res =  await client.get("https://api.github.com/user/repos",
                                    headers={
                                        "Authorization":f"Bearer {token}",
                                        "Accept":"application/vnd.github+json"
                                    })
        
        
    repo_data = repo_res.json()
    public_repos = [repo for repo in repo_data if not repo.get("private")]
    private_repos = [repo for repo in repo_data if repo.get("private")]

    public_repos_res = [
        {
            "name": repo["name"],
            "full_name": repo["full_name"],
            "html_url": repo["html_url"],
            "url": repo["url"],
            "stars": repo["stargazers_count"],
            "forks": repo["forks"]
        }
        for repo in public_repos
    ]

    private_repos_res = [
        {
            "name": repo["name"],
            "full_name": repo["full_name"],
            "html_url": repo["html_url"],
            "url": repo["url"],
            "stars": repo["stargazers_count"],
            "forks": repo["forks"]
        }
        for repo in private_repos
    ]

    user_data =user_res.json()

    return GithubUserResponse(
                                        avatar=user_data["avatar_url"],
                                        username=user_data["login"],
                                        name=user_data["name"],
                                        public_repos_count=user_data["public_repos"],
                                        private_repos_count=user_data.get("total_private_repos", 0),
                                        public_repos=public_repos_res,
                                        private_repos= private_repos_res
                                    )
    

@git_router.post("/create-webhook")
async def create_webhook(request:WebHookRequest):
    
    webhook_secret = os.getenv("WEBHOOK_SECRET")
    access_token = os.getenv("TOKEN")
    
    payload={
        "name":"web",
        "active":True,
        "events":["push"],
        "config":{
            "url":"https://30b8-106-219-160-120.ngrok-free.app/api/github/generate",
            "content_type":"json",
            "secret":webhook_secret,
            "insecure_ssl":"0"
        }
    }
    
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Accept": "application/vnd.github+json"
    }
    
    async with httpx.AsyncClient() as client:
        response = await client.post(request.repo_url+"/hooks",headers=headers,json=payload)
        
        if response.status_code > 400:
            raise HTTPException(status_code=response.status_code,detail=response.json())
        
        return ({"message":"Webhook Set Successfully","webhook_data":response.json()})



@git_router.post("/generate")
async def webhook_readme_generate(request:Request):
    
    body = await request.json()
    
    modified_files = []
    
    for commit in body.get("commits",[]):
        modified_files.extend(commit.get("modified",[]))
        
    if all(f.lower() == "readme.md" for f in modified_files):
        print("Skipped: Only README.md was modified")
        return {"message": "Skipped: Only README.md was modified"}
    
    ref= body.get("ref").replace("refs/heads/",'')
    name = body["repository"]["name"]
    full_name = body["repository"]["full_name"]
    url = body["repository"]["html_url"]
    clone_url = body["repository"]["clone_url"]
    
    
    try:
        
        state = await run_in_threadpool(
            webhook_pipeline,
            url=clone_url,
            description="",
            preferences={
                            "title": True,
                            "badge": True,
                            "introduction": True,
                            "table_of_contents": True,
                            "key_features": True,
                            "install_guide": True,
                            "usage": True,
                            "api_ref": True,
                            "env_var": True,
                            "project_structure": True,
                            "tech_used": True,
                            "licenses": True
                        }
                )
        token = os.getenv("TOKEN")
        readme_name = await get_existing_readme_filename(repo=full_name,token=token)
        webhook_response = await update_github_readme(file_name=readme_name,readme_text=state.get("readme"),repo_full_name=full_name,access_token=token)
        
        return webhook_response
        
        
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    
    
    
    





