from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.routes.chatbot import router

app = FastAPI(
    title="Lagos Analytics Chatbot",
    description="""
API RAG para responder dúvidas sobre processos internos da empresa.

## Tecnologias

- FastAPI
- Google Gemini 2.5 Flash
- Google GenAI
- BigQuery Vector Search
- LangChain

## Fluxo

Pergunta → Embedding → BigQuery → Recuperação → Gemini → Resposta
""",
    version="1.0.0",
)

app.include_router(router)


@app.get(
    "/status",
    tags=["Status"],
)
def status():
    return {
        "status": "online",
        "api": "Lagos Analytics Chatbot",
        "version": "1.0.0",
    }


# Serve the React/HTML frontend (must be mounted AFTER all API routes)
app.mount("/", StaticFiles(directory="frontend", html=True), name="frontend")