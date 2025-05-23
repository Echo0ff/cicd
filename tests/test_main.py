from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/api/hello")
    assert response.status_code == 200
    assert "message" in response.json()