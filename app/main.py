from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles
from app.brain import ask_ai

app = FastAPI(
    title="Sahood's Assistant ProGPT_MODv1",
    version="0.1.0"
)

BASE_DIR = Path(__file__).resolve().parent
app.mount(
    "/static",
    StaticFiles(directory=BASE_DIR / "static"),
    name="static"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    message: str

@app.get("/")
async def home():
    return FileResponse(
        BASE_DIR / "templates" / "index.html"
    )

@app.post("/chat")
async def chat(request: ChatRequest):
    try:
        answer = ask_ai(request.message)

        return {
            "reply": answer,
            "status": "success"
        }

    except Exception as e:
        return {
            "reply": f"AI Error: {str(e)}",
            "status": "error"
        }
