# Chatbot Onboarding RAG

Uma aplicação RAG para consultas a procedimentos operacionais. A API transforma a pergunta em embedding, recupera trechos semanticamente relacionados no BigQuery e pede ao Gemini uma resposta limitada ao contexto recuperado.

## Arquitetura

```text
Browser -> FastAPI /chat -> Vertex AI embeddings -> BigQuery VECTOR_SEARCH -> Gemini -> resposta
```

O frontend estático e a API são servidos pelo mesmo contêiner. A ingestão lê Markdown, cria chunks com sobreposição, gera embeddings e grava os registros no BigQuery.

## Stack

- Python, FastAPI e Pydantic
- Google GenAI / Vertex AI (Gemini e embeddings)
- BigQuery Vector Search
- LangChain Text Splitters
- HTML, CSS e JavaScript
- Docker e Cloud Run

## Executar localmente

1. Crie e ative um ambiente virtual.
2. Instale dependências com `pip install -r requirements.txt`.
3. Copie `.env.example` para `.env` e informe os recursos GCP.
4. Autentique-se no Google Cloud com uma conta autorizada.
5. Execute `uvicorn app.main:app --reload`.
6. Abra `http://localhost:8000`; a documentação OpenAPI fica em `/docs`.

### Variáveis de ambiente

| Variável | Descrição |
| --- | --- |
| `PROJECT_ID` | Projeto Google Cloud |
| `REGION` | Região do Vertex AI e BigQuery |
| `BQ_DATASET` / `BQ_TABLE` | Base vetorial no BigQuery |
| `MODELO_CHAT` | Modelo Gemini para respostas |
| `MODELO_EMBEDDINGS` | Modelo de embeddings |
| `TOP_K` | Número de trechos recuperados |

## API

`POST /chat`

```json
{ "pergunta": "Como realizo este procedimento?" }
```

```json
{ "resposta": "..." }
```

`GET /status` retorna a disponibilidade básica do serviço.

## Ingestão

Coloque apenas documentos autorizados em `data/` e execute:

```powershell
python -m app.services.ingestion_service
```

Os documentos da base RAG não são versionados. Consulte [`data/README.md`](data/README.md) antes de adicionar um manual local.

## Contêiner

```powershell
docker build -t chatbot-onboarding .
docker run --rm -p 8080:8080 --env-file .env chatbot-onboarding
```

O `Dockerfile` expõe a porta 8080, adequada ao Cloud Run.

## Limitações atuais

- Não há testes automatizados ou pipeline CI.
- As respostas ainda não devolvem as fontes recuperadas.
- Não há rate limit, autenticação ou métricas estruturadas.
- Os parâmetros `TEMPERATURE` e `MAX_OUTPUT_TOKENS` estão configurados, mas ainda não são enviados à chamada do modelo.
