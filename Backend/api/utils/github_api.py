import httpx
import uuid


async def get_github_user_info(token:str):
    async with httpx.AsyncClient() as client:
        user_res = await client.get("https://api.github.com/user",
                                    headers={
                                        "Authorization":f"Bearer {token}",
                                        "Accept":"application/vnd.github+json"
                                    }
                                    )
        
        user_data =  user_res.json()
        
        final_user_data={
                            "user_id":str(uuid.uuid4()),
                            "name":user_data.get("name",""),
                            "username":user_data["login"],
                            "avatar_url":user_data.get("avatar_url",""),
                            "github_token":token
                        }
        
        
        
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
                "repo_id":str(uuid.uuid4()),
                "repo_name": repo["name"],
                "repo_fullname": repo["full_name"],
                "html_url": repo["html_url"],
                "url": repo["url"],
                "stars": repo["stargazers_count"],
                "forks": repo["forks"],
                "is_private":False,
                "user_id":final_user_data["user_id"]
                
            }
            for repo in public_repos
        ]

        private_repos_res = [
            {
                "repo_id":str(uuid.uuid4()),
                "repo_name": repo["name"],
                "repo_fullname": repo["full_name"],
                "html_url": repo["html_url"],
                "url": repo["url"],
                "stars": repo["stargazers_count"],
                "forks": repo["forks"],
                "is_private":True,
                "user_id":final_user_data["user_id"]
            }
            for repo in private_repos
        ]
        
        final_repos = public_repos_res + private_repos_res
        return [final_user_data,final_repos]
    


async def get_github_user_repo_info(token:str,user_id:str):
    async with httpx.AsyncClient(timeout=10.0) as client:
        
        
        
        
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
                "repo_id":str(uuid.uuid4()),
                "repo_name": repo["name"],
                "repo_fullname": repo["full_name"],
                "html_url": repo["html_url"],
                "url": repo["url"],
                "stars": repo["stargazers_count"],
                "forks": repo["forks"],
                "is_private":False,
                "user_id":user_id
                
            }
            for repo in public_repos
        ]

        private_repos_res = [
            {
                "repo_id":str(uuid.uuid4()),
                "repo_name": repo["name"],
                "repo_fullname": repo["full_name"],
                "html_url": repo["html_url"],
                "url": repo["url"],
                "stars": repo["stargazers_count"],
                "forks": repo["forks"],
                "is_private":True,
                "user_id":user_id
            }
            for repo in private_repos
        ]
        
        final_repos = public_repos_res + private_repos_res
        return final_repos

        

    