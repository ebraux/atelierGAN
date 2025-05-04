import torch  # Pour le GAN (pas encore utilisé ici)
import legacy  # Pour le GAN (pas encore utilisé ici)
from PIL import Image  # Pour manipuler et charger les images
import io  # Pour créer un buffer mémoire en bytes
from fastapi import FastAPI, Response  # Pour créer l’API web et envoyer des réponses
import os  # Pour manipuler les chemins de fichiers
from datetime import datetime  # Pour les dates et horodatage (pas encore utilisé)

# Répertoire où sont stockées les images existantes
IMAGE_DIR = "../images"
# Crée le répertoire s’il n’existe pas déjà
os.makedirs(IMAGE_DIR, exist_ok=True)

# Initialise l’application FastAPI
app = FastAPI()

# Fonction pour générer (pour l’instant, charger) une image et la retourner sous forme de bytes
def generate_stylegan_image(G=None) -> bytes:
    # Nom du fichier image à charger
    filename = "face_1.jpg"
    # Chemin complet vers l’image
    filepath = os.path.join(IMAGE_DIR, filename)

    # Charge l’image en mémoire avec PIL
    pil_img = Image.open(filepath)

    # Crée un buffer mémoire pour stocker l’image en bytes
    buffer = io.BytesIO()
    # Sauvegarde l’image au format JPEG dans le buffer
    pil_img.save(buffer, format='JPEG')
    # Retourne les bytes contenus dans le buffer
    return buffer.getvalue()

# Endpoint racine (accueil) de l’API
@app.get("/")
async def index():
    # Retourne un message texte simple pour vérifier que l’API fonctionne
    return "API Génération d'image (sans GAN pour le moment) !"

# Endpoint qui retourne l’image en réponse
@app.get("/generate_image")
async def generate_image():
    """
    Retourne une image existante du dossier /images au format JPEG.
    """
    # Appelle la fonction pour récupérer l’image en bytes
    image_data = generate_stylegan_image()
    # Retourne l’image en réponse HTTP avec le type MIME 'image/jpeg'
    return Response(content=image_data, media_type="image/jpeg")
