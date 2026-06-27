# Imortar o cliente do bigquery para consguir armazenas os chunks em formato de embeddings no bigquery, e depois fazer a 
# busca por similaridade com base nos embeddings

# Aqui vai ter todo o codigo da classe ClientBigQuery, esta classe vai ser responsavel
# por fazer a conexão com o bigqeury para retornar os chunks em embeddings e texto para recuperação hibrida


from google.cloud import bigquery

from app.config import (
    PROJECT_ID,
    BQ_DATASET,
    REGION,
)


class ClientBigQuery:
    """
    Cliente responsável pela comunicação com o BigQuery.

    Responsabilidades:
    - Executar consultas SQL.
    - Criar conexão com o BigQuery.
    """

    def __init__(self):
        """Inicializa o cliente do BigQuery."""

        self.client = bigquery.Client(
            project=PROJECT_ID,
            location=REGION,
        )

        self.dataset = BQ_DATASET

    def executar_query(self, query: str):
        """
        Executa uma consulta SQL no BigQuery.

        Args:
            query: Consulta SQL.

        Returns:
            Resultado da consulta.
        """

        query_job = self.client.query(query)

        return query_job.result()

    def testar_conexao(self):
        """
        Testa se o cliente consegue executar uma consulta no BigQuery.
        """

        query = """
        SELECT 1 AS teste
        """

        resultado = self.executar_query(query)

        for linha in resultado:
            print(linha.teste)


if __name__ == "__main__":

    client = ClientBigQuery()

    client.testar_conexao()