import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from fastapi import FastAPI
from api.router import router
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Readme Generator API",
    description="Generate README.md from GitHub repo using LangGraph",
    version="1.0"
)

origins = [
    "http://localhost:3000",
      "https://readme-generator-uisng-langgraph.vercel.app" ,
      "https://readmeai.anand106.me" # React dev server
    # Add more origins here if needed
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,              # Or ["*"] to allow all
    allow_credentials=True,
    allow_methods=["*"],                # Allow all methods (GET, POST, etc.)
    allow_headers=["*"],                # Allow all headers
)



app.include_router(router)


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)