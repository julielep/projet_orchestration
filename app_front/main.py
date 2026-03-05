import streamlit as st

st.set_page_config(
    page_title="Mini Calculatrice",
    page_icon="🧮",
    layout="centered"
)

st.title("🧮 Application de Calcul")

st.markdown("""
Bienvenue dans l'application.

Utilisez le menu à gauche pour :
- ➕ Insérer une opération
- 📖 Voir les résultats
""")

st.info("API FastAPI requise sur http://localhost:8000")