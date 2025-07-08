from pydantic import BaseModel
from typing import Dict,Any,List

class ReadPreferences(BaseModel):
    title: bool
    badge : bool
    introduction:bool
    table_of_contents:bool
    key_features:bool
    install_guide:bool
    usage:bool
    api_ref:bool
    env_var:bool
    project_structure:bool
    tech_used:bool
    licenses:bool
class ReadmeRequest(BaseModel):
    github_url: str
    project_description: str
    preferences: ReadPreferences
    

class ResumeRequest(BaseModel):
    action: str
    project_description: str
    preferences: ReadPreferences


class ReadmeResponse(BaseModel):
    readme: str

class GithubUserResponse(BaseModel):
    avatar: str
    username: str
    name: str
    repos:List
    
class WebHookRequest(BaseModel):
    username:str
    repo_name:str
    repo_url:str
    repo_id:str

