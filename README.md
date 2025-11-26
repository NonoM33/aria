# SYSTEM_VOID - Alternate Reality Game MVP

ARG web-based avec interface terminal rétro style hacker années 90.

## Structure du projet

```
codex/
├── backend/          # API FastAPI
├── frontend/         # Application React + Vite
└── README.md
```

## Installation

### Backend

```bash
cd backend
python -m venv venv
source venv/bin/activate  # Sur Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Frontend

```bash
cd frontend
npm install
```

## Démarrage

### Backend

Depuis la racine du projet :

```bash
cd backend
uvicorn main:app --reload --port 8000
```

Ou si vous êtes déjà dans le répertoire `backend` :

```bash
uvicorn main:app --reload --port 8000
```

L'API sera accessible sur `http://localhost:8000`

### Frontend

Depuis la racine du projet :

```bash
cd frontend
npm run dev
```

Ou si vous êtes déjà dans le répertoire `frontend` :

```bash
npm run dev
```

L'application sera accessible sur `http://localhost:5173`

## Fonctionnalités

### Interface

- Terminal rétro style années 90 avec effet scanline
- Input inline (comme un vrai terminal)
- Effet de frappe caractère par caractère
- Support multilingue FR/EN avec menu de sélection

### Aventure

- Histoire complète de ~1 heure
- 5 chapitres progressifs
- Énigmes variées (décodage, énigmes, calculs)
- Fichiers cachés à découvrir
- Système de progression par niveaux

### Commandes disponibles

**Niveau 0 (Début)**

- `HELP` - Liste des commandes
- `STATUS` - État du système
- `LOGIN <clé>` - Connexion au système

**Niveau 1+ (Après connexion)**

- `SCAN` - Scanner le système
- `DECODE <texte>` - Décoder du Base64
- `ACCESS <fichier>` - Lire un fichier

**Niveau 2+**

- `ACTIVATE <protocole>` - Activer un protocole
- `NETWORK` - Accéder au réseau
- `ANALYZE` - Analyser la sécurité
- `BYPASS <code>` - Contourner la sécurité

**Niveau 3+**

- `CONNECT <serveur> <password>` - Se connecter à un serveur
- `RESTORE <code>` - Restaurer le système
- `SOLVE <réponse>` - Résoudre l'énigme finale

## Technologies utilisées

- **Backend**: FastAPI, Python
- **Frontend**: React, Vite, TailwindCSS
- **Styling**: CSS personnalisé avec effets rétro (scanlines, curseur clignotant)

## Tests

### Installation des dépendances de test

Le script `run_tests.sh` crée automatiquement un environnement virtuel si nécessaire.

**Méthode automatique (recommandée) :**

```bash
cd backend
./run_tests.sh
```

**Méthode manuelle :**

```bash
cd backend

# Créer un venv (si pas déjà fait)
python3 -m venv venv

# Activer le venv
source venv/bin/activate

# Installer les dépendances
pip install -r requirements.txt
```

### Lancement des tests

```bash
cd backend

# Méthode 1 : Script automatique (recommandé)
./run_tests.sh

# Méthode 2 : Commandes manuelles
# Tous les tests
python3 -m pytest

# Avec détails
python3 -m pytest -v

# Un test spécifique
python3 -m pytest test_adventure.py::test_login_with_correct_key -v
```

Les tests couvrent :

- Toutes les commandes de base
- La progression complète de l'aventure
- La gestion des langues (FR/EN)
- La structure des données
- Les énigmes et leurs solutions

Voir `backend/README_TESTS.md` pour plus de détails.

## Génération d'Aventures

Le système inclut un template pour générer automatiquement de nouvelles aventures. Voir `ADVENTURE_GENERATOR.md` pour plus de détails.
