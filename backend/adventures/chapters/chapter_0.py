CHAPTER_FR = {
    "title": "L'Infiltration Initiale",
    "intro": """SYSTEM_VOID v2.0 - Système de base de données compromis

Vous êtes un hacker éthique qui doit infiltrer le système.
Votre première mission: exploiter une vulnérabilité dans la base de données
pour créer un accès SSH.

Commandes disponibles: SCAN, EXPLOIT, CREATE_USER, SSH

Commencez par scanner le système avec SCAN pour trouver les vulnérabilités.""",
    "files": {
        "vulnerability_log.txt": """[VULNERABILITY LOG]
Date: 2024-01-15 10:23:45
Status: CRITICAL VULNERABILITY DETECTED

Une vulnérabilité SQL a été détectée dans la base de données.
CVE-2024-DB-001: Injection SQL non sécurisée

Pour exploiter cette vulnérabilité:
1. Utilisez: EXPLOIT CVE-2024-DB-001
2. Créez un utilisateur avec: CREATE_USER <username> <password>
3. Connectez-vous avec: ssh <username>@system-void.local

Attention: Cette vulnérabilité peut être corrigée à tout moment.""",
        "database_schema.txt": """[DATABASE SCHEMA]

Table: players
- id (INTEGER PRIMARY KEY)
- username (STRING UNIQUE)
- password_hash (STRING)
- level (INTEGER)
- chapter (STRING)

La table est vulnérable aux injections SQL.""",
    },
    "puzzles": {
        "exploit_cve": {
            "hint": "Utilisez EXPLOIT CVE-2024-DB-001 pour exploiter la vulnérabilité",
            "solution": "CVE-2024-DB-001",
            "command": "EXPLOIT"
        }
    }
}

CHAPTER_EN = {
    "title": "Initial Infiltration",
    "intro": """SYSTEM_VOID v2.0 - Compromised Database System

You are an ethical hacker who must infiltrate the system.
Your first mission: exploit a vulnerability in the database
to create SSH access.

Available commands: SCAN, EXPLOIT, CREATE_USER, SSH

Start by scanning the system with SCAN to find vulnerabilities.""",
    "files": {
        "vulnerability_log.txt": """[VULNERABILITY LOG]
Date: 2024-01-15 10:23:45
Status: CRITICAL VULNERABILITY DETECTED

A SQL vulnerability has been detected in the database.
CVE-2024-DB-001: Unsecured SQL injection

To exploit this vulnerability:
1. Use: EXPLOIT CVE-2024-DB-001
2. Create a user with: CREATE_USER <username> <password>
3. Connect with: ssh <username>@system-void.local

Warning: This vulnerability may be patched at any time.""",
        "database_schema.txt": """[DATABASE SCHEMA]

Table: players
- id (INTEGER PRIMARY KEY)
- username (STRING UNIQUE)
- password_hash (STRING)
- level (INTEGER)
- chapter (STRING)

The table is vulnerable to SQL injections.""",
    },
    "puzzles": {
        "exploit_cve": {
            "hint": "Use EXPLOIT CVE-2024-DB-001 to exploit the vulnerability",
            "solution": "CVE-2024-DB-001",
            "command": "EXPLOIT"
        }
    }
}

