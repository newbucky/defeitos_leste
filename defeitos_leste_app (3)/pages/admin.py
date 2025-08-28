
import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Área do Admin", layout="wide")
st.title("Área do Administrador")

# Criar pasta data se não existir
os.makedirs("data", exist_ok=True)

# Upload do arquivo Excel
uploaded_file = st.file_uploader("Importar arquivo Excel (.xlsx)", type=["xlsx"])
if uploaded_file:
    try:
        df = pd.read_excel(uploaded_file, engine="openpyxl")
        df.to_csv("data/defeitos_leste.csv", index=False)
        st.success("Arquivo importado e salvo com sucesso como defeitos_leste.csv")
    except Exception as e:
        st.error(f"Erro ao importar o arquivo: {e}")

# Verificar se o CSV existe
csv_path = "data/defeitos_leste.csv"
if os.path.exists(csv_path):
    df = pd.read_csv(csv_path)
    st.subheader("Pré-visualização dos dados")
    st.dataframe(df.head())
else:
    st.warning("Nenhum arquivo CSV encontrado. Importe um arquivo Excel para começar.")
