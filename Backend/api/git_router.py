import httpx
import os
from pprint import pprint
from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, HTTPException,Request,Cookie
from fastapi.responses import RedirectResponse
from .model import GithubUserResponse,WebHookRequest
from agent.agent import webhook_pipeline
from .utils.github_utils import get_existing_readme_filename,update_github_readme
from .utils.jwt import create_jwt_token,verify_jwt_token
from fastapi.concurrency import run_in_threadpool
import secrets
from .utils.github_api import get_github_user_info,get_github_user_repo_info
from database.api import register_user_db,get_github_user_data,set_webhook_db


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
        
        print(f'the token is : {access_token}')
        

        if not access_token:
            raise HTTPException(status_code=400, detail="GitHub OAuth failed")
        
        user_data,repo_data = await get_github_user_info(access_token)
        
        
        await register_user_db(user_data,repo_data)
        
            
        jwt_token = create_jwt_token({"username":user_data["username"]})
        response = RedirectResponse(f'http://localhost:3000/github/{user_data["username"]}')
        response.set_cookie(
            key="access_token",
            value=jwt_token,
            httponly=True,
            secure=False,
            max_age=86000,
            path='/'
        )
        # pprint(user_data.json())
        return response


@git_router.get("/user",response_model=GithubUserResponse)
async def get_user_info(access_token:str = Cookie(None)):
    
    print("Backend /user route hit")
    
    # token = os.getenv("TOKEN")
    payload = verify_jwt_token(access_token)
    print(f"the token from cookie is : {payload}")

    user_data = await get_github_user_data(payload["username"])
    if not user_data:
        print(" No user found in DB for", payload["username"])
        raise HTTPException(status_code=404, detail="User not found in DB")
    
    
    repodata = await get_github_user_repo_info(user_data["github_token"],user_data["user_id"])
    
    

    return GithubUserResponse(
                                        avatar=user_data["avatar_url"],
                                        username=user_data["username"],
                                        name=user_data["name"],
                                        repos=repodata
                                    )
    

@git_router.post("/create-webhook")
async def create_webhook(request:WebHookRequest,access_token:str = Cookie(None)):
    
    print("Received request:", request.model_dump())
    payload= verify_jwt_token(access_token)
    user_data = await get_github_user_data(payload["username"])
    if not user_data:
        print(" No user found in DB for", payload["username"])
        raise HTTPException(status_code=404, detail="User not found in DB")
    
    
    webhook_data = await set_webhook_db(user_data["user_id"],request.repo_id)
    
    payload={
        "name":"web",
        "active":True,
        "events":["push"],
        "config":{
            "url":webhook_data["webhook_url"],
            "content_type":"json",
            "secret":webhook_data["secret"],
            "insecure_ssl":"0"
        }
    }
    
    headers = {
        "Authorization": f"Bearer {user_data['github_token']}",
        "Accept": "application/vnd.github+json"
    }
    
    async with httpx.AsyncClient() as client:
        response = await client.post("https://api.github.com/repos/"+request.repo_name+"/hooks",headers=headers,json=payload)
        
        if response.status_code > 400:
            raise HTTPException(status_code=response.status_code,detail=response.json())
        
        return ({"message":"Webhook Set Successfully","webhook_data":response.json()})



@git_router.post("/generate")
async def webhook_readme_generate(request:Request):
    '''
    get the webseceret from the secret and look for the payload with the username and with that username we take the github oauth token from the database
    '''
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
    
    
    
    
    





