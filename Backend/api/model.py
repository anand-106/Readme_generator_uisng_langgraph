from pydantic import BaseModel
from typing import Dict

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
