from fastapi import FastAPI
from api.router import router
import uvicorn

app = FastAPI(
    title="Readme Generator API",
    description="Generate README.md from GitHub repo using LangGraph",
    version="1.0"
)

app.include_router(router)


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)