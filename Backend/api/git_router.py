import httpx
import os
from pprint import pprint
from dotenv import load_dotenv
from fastapi import APIRouter, HTTPException
from fastapi.responses import RedirectResponse
from .model import GithubUserResponse


git_router = APIRouter(prefix="/api/github",tags=["Github"])

load_dotenv()


@git_router.get("/auth/callback")
async def github_callback(code:str):

    GITHUB_CLIENT_ID = os.getenv("GITHUB_CLIENT_ID")
    GITHUB_CLIENT_SECRET = os.getenv("GITHUB_CLIENT_SECRET")
    print(GITHUB_CLIENT_ID,GITHUB_CLIENT_SECRET)
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
        print("TOKEN RESPONSE:", token_data)
        access_token = token_data["access_token"]

        if not access_token:
            raise HTTPException(status_code=400, detail="GitHub OAuth failed")
        
        async with httpx.AsyncClient() as client:
            user_data = await client.get("https://api.github.com/user",
            headers={"Authorization": f"Bearer {access_token}"})
            pprint(user_data.json())
            return RedirectResponse(FRONTEND_URL)


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





