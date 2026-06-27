# Importar langchain -> recursive character split, fazer o split com base nos paragrafos do 
# texto em markdown, os chunks vao ter cerca de 800 com 150 de overlap, eles vão ser divididos com prioridade em titulos em 
# markdown

# Aqui vai ter a classe ChunkProcessor que vai ser responsavel por fazer o split do texto em chunks e gerar embeddings para 
# cada chunk, e salvar no banco de dados do BigQuery