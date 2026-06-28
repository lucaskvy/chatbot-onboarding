from app.clients.client_bigquery import ClientBigQuery
from app.clients.client_vertex import ClientVertex
from app.prompts.chatbot_prompt import PROMPT_CHAT
from app.config import TOP_K

class ChatService:
    """
    Serviço responsável pelo fluxo completo do chatbot.

    Fluxo:

    Pergunta
        ↓
    Embedding
        ↓
    Busca vetorial
        ↓
    Monta contexto
        ↓
    Gemini
        ↓
    Resposta
    """

    def __init__(self):

        self.vertex = ClientVertex()

        self.bigquery = ClientBigQuery()

    def responder(self, pergunta: str) -> str:
        """
        Responde uma pergunta utilizando RAG.
        """

        # 1. Gera o embedding da pergunta
        embedding = self.vertex.gerar_embedding(pergunta)

        # 2. Busca os chunks mais relevantes
        resultados = self.bigquery.buscar_chunks_similares(
            embedding=embedding,
            top_k=TOP_K,
        )
        print("\nChunks recuperados:\n")

        for i, item in enumerate(resultados, start=1):
            print(f"Chunk {i}")
            print(item["chunk"][:200])
            print("-" * 80)

        # 3. Junta todos os chunks
        contexto = "\n\n".join(
            item["chunk"]
            for item in resultados
        )

        # 4. Monta o prompt
        prompt = PROMPT_CHAT.format(
            contexto=contexto,
            pergunta=pergunta,
)

        # 5. Chama o Gemini
        resposta = self.vertex.gerar_resposta(prompt)

        return resposta


if __name__ == "__main__":

    chat = ChatService()

    while True:

        pergunta = input("\nPergunta: ")

        if pergunta.lower() in ["sair", "exit", "quit"]:
            break

        resposta = chat.responder(pergunta)

        print("\nResposta:\n")

        print(resposta)