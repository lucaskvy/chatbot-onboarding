# Guia Completo de Atualização da Base de Dados da Único

## Objetivo

Este procedimento tem como objetivo atualizar a base de dados da Único através da coleta de informações no VTracker, processamento dos dados via R/RStudio e envio automático da planilha consolidada para o Google Drive da equipe de Dados.

Ao final do processo, o responsável deverá validar que a planilha foi enviada corretamente e comunicar a conclusão da atualização no canal **#unico** do Discord.

---
# Requisito

- Checar se a atualização da base da XP já foi realizada. Pois utilizamos dados atualizados de lá.

# Frequência da Atualização

> **Periodicidade:** Semanal, às sextas-feiras

# Visão Geral do Processo

O fluxo completo consiste em:

1. Atualizar o repositório do projeto.
2. Baixar os arquivos necessários no VTracker.
3. Salvar os arquivos na pasta correta.
4. Configurar o ambiente de execução.
5. Executar o script de processamento.
6. Validar a execução.
7. Confirmar o envio da planilha para o Google Drive.
8. Comunicar a atualização no Discord.

---

# Pré-requisitos

Antes de iniciar, confirme que possui acesso a:

## Ferramentas

* Git
* RStudio
* Ambiente R configurado
* Google Chrome
* VTracker
* Google Drive corporativo
* Discord corporativo

## Acessos Necessários

* Repositório do projeto Único
* Plataforma VTracker
* Drive da equipe de Dados
* Canal **#unico** no Discord

---

# Etapa 1 — Atualização do Repositório

Antes de qualquer execução, garanta que está utilizando a versão mais recente do projeto.

## Clonar o Repositório (primeira utilização)

```bash
git clone https://github.com/Lagos-Data-Intelligence/UnicoSemanal
```

### Importante

Sempre trabalhe com a versão mais recente do código para evitar incompatibilidades entre scripts e estrutura de pastas.

---

# Etapa 2 — Download dos Arquivos no VTracker

## Objetivo

Baixar os arquivos de ocorrências dos últimos 7 dias que serão utilizados pelo script de atualização da Único.

**IMPORTANTE:** Este processo deve ser realizado duas vezes:

1. Câmara Legislativa
2. Senado Federal

Ao finalizar o primeiro download, repita todo o procedimento para a segunda fonte.

---

## Acessar o VTracker

1. Abra o navegador.
2. Acesse o VTracker.
3. Realize o login com sua conta.

---

## Navegar para Monitoramento

Após o login:

1. Acesse a aba **Monitoramento**.
2. Aguarde o carregamento da listagem de ocorrências.

---

## Configurar o Período

1. Localize o filtro de período.
2. Selecione os **últimos 7 dias**.
3. Clique em **Filtrar**.

### Validação

Aguarde o carregamento dos resultados.

O sistema exibirá a quantidade total de ocorrências encontradas para o período selecionado.

---

## Selecionar Todas as Ocorrências

Após o carregamento:

1. Marque a caixa de seleção localizada à esquerda da tabela (próxima à opção de ocorrências por página).
2. Após marcar a caixa, aparecerá a mensagem:

```text
Clique aqui para selecionar todas as X ocorrências
```

3. Clique nessa mensagem.

### Importante

Não basta selecionar apenas os registros da página atual.

É obrigatório clicar em:

```text
Clique aqui para selecionar todas as X ocorrências
```

para garantir que TODAS as ocorrências do período serão exportadas.

---

## Exportar os Dados

Com todas as ocorrências selecionadas:

1. Localize o botão **Exportar** no canto direito da tela.
2. Clique em **Exportar**.
3. Selecione a opção:

```text
Excel
```

4. Aguarde o processamento da exportação.

---

## Acompanhar a Geração do Arquivo

A exportação não é baixada imediatamente.

Quando o processamento terminar:

1. Clique na **Caixa de Mensagens** (ícone de envelope localizado próximo ao perfil do usuário).
2. Procure pela mensagem:

```text
Exportação das ocorrências finalizada
```

### Importante

Enquanto essa mensagem não aparecer, o arquivo ainda está sendo preparado pelo sistema.

---

## Baixar o Arquivo Gerado

Após localizar a mensagem:

1. Clique na mensagem de exportação concluída.
2. Faça o download do arquivo para sua máquina.

## Salvar na Pasta do Projeto

Após o download:

