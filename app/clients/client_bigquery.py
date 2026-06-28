# Imortar o cliente do bigquery para consguir armazenas os chunks em formato de embeddings no bigquery, e depois fazer a 
# busca por similaridade com base nos embeddings

# Aqui vai ter todo o codigo da classe ClientBigQuery, esta classe vai ser responsavel
# por fazer a conexão com o bigqeury para retornar os chunks em embeddings e texto para recuperação hibrida


from duckdb import query
from google.cloud import bigquery
import logging
import uuid

from app.config import (
    BQ_TABLE,
    PROJECT_ID,
    BQ_DATASET,
    REGION,
    TOP_K,
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
        self.logger = logging.getLogger(__name__)

    def inserir_documento(
        self,
        documento: str,
        chunk: str,
        embedding: list[float],
    ) -> None:
        """
        Insere um documento no BigQuery.

        Args:
            documento: Nome do documento.
            chunk: Texto do chunk.
            embedding: Vetor de embedding do chunk.
        """

        table_id = f"{PROJECT_ID}.{self.dataset}.{BQ_TABLE}"

        rows = [
            {
                "id": str(uuid.uuid4()),
                "documento": documento,
                "chunk": chunk,
                "embedding": embedding,
            }
        ]

        errors = self.client.insert_rows_json(table_id, rows)

        if errors:
            raise RuntimeError(f"Erro ao inserir documento: {errors}")
        
    def executar_query(self, query: str):
        """
        Executa uma consulta SQL no BigQuery.

        Args:
            query: Consulta SQL.

        Returns:
            Resultado da consulta.
        """

        try:
            query_job = self.client.query(query)
            return query_job.result()

        except Exception as e:
            raise RuntimeError(
                f"Erro ao executar consulta no BigQuery: {e}\nQuery: {query}"
            )

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

    def buscar_chunks_similares(
        self,
        embedding: list[float],
        top_k: int = TOP_K,
    ):
        """
        Busca os chunks mais similares utilizando VECTOR_SEARCH.

        Args:
            embedding: Embedding da pergunta.
            top_k: Quantidade de chunks retornados.

        Returns:
            Lista de dicionários contendo documento, chunk e distância.
        """

        embedding_sql = ", ".join(map(str, embedding))

        # sanitize identifiers to avoid accidental newlines or backticks
        safe_project = str(PROJECT_ID).replace("`", "").replace("\r", "").replace("\n", "").strip()
        safe_dataset = str(self.dataset).replace("`", "").replace("\r", "").replace("\n", "").strip()
        safe_table = str(BQ_TABLE).replace("`", "").replace("\r", "").replace("\n", "").strip()

        table_ref = f"{safe_project}.{safe_dataset}.{safe_table}"

        query = f"""
        SELECT
            base.documento,
            base.chunk,
            distance
        FROM VECTOR_SEARCH(
            TABLE `{table_ref}`,
            'embedding',
            (
                SELECT
                    [{embedding_sql}] AS embedding
            ),
            top_k => {top_k}
        );
        """

        # log the query (first 2000 chars) to help debugging without overflowing logs
        try:
            self.logger.debug("VECTOR_SEARCH query: %s", query[:2000])
        except Exception:
            pass

        resultado = self.executar_query(query)

        return [
            {
                "documento": row.documento,
                "chunk": row.chunk,
                "distance": row.distance,
            }
            for row in resultado
        ]

if __name__ == "__main__":

    from app.clients.client_vertex import ClientVertex
    vertex = ClientVertex()

    embedding = vertex.gerar_embedding(
        "Como atualizar a base da Único?"
    )

    client = ClientBigQuery()

    resultado = client.buscar_chunks_similares(embedding)

    for item in resultado:
        print("-" * 80)
        print(item["distance"])
        print(item["chunk"][:300])