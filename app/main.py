import torch
import legacy
from PIL import Image
import io
from fastapi import FastAPI, Response
import os
from datetime import datetime

# Répertoire d’images existantes
IMAGE_DIR = "../images"
os.makedirs(IMAGE_DIR, exist_ok=True)

# Initialise l’application FastAPI
app = FastAPI()

# Fonction pour sélectionner une image existante et retourner ses octets
def generate_stylegan_image(G=None) -> bytes:
    # Chemin vers une image de test
    filename = "face_1.jpg"
    filepath = os.path.join(IMAGE_DIR, filename)

    # Charge l’image
    pil_img = Image.open(filepath)

    # Convertit l’image en bytes pour la réponse API
    buffer = io.BytesIO()
    pil_img.save(buffer, format='JPEG')
    return buffer.getvalue()

@app.get("/")
async def index():
    return "API Génération d'image (sans GAN pour le moment) !"

@app.get("/generate_image")
async def generate_image():
    """
    Retourne une image existante du dossier /images au format JPEG.
    """
    image_data = generate_stylegan_image()
    return Response(content=image_data, media_type="image/jpeg")
