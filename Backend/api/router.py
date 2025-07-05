from fastapi import APIRouter, HTTPException, Response,Cookie
from fastapi.concurrency import run_in_threadpool
from fastapi.responses import RedirectResponse
from .model import ReadmeRequest, ReadmeResponse, ResumeRequest
from agent.agent import run_readme_pipeline, resume_readme_pipeline
from pprint import pprint
from dotenv import load_dotenv
import secrets
import httpx
import os

load_dotenv()

router = APIRouter(prefix="/api/readme", tags=["Readme Generator"])

sessions = {}




# @router.get("/auth/github/callback")
# async def github_callback(code:str):

#     GITHUB_CLIENT_ID = os.getenv("GITHUB_CLIENT_ID")
#     GITHUB_CLIENT_SECRET = os.getenv("GITHUB_CLIENT_SECRET")
#     print(GITHUB_CLIENT_ID,GITHUB_CLIENT_SECRET)
#     FRONTEND_URL = "http://localhost:3000/github"

#     async with httpx.AsyncClient() as client:
#         token_res= await client.post("https://github.com/login/oauth/access_token",
#                                      headers={"Accept": "application/json"},
#                                      data={
#                                             "client_id": GITHUB_CLIENT_ID,
#                                             "client_secret": GITHUB_CLIENT_SECRET,
#                                             "code": code
#                                             }
#                                      )
        

#         token_data = token_res.json()
#         print("TOKEN RESPONSE:", token_data)
#         access_token = token_data["access_token"]

#         if not access_token:
#             raise HTTPException(status_code=400, detail="GitHub OAuth failed")
        
#         async with httpx.AsyncClient() as client:
#             user_data = await client.get("https://api.github.com/user",
#             headers={"Authorization": f"Bearer {access_token}"})
#             pprint(user_data.json())
#             return RedirectResponse(FRONTEND_URL)



@router.post("/start")
async def start_session(response: Response):
    session_id = secrets.token_hex(32)
    sessions[session_id]={"state":"new"}
    response.set_cookie(
        key="session_id",
        value=session_id,
        httponly=True,
        secure=True,
        samesite="none",
        max_age=86400
    )
    return {"message": "Session started"}



@router.post("/generate", response_model=ReadmeResponse)
async def generate_readme(request: ReadmeRequest,session_id:str = Cookie(None) ):

    if not session_id:
        raise HTTPException(status_code=401, detail="Missing session cookie")

    if session_id not in sessions:
        raise HTTPException(status_code=401, detail="Invalid or expired session")

    
    # pprint(request)
    try:
        # state = run_readme_pipeline(
        #     url=request.github_url,
        #     description=request.project_description,
        #     preferences=request.preferences,
        #     session_id=session_id
        # )
        state = await run_in_threadpool(
            run_readme_pipeline,
            url=request.github_url,
            description=request.project_description,
            preferences=request.preferences,
            session_id=session_id
        )

        return ReadmeResponse(readme=state.get('readme'))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/resume", response_model=ReadmeResponse)
async def resume_readme(request: ResumeRequest,session_id: str = Cookie(None)):


    if not session_id:
        raise HTTPException(status_code=401, detail="Missing session cookie")

    if session_id not in sessions:
        raise HTTPException(status_code=401, detail="Invalid or expired session")

    try:
        #state = resume_readme_pipeline(session_id=session_id, action=request.action,preferences=request.preferences,description=request.project_description)
        state = await run_in_threadpool(
            resume_readme_pipeline,
            session_id=session_id,
            preferences=request.preferences,
            description=request.project_description,
            action=request.action
        )
        return ReadmeResponse(readme=state.get('readme'))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
