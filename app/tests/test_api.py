import sys
import os
# Ajoute le répertoire parent au chemin Python pour pouvoir importer main.py
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")

from fastapi.testclient import TestClient
from main import app

# Crée un client de test pour l’application FastAPI
client = TestClient(app)

def test_index():
    # Teste la route GET "/"
    response = client.get("/")
    # Vérifie que le serveur répond avec un code 200 (OK)
    assert response.status_code == 200
    # Vérifie que le texte retourné contient "API Génération"
    assert "API Génération" in response.text

def test_generate_image():
    # Teste la route GET "/generate_image" avec un prompt JSON
    response = client.get("/generate_image")
    # Vérifie que le serveur répond avec un code 200 (OK)
    assert response.status_code == 200
    # Vérifie que le header indique un contenu image JPEG
    assert response.headers["content-type"] == "image/jpeg"
    # Vérifie que le contenu retourné (l'image) n'est pas vide (au moins 1000 octets)
    assert len(response.content) > 1000  # image non vide
