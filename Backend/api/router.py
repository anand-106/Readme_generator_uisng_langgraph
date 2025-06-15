from fastapi import APIRouter, HTTPException
from .model import ReadmeRequest, ReadmeResponse, ResumeRequest
from agent.agent import run_readme_pipeline, resume_readme_pipeline

router = APIRouter(prefix="/api/readme", tags=["Readme Generator"])

@router.post("/generate", response_model=ReadmeResponse)
async def generate_readme(request: ReadmeRequest):
    try:
        state = run_readme_pipeline(
            url=request.github_url,
            description=request.project_description,
            preferences=request.preferences,
            session_id=request.session_id
        )
        return ReadmeResponse(readme=state.get('readme'))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/resume", response_model=ReadmeResponse)
async def resume_readme(request: ResumeRequest):
    try:
        state = resume_readme_pipeline(session_id=request.session_id, action=request.action)
        return ReadmeResponse(readme=state.get('readme'))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
