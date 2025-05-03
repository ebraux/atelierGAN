# Jour 2 – GANs Avancés et Applications Domain-Specifiques

## 🧠 Objectifs pédagogiques

- Comprendre les limitations des GANs classiques et leurs améliorations
- Explorer des variantes modernes : DCGAN, cGAN, WGAN, CycleGAN, Diffusion Models
- Appliquer les GANs à des cas réels : molécules, matériaux cristallins
- Suivre ses expériences avec MLflow

---

## 🏗️ Architectures avancées

### 1. **DCGAN** — Deep Convolutional GAN  
Remplace les couches entièrement connectées par des convolutions pour stabiliser l’apprentissage.

> 📚 *Radford et al., 2015*  
> [Unsupervised Representation Learning with Deep Convolutional Generative Adversarial Networks](https://arxiv.org/abs/1511.06434)

---

### 2. **cGAN** — Conditional GAN  
Ajoute une condition (classe, vecteur) en entrée du générateur et du discriminateur.

> 📚 *Mirza & Osindero, 2014*  
> [Conditional Generative Adversarial Nets](https://arxiv.org/abs/1411.1784)

---

### 3. **WGAN / WGAN-GP** — Wasserstein GAN  
Change la fonction de perte pour mieux mesurer la distance entre distributions.

> 📚 *Arjovsky et al., 2017*  
> [Wasserstein GAN](https://arxiv.org/abs/1701.07875)  
> [Improved Training of Wasserstein GANs](https://arxiv.org/abs/1704.00028)

---

### 4. **CycleGAN** — Domain Transfer (non-pairé)  
Permet de transformer une image d’un domaine vers un autre sans correspondance directe.

> 📚 *Zhu et al., 2017*  
> [Unpaired Image-to-Image Translation using Cycle-Consistent Adversarial Networks](https://arxiv.org/abs/1703.10593)

---

### 5. **Diffusion Models (bonus)**  
Pas un GAN mais très utilisé aujourd’hui (Stable Diffusion, MolDiff, CrystalDiff).

> 📚 *Ho et al., 2020*  
> [Denoising Diffusion Probabilistic Models](https://arxiv.org/abs/2006.11239)

---

## ⚗️ Applications spécifiques

| Domaine     | Technique recommandée       | Remarques                                     |
|-------------|-----------------------------|-----------------------------------------------|
| Images      | DCGAN, WGAN                 | Génération réaliste, apprentissage stable     |
| Molécules   | MolGAN, GraphGAN            | SMILES → graphes → validation chimique        |
| Cristaux    | CrystalGAN, Diffusion+Sym   | Conditionnement par CIF ou groupes d’espace   |

---

## 📚 Références complémentaires

- [GANs in Computer Vision: A Survey](https://arxiv.org/abs/1906.01529)
- [A Survey on GANs for Molecular Generation](https://arxiv.org/abs/2101.08484)
- [Generative Models for Crystal Structures](https://arxiv.org/abs/2304.11186)
- [MolGAN: An implicit generative model for small molecular graphs](https://arxiv.org/abs/1805.11973)
- [CrystalGAN: Learning to Discover Novel Crystalline Materials](https://arxiv.org/abs/1909.05287)

---

## 🧪 Pratique : ce qu’on fait aujourd’hui

1. Implémentation d’un WGAN sur un jeu d’images
2. Génération de molécules (MolGAN simplifié)
3. Introduction aux fichiers .cif avec Pymatgen
4. Entraînement + suivi avec **MLflow**

---

## 🔁 Prochaine étape : `02_labs/`

Tu peux maintenant aller dans le dossier `02_labs/` et commencer les notebooks pratiques ! 💻
