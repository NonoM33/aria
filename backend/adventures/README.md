# Système d'Aventures Modulaire - SYSTEM_VOID

## Structure

```
adventures/
  __init__.py
  adventure_loader.py      # Chargeur dynamique de chapitres
  adventure_data.py        # Wrapper pour compatibilité
  global_state.py          # État global partagé (multi-joueur)
  chapters/
    __init__.py
    chapter_1.py           # Chapitre 1 (FR + EN)
    chapter_2.py           # Chapitre 2 (FR + EN)
    ...
    chapter_10.py          # Chapitre 10 (FR + EN)
```

## Ajouter un nouveau chapitre

1. Créez `chapters/chapter_X.py`
2. Définissez `CHAPTER_FR` et `CHAPTER_EN`
3. Le système le charge automatiquement !

### Format d'un chapitre

```python
CHAPTER_FR = {
    "title": "Titre du chapitre",
    "intro": "Message d'introduction quand le chapitre commence",
    "files": {
        "fichier.txt": "Contenu du fichier",
        "autre.txt": "Autre contenu"
    },
    "puzzles": {
        "puzzle_id": {
            "question": "Question de l'énigme",
            "solution": "REPONSE",
            "hint": "Indice optionnel",
            "command": "COMMANDE_POUR_RESOUDRE"
        }
    }
}

CHAPTER_EN = {
    # Même structure en anglais
}
```

## Système multi-joueur global

Tous les joueurs partagent le même état global via `GlobalState` :

- **Intégrité globale** : Augmente avec les actions collectives
- **Chapitres débloqués** : Débloqués pour tous
- **Événements globaux** : Historique des actions importantes
- **Joueurs en ligne** : Compteur en temps réel

### Impact collectif

Chaque action d'un joueur peut impacter l'état global :

- Connexion → +1 intégrité
- Déblocage de chapitre → Disponible pour tous
- Résolution d'énigme → +X intégrité globale

## DLC et extensions

Pour créer un DLC :

1. Créez `chapters/dlc_X.py` ou `chapters/expansion_X.py`
2. Le système le charge automatiquement
3. Utilisez `DEV JUMP dlc_X` pour tester

Les DLC peuvent avoir :

- Leurs propres mécaniques
- De nouveaux types d'énigmes
- Des commandes spéciales
- Des impacts sur l'état global

## Exemple de DLC

```python
# chapters/dlc_cyberpunk.py
CHAPTER_FR = {
    "title": "Cyberpunk Expansion",
    "intro": "Nouveau monde débloqué...",
    "files": {...},
    "puzzles": {...}
}
```

Le système le détecte et le charge automatiquement !
