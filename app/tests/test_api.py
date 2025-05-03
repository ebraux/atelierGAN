import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_index():
    response = client.get("/")
    assert response.status_code == 200
    assert "API Génération" in response.text

def test_generate_image():
    response = client.post("/generate_image", json={"prompt": "test"})
    assert response.status_code == 200
    assert response.headers["content-type"] == "image/jpeg"
    assert len(response.content) > 1000  # image non vide
