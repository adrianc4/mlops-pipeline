#  Run tests on windows with:
# $env:PYTHONPATH="."; pytest tests/
from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)


def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()


def test_predict():
    payload = {"features": [5.1, 3.5, 1.4, 0.2]}
    response = client.post("/predict", json=payload)
    assert response.status_code == 200
    assert "prediction" in response.json()
