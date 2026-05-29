from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["healthy"] is True

def test_get_libros():
    response = client.get("/libros")
    assert response.status_code == 200
    assert response.json()["total"] == 5

def test_get_libro():
    response = client.get("/libros/1")
    assert response.status_code == 200
    assert response.json()["titulo"] == "Cien años de soledad"
