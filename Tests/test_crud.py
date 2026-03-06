from app_api.api import app, get_db
from app_api.Database.database import Base
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# 1. On crée une base SQLite en mémoire pour les tests
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 2. On crée les tables dans la base de test
Base.metadata.create_all(bind=engine)

# 3. On remplace la dépendance get_db par notre base de test
def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)


def test_create_data():
    # Ce test va maintenant écrire dans SQLite au lieu de PostgreSQL !
    response = client.post("/data/", json={"a": 2, "b": 3})
    assert response.status_code == 200
    assert response.json()["result"] == 5
