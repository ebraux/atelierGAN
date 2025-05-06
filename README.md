# Atelier GAN - Web scraping

![web scraping infographie](ressources/web-scraping.webp)

Le **web scraping** est une technique qui permet d’extraire automatiquement des informations à partir de pages web.
Il est utilisé, par exemple, pour :

* récupérer des prix ou des avis sur des sites e-commerce,
* collecter des articles ou données scientifiques,
* constituer des jeux de données pour l’entraînement en machine learning (images, textes),
* surveiller l’évolution de contenus en ligne (météo, sport, bourse…).

⚠️ Attention : le scraping doit toujours être fait **dans le respect des conditions d’utilisation du site et de la loi**.

---

## 1. Accès à la page web avec `requests`

La première étape consiste à télécharger le code HTML de la page. On utilise pour cela la bibliothèque **requests**.

### Code exemple

```python
import requests

url = 'https://generated.photos/faces'
response = requests.get(url)

if response.status_code == 200:
    print("Succès ! Contenu de la page récupéré.")
    print(response.text[:500])  # Affiche les 500 premiers caractères
else:
    print(f"Erreur : statut {response.status_code}")
```

### Explication

* `requests.get(url)` → envoie une requête au serveur web.
* `response.status_code` → vérifie que le code est `200` (succès).
* `response.text` → contient le code HTML de la page.

---

## 2. BeautifulSoup : installation et documentation

![logo BeautifulSoup](ressources/bs.png)

**BeautifulSoup** est une bibliothèque qui permet de lire et d’extraire facilement des éléments HTML.

### Installation

```bash
pip install beautifulsoup4
```

👉 Si besoin, installe aussi requests :

```bash
pip install requests
```

### Documentation officielle

[https://www.crummy.com/software/BeautifulSoup/bs4/doc/](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

---

## 3. Comprendre le scraping par balise HTML

Pour extraire des images, des titres, des liens, il faut :

1. **Examiner le HTML de la page**

   * Sur Chrome / Firefox → clic droit → *Inspecter* → repérer les balises `<img>`, `<a>`, `<div>`, etc.
2. **Identifier les sélecteurs**

   * Exemple pour `https://generated.photos/faces` :

     ```html
     <a href="/face/...">
       <img src="https://images.generated.photos/..." alt="...">
     </a>
     ```

   → On va cibler les `<img>` contenus dans les `<a>`.

---

## 4. Code exemple complet + explications

```python
import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin
import time

# URL à scraper
URL = 'https://generated.photos/faces'

# Dossier pour enregistrer les images
IMAGE_DIR = '../images'
os.makedirs(IMAGE_DIR, exist_ok=True)

# Headers pour simuler un vrai navigateur
HEADERS = {'User-Agent': 'Mozilla/5.0'}

def download_image(img_url, filename):
    response = requests.get(img_url, headers=HEADERS)
    if response.status_code == 200:
        with open(filename, 'wb') as f:
            f.write(response.content)
        print(f"Image enregistrée : {filename}")
    else:
        print(f"Erreur pour {img_url}")

def scrape_faces(url, max_images=5):
    response = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    img_tags = soup.select('a img')
    count = 0
    
    for img in img_tags:
        img_url = img.get('src')
        if img_url:
            full_url = urljoin(url, img_url)
            filename = os.path.join(IMAGE_DIR, f'face_{count + 1}.jpg')
            download_image(full_url, filename)
            count += 1
            if count >= max_images:
                break
            time.sleep(1)  # Pause pour respecter le serveur

scrape_faces(URL, max_images=5)
```

### Explications

* **`BeautifulSoup(response.text, 'html.parser')`** → crée un objet analysable.
* **`soup.select('a img')`** → sélectionne les balises `<img>` contenues dans des `<a>`.
* **`img.get('src')`** → récupère l’URL de l’image.
* **`urljoin(url, img_url)`** → reconstruit une URL complète même si elle est relative.
* **`download_image()`** → télécharge et sauvegarde l’image.

### Exécuter le wep scraping
Le code doit être lancé à partir du répertoire /scrap
 ```bash
 cd scrap
 python scraper.py 
 ```

---

## 5. Bonnes pratiques du scraping

* Consulte toujours le fichier `robots.txt` du site pour vérifier ce qui est autorisé.
* Respecte les conditions d’utilisation du site.
* Ajoute un **User-Agent** pour simuler un vrai navigateur.
* Ne surcharge pas les serveurs → utilise `time.sleep()` entre les requêtes.
* Limite le nombre de pages/images téléchargées.
* Garde une trace des URLs et des erreurs rencontrées.

---

## 6. Limites de BeautifulSoup

* BeautifulSoup ne voit que **le HTML initial**.
  Si le contenu est chargé **par JavaScript** (comme souvent sur les sites modernes), il ne sera pas accessible.
* Pour ces cas, il faut utiliser :

  * **Selenium** → simule un navigateur réel.
  * **Playwright** → plus moderne et rapide.
* BeautifulSoup ne remplace pas un vrai moteur de rendu et ne gère pas les interactions dynamiques.

---
