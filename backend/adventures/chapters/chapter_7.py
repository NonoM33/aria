CHAPTER_FR = {
    "title": "Le Réseau Avancé",
    "intro": "Niveau 6 débloqué.\n\nVous devez maintenant scanner le réseau pour trouver des vulnérabilités.\nNouvelles commandes: PORTSCAN, BRUTEFORCE, SPLIT\n\nUtilisez SPLIT pour créer plusieurs terminaux et lancer des scans en parallèle.",
    "files": {
        "network_targets.txt": """CIBLES RÉSEAU
==============

Serveurs à scanner:
- 192.168.1.100 (Firewall principal)
- 192.168.1.101 (Base de données)
- 192.168.1.102 (API Gateway)

Ports suspects détectés:
- 22 (SSH)
- 80 (HTTP)
- 443 (HTTPS)
- 3306 (MySQL)
- 5432 (PostgreSQL)

Utilisez PORTSCAN pour analyser ces serveurs.""",
        "wordlist.txt": """LISTE DE MOTS DE PASSE
========================

admin
password
123456
void2024
system
root
toor
admin123
password123""",
    }
}

CHAPTER_EN = {
    "title": "Advanced Network",
    "intro": "Level 6 unlocked.\n\nYou must now scan the network to find vulnerabilities.\nNew commands: PORTSCAN, BRUTEFORCE, SPLIT\n\nUse SPLIT to create multiple terminals and run scans in parallel.",
    "files": {
        "network_targets.txt": """NETWORK TARGETS
===============

Servers to scan:
- 192.168.1.100 (Main firewall)
- 192.168.1.101 (Database)
- 192.168.1.102 (API Gateway)

Suspicious ports detected:
- 22 (SSH)
- 80 (HTTP)
- 443 (HTTPS)
- 3306 (MySQL)
- 5432 (PostgreSQL)

Use PORTSCAN to analyze these servers.""",
        "wordlist.txt": """PASSWORD WORDLIST
==================

admin
password
123456
void2024
system
root
toor
admin123
password123""",
    }
}

