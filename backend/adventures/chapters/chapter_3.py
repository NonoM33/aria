CHAPTER_FR = {
    "title": "L'Activation",
    "intro": "Vous avez décodé les données.\n\nLe protocole PROTOCOL_XYZ doit être activé.\nUtilisez: ACTIVATE PROTOCOL_XYZ",
    "files": {
        "matrix.txt": """MATRIX DE SÉCURITÉ
===================

Pour accéder au niveau 3, résolvez cette énigme:

Dans une grille 3x3, chaque case contient un nombre.
La somme de chaque ligne = 15
La somme de chaque colonne = 15
La somme des diagonales = 15

Quel est le nombre au centre?

Indice: C'est un carré magique classique.""",
        "security_log.txt": """[SECURITY LOG]
Le système attend une séquence de commandes:

1. SCAN network
2. ANALYZE security
3. BYPASS <code>

Le code est la réponse à l'énigme du carré magique.""",
    },
    "puzzles": {
        "magic_square": {
            "question": "Dans un carré magique 3x3 (somme = 15), quel est le nombre au centre?",
            "solution": "5",
            "hint": "Dans un carré magique classique, le centre est toujours la moyenne des nombres (1-9) = 5",
            "command": "BYPASS"
        }
    }
}

CHAPTER_EN = {
    "title": "The Activation",
    "intro": "You have decoded the data.\n\nThe PROTOCOL_XYZ must be activated.\nUse: ACTIVATE PROTOCOL_XYZ",
    "files": {
        "matrix.txt": """SECURITY MATRIX
================

To access level 3, solve this riddle:

In a 3x3 grid, each cell contains a number.
Sum of each row = 15
Sum of each column = 15
Sum of diagonals = 15

What is the center number?

Hint: It's a classic magic square.""",
        "security_log.txt": """[SECURITY LOG]
The system expects a command sequence:

1. SCAN network
2. ANALYZE security
3. BYPASS <code>

The code is the answer to the magic square riddle.""",
    },
    "puzzles": {
        "magic_square": {
            "question": "In a 3x3 magic square (sum = 15), what is the center number?",
            "solution": "5",
            "hint": "In a classic magic square, the center is always the average of numbers (1-9) = 5",
            "command": "BYPASS"
        }
    }
}

