from pydantic import BaseModel
from typing import Dict

class ReadmeRequest(BaseModel):
    github_url: str
    project_description: str
    preferences: Dict
    session_id: str

class ResumeRequest(BaseModel):
    session_id: str
    action: str  # "regenerate" or "end"

class ReadmeResponse(BaseModel):
    readme: str
