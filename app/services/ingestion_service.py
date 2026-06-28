from app.clients.client_bigquery import ClientBigQuery
from app.clients.client_vertex import ClientVertex
from app.processamento.chunker import Chunker


class IngestionService:
    """
    Responsável por ingerir documentos no BigQuery.

    Fluxo:

    Documento
        ↓
    Chunker
        ↓
    Embeddings
        ↓
    BigQuery
    """

    def __init__(self):

        self.chunker = Chunker()

        self.vertex = ClientVertex()

        self.bigquery = ClientBigQuery()

    def ingerir_documento(
        self,
        caminho_arquivo: str,
        nome_documento: str,
    ):

        print(f"Lendo documento: {nome_documento}")

        texto = self.chunker.ler_markdown(caminho_arquivo)

        chunks = self.chunker.gerar_chunks(texto)

        print(f"{len(chunks)} chunks encontrados.\n")

        for indice, chunk in enumerate(chunks, start=1):

            print(f"Chunk {indice}/{len(chunks)}")

            embedding = self.vertex.gerar_embedding(chunk)

            self.bigquery.inserir_documento(
                documento=nome_documento,
                chunk=chunk,
                embedding=embedding,
            )

        print("\nIngestão concluída!")


if __name__ == "__main__":

    service = IngestionService()

    service.ingerir_documento(
        caminho_arquivo="data/manual.md",
        nome_documento="Manual Único/Cnseg",
    )