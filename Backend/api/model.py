from pydantic import BaseModel,HttpUrl
from typing import Dict


class ReadmeRequest(BaseModel):
    github_url: HttpUrl
    project_description: str
    preferences: Dict
    session_id: str

class ResumeRequest(BaseModel):
    session_id: str
    action: str  # "regenerate" or "end"

class ReadmeResponse(BaseModel):
    readme: str
