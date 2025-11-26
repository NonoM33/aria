CHAPTER_FR = {
    "title": "Le Réseau",
    "intro": "Niveau 2 débloqué.\n\nVous avez accès au réseau interne.\nNouvelles commandes: NETWORK, ANALYZE, BYPASS",
    "files": {
        "network_map.txt": """CARTE DU RÉSEAU
================

Serveurs détectés:
- SERVER_ALPHA (192.168.1.10) - Status: OFFLINE
- SERVER_BETA (192.168.1.20) - Status: ONLINE
- SERVER_GAMMA (192.168.1.30) - Status: LOCKED

Pour déverrouiller SERVER_GAMMA:
1. Trouvez le mot de passe dans les logs
2. Utilisez: CONNECT SERVER_GAMMA <password>

Le mot de passe est l'inverse de "VOID" en code ASCII.""",
        "server_logs.txt": """[SERVER LOGS]
Password hint: Reverse ASCII of VOID
V = 86, O = 79, I = 73, D = 68
Reverse: 68-73-79-86

Mais attendez... le vrai mot de passe est l'inverse du mot lui-même.
VOID inversé = DIOV
Mais en ASCII inversé...""",
    },
    "puzzles": {
        "server_password": {
            "question": "Trouvez le mot de passe pour SERVER_GAMMA. C'est l'inverse de VOID.",
            "solution": "DIOV",
            "hint": "Inversez simplement les lettres: V-O-I-D devient D-I-O-V",
            "command": "CONNECT"
        }
    }
}

CHAPTER_EN = {
    "title": "The Network",
    "intro": "Level 2 unlocked.\n\nYou have access to the internal network.\nNew commands: NETWORK, ANALYZE, BYPASS",
    "files": {
        "network_map.txt": """NETWORK MAP
===========

Detected servers:
- SERVER_ALPHA (192.168.1.10) - Status: OFFLINE
- SERVER_BETA (192.168.1.20) - Status: ONLINE
- SERVER_GAMMA (192.168.1.30) - Status: LOCKED

To unlock SERVER_GAMMA:
1. Find password in logs
2. Use: CONNECT SERVER_GAMMA <password>

Password is the reverse of "VOID" in ASCII code.""",
        "server_logs.txt": """[SERVER LOGS]
Password hint: Reverse ASCII of VOID
V = 86, O = 79, I = 73, D = 68
Reverse: 68-73-79-86

But wait... the real password is the reverse of the word itself.
VOID reversed = DIOV
But in reversed ASCII...""",
    },
    "puzzles": {
        "server_password": {
            "question": "Find the password for SERVER_GAMMA. It's the reverse of VOID.",
            "solution": "DIOV",
            "hint": "Simply reverse the letters: V-O-I-D becomes D-I-O-V",
            "command": "CONNECT"
        }
    }
}

