# Atelier GAN - Génération de visages

## Qu’est-ce que Git ?

Git est un système de gestion de versions.
Il permet de **suivre l’historique des fichiers**, **travailler à plusieurs** sur un même projet et **revenir en arrière** en cas d’erreur.

---

## Comment installer Git

✅ **Sur Linux (Debian/Ubuntu) :**

```bash
sudo apt update
sudo apt install git
```

✅ **Sur Windows :**

1. Va sur [https://git-scm.com](https://git-scm.com)
2. Clique sur **Download** (le site détectera ton OS)
3. Lance l’installeur et laisse les options par défaut (ça suffit pour commencer)

---

## Initialiser un dépôt Git

Dans le dossier de ton projet :

```bash
git init
```

Cela crée un dossier `.git` qui stocke l’historique et les métadonnées.

---

## Écrire un `.gitignore`

Crée un fichier nommé `.gitignore` dans ton projet.
Dedans, liste les fichiers/dossiers à ignorer, par exemple :

```
node_modules/
.env
*.log
```

---

## Créer une branche

```bash
git checkout -b nouvelle-branche
```

Exemple :

```bash
git checkout -b feature-login
```

---

## Ajouter et commiter le code

1. **Ajouter les fichiers modifiés au suivi :**

```bash
git add .
```

2. **Créer un commit avec un message :**

```bash
git commit -m "Ajout de la fonctionnalité login"
```

---

## Qu’est-ce que GitHub ?

GitHub est une plateforme en ligne pour héberger tes dépôts Git.
Il permet de **partager ton code**, **collaborer à plusieurs** et **gérer les issues/pull requests**.

---

## Relier un dépôt distant sur GitHub

1. Crée un dépôt sur GitHub (via le site) sans cocher “Initialize with README”.

2. Dans ton terminal :

```bash
git remote add origin https://github.com/ton-utilisateur/ton-repo.git
```

---

## Envoyer le code

```bash
git push -u origin nouvelle-branche
```

Pour les prochains push :

```bash
git push
```

---
