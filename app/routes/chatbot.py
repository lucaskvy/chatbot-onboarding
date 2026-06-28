from fastapi import APIRouter, HTTPException

from app.schemas.chat import (
    ChatRequest,
    ChatResponse,
)

from app.services.chat_service import ChatService

router = APIRouter(
    prefix="/chat",
    tags=["Chatbot"],
)

chat_service = ChatService()


@router.post(
    "",
    response_model=ChatResponse,
    summary="Enviar pergunta ao chatbot",
    description="Recebe uma pergunta e retorna uma resposta baseada na base de conhecimento utilizando RAG.",
)
def chat(request: ChatRequest):

    try:

        resposta = chat_service.responder(
            request.pergunta
        )

        return ChatResponse(
            resposta=resposta
        )

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )