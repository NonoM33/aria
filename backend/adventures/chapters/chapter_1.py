CHAPTER_FR = {
    "title": "L'Infiltration",
    "intro": "SYSTEM_VOID v2.0 - Système d'exploitation corrompu\n\nVous êtes un hacker éthique infiltré dans le système.\nVotre mission: restaurer l'intégrité du système avant qu'il ne s'effondre.\n\nCommencez par analyser le système avec STATUS.",
    "files": {
        "mission.txt": """MISSION BRIEFING
==================

Objectif: Restaurer SYSTEM_VOID
Niveau de sécurité: CRITIQUE
Temps estimé: 1 heure

Le système a été compromis par une entité inconnue.
Vous devez:
1. Trouver la clé d'encryption principale
2. Décoder les fichiers corrompus
3. Résoudre les énigmes de sécurité
4. Accéder au noyau du système

Indice: La clé est cachée dans les messages système.
Cherchez le pattern: VOID + année actuelle""",
        "log_001.txt": """[SYSTEM LOG - Entry 001]
Date: 2024-01-15 10:23:45
Status: CRITICAL BREACH DETECTED

Le système a détecté une intrusion majeure.
Tous les fichiers critiques ont été chiffrés.

Clé d'encryption partielle trouvée dans les logs:
Pattern détecté: V***2***4

Analyse en cours...""",
    },
    "puzzles": {
        "encryption_key": {
            "hint": "La clé est VOID + l'année actuelle (2024)",
            "solution": "VOID2024",
            "command": "LOGIN"
        }
    }
}

CHAPTER_EN = {
    "title": "The Infiltration",
    "intro": "SYSTEM_VOID v2.0 - Corrupted Operating System\n\nYou are an ethical hacker infiltrated into the system.\nYour mission: restore system integrity before it collapses.\n\nStart by analyzing the system with STATUS.",
    "files": {
        "mission.txt": """MISSION BRIEFING
==================

Objective: Restore SYSTEM_VOID
Security Level: CRITICAL
Estimated Time: 1 hour

The system has been compromised by an unknown entity.
You must:
1. Find the main encryption key
2. Decode corrupted files
3. Solve security riddles
4. Access the system core

Hint: The key is hidden in system messages.
Look for the pattern: VOID + current year""",
        "log_001.txt": """[SYSTEM LOG - Entry 001]
Date: 2024-01-15 10:23:45
Status: CRITICAL BREACH DETECTED

The system has detected a major intrusion.
All critical files have been encrypted.

Partial encryption key found in logs:
Pattern detected: V***2***4

Analysis in progress...""",
    },
    "puzzles": {
        "encryption_key": {
            "hint": "The key is VOID + current year (2024)",
            "solution": "VOID2024",
            "command": "LOGIN"
        }
    }
}

