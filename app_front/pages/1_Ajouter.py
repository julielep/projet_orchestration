import streamlit as st
import requests
from dotenv import load_dotenv
import os

load_dotenv()

API_URL = os.getenv("STREAMLIT_API_URL", "http://api_backend:8000")

st.set_page_config(page_title="Mini Calculatrice API", page_icon="🧮")

st.title("🧮 Application de calcul")

# -------------------------
# SECTION INSERTION
# -------------------------

st.subheader("➕ Additionner deux nombres")

# Inputs numériques
a = st.number_input("Entrez la valeur de a", value=0.0)
b = st.number_input("Entrez la valeur de b", value=0.0)

if st.button("Calculer et sauvegarder"):
    try:
        response = requests.post(f"{API_URL}/data/", json={"a": a, "b": b})
        response.raise_for_status()

        result_data = response.json()

        st.success("Calcul effectué et sauvegardé ✅")
        st.write(f"Résultat : {result_data['result']}")

        st.json(result_data)

    except requests.exceptions.RequestException as e:
        st.error(f"Erreur API : {e}")
