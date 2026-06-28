# Importar langchain -> recursive character split, fazer o split com base nos paragrafos do 
# texto em markdown, os chunks vao ter cerca de 800 com 150 de overlap, eles vão ser divididos com prioridade em titulos em 
# markdown

# Aqui vai ter a classe ChunkProcessor que vai ser responsavel por fazer o split do texto em chunks e gerar embeddings para 
# cada chunk, e salvar no banco de dados do BigQuery

from pathlib import Path

from langchain_text_splitters import RecursiveCharacterTextSplitter


class Chunker:
    """
    Responsável por ler documentos e dividi-los em chunks.
    """

    def __init__(
        self,
        chunk_size: int = 1200,
        chunk_overlap: int = 200,
    ):
        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            separators=[
                "\n\n",
                "\n",
                ". ",
                " ",
                "",
            ],
        )

    def ler_markdown(self, caminho: str) -> str:
        """
        Lê um arquivo Markdown.

        Args:
            caminho: Caminho do arquivo.

        Returns:
            Texto completo do arquivo.
        """

        return Path(caminho).read_text(
            encoding="utf-8"
        )

    def gerar_chunks(self, texto: str) -> list[str]:
        """
        Divide um texto em chunks.

        Args:
            texto: Texto completo.

        Returns:
            Lista de chunks.
        """

        return self.splitter.split_text(texto)


if __name__ == "__main__":

    chunker = Chunker()

    texto = chunker.ler_markdown("data/manual.md")

    chunks = chunker.gerar_chunks(texto)

    print(f"Quantidade de chunks: {len(chunks)}")

    print("\nPrimeiro chunk:\n")

    print(chunks[0])