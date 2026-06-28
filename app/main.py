from fastapi import FastAPI
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
    "/",
    tags=["Status"],
)
def home():
    return {
        "status": "online",
        "api": "Lagos Analytics Chatbot",
        "version": "1.0.0",
    }