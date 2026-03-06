# 🚀 Projet Orchestration MLOps

![Security](https://github.com/julielep/projet_orchestration/actions/workflows/ci.yml/badge.svg?branch=master&event=push)
![Quality & Tests](https://github.com/julielep/projet_orchestration/actions/workflows/ci.yml/badge.svg?branch=master)
![Python Version](https://img.shields.io/badge/python-3.11-blue.svg)
![Docker](https://img.shields.io/badge/docker-verified-blue.svg?logo=docker)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

Ce projet est une application complète orchestrée avec **Docker**, combinant un backend **FastAPI**, un frontend **Streamlit** et une base de données **PostgreSQL**. Il intègre un pipeline CI/CD robuste avec des tests unitaires, un scan de sécurité et une documentation automatisée.

---

## 📂 Arborescence du Projet

```text
projet_orchestration/
├── app_api/               # Backend FastAPI (Logique métier & ORM)
│   ├── api.py             # Point d'entrée de l'API
│   └── ...
├── app_front/             # Frontend Streamlit (Interface utilisateur)
│   ├── main.py            # Point d'entrée Streamlit
│   └── ...
├── Tests/                 # Suite de tests Pytest (CRUD & Connectivité)
├── docs/                  # Documentation technique Sphinx
├── .github/workflows/     # CI/CD (GitHub Actions)
│   ├── ci.yml             # Tests, Linting & Security
│   └── cd.yml             # Docker Build & Deployment Check
├── docker-compose.yml     # Orchestration des services
├── pyproject.toml         # Gestion des dépendances (uv/pip)
└── .env.example           # Template des variables d'environnement
```

## 🛠️ Configuration Initiale
### 1. Variables d'environnement
Le projet nécessite un fichier .env à la racine pour fonctionner.
Note : Le fichier .env réel est ignoré par Git pour des raisons de sécurité.

Créez un fichier .env en vous basant sur cet exemple :
```
# Configuration PostgreSQL
POSTGRES_USER=myuser
POSTGRES_PASSWORD=mypassword
POSTGRES_DB=app_db

# URLs de connexion
DATABASE_URL=postgresql://myuser:mypassword@database:5432/app_db
API_URL=http://api_backend:8000
```

### 2. Installation locale (sans Docker)
Si vous souhaitez lancer les services individuellement avec uv :
```
# Installation des dépendances
uv sync

# Lancement du backend
uv run uvicorn app_api.api:app --reload

# Lancement du frontend (dans un autre terminal)
uv run streamlit run app_front/main.py
```

## 🐳 Lancement avec Docker (Recommandé)
L'ensemble de la stack peut être lancée en une seule commande grâce à l'orchestration Docker :
```
# Construction et lancement des conteneurs
docker compose up -d --build

# Vérifier l'état des services
docker compose ps
```

-> 3 services s'activent : (à modifier)
```
NAME              IMAGE                           COMMAND                  SERVICE    CREATED         STATUS         PORTS
postgres_db       postgres:15-alpine              "docker-entrypoint.s…"   database   5 hours ago     Up 5 hours     0.0.0.0:5432->5432/tcp, [::]:5432->5432/tcp       
streamlit_front   projet_orchestration-frontend   "streamlit run main.…"   frontend   7 seconds ago   Up 2 seconds   0.0.0.0:8501->8501/tcp, [::]:8501->8501/tcp       
```


- Frontend : Accessbile sur http://localhost:8501

- API (Swagger) : Accessible sur http://localhost:8000/docs


## 🧪 Tests et Qualité
Exécution des tests unitaires
Les tests sont automatisés dans la CI, mais peuvent être lancés localement :
```
uv run pytest --cov=app_api --cov=app_front .
```
Sécurité (Gitleaks)
Le projet utilise Gitleaks pour empêcher la fuite de secrets dans l'historique Git. Tout commit contenant une clé sensible sera bloqué par la CI.

## 📚 Documentation
La documentation technique est générée avec Sphinx et le thème Furo.
```
# Générer la documentation HTML
uv run sphinx-build -b html docs/source/ build/html
```

Pour consulter la doc, ouvrez ```start build/html/index.html``` dans votre navigateur.


## 🚀 CI/CD Workflow
Le projet utilise GitHub Actions pour automatiser le cycle de vie :

1. Job Security : Scan Gitleaks sur tout l'historique.

2. Job Quality : Linting avec Ruff et tests avec Pytest.

3. Job Docker : Build des images et test de connectivité réseau entre le Front et le Back.