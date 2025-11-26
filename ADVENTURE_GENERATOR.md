# Système de Génération d'Aventures - SYSTEM_VOID

## Vue d'ensemble

Ce document décrit le système de template permettant à une IA de générer automatiquement de nouvelles aventures pour SYSTEM_VOID.

## Structure du Template

Le template est défini dans `backend/adventure_template.json`. Il suit une structure hiérarchique permettant de définir:

1. **Métadonnées** : Titre, durée estimée, difficulté, langue
2. **Chapitres** : Séquence d'étapes de l'aventure
3. **Fichiers** : Documents cachés à découvrir
4. **Énigmes** : Puzzles à résoudre
5. **Commandes** : Actions disponibles
6. **Traductions** : Support multilingue (FR/EN)

## Format JSON du Template

```json
{
  "metadata": {
    "title": "Titre de l'aventure",
    "estimated_duration_minutes": 60,
    "difficulty": "MEDIUM",
    "language": "FR"
  },
  "chapters": [
    {
      "chapter_id": "chapter_1",
      "chapter_number": 1,
      "title": "Titre du chapitre",
      "description": "Description",
      "objectives": ["Objectif 1", "Objectif 2"],
      "triggers": {
        "command": "STATUS",
        "conditions": {
          "level": 0,
          "completed_chapters": [],
          "items_collected": [],
          "flags": []
        }
      },
      "content": {
        "intro_message": "Message d'introduction",
        "files": {
          "filename.txt": {
            "content": "Contenu du fichier",
            "hint": "Indice optionnel",
            "unlocks": {
              "commands": ["SCAN"],
              "items": ["key"],
              "flags": ["file_read"],
              "next_chapter": "chapter_2"
            }
          }
        },
        "puzzles": [
          {
            "puzzle_id": "puzzle_1",
            "type": "RIDDLE",
            "question": "Question de l'énigme",
            "hints": ["Indice 1", "Indice 2"],
            "solution": "REPONSE",
            "solution_variants": ["REPONSE2"],
            "unlocks": {
              "commands": ["DECODE"],
              "items": [],
              "flags": ["puzzle_solved"],
              "next_chapter": "chapter_2"
            },
            "command": "SOLVE"
          }
        ]
      }
    }
  ]
}
```

## Guide de Génération pour IA

### Étapes de Création

1. **Définir les Métadonnées**

   - Titre accrocheur
   - Durée estimée (pour 1h, prévoir 5-7 chapitres)
   - Difficulté progressive

2. **Créer les Chapitres**

   - Chaque chapitre = 8-12 minutes de jeu
   - Progression logique
   - Objectifs clairs

3. **Ajouter les Fichiers**

   - Fichiers avec indices
   - Fichiers avec énigmes
   - Fichiers avec codes/passwords

4. **Créer les Énigmes**

   - Types possibles: RIDDLE, DECODE, MATH, SEQUENCE, LOGIC
   - Solutions progressives
   - Indices multiples

5. **Définir les Commandes**

   - Commandes de base: HELP, STATUS, LOGIN
   - Commandes de progression: SCAN, DECODE, ACCESS
   - Commandes spéciales: ACTIVATE, CONNECT, SOLVE

6. **Ajouter les Traductions**
   - Tous les textes en FR et EN
   - Cohérence terminologique

### Exemple de Chapitre Complet

```json
{
  "chapter_id": "chapter_1",
  "title": "L'Infiltration",
  "intro": "SYSTEM_VOID v2.0 - Système corrompu\n\nVous êtes un hacker éthique...",
  "files": {
    "mission.txt": {
      "content": "MISSION BRIEFING\n\nObjectif: ...",
      "unlocks": {
        "next_chapter": "chapter_2"
      }
    }
  },
  "puzzles": {
    "encryption_key": {
      "question": "Trouvez la clé d'encryption",
      "solution": "VOID2024",
      "command": "LOGIN"
    }
  }
}
```

## Intégration dans le Backend

Le fichier `backend/adventure_data.py` contient la structure Python équivalente au JSON. Pour générer une nouvelle aventure:

1. Créer le JSON selon le template
2. Convertir en structure Python (dict)
3. Ajouter dans `ADVENTURE_DATA`
4. Mettre à jour `main.py` pour gérer les nouvelles commandes/énigmes

## Bonnes Pratiques

- **Progression** : Commencer facile, augmenter la difficulté
- **Indices** : Toujours donner des indices, pas de solutions directes
- **Feedback** : Messages clairs pour succès/échec
- **Cohérence** : Histoire logique et immersive
- **Accessibilité** : Support FR/EN complet

## Exemple de Workflow IA

```
1. Analyser le template adventure_template.json
2. Générer les métadonnées (titre, durée, difficulté)
3. Créer 5-7 chapitres avec:
   - Intro message
   - 2-4 fichiers par chapitre
   - 1-2 énigmes par chapitre
   - Commandes à débloquer
4. Ajouter traductions FR/EN
5. Valider la cohérence de l'histoire
6. Générer le fichier adventure_data.py
```

## Structure des Énigmes

Types d'énigmes supportées:

- **RIDDLE** : Énigmes classiques
- **DECODE** : Base64, ROT13, etc.
- **MATH** : Calculs, séquences
- **SEQUENCE** : Patterns à identifier
- **LOGIC** : Problèmes logiques
- **PASSWORD** : Mots de passe à trouver

Chaque énigme doit avoir:

- Une question claire
- Une solution unique (ou variantes)
- Des indices progressifs
- Une commande associée
