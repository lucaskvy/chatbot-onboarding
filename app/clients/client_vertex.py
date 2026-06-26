# Importar o cliente do google AI plataform para resgatar os modelos Gemini 3.5-flash e modelo de embeddings

# Aqui vai ter a classe ClientVertex que vai ser responsavel por chamar os modelos 
# gemini para o chatbot e para gerar embeddings para o banco de dados do BigQuery

from google import genai

from app.config import (
    PROJECT_ID,
    REGION,
    MODELO_CHAT,
    MODELO_EMBEDDINGS,
)


class ClientVertex:
    """
    Cliente responsável por toda comunicação com o Vertex AI.

    Responsabilidades:
    - Gerar respostas utilizando o modelo Gemini.
    - Gerar embeddings para armazenamento e busca vetorial.
    """

    def __init__(self):
        """Inicializa o cliente do Vertex AI."""

        self.client = genai.Client(
            vertexai=True,
            project=PROJECT_ID,
            location=REGION,
        )

    def gerar_resposta(self, pergunta: str) -> str:
        """
        Gera uma resposta utilizando o modelo de linguagem.

        Args:
            pergunta: Pergunta enviada ao modelo.

        Returns:
            Texto gerado pelo Gemini.
        """

        if not pergunta.strip():
            raise ValueError("A pergunta não pode estar vazia.")

        try:
            response = self.client.models.generate_content(
                model=MODELO_CHAT,
                contents=pergunta,
            )

            return response.text

        except Exception as e:
            raise RuntimeError(f"Erro ao gerar resposta: {e}")

    def gerar_embedding(self, texto: str) -> list[float]:
        """
        Gera o embedding de um texto.

        Args:
            texto: Texto para geração do embedding.

        Returns:
            Lista de floats representando o vetor do embedding.
        """

        if not texto.strip():
            raise ValueError("O texto não pode estar vazio.")

        try:
            response = self.client.models.embed_content(
                model=MODELO_EMBEDDINGS,
                contents=texto,
            )

            return response.embeddings[0].values

        except Exception as e:
            raise RuntimeError(f"Erro ao gerar embedding: {e}")


if __name__ == "__main__":

    client = ClientVertex()

    print(client.gerar_resposta("Olá! Quem é você?"))

    embedding = client.gerar_embedding("Olá mundo")

    print(embedding[:10])