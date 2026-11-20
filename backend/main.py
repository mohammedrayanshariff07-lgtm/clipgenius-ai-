
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, HttpUrl

app = FastAPI(title="ClipGenius AI Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class VideoRequest(BaseModel):
    url: HttpUrl

@app.get("/")
def home():
    return {
        "status": "online",
        "message": "ClipGenius AI Backend is running!"
    }

@app.post("/fetch-video")
def fetch_video(data: VideoRequest):
    return {
        "status": "received",
        "url": str(data.url),
        "message": "Video link received. Downloader is not connected yet."
    }
