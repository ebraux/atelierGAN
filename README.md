# Atelier GAN - Génération de visages

Dans cet atelier, nous allons découvrir les **GANs (Generative Adversarial Networks)**, une famille de modèles d’intelligence artificielle capables de **générer des images réalistes à partir de bruit aléatoire**. Un GAN fonctionne grâce à l’opposition de deux réseaux de neurones : un **générateur**, qui produit de fausses images, et un **discriminateur**, qui apprend à les distinguer des vraies.

Nous mettrons en pratique ce principe en **entraînant un GAN à générer des visages humains** à partir d’un jeu de données. Une fois le modèle entraîné, nous l’intégrerons dans une **API web** capable de produire des visages synthétiques à la demande.



**📅 Durée : 2 jours** 

## **Intervenants :**  
- **Kheireddin Kadri** - Chercheur R&D Aptiskills, intervenant école Léonard de Vinci  
- **Stéphane Jamin-Normand** - Enseignant à l'ISEN, formateur référent de l'école IA

![intervenants](ressources/Kheireddin KADRI-2©MG-2022 (1).jpg)

## 🗓️ Plan de la formation

**Jour 1 — Introduction & GAN de base**
- Théorie GAN : architecture, fonction de perte, entraînement, variantes, métriques et évaluations
- Cas pratique : génération d’images

**Jour 2 — GAN avancés & Domaines spécifiques**
- GAN conditionnels, DCGAN, CycleGAN, Diffusion
- Cas pratiques :
  - Molécules (SMILES → molGAN)
  - Cristaux (.cif → CGAN)
  - Visage humain : CelebA
  - Intégration MLflow pour suivi d’expériences

## 🧪 Labs disponibles

| Domaine      | Dataset         | Notebook                          |
|--------------|-----------------|-----------------------------------|
| Images       | MNIST/CelebA    | `02_labs/images_gan/train_gan_images.ipynb` |
| Molécules    | ZINC/ChEMBL     | `02_labs/molecules_gan/train_gan_molecules.ipynb` |
| Cristaux     | Materials Project | `02_labs/crystals_gan/train_gan_crystals.ipynb` |
| Visage       | CelebA            | `02_labs\Human_faces\GAN_faces.ipynb` |


## 🎯 Objectifs pédagogiques du cours
Au cours de ces deux journées, les participants pourront :

- ✅ Comprendre les fondements mathématiques des GANs, notamment la formulation min-max, les divergences (JS, Wasserstein) et les fonctions de perte.

- 🧠 Identifier les différents types de GANs (DCGAN, WGAN, CGAN, CycleGAN, etc.) et comprendre leurs avantages et limitations selon le domaine d’application.

- 🔍 Évaluer un modèle GAN à l’aide de métriques pertinentes telles que l’Inception Score (IS), la Fréchet Inception Distance (FID), et d'autres spécifiques aux domaines (molécules, graphes, ou images).

- 💻 Implémenter pas à pas plusieurs architectures GANs en PyTorch et/ou TensorFlow à travers des notebooks pratiques.

- ⚙️ Appliquer les GANs à des jeux de données variés : images, spectres de molécules, structures de graphes, texte, IRM médicales…

- 🚀 Explorer des cas d’usage avancés comme la génération de molécules, la synthèse vocale, ou la création de nouveaux cristaux pour la découverte de matériaux.
 
- 📊 Construire une visualisation **MLops** pour interagir avec le modèle entraîné via MLflow 

- 🧩 Comprendre les défis actuels des GANs : stabilité de l’entraînement, collapse de mode, qualité/diversité, etc.

- 📚 S’orienter vers la recherche ou la production en ayant une vision critique des méthodes actuelles et des directions futures en génération de données.


📌 Cet atelier est conçu pour être **pratique et immersif**, avec un focus sur un **cas d'usage réel** pour mieux comprendre l'application des **GANs** à la génération d'images entre autres. 

### Déroulé de l'atelier

- Jour 1 : Introduction et workflow complet d’un GAN

  **Matin :**
  
  * Introduction aux GAN et à leurs applications dans la génération d’images.
    - Atelier : collecte de données d’images via web scraping et préparation du dataset.
    - Technologies : Python, BeautifulSoup, Pandas.

  **Après-midi :**
 
  * Création d’un modèle GAN avec PyTorch pour générer des images.
    - Atelier : suivi des expériences et comparaison des résultats avec MLFlow.
    - Technologies : PyTorch, MLFlow.

- Jour 2 : Entraînement avancé, déploiement, éthique et témoignage

  **Matin :**
  
  * Entraînement du GAN, analyse des résultats et optimisation des hyperparamètres.
    - Atelier : conteneurisation du modèle GAN avec Docker.
    - Technologies : Docker, PyTorch.

  **Après-midi :**

 * Témoignage d’un professionnel travaillant sur les GAN.
    - Atelier : déploiement du modèle GAN sur une infrastructure locale.
    - Discussion sur l’éthique et les implications des modèles génératifs, notamment sur les biais et les usages abusifs.



## ⚙️ Outils

- Visual Studio / VS Code
- Python 3.10+
- TensorFlow / PyTorch
- MLflow

## 📦 Installation

```bash
git clone https://github.com/steinnberg/GAN_mastery.git
cd GAN_mastery
pip install -r requirements.txt


### **Étapes d’Installation**
### **1. Clonez le dépôt :**
   ```bash
   git clone https://github.com/steinnberg/GAN_Mastery.git
   cd votre-repo
  ```

### **2. Installez les dépendances :**
```bash
pip install -r requirements.txt
````



### **3. Contributions**
Les contributions sont les bienvenues !
Si vous souhaitez signaler un bug ou proposer une nouvelle fonctionnalité, ouvrez une issue ou soumettez une pull request.


### **4. Licence**
Ce projet est sous licence MIT. Voir le fichier LICENSE pour plus d’informations.

### **5. Contact**
📧 kheireddin.kadri@ext.devinci.fr

