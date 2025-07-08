from pydantic import BaseModel, Field
from typing import List, Optional


class Webhook(BaseModel):
    user_id:str
    repo_id:str
    webhook_id: str
    secret: str
    webhook_url: str 


class Repository(BaseModel):
    user_id:str
    repo_id: str
    repo_name: str 
    repo_fullname: str 
    url: str
    html_url: str 
    is_private: bool
    stars: int
    forks: int


class User(BaseModel):
    user_id: str
    name: Optional[str]
    username: str
    avatar_url: Optional[str]
    github_token: str 

