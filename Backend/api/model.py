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
    session_id: str

class ResumeRequest(BaseModel):
    session_id: str
    action: str  # "regenerate" or "end"

class ReadmeResponse(BaseModel):
    readme: str
