from pydantic import BaseModel, Field


class ChatRequest(BaseModel):

    pergunta: str = Field(
        ...,
        description="Pergunta enviada ao chatbot.",
        examples=["Como atualizar a base da Único?"],
    )


class ChatResponse(BaseModel):

    resposta: str = Field(
        ...,
        description="Resposta gerada pelo chatbot.",
    )