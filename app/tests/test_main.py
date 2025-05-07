import sys
import os
from fastapi.testclient import TestClient

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")
from main import app
from main import load_generator



client = TestClient(app)

def test_generate_image():
    response = client.get("/generate_image")
    assert response.status_code == 200
    assert response.headers["content-type"] == "image/jpeg"
    assert len(response.content) > 1000  # Vérifie que l'image n'est pas vide

def test_load_generator():
    """
    Teste si la fonction load_generator charge correctement le modèle.
    """
    pkl_path = "./stylegan3-r-ffhqu-256x256.pkl"
    try:
        generator = load_generator(pkl_path)
        assert generator is not None
        assert hasattr(generator, 'z_dim')  # Vérifie que l'attribut z_dim existe
    except FileNotFoundError:
        pytest.skip(f"Le fichier {pkl_path} est introuvable. Test ignoré.")