# Imortar o cliente do bigquery para consguir armazenas os chunks em formato de embeddings no bigquery, e depois fazer a 
# busca por similaridade com base nos embeddings

# Aqui vai ter todo o codigo da classe ClientBigQuery, esta classe vai ser responsavel
# por fazer a conexão com o bigqeury para retornar os chunks em embeddings e texto para recuperação hibrida


from google.cloud import bigquery

from app.config import (
    PROJECT_ID,
    BQ_DATASET,
)

class ClientBigQuery:

    def __init__(self):

        self.client = bigquery.Client(
            project=PROJECT_ID
        )