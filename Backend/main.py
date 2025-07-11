import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from fastapi import FastAPI
from api.router import router
from api.git_router import git_router
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
      "https://readmeai.anand106.me" 
    
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,              
    allow_credentials=True,
    allow_methods=["*"],                
    allow_headers=["*"],                
)

# Add root-level health endpoints for server wake-up
@app.get("/")
async def root_health():
    return {"status": "ok", "message": "Server is running"}

@app.get("/health") 
async def health():
    return {"status": "ok"}

app.include_router(router)
app.include_router(git_router)


# if __name__ == "__main__":
#     uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)
