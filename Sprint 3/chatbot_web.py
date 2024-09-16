from flask import Flask, render_template, request, redirect, url_for, session
import os
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)
app.secret_key = 'super_secret_key'  # Necessário para usar sessões

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

# Função para adicionar nova pergunta e resposta ao CSV
def adicionar_nova_pergunta(pergunta, resposta, csv_file='perguntas_respostas.csv'):
    nova_linha = pd.DataFrame({'pergunta': [pergunta], 'resposta': [resposta]})
    nova_linha.to_csv(csv_file, mode='a', header=False, index=False)
    print(f"Nova pergunta e resposta adicionadas: {pergunta} -> {resposta}")

# Função para salvar feedback
def salvar_feedback(pergunta, resposta, util):
    feedback = pd.DataFrame({'Pergunta': [pergunta], 'Resposta': [resposta], 'Util': [util]})
    feedback.to_csv('feedback.csv', mode='a', header=not os.path.exists('feedback.csv'), index=False)

# Carregar perguntas e respostas do CSV
perguntas_respostas = carregar_perguntas_respostas('perguntas_respostas.csv')

# Rota principal
@app.route('/', methods=['GET', 'POST'])
def index():
    if 'historico' not in session:
        session['historico'] = []

    if request.method == 'POST':
        pergunta = request.form['pergunta']
        resposta = detectar_intencao(pergunta, perguntas_respostas)
        
        # Adicionar ao histórico na sessão
        session['historico'].append({'pergunta': pergunta, 'resposta': resposta})
        session.modified = True  # Marcar a sessão como modificada

        # Adicionar nova pergunta e resposta se não reconhecida
        if resposta == "Desculpe, eu não entendi essa pergunta.":
            return render_template('index.html', resposta=resposta, pergunta=pergunta, adicionar=True, historico=session['historico'])

        return render_template('index.html', resposta=resposta, historico=session['historico'])

    return render_template('index.html', historico=session['historico'])

# Rota para adicionar nova pergunta
@app.route('/adicionar', methods=['POST'])
def adicionar():
    pergunta = request.form['nova_pergunta']
    resposta = request.form['nova_resposta']
    adicionar_nova_pergunta(pergunta, resposta)
    
    # Recarregar as perguntas e respostas
    global perguntas_respostas
    perguntas_respostas = carregar_perguntas_respostas('perguntas_respostas.csv')
    
    return redirect(url_for('index'))

# Rota para processar feedback
@app.route('/feedback', methods=['POST'])
def feedback():
    pergunta = request.form['pergunta']
    resposta = request.form['resposta']
    util = request.form['feedback'] == 'sim'
    
    salvar_feedback(pergunta, resposta, util)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
