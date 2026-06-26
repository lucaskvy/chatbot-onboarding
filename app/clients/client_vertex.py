# Importar o cliente do google AI plataform para resgatar os modelos Gemini 3.5-flash e modelo de embeddings

# Aqui vai ter a classe ClientVertex que vai ser responsavel por chamar os modelos 
# gemini para o chatbot e para gerar embeddings para o banco de dados do BigQuery

from urllib import response

import vertexai

from vertexai.generative_models import GenerativeModel
from vertexai.language_models import TextEmbeddingModel

from app.config import (
    MODELO_EMBEDDINGS,
    PROJECT_ID,
    REGION,
    MODELO_CHAT,
)


class ClientVertex:

    def __init__(self):

        vertexai.init(
            project=PROJECT_ID,
            location=REGION
        )

        self.chat_model = GenerativeModel(MODELO_CHAT)
        self.embedding_model = TextEmbeddingModel.from_pretrained(
    MODELO_EMBEDDINGS
)

    def gerar_resposta(self, pergunta: str):

        response = self.chat_model.generate_content(pergunta)

        return response.text
    
    def gerar_embedding(self, texto: str):

        embedding = self.embedding_model.get_embeddings([texto])

        return embedding[0].values

if __name__ == "__main__":

    client = ClientVertex()

    vetor = client.gerar_embedding("Olá mundo")

    print(vetor[:10])