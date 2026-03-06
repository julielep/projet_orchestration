# Image officielle Python 3.11 slim
FROM python:3.11-slim-bookworm

WORKDIR /app

# Copie des fichiers de dépendances
COPY pyproject.toml uv.lock ./

# Installation des dépendances
RUN pip install --no-cache-dir -r pyproject.toml

# # Copie du code source Streamlit
COPY . .

# Exposition du port Streamlit
EXPOSE 8501

# Lancement de Streamlit
CMD ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]