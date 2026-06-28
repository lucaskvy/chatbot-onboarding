from fastapi import FastAPI
from app.routes.chatbot import router

app = FastAPI(
    title="Chatbot Onboarding API",
    version="1.0.0"
)

app.include_router(router)

@app.get("/")
def home():
    return {
        "status": "ok",
        "message": "API funcionando"
    }
