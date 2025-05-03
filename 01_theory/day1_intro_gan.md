# Jour 1 – Introduction aux GANs (Generative Adversarial Networks)

## 🎯 Objectifs du jour

- Comprendre le principe fondamental des GANs
- Étudier l’architecture de base : Générateur vs Discriminateur
- Explorer les fonctions de coût et l'entraînement par jeu à somme nulle
- Implémenter un GAN simple pour générer des images

---

## 🤖 Qu’est-ce qu’un GAN ?

Un **GAN** est un type de réseau de neurones génératif qui repose sur une **confrontation** entre deux modèles :
- **Générateur (G)** : crée de nouvelles données à partir d’un bruit aléatoire
- **Discriminateur (D)** : essaie de distinguer les vraies données des données générées

### 🧠 Idée clé : Apprentissage par confrontation
C’est un **jeu à somme nulle** entre deux réseaux :
- Le générateur apprend à "tromper" le discriminateur
- Le discriminateur apprend à mieux détecter les fausses données

> 🧾 Référence fondatrice :
> [Generative Adversarial Networks (Goodfellow et al., 2014)](https://arxiv.org/abs/1406.2661)

---

## 🏗️ Architecture GAN de base

```plaintext
Bruitage z ~ N(0,1)
    │
    ▼
[ Générateur G ]
    │
    ▼
Image générée
    ▼
[ Discriminateur D ] ← Image réelle
    │
    ▼
Prédiction : vraie ou fausse ?

Le générateur prend un vecteur aléatoire (bruit) comme entrée et produit une image.

Le discriminateur évalue si cette image est réelle ou générée.

```
# 🧮 Fonction de coût (minimax)

La fonction de coût des GANs est une fonction **minimax** :

\[
\min_G \max_D \mathbb{E}_{x \sim p_{data}}[\log D(x)] + \mathbb{E}_{z \sim p_z}[\log(1 - D(G(z)))]
\]

- Le **discriminateur maximise** sa capacité à détecter les vrais/faux
- Le **générateur minimise** la capacité du discriminateur à le repérer

---

# 🧨 Problèmes courants

| Problème            | Description                                       |
|---------------------|---------------------------------------------------|
| Mode Collapse       | Le générateur produit toujours les mêmes exemples |
| Training Instability| Oscillations ou convergence difficile             |
| Vanishing Gradients | D devient trop fort, G n’apprend plus             |

---

# 🛠️ Entraînement d’un GAN simple (MNIST)

Aujourd’hui, on implémente un **GAN simple sur MNIST** :

- **Générateur** : quelques couches `Linear` + `ReLU`
- **Discriminateur** : `Linear` + `LeakyReLU`
- **Perte** : `BCELoss` (Binary Cross Entropy)

---

# 💡 Concepts clés à retenir

- **Nash Equilibrium** : point où G et D n’ont plus d’intérêt à changer
- **Latent space** : espace de bruit structuré permettant la génération
- **Adversarial loss** : moteur de l’apprentissage

---

# 📚 Références complémentaires

- [Tutorial: Generative Adversarial Networks](https://arxiv.org/abs/1701.00160)
- [GAN Hacks – Soumith Chintala](https://github.com/soumith/ganhacks)
- [A Visual Introduction to GANs](https://poloclub.github.io/ganlab/)
- [Cours au Collège de France](https://www.college-de-france.fr/fr/agenda/cours/generation-de-donnees-en-ia-par-transport-et-debruitage/generation-de-donnees-en-ia-par-transport-et-debruitage-1)

---

# 🔁 Prochaine étape

👉 Passe au notebook [`02_labs/images_gan/train_gan_images.ipynb`](../02_labs/images_gan/train_gan_images.ipynb) pour coder ton premier GAN 🎨


