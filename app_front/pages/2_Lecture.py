import streamlit as st
import requests
from dotenv import load_dotenv
import os

load_dotenv()

API_URL = os.getenv(
    "STREAMLIT_API_URL", "http://api_backend:8000"
)  # Avant on était sur localhost mais maintenant api_backend qui est le nom du conteneur pour se connecter à la base de données

st.set_page_config(page_title="Mini Calculatrice API", page_icon="🧮")

st.title("🧮 Application de calcul")

# -------------------------
# SECTION LECTURE
# -------------------------

st.subheader("📖 Historique des opérations")

if st.button("Afficher l'historique"):
    try:
        response = requests.get(f"{API_URL}/data")
        response.raise_for_status()
        data = response.json()

        if data:
            st.table(data)
        else:
            st.info("Aucune donnée enregistrée.")
    except requests.exceptions.RequestException as e:
        st.error(f"Erreur API : {e}")
