import httpx
import os
from pprint import pprint
from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, HTTPException,Request,Cookie,Response
from fastapi.responses import RedirectResponse
from .model import GithubUserResponse,WebHookRequest
from agent.agent import webhook_pipeline
from .utils.github_utils import get_existing_readme_filename,update_github_readme
from .utils.jwt import create_jwt_token,verify_jwt_token
from fastapi.concurrency import run_in_threadpool
import secrets
from .utils.github_api import get_github_user_info,get_github_user_repo_info,webhook_data
from database.api import register_user_db,get_github_user_data,set_webhook_db,set_status_webhook_be,delete_webhook_be,get_webhook_repos,update_webhook_db,get_webhook_data_db,get_repo_by_url
from database.database import get_repos


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
        response = RedirectResponse(f'https://readmeai.anand106.me/github/{user_data["username"]}')
        response.set_cookie(
            key="access_token",
            value=jwt_token,
            httponly=True,
            secure=True,
            samesite="None",
            max_age=86000,
            path='/'
        )
        # pprint(user_data.json())
        return response
    

@git_router.get("/login")
async def check_login(access_token:str = Cookie(None)):
    
    if access_token:
        payload = verify_jwt_token(access_token)
        return {
            "authenticated":True,
            "username":payload["username"]
        }
    else:
        return {
            "authenticated":False
        }
        
        
@git_router.post('/logout')
async def logout(response:Response):
    response.delete_cookie(
        key="access_token",
        path="/",
        secure=True,
        httponly=True,
        samesite="none"
    )
    
    return {"message": "Logged out successfully"}
        
    


@git_router.get("/user",response_model=GithubUserResponse)
async def get_user_info(access_token:str = Cookie(None)):
    
    print("Backend /user route hit")
    
    # token = os.getenv("TOKEN")
    payload = verify_jwt_token(access_token)
    print(f"the token from cookie is : {payload}")
    
    # repo_data = await get_webhook_repos(payload["username"])

    user_data = await get_github_user_data(payload["username"])
    
    if not user_data:
        print(" No user found in DB for", payload["username"])
        raise HTTPException(status_code=404, detail="User not found in DB")
    
    
    # repodata = await get_github_user_repo_info(user_data["github_token"],user_data["user_id"])
    
    repodata = await get_repos(user_id=user_data["user_id"])
    
    
    webhooks = await get_webhook_repos(user_id=user_data["user_id"])
    
    webhook_repoids = [repo["repo_id"] for repo in webhooks]
    
    filtered_repos = [repo for repo in repodata if repo["repo_id"] not in webhook_repoids]
    

    return GithubUserResponse(
                                        avatar=user_data["avatar_url"],
                                        username=user_data["username"],
                                        name=user_data["name"],
                                        repos=filtered_repos,
                                        whrepos=webhooks
                                    )



@git_router.post('/update-webhook')
async def update_webhook(request:Request,access_token:str = Cookie(None)):
    
    payload= verify_jwt_token(access_token)
    
    body = await request.json()
    
    
    await update_webhook_db(repo_id=body["repo_id"],preferences=body["preferences"],description=body["description"])
    
    return {"message":"updated"}
    
    
@git_router.post('/webhook')
async def get_webhook(request:Request,access_token:str = Cookie(None)):
    
    payload= verify_jwt_token(access_token)
    
    body = await request.json()
    
    wh_data= await webhook_data(repo_id=body["repo_id"])
    
    return wh_data
    
    
       
    

@git_router.post("/create-webhook")
async def create_webhook(request:WebHookRequest,access_token:str = Cookie(None)):
    
    print("Received request:", request.model_dump())
    payload= verify_jwt_token(access_token)
    user_data = await get_github_user_data(payload["username"])
    if not user_data:
        print(" No user found in DB for", payload["username"])
        raise HTTPException(status_code=404, detail="User not found in DB")
    
    secret = secrets.token_hex(32)
    
    payload={
        "name":"web",
        "active":True,
        "events":["push"],
        "config":{
            "url":"https://readme-generator-uisng-langgraph.onrender.com/api/github/generate",
            "content_type":"json",
            "secret":secret,
            "insecure_ssl":"0"
        }
    }
    
    headers = {
        "Authorization": f"Bearer {user_data['github_token']}",
        "Accept": "application/vnd.github+json"
    }
    
    async with httpx.AsyncClient() as client:
        response = await client.post("https://api.github.com/repos/"+request.repo_name+"/hooks",headers=headers,json=payload)
        
        res_data = response.json()
        
        pprint(res_data)
        
        webhook_data = await set_webhook_db(user_data["user_id"],request.repo_id,res_data["url"],res_data["id"],secret,request.preferences,request.description)
        
        if response.status_code > 400:
            raise HTTPException(status_code=response.status_code,detail=res_data)
        
        return ({"message":"Webhook Set Successfully","webhook_data":res_data})
    

@git_router.post("/disable-webhook")
async def disable_webhook(request:Request,access_token:str = Cookie(None)):
    
    body = await request.json()

    repo_id = body.get("repo_id")
    isActive = body.get("isActive")
    
    payload = verify_jwt_token(access_token)
    print(f"the token from cookie is : {payload}")
    
    user_data = await get_github_user_data(payload["username"])
    if not user_data:
        raise HTTPException(status_code=404, detail="User not found in DB")
    
    await set_status_webhook_be(repo_id=repo_id,access_token=user_data["github_token"],isActive=isActive)
    
    print("webhook diabled fully")

@git_router.post("/delete-webhook")
async def delete_webhook(request:Request,access_token:str = Cookie(None)):
    body = await request.json()

    repo_id = body.get("repo_id")
    payload = verify_jwt_token(access_token)
    print(f"the token from cookie is : {payload}")
    
    user_data = await get_github_user_data(payload["username"])
    if not user_data:
        raise HTTPException(status_code=404, detail="User not found in DB")
    
    await delete_webhook_be(repo_id=repo_id,access_token=user_data["github_token"])
    print("webhook deleted fully")
    
    

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
    username=body["repository"]["owner"]["login"]
    full_name = body["repository"]["full_name"]
    url = body["repository"]["html_url"]
    clone_url = body["repository"]["clone_url"]
    
    repo_data = await get_repo_by_url(html_url=url)
    
    pprint(f"repo data received is ${repo_data}")
    
    wh_data = await get_webhook_data_db(repo_id=repo_data['repo_id'])
    
    
    user_data = await get_github_user_data(username)
    if not user_data:
        raise HTTPException(status_code=404, detail="User not found in DB")
    
    print(f"the user data is ${user_data}")
    
    try:
        
        state = await run_in_threadpool(
            webhook_pipeline,
            url=clone_url,
            description=wh_data["description"],
            preferences=wh_data["preferences"]
                )
        token = user_data["github_token"]
        readme_name = await get_existing_readme_filename(repo=full_name,token=token)
        webhook_response = await update_github_readme(file_name=readme_name,readme_text=state.get("readme"),repo_full_name=full_name,access_token=token)
        
        return webhook_response
        
        
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    
    
    
    





