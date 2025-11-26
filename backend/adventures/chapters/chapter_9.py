CHAPTER_FR = {
    "title": "L'Infiltration Profonde",
    "intro": "Niveau 8 débloqué.\n\nInfiltrez-vous plus profondément dans le système.\nNouvelles commandes: EXPLOIT, ENCRYPT, DECRYPT\n\nCombinez toutes vos compétences pour accéder au noyau.",
    "files": {
        "exploit_list.txt": """EXPLOITS DISPONIBLES
====================

CVE-2024-001: Buffer overflow dans kernel.bin
CVE-2024-002: Injection SQL dans users.db
CVE-2024-003: RCE dans API Gateway

Pour utiliser un exploit:
EXPLOIT CVE-2024-001

Attention: Les exploits peuvent être détectés.""",
        "encryption_key.txt": """CLÉ DE CHIFFREMENT
===================

Pour déchiffrer config.enc:
DECRYPT config.enc VOID_MASTER_KEY_2024

La clé maître est cachée dans les logs système.""",
    },
    "puzzles": {
        "master_key": {
            "question": "Trouvez la clé maître dans les logs. Elle contient VOID, MASTER, KEY et 2024.",
            "solution": "VOID_MASTER_KEY_2024",
            "hint": "Combine VOID + MASTER + KEY + 2024 avec des underscores",
            "command": "DECRYPT"
        }
    }
}

CHAPTER_EN = {
    "title": "Deep Infiltration",
    "intro": "Level 8 unlocked.\n\nInfiltrate deeper into the system.\nNew commands: EXPLOIT, ENCRYPT, DECRYPT\n\nCombine all your skills to access the core.",
    "files": {
        "exploit_list.txt": """AVAILABLE EXPLOITS
===================

CVE-2024-001: Buffer overflow in kernel.bin
CVE-2024-002: SQL injection in users.db
CVE-2024-003: RCE in API Gateway

To use an exploit:
EXPLOIT CVE-2024-001

Warning: Exploits may be detected.""",
        "encryption_key.txt": """ENCRYPTION KEY
==============

To decrypt config.enc:
DECRYPT config.enc VOID_MASTER_KEY_2024

The master key is hidden in system logs.""",
    },
    "puzzles": {
        "master_key": {
            "question": "Find the master key in logs. It contains VOID, MASTER, KEY and 2024.",
            "solution": "VOID_MASTER_KEY_2024",
            "hint": "Combine VOID + MASTER + KEY + 2024 with underscores",
            "command": "DECRYPT"
        }
    }
}

