# Sprint_3 IA

552421 - Flavio Sousa Vasconcelos

552368 - WELLINGTON DE OLIVEIRA URCINO DA SILVA

97887 - João Carlos França Figueiredo

550200 - Leonardo Oliveira Esparza

1. Introdução
O Chatbot de Assistência ao Currículo é um aplicativo web desenvolvido para responder a perguntas relacionadas à elaboração e melhoria de currículos. Este chatbot usa um arquivo CSV com um conjunto pré-definido de perguntas e respostas e emprega um sistema de análise de similaridade de texto para fornecer respostas relevantes. Ele foi implementado em Python com o uso do framework Flask e um modelo de similaridade usando TF-IDF.

2. Arquitetura do Sistema
Linguagem de Programação: Python
Framework: Flask (para a construção do aplicativo web)
Bibliotecas:
pandas: para manipulação de dados do arquivo CSV.
sklearn (Scikit-learn): para calcular similaridade entre a entrada do usuário e as perguntas no CSV usando TF-IDF.
Front-end: HTML e CSS, embutidos no Flask para construir a interface web.

3. Funcionalidades
Entrada de Pergunta do Usuário: Permite que o usuário insira uma pergunta relacionada à melhoria de currículos.
Carregamento de Dados: O sistema carrega um arquivo CSV com perguntas, respostas e descrições que formam a base de conhecimento do chatbot.
Detecção de Intenção: Utiliza um modelo de similaridade de texto baseado em TF-IDF para identificar a pergunta mais similar no banco de dados e retornar uma resposta apropriada.
Resposta Contextualizada: O chatbot exibe a resposta correspondente e, quando disponível, apresenta uma descrição adicional para fornecer mais contexto.
Histórico de Conversa: A interface exibe um histórico das perguntas e respostas, ajudando o usuário a acompanhar suas interações.
Design Responsivo: A página HTML é estilizada com CSS para apresentar uma interface limpa, em tema escuro, tornando a experiência do usuário mais agradável.

4. Estrutura do Código

a. Arquivo Principal: chatbot_web.py
Bibliotecas Importadas:
flask: Para criar rotas e renderizar templates.
pandas: Para carregar e manipular dados do CSV.
sklearn.feature_extraction.text.TfidfVectorizer: Para calcular a similaridade entre a entrada do usuário e as perguntas no banco de dados.

Funções Chave:
carregar_perguntas_respostas(csv_file): Carrega as perguntas, respostas e descrições do arquivo CSV e retorna uma lista de dicionários.
calcular_similaridade_tfidf(pergunta, perguntas_respostas): Calcula a similaridade entre a pergunta do usuário e as perguntas no banco de dados usando TF-IDF.
detectar_intencao(pergunta, perguntas_respostas): Utiliza a função de similaridade para encontrar a resposta mais adequada.
Rota /: Controla a página principal do chatbot, incluindo a entrada do usuário e a exibição das respostas.

Fluxo Geral:
O usuário insere uma pergunta na interface web.
O Flask chama a função detectar_intencao para comparar a entrada do usuário com as perguntas no CSV.
A resposta mais relevante é exibida na interface, juntamente com uma possível descrição adicional.
O histórico da conversa é atualizado em tempo real.

b. Arquivo CSV: perguntas_respostas.csv
Contém três colunas: pergunta, resposta e descricao.
pergunta: A pergunta que pode ser feita pelo usuário.
resposta: A resposta que o chatbot deve fornecer quando a pergunta é detectada.
descricao: (Opcional) Informação adicional para contextualizar ou detalhar a resposta.

c. Arquivo HTML: index.html
Estrutura HTML para a interface do chatbot.
Inclui um formulário para entrada de perguntas do usuário.
Apresenta a resposta do chatbot e mantém um histórico da conversa.
Estilização com CSS para um tema escuro e elementos visuais como animações e transições.


5. Orientações para Uso
Requisitos:
Python 3.x
Bibliotecas: Flask, pandas, scikit-learn.
Arquivo CSV com as perguntas e respostas.

Execução:
Execute o servidor Flask com o comando:
python chatbot_web.py
Acesse o chatbot no navegador em: http://127.0.0.1:5000/

Interação:
Insira uma pergunta relacionada a melhorias de currículo.
O chatbot processa a pergunta e retorna a resposta mais adequada.
Visualize o histórico da conversa para acompanhar as interações.

6. Exemplo de Interações
Usuário: "Como posso melhorar meu currículo?"
Chatbot: "Para melhorar seu currículo, mantenha-o conciso e direto, destacando suas experiências mais relevantes. Use palavras-chave relacionadas à sua área e evite informações desnecessárias, como cursos que não agregam valor à vaga desejada."

7. Melhorias Futuras
Banco de Dados: Substituir o arquivo CSV por um banco de dados (SQLite, MySQL) para armazenamento e manipulação mais eficiente das perguntas e respostas.
Treinamento de Modelo de Linguagem: Implementar um modelo mais avançado de processamento de linguagem natural (NLP) para entender melhor as perguntas do usuário.
Upload Dinâmico: Permitir que usuários atualizem o arquivo CSV com novas perguntas e respostas diretamente pela interface.

8. Conclusão
O Chatbot de Assistência ao Currículo é uma ferramenta prática para ajudar usuários a aprimorar seus currículos. Com uma interface simples e uma lógica de comparação baseada em TF-IDF, ele responde a uma variedade de perguntas relacionadas ao desenvolvimento profissional.
