# 1. Utilise l'image Python officielle
FROM python:3.11-slim-bookworm

# 2. INSTALLATION DE UV : C'est cette ligne qui manquait (Erreur 127)
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

# 3. Copie des fichiers de dépendances (avec l'astuce pour le lock)
COPY pyproject.toml  ./
#J'ai enlevé le uv.lock car il ne se créer pas dans mon dossier mais si il est présent alors on ajoute uv.loc[k]
# 4. Installation des dépendances dans le système du conteneur
RUN uv pip install --system --no-cache -r pyproject.toml

# 5. Copie de TOUT le code (Notez bien l'espace entre les deux points)
COPY . .

# 6. Lancement (Vérifiez bien si c'est main.py ou streamlit_app.py !)
CMD ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]