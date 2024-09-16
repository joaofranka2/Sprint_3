import csv
import os
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Carregar dados de perguntas e respostas do CSV
def carregar_perguntas_respostas(csv_file):
    try:
        df = pd.read_csv(csv_file, encoding='utf-8')
        if 'pergunta' not in df.columns or 'resposta' not in df.columns:
            raise ValueError("O arquivo CSV deve conter as colunas 'pergunta' e 'resposta'.")
        return df.to_dict('records')
    except Exception as e:
        print(f"Erro ao carregar o arquivo: {e}")
        return []

# Função para calcular a similaridade usando TF-IDF
def calcular_similaridade_tfidf(pergunta, perguntas_respostas):
    perguntas = [item['pergunta'] for item in perguntas_respostas]
    perguntas.append(pergunta)
    
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(perguntas)
    
    cosine_similarities = cosine_similarity(tfidf_matrix[-1], tfidf_matrix[:-1])
    return cosine_similarities.flatten()

# Função para detectar a intenção da pergunta
def detectar_intencao(pergunta, perguntas_respostas):
    similaridades = calcular_similaridade_tfidf(pergunta, perguntas_respostas)
    max_similarity_index = similaridades.argmax()
    max_similarity = similaridades[max_similarity_index]
    
    threshold = 0.3  # Ajuste conforme necessário
    if max_similarity > threshold:
        return perguntas_respostas[max_similarity_index]['resposta']
    else:
        return "Desculpe, eu não entendi essa pergunta."

# Função para responder a pergunta com personalização de contexto
def responder_pergunta(pergunta, perguntas_respostas, contexto):
    resposta = detectar_intencao(pergunta, perguntas_respostas)
    for chave in contexto:
        resposta = resposta.replace(f"{{{chave}}}", contexto[chave])
    return resposta

# Função para atualizar o contexto com informações do usuário
def atualizar_contexto(pergunta, contexto):
    if "meu nome é" in pergunta.lower():
        nome = pergunta.split("meu nome é")[-1].strip()
        contexto["nome"] = nome
        print(f"Prazer em te conhecer, {nome}!")
        return True
    elif "minha área é" in pergunta.lower():
        area = pergunta.split("minha área é")[-1].strip()
        contexto["area"] = area
        print(f"Entendi, você trabalha na área de {area}.")
        return True
    return False

# Função para salvar feedback usando pd.concat
def salvar_feedback(feedback_df, pergunta, resposta, util):
    novo_feedback = pd.DataFrame({'Pergunta': [pergunta], 'Resposta': [resposta], 'Util': [util]})
    feedback_df = pd.concat([feedback_df, novo_feedback], ignore_index=True)
    return feedback_df

# Função para adicionar nova pergunta e resposta ao CSV
def adicionar_nova_pergunta(pergunta, resposta, csv_file='perguntas_respostas.csv'):
    nova_linha = pd.DataFrame({'pergunta': [pergunta], 'resposta': [resposta]})
    nova_linha.to_csv(csv_file, mode='a', header=False, index=False)
    print(f"Nova pergunta e resposta adicionadas: {pergunta} -> {resposta}")

# Carregar perguntas e respostas do CSV
perguntas_respostas = carregar_perguntas_respostas('perguntas_respostas.csv')

# Inicializar contexto da conversa, histórico e feedback DataFrame
contexto = {}
feedback_df = pd.DataFrame(columns=['Pergunta', 'Resposta', 'Util'])
historico_conversa = []

# Loop principal com personalização, histórico e feedback
print("Olá! Eu sou o Chatbot. Como posso te ajudar hoje?")
while True:
    pergunta = input("Faça uma pergunta (ou digite 'sair' para encerrar): ")
    if pergunta.lower() == "sair":
        print("Até mais!")
        break

    # Atualizar contexto
    if atualizar_contexto(pergunta, contexto):
        historico_conversa.append({"pergunta": pergunta, "resposta": None})  # Atualiza o histórico
        continue

    resposta = responder_pergunta(pergunta, perguntas_respostas, contexto)
    
    # Verificar se a resposta é desconhecida e oferecer adicionar uma nova
    if resposta == "Desculpe, eu não entendi essa pergunta.":
        print(resposta)
        adicionar = input("Gostaria de adicionar uma resposta para esta pergunta? (sim/não): ").strip().lower()
        if adicionar == "sim":
            nova_resposta = input("Digite a resposta para esta pergunta: ").strip()
            adicionar_nova_pergunta(pergunta, nova_resposta)
            perguntas_respostas = carregar_perguntas_respostas('perguntas_respostas.csv')  # Recarregar as perguntas
        continue

    print(resposta)

    # Adicionar ao histórico
    historico_conversa.append({"pergunta": pergunta, "resposta": resposta})

    # Solicitar feedback do usuário
    util = input("Essa resposta foi útil? (sim/não): ").strip().lower()
    util = True if util == "sim" else False if util == "não" else None

    if util is not None:
        feedback_df = salvar_feedback(feedback_df, pergunta, resposta, util)
        print("Obrigado pelo seu feedback!")
    else:
        print("Resposta inválida. Feedback não registrado.")

# Salvar histórico da conversa em um arquivo
pd.DataFrame(historico_conversa).to_csv('historico_conversa.csv', index=False)

# Salvar feedback ao final do loop
if not feedback_df.empty:
    feedback_df.to_csv('feedback.csv', mode='a', header=not os.path.exists('feedback.csv'), index=False)
    print("Feedback salvo com sucesso!")
