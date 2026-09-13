from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.chat import router as chat_router
from config.settings import settings

app = FastAPI(
    title=settings.APP_NAME,
    description="Chat Assisstant powered by Google Gemini",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chat_router, prefix="/api/v1", tags=["chat"])
@app.get("/")
async def root():
    return {"message": "Welcome to the AI Chat Assisstant API."}
