CHAPTER_FR = {
    "title": "Le Noyau",
    "intro": "Serveur GAMMA connecté.\n\nVous avez accès au noyau du système.\nDernière étape: restaurer l'intégrité.",
    "files": {
        "core_access.txt": """ACCÈS AU NOYAU
===============

Pour restaurer le système, vous devez:
1. Trouver le code de restauration
2. Le code est la somme de: 34 + 15 + 5 + 1
3. Utilisez: RESTORE <code>

Attention: Vous n'avez qu'une seule tentative.""",
        "final_riddle.txt": """ÉNIGME FINALE
==============

Je suis le début de la fin,
La fin de l'éternité,
Le début de chaque fin,
Et la fin de chaque début.

Qui suis-je?

La réponse est la première lettre de chaque mot de l'énigme.""",
    },
    "puzzles": {
        "restore_code": {
            "question": "Calculez le code de restauration: 34 + 15 + 5 + 1",
            "solution": "55",
            "command": "RESTORE"
        },
        "final_riddle": {
            "question": "Je suis le début de la fin, la fin de l'éternité... Qui suis-je?",
            "solution": "E",
            "hint": "La première lettre de chaque mot-clé: début, fin, éternité, début, fin, début = E",
            "command": "SOLVE"
        }
    }
}

CHAPTER_EN = {
    "title": "The Core",
    "intro": "Server GAMMA connected.\n\nYou have access to the system core.\nFinal step: restore integrity.",
    "files": {
        "core_access.txt": """CORE ACCESS
===========

To restore the system, you must:
1. Find the restoration code
2. Code is the sum of: 34 + 15 + 5 + 1
3. Use: RESTORE <code>

Warning: You only have one attempt.""",
        "final_riddle.txt": """FINAL RIDDLE
============

I am the beginning of the end,
The end of eternity,
The beginning of every end,
And the end of every beginning.

What am I?

The answer is the first letter of each key word in the riddle.""",
    },
    "puzzles": {
        "restore_code": {
            "question": "Calculate restoration code: 34 + 15 + 5 + 1",
            "solution": "55",
            "command": "RESTORE"
        },
        "final_riddle": {
            "question": "I am the beginning of the end, the end of eternity... What am I?",
            "solution": "E",
            "hint": "First letter of key words: beginning, end, eternity, beginning, end, beginning = E",
            "command": "SOLVE"
        }
    }
}