1. Localize o arquivo baixado.
2. Mova o arquivo para a pasta:

```text
/data
```

ou para a pasta de dados definida pelo projeto.

## Repetir o Processo para a Segunda Fonte

Após concluir o download da primeira fonte:

Repita exatamente os mesmos passos para:

```text
Senado Federal
```

ou

```text
Câmara Legislativa
```

(dependendo de qual foi processada primeiro).

Ao final desta etapa, deverão existir dois arquivos baixados e armazenados na pasta de dados do projeto.

---

# Checklist da Etapa

Antes de prosseguir para a execução do script, confirme:

* [ ] Acessou Monitoramento
* [ ] Selecionou os últimos 7 dias
* [ ] Clicou em Filtrar
* [ ] Selecionou todas as ocorrências
* [ ] Clicou em "Clique aqui para selecionar todas as X ocorrências"
* [ ] Exportou para Excel
* [ ] Aguardou a mensagem de exportação concluída
* [ ] Baixou o arquivo pelo envelope de mensagens
* [ ] Moveu o arquivo para a pasta /data
* [ ] Repetiu o processo para a segunda fonte
* [ ] Os dois arquivos estão disponíveis para processamento


# Etapa 3 — Organizar os Arquivos

Após o download:

1. Localize os arquivos baixados.
2. Mova-os para a pasta utilizada pelo projeto.

Exemplo:

```text
projeto/
└── data/
```

ou

```text
projeto/
└── dados/
```

### Importante

* Não alterar o nome dos arquivos.
* Não extrair manualmente os arquivos ZIP.
* Não abrir os arquivos em Excel antes da execução.

A extração será realizada automaticamente pelo script.

---

# Etapa 4 — Abrir o Projeto no RStudio

1. Abrir o RStudio.
2. Abrir o projeto da Único.
3. Aguardar o carregamento completo.

Verifique se todos os scripts aparecem normalmente no painel do projeto.

---

# Etapa 5 — Localização do Arquivo com file.choose()

Caso seja necessário atualizar o caminho do arquivo de entrada:

No Console do RStudio execute:

```r
file.choose()
```

Uma janela do Windows será aberta.

---

## Selecionar o Arquivo

1. Navegue até o arquivo baixado.
2. Selecione o arquivo correto.
3. Clique em "Abrir".

O R retornará algo semelhante a:

```r
"C:\\Projetos\\Unico\\data\\arquivo.zip"
```

Copie esse caminho.

---

# Etapa 6 — Atualizar o Path no Script

Localize no script a variável responsável pelo arquivo de entrada.

Exemplo:

```r
zip_file <- "C:\\Projetos\\Unico\\data\\arquivo.zip"
```

Substitua pelo caminho retornado pelo comando:

```r
file.choose()
```

---

# Etapa 7 — Conferir Configurações do Script

Antes da execução, confirme:

* Arquivo correto selecionado.
* Diretório correto.
* Dados mais recentes disponíveis.
* Nenhum arquivo aberto em Excel.

---

# Etapa 8 — Executar o Script Principal

Abra o script principal.

Exemplo observado:

```text
Unico_Semanal.R
```

Execute o script completo.

---

# O que o Script Faz

Durante a execução o script:

1. Carrega bibliotecas.
2. Autentica serviços Google.
3. Processa arquivos baixados.
4. Extrai arquivos ZIP.
5. Consolida os dados.
6. Realiza tratamentos e transformações.
7. Gera a base final.
8. Envia a planilha consolidada para o Google Drive.

---

# Etapa 9 — Aguardar a Conclusão

Durante a execução:

### Não faça

* Não fechar o RStudio.
* Não interromper o processo.
* Não reiniciar o computador.
* Não fechar janelas utilizadas pelo processo.

---

# Etapa 10 — Verificar se Houve Erro

Ao final da execução:

## Sucesso

O console finaliza normalmente.

Sem mensagens vermelhas.

Sem interrupções.

---

## Falha

Caso apareçam erros:

1. Capturar print da tela.
2. Salvar a mensagem completa.
3. Informar a equipe responsável.

### Nunca

* Alterar o código por conta própria.
* Ignorar mensagens de erro.
* Reexecutar indefinidamente sem entender a falha.

---

# Etapa 11 — Validar Arquivos Processados

Verifique se a pasta de extração foi criada corretamente.

Exemplo:

```text
data/
└── unzipped/
```

