"""Tests/tests.maths.py
Test les fonctions mathématiques.
"""

from fastapi.testclient import TestClient
from app_api.api import app

client = TestClient(app)


def test_create_data():
    response = client.post("/data/", json={"a": 2, "b": 3})

    assert response.status_code == 200
    data = response.json()

    assert data["a"] == 2
    assert data["b"] == 3
    assert data["result"] == 5


def test_get_data():
    response = client.get("/data/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
