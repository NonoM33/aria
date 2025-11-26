# Mode Développement - SYSTEM_VOID

## Activation

Pour activer le mode dev, définissez la variable d'environnement `DEV_MODE=true` :

```bash
export DEV_MODE=true
uvicorn main:app --reload
```

Ou dans un fichier `.env` :

```
DEV_MODE=true
```

## Commandes DEV disponibles

Une fois le mode dev activé, vous pouvez utiliser la commande `DEV` dans le terminal :

### DEV JUMP

Aller directement à un chapitre spécifique pour tester.

```
> DEV JUMP chapter_6
```

### DEV LEVEL

Définir votre niveau directement.

```
> DEV LEVEL 5
```

### DEV GLOBAL

Voir l'état global du système (intégrité mondiale, joueurs, etc.)

```
> DEV GLOBAL
```

### DEV RESET

Réinitialiser complètement votre session.

```
> DEV RESET
```

### DEV LIST

Lister tous les chapitres disponibles.

```
> DEV LIST
```

## Structure modulaire des chapitres

Les chapitres sont maintenant dans `adventures/chapters/` :

```
adventures/
  chapters/
    chapter_1.py
    chapter_2.py
    ...
    chapter_10.py
```

Chaque fichier contient :

- `CHAPTER_FR` : Version française
- `CHAPTER_EN` : Version anglaise

### Ajouter un nouveau chapitre

1. Créez `adventures/chapters/chapter_X.py`
2. Définissez `CHAPTER_FR` et `CHAPTER_EN`
3. Le système le chargera automatiquement !

### Exemple de structure

```python
CHAPTER_FR = {
    "title": "Titre du chapitre",
    "intro": "Message d'introduction",
    "files": {
        "fichier.txt": "Contenu du fichier"
    },
    "puzzles": {
        "puzzle_id": {
            "question": "Question",
            "solution": "Réponse",
            "hint": "Indice",
            "command": "COMMANDE"
        }
    }
}
```

## Système multi-joueur global

Tous les joueurs partagent le même état global :

- **Intégrité globale** : Augmente avec les actions de tous les joueurs
- **Chapitres débloqués** : Débloqués collectivement
- **Événements globaux** : Historique des actions importantes

### Impact collectif

Quand un joueur :

- Se connecte → Intégrité globale +1
- Débloque un chapitre → Disponible pour tous
- Complète une mission → Intégrité globale augmente

L'état global est visible avec `STATUS` ou `DEV GLOBAL`.

## DLC et extensions

Pour ajouter un DLC :

1. Créez `adventures/chapters/dlc_chapter_X.py`
2. Le système le chargera automatiquement
3. Utilisez `DEV JUMP dlc_chapter_X` pour tester

Les DLC peuvent avoir leurs propres mécaniques et énigmes !
