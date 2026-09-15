# Documentos para ingestão

Esta pasta é destinada a documentos Markdown usados localmente na base RAG.

Não versione documentos internos, dados pessoais, credenciais, links privados ou informações de clientes. Para executar a ingestão, disponibilize localmente um arquivo autorizado com o nome `manual.md` e rode:

```powershell
python -m app.services.ingestion_service
```

O arquivo `manual.md` é ignorado pelo Git e permanecerá somente no ambiente local.
