from fastapi import APIRouter

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
)
def chat(request: ChatRequest):

    resposta = chat_service.responder(
        request.pergunta
    )

    return ChatResponse(
        resposta=resposta
    )