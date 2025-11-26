# Quick Start - SYSTEM_VOID

## Démarrage rapide

### Backend

```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

## Mode Développement

Pour activer le mode dev avec terminal de debug :

```bash
cd backend
export DEV_MODE=true
uvicorn main:app --reload
```

Puis dans le terminal du jeu :

```
> DEV LIST
[Affiche tous les chapitres disponibles]

> DEV JUMP chapter_6
[Saute directement au chapitre 6]

> DEV LEVEL 5
[Définit votre niveau à 5]

> DEV GLOBAL
[Voir l'état global multi-joueur]

> DEV RESET
[Réinitialise votre session]
```

## Structure Modulaire

Les chapitres sont maintenant dans `backend/adventures/chapters/` :

- `chapter_1.py` à `chapter_10.py` : Chapitres de base
- Ajoutez `dlc_X.py` pour des extensions
- Le système charge automatiquement tous les fichiers `.py`

## Système Multi-Joueur

Tous les joueurs partagent :

- **Intégrité globale** : Augmente avec les actions de tous
- **Chapitres débloqués** : Disponibles pour tous une fois débloqués
- **État du monde** : Impact collectif sur l'histoire

Voir `STATUS` pour l'intégrité globale !

## Ajouter un DLC

1. Créez `backend/adventures/chapters/dlc_cyberpunk.py`
2. Définissez `CHAPTER_FR` et `CHAPTER_EN`
3. C'est tout ! Le système le charge automatiquement

Exemple :

```python
CHAPTER_FR = {
    "title": "Cyberpunk DLC",
    "intro": "Nouveau monde...",
    "files": {...},
    "puzzles": {...}
}
```
