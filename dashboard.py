import streamlit as st
import mysql.connector
import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('punkt_tab')

def conectar_banco():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="959493",
        database="analise_feedback"
    )

def classificar_sentimento(texto):
    texto = texto.lower()
    if any(palavra in texto for palavra in ["ruim", "péssimo", "horrível", "lento", "odiei", "fraco", "não atendeu"]):
        return "Negativo"
    elif any(palavra in texto for palavra in ["ótimo", "excelente", "gostei", "bom", "maravilhoso", "recomendo", "atrativo", "amei"]):
        return "Positivo"
    else:
        return "Neutro"

def carregar_comentarios():
    conn = conectar_banco()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT id, texto, hora FROM comentarios ORDER BY hora DESC")
    dados = cursor.fetchall()
    conn.close()
    return pd.DataFrame(dados)

def contar_palavras(df):
    stop_words = set(stopwords.words('portuguese'))
    todas = " ".join(df["texto"].tolist()).lower()
    palavras = word_tokenize(todas)
    palavras_filtradas = [p for p in palavras if p.isalpha() and p not in stop_words]
    contagem = Counter(palavras_filtradas)
    return contagem.most_common(15)

st.set_page_config(page_title="Dashboard de Comentários", layout="wide")
st.title("🧠 Dashboard de Feedbacks")

df = carregar_comentarios()
df["Sentimento"] = df["texto"].apply(classificar_sentimento)

col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("📝 Comentários")
    st.dataframe(df[["hora", "texto", "Sentimento"]], height=500, use_container_width=True)

with col2:
    st.subheader("📊 Análise de Sentimentos")
    st.bar_chart(df["Sentimento"].value_counts())

stop_words = set(stopwords.words('portuguese'))
todas_palavras = []

for texto in df['texto']:
    palavras = word_tokenize(texto.lower())
    palavras_filtradas = [p for p in palavras if p.isalpha() and p not in stop_words]
    todas_palavras.extend(palavras_filtradas)

frequencia = Counter(todas_palavras).most_common(10)
palavras, contagens = zip(*frequencia)

st.subheader("📊Palavras Mais Usadas")
palavras_df = pd.DataFrame({'Palavras': palavras, 'Frequência': contagens})
palavras_df.set_index('Palavras', inplace=True)
st.bar_chart(palavras_df)