Os arquivos devem ter sido processados sem necessidade de intervenção manual.

---

# Etapa 12 — Confirmar Envio para o Google Drive

Esta é a validação mais importante do processo.

A atualização NÃO deve ser considerada concluída apenas porque o script terminou.

---

## Acessar o Google Drive

1. Abrir o Drive da equipe.
2. Navegar até a pasta utilizada pela área de Dados.

---

## Verificar a Planilha Gerada

Confirmar:

* Existência da planilha.
* Data de atualização correta.
* Arquivo mais recente disponível.

### Resultado Esperado

A planilha gerada pelo script deve aparecer no Google Drive após a execução.

Caso a planilha não esteja presente:

* Considere o processo incompleto.
* Verifique possíveis erros na execução.
* Acione a equipe responsável.

---

# Como Saber se a Atualização Deu Certo?

A atualização só pode ser considerada concluída quando TODOS os critérios abaixo forem atendidos:

* Script executado até o final.
* Nenhum erro apresentado.
* Arquivos processados corretamente.
* Planilha final gerada.
* Planilha enviada para o Google Drive.
* Planilha localizada no Drive da equipe.

Se qualquer um desses itens falhar, a atualização não foi concluída.

---

# Etapa 13 — Comunicação da Atualização

Após validar o envio da planilha para o Google Drive:

1. Abrir o Discord.
2. Localizar o canal:

```text
#unico
```

3. Informar a conclusão da atualização.

---

## Modelo de Mensagem

```text
Único Semanal atualizado  @Responsável_pelo_alerta
Segue o link: (link da planilha gerada no google drive)

```
link da pasta do google drive onde estará a planilha: https://drive.google.com/drive/folders/1eNs_ZuaHTBewYTWt1XW4W6XkxqKsnkGB
---

# Checklist Final

Antes de encerrar a atividade, confirme:

* [ ] Repositório atualizado
* [ ] Arquivos baixados no VTracker
* [ ] Arquivos movidos para a pasta correta
* [ ] Path configurado corretamente
* [ ] Script executado
* [ ] Nenhum erro apresentado
* [ ] Arquivos processados
* [ ] Planilha gerada
* [ ] Planilha encontrada no Google Drive
* [ ] Atualização comunicada no canal #unico

Somente após todos os itens acima o processo deve ser considerado concluído.

---

# Notas Técnicas Importantes

## Escape de Caracteres no Windows

Sempre utilize:

```r
"C:\\pasta\\arquivo.zip"
```

ou

```r
"C:/pasta/arquivo.zip"
```

Nunca utilize:

```r
"C:\pasta\arquivo.zip"
```

pois o R interpreta a barra invertida como caractere especial.

---

## Troca de Máquina ou Usuário

Ao utilizar outro computador ou perfil Windows:

Execute novamente:

```r
file.choose()
```

para obter o novo caminho absoluto do arquivo.

---

## Arquivos Abertos

Antes de executar o script:

* Feche Excel.
* Feche LibreOffice.
* Feche qualquer programa utilizando os arquivos.

Arquivos abertos podem impedir a leitura e causar falhas na execução.

---

# FAQ

## Qual a frequência dessa alimentação?

Semanal, ocorre às sextas-feiras.

## Preciso extrair os ZIPs manualmente?

Não. O script faz isso automaticamente.

---

## Posso alterar o nome dos arquivos baixados?

Não. Os arquivos devem manter o nome original.

---

## Posso abrir o arquivo antes da execução?

Não é recomendado.

---

## Como saber se deu certo?

Verifique se a planilha final foi enviada para o Google Drive da equipe.

---

## O script terminou sem erro. Posso encerrar?

Não.

Primeiro confirme que a planilha foi enviada para o Google Drive.

---

## Qual é a última etapa obrigatória?

Enviar a comunicação de atualização concluída no canal **#unico** do Discord.

# Guia Completo de Atualização dos Dados - CNseg Assembleias Legislativas Performance

## Objetivo

Este procedimento tem como objetivo atualizar diariamente a base de dados do projeto **CNseg Assembleias Legislativas Performance**, realizando a coleta das publicações do dia no FanPageKarma, processando-as através do script em R e enviando automaticamente os dados atualizados para a base utilizada pela equipe.

Ao final da execução, o responsável deverá validar que o script foi executado corretamente e comunicar a conclusão da atualização no Discord.

---

# Frequência da Atualização

