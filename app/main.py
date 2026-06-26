from fastapi import FastAPI

app = FastAPI(
    title="Chatbot Onboarding API",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "status": "ok",
        "message": "API funcionando"
    }