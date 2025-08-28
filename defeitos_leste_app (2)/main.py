
import streamlit as st

st.set_page_config(page_title="Defeitos Leste App", layout="wide")

st.title("Bem-vindo ao App de Defeitos Leste")

menu = {
    "admin": "pages/admin.py",
    "leste": "pages/leste.py"
}

st.markdown("### Escolha seu perfil para continuar:")
col1, col2 = st.columns(2)

with col1:
    if st.button("Entrar como Admin"):
        st.switch_page(menu["admin"])

with col2:
    if st.button("Entrar como Leste"):
        st.switch_page(menu["leste"])