> **Periodicidade:** Diária

A atualização deve ser realizada **todos os dias**, preferencialmente **no período da tarde**, coletando apenas as publicações referentes ao dia atual.

---

# Visão Geral do Processo

O fluxo completo consiste em:

1. Atualizar o repositório do projeto.
2. Configurar o ambiente do R.
3. Acessar o FanPageKarma.
4. Atualizar os dados do dashboard.
5. Exportar as publicações do dia.
6. Colocar o arquivo na pasta `/data`.
7. Executar o script `AssembleiasEstaduais.R`.
8. Validar que o script foi executado corretamente.
9. Comunicar a atualização no Discord.

---

# Pré-requisitos

Antes de iniciar, confirme que possui acesso a:

## Ferramentas

* Git
* RStudio
* Ambiente R configurado
* Google Chrome
* FanPageKarma
* Discord

## Acessos

* Repositório do projeto
* Planilha corporativa de senhas
* FanPageKarma
* Canal **#cnseg** no Discord

---

# Etapa 1 — Atualizar o Repositório

Antes de iniciar qualquer atualização, garanta que está utilizando a versão mais recente do projeto.

## Primeira utilização

Clone o repositório:

```bash
git clone https://github.com/Lagos-Data-Intelligence/AssembleiasLegislativas
```

## Caso o projeto já exista

Atualize o repositório:

```bash
git pull
```

### Importante

Sempre utilize a versão mais recente do projeto para evitar incompatibilidades.

---

# Etapa 2 — Configurar o Ambiente do R

Caso esteja utilizando outra máquina ou usuário Windows, configure o caminho do arquivo de entrada.

No Console do RStudio execute:

```r
file.choose()
```

Será aberta uma janela do Windows.

Selecione o arquivo que será utilizado.

O R retornará um caminho semelhante a:

```r
"C:\\ProjetosLagos\\AssembleiasLegislativas\\data\\arquivo.xlsx"
```

Copie esse caminho.

---

## Atualizar o caminho no Script

Localize a variável correspondente ao diretório de trabalho.

Exemplo:

```r
setwd("C:\\Local\\data\\")
```

Substitua pelo diretório correspondente à sua máquina.

---

# Etapa 3 — Acessar o FanPageKarma

Acesse:

https://app.fanpagekarma.com/login

Realize o login utilizando as credenciais disponíveis na **planilha corporativa de senhas**.

**Importante:** O login deve ser realizado utilizando a autenticação via Facebook.

---

# Etapa 4 — Abrir o Dashboard

Após o login:

Localize o dashboard:

```text
CnSeg :: Assembleias Estaduais
```

Abra o dashboard.

---

# Etapa 5 — Acessar a Aba Content

Dentro do dashboard:

1. Clique na aba **Content**.

Esta será a tela utilizada para realizar a coleta diária.

---

# Etapa 6 — Configurar o Período

Na área de filtros:

Selecione:

```text
Today
```

ou escolha manualmente a **data atual**.

### Importante

A coleta deve conter **somente os dados do dia da atualização**.

Não utilize períodos maiores.

---

# Etapa 7 — Atualizar os Dados

Após aplicar o filtro:

Clique no botão amarelo:

```text
Update now
```

Aguarde o processamento completo.

### Importante

Não prossiga para a exportação antes da conclusão da atualização.

A aba deve estar completamente atualizada antes de continuar.

---

# Etapa 8 — Exportar os Dados

Após a atualização:

1. Acesse a aba:

```text
Top 5000 posts overview
```

2. No canto superior direito clique nos **três pontos**.

3. Clique em:

```text
Export
```

4. Escolha o formato:

```text
Excel
```

Aguarde o download do arquivo.

---

# Etapa 9 — Organizar o Arquivo

Após concluir o download:

Localize o arquivo baixado.

Mova-o para:

```text
/data
```

na raiz do projeto.

### Importante

* Não alterar o nome do arquivo.
* Não abrir o arquivo no Excel antes da execução.
* Deve existir apenas o arquivo correspondente ao dia da atualização.

---

# Etapa 10 — Executar o Script

Abra o projeto no RStudio.

Abra o arquivo:

```text
AssembleiasEstaduais.R
```

Execute o script completo.

---

# O que o Script Faz

Durante a execução o script:

