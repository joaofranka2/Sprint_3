# Sprint_3 IA


## Integrantes

552421 - Flavio Sousa Vasconcelos

552368 - WELLINGTON DE OLIVEIRA URCINO DA SILVA

97887 - João Carlos França Figueiredo

550200 - Leonardo Oliveira Esparza

## 📋 Sumário
1. [Introdução](#introdução)
2. [Objetivos do Projeto](#objetivos-do-projeto)
3. [Funcionalidades](#funcionalidades)
4. [Arquitetura do Projeto](#arquitetura-do-projeto)
5. [Base de Dados](#base-de-dados)
6. [Como Executar o Projeto](#como-executar-o-projeto)
7. [Demonstração](#demonstração)
8. [Contribuindo](#contribuindo)
9. [Próximas Etapas](#próximas-etapas)
10. [Licença](#licença)

## Introdução
O Chatbot de Assistência ao Currículo é uma aplicação web desenvolvida para fornecer orientações rápidas e precisas sobre a elaboração e melhoria de currículos. Utilizando um conjunto pré-definido de perguntas e respostas, ele permite que usuários obtenham conselhos relevantes para melhorar a qualidade de seus currículos de maneira prática e eficiente.

## Objetivos da sprint 3
- **Demonstração do protótipo funcional**: Apresentar as funcionalidades implementadas, como resposta a perguntas e histórico de conversas.
- **Detalhamento da arquitetura de IA**: Explicar a implementação e o funcionamento do modelo de similaridade TF-IDF.
- **Apresentação da base de dados**: Descrever o uso do arquivo CSV para armazenar as perguntas e respostas.

## Funcionalidades
- **Resposta a perguntas**: O chatbot responde a perguntas relacionadas à melhoria de currículos usando um modelo de processamento de linguagem natural.
- **Histórico de conversas**: Mantém um registro das interações, facilitando o acompanhamento das respostas.
- **Expansibilidade**: O conjunto de perguntas e respostas pode ser facilmente atualizado por meio de um arquivo CSV.
- **Design responsivo**: A interface é estilizada em um tema escuro para melhorar a experiência do usuário.

## Arquitetura do Projeto
O projeto foi construído com as seguintes tecnologias:
- **Python**: Linguagem principal utilizada para o desenvolvimento do chatbot.
- **Flask**: Framework web usado para a criação da interface e gerenciamento de rotas.
- **Scikit-learn**: Para implementar o modelo de análise de similaridade usando TF-IDF.
- **Pandas**: Para manipulação e leitura de dados do arquivo CSV.
- **HTML/CSS**: Para desenvolver a interface do usuário do chatbot.

### Diagrama da Arquitetura

O fluxo do chatbot segue os seguintes passos:
1. O usuário insere uma pergunta na interface web.
2. A aplicação usa o modelo de similaridade de texto baseado em TF-IDF para encontrar a resposta mais relevante no banco de dados (arquivo CSV).
3. A resposta é retornada e exibida na interface, juntamente com o histórico de conversas.

## Base de Dados
A base de conhecimento do chatbot é alimentada por um arquivo CSV chamado `perguntas_respostas.csv`, contendo três colunas:
- **pergunta**: A pergunta que o usuário pode fazer.
- **resposta**: A resposta correspondente fornecida pelo chatbot.
- **descrição**: Informações adicionais que enriquecem a resposta.

Outros arquivos utilizados incluem:
- **`historico_conversa.csv`**: Armazena o histórico de interações do usuário.
- **`feedback.csv`**: Registra o feedback dos usuários sobre a utilidade das respostas.

## Como Executar o Projeto
### Pré-requisitos
- Python 3.x instalado.
- Bibliotecas necessárias: Flask, pandas, scikit-learn.


## Passo a Passo Simplificado para Uso do Código

Baixe o projeto:

Clique no botão verde "Code" na página do GitHub e escolha "Download ZIP".
Extraia o conteúdo do arquivo ZIP em uma pasta de sua escolha.
Abra o terminal:

No Windows: Use "Prompt de Comando" ou "PowerShell".
No Mac/Linux: Use o "Terminal".
Navegue até a pasta do projeto:

Use o comando cd para entrar na pasta onde você extraiu o projeto. Exemplo

cd caminho/para/a/pasta-do-projeto

Inicie o chatbot:

No mesmo terminal, rode o comando:

python chatbot_web.py

Acesse o chatbot no navegador:

Abra seu navegador (Chrome, Firefox, etc.) e digite:

http://127.0.0.1:5000/

Agora você verá a página do chatbot!
Faça suas perguntas:

Na página do chatbot, escreva uma pergunta sobre currículos e clique no botão "Enviar".
O chatbot responderá com dicas e conselhos sobre como melhorar seu currículo.
Para parar o chatbot:

No terminal onde você iniciou o chatbot, pressione Ctrl + C para parar o servidor.
Como adicionar mais perguntas e respostas
Abra o arquivo perguntas_respostas.csv em um editor de texto (Bloco de Notas, Excel, etc.).
Adicione novas linhas com suas perguntas e respostas, seguindo o formato das outras linhas.
Salve o arquivo e reinicie o chatbot seguindo os passos 5 e 6.
