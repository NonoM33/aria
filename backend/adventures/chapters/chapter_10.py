CHAPTER_FR = {
    "title": "La Finale",
    "intro": "Niveau 9 débloqué.\n\nDernière étape: Accéder au noyau et restaurer complètement le système.\n\nUtilisez toutes vos compétences pour compléter la mission.",
    "files": {
        "final_access.txt": """ACCÈS FINAL
============

Pour accéder au noyau:
1. Déchiffrez config.enc
2. Utilisez l'exploit CVE-2024-001
3. Modifiez kernel.bin avec NVIM
4. Redémarrez le système avec RESTART

La commande finale est: RESTART SYSTEM""",
    },
    "puzzles": {
        "final_command": {
            "question": "Quelle est la commande pour redémarrer le système?",
            "solution": "RESTART SYSTEM",
            "hint": "RESTART + SYSTEM",
            "command": "RESTART"
        }
    }
}

CHAPTER_EN = {
    "title": "The Finale",
    "intro": "Level 9 unlocked.\n\nFinal step: Access the core and fully restore the system.\n\nUse all your skills to complete the mission.",
    "files": {
        "final_access.txt": """FINAL ACCESS
============

To access the core:
1. Decrypt config.enc
2. Use exploit CVE-2024-001
3. Edit kernel.bin with NVIM
4. Restart system with RESTART

The final command is: RESTART SYSTEM""",
    },
    "puzzles": {
        "final_command": {
            "question": "What is the command to restart the system?",
            "solution": "RESTART SYSTEM",
            "hint": "RESTART + SYSTEM",
            "command": "RESTART"
        }
    }
}