* Carrega as bibliotecas necessárias.
* Processa o arquivo exportado.
* Realiza os tratamentos dos dados.
* Identifica projetos relacionados.
* Atualiza automaticamente a base de dados.
* Envia os dados consolidados para a planilha utilizada pela equipe.

---

# Etapa 11 — Validação dos Projetos

Antes do envio final, é necessário verificar os projetos encontrados pelo processamento.

### Importante

Nem todas as Assembleias citarão projetos de interesse.

Por isso:

* confirme se os projetos encontrados realmente existem;
* valide se estão corretos;
* confirme que pertencem à base monitorada.

Caso nenhum projeto seja encontrado, o trecho responsável pelo envio dos projetos ficará vazio. Nessa situação, **não execute a etapa de envio dos projetos**, pois ela não terá efeito.

---

# Etapa 12 — Validar a Execução

Ao término do script:

Verifique:

* ausência de erros no Console;
* execução completa do script;
* atualização da planilha de destino.

### Resultado esperado

O script finaliza normalmente e envia automaticamente os novos dados para a base.

---

# Etapa 13 — Comunicação da Atualização

Após confirmar que a execução foi concluída:

Abra o Discord.

Acesse o canal:

```text
#cnseg
```

Dentro do canal, localize a thread:

```text
Monitoramento Assembleias Redes Sociais
```

Envie uma mensagem informando a conclusão da atualização.

### Modelo

```text
Os dados das Assembleias já estão disponíveis. @Responsavel_pelo_alerta
```

---

# Checklist Final

Antes de encerrar a atividade, confirme:

* [ ] Repositório atualizado
* [ ] Ambiente configurado
* [ ] Login realizado no FanPageKarma
* [ ] Dashboard correto aberto
* [ ] Aba Content acessada
* [ ] Período configurado para Today
* [ ] Botão Update now executado
* [ ] Atualização concluída
* [ ] Exportação em Excel realizada
* [ ] Arquivo movido para a pasta `/data`
* [ ] Script `AssembleiasEstaduais.R` executado
* [ ] Projetos validados
* [ ] Script finalizado sem erros
* [ ] Dados enviados automaticamente para a base
* [ ] Atualização comunicada na thread **Monitoramento Assembleias Redes Sociais**

---

# Notas Técnicas

## Atualização Diária

Este processo deve ser executado diariamente.

Sempre utilize apenas os dados referentes ao dia da atualização.

---

## Configuração do Ambiente

Ao trocar de computador ou usuário Windows, execute novamente:

```r
file.choose()
```

para localizar corretamente os arquivos.

---

## Arquivos

Nunca altere o nome do arquivo exportado.

---

## Excel

Evite abrir o arquivo antes da execução do script.

Arquivos abertos podem impedir a leitura pelo R.

---

# FAQ

## Qual período devo selecionar?

Sempre **Today** (ou a data do dia atual).

---

## Posso baixar mais de um dia?

Não. A rotina foi desenvolvida para processar apenas as publicações do dia.

---

## Qual dashboard devo acessar?

**CnSeg :: Assembleias Estaduais**.

---

## Qual aba devo utilizar?

**Content**.

---

## Preciso clicar em "Update now"?

Sim. A exportação só deve ser realizada após a atualização completa dos dados.

---

## De onde exporto os dados?

Na aba **Top 5000 posts overview**, clicando nos três pontos no canto superior direito e escolhendo **Export > Excel**.

---

## Qual formato devo baixar?

Sempre **Excel (.xlsx)**.

---

## Onde devo colocar o arquivo baixado?

Na pasta:

```text
/data
```

do projeto.

---

## Qual script devo executar?

```text
AssembleiasEstaduais.R
```

---

## O script envia os dados automaticamente?

Sim. Ao finalizar com sucesso, o script atualiza automaticamente a base de dados utilizada pela equipe.

---

## Preciso verificar os projetos encontrados?

Sim. Antes do envio, confirme se os projetos identificados realmente existem e pertencem à base monitorada.

---

## O que fazer se nenhum projeto for encontrado?

Não execute a etapa de envio dos projetos. O trecho correspondente ficará vazio e essa situação é esperada em alguns dias.

---

## Como sei que a atualização terminou?

Quando o script finalizar sem erros e os dados forem enviados automaticamente para a base.

---

## O que devo fazer após concluir a atualização?

Enviar uma mensagem na thread **Monitoramento Assembleias Redes Sociais**, dentro do canal **#cnseg**, informando que a atualização diária foi concluída.

