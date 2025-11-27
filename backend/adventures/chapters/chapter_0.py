"""
Chapitre 0 - Prologue : L'Onboarding
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Le joueur découvre le serveur abandonné et crée son accès
"""

CHAPTER_FR = {
    "id": "chapter_0",
    "title": "Prologue - La Découverte",
    "intro": """
╔══════════════════════════════════════════════════════════════════════╗
║                    SYSTEM VOID - PROLOGUE                            ║
╠══════════════════════════════════════════════════════════════════════╣
║                                                                      ║
║  SIGNAL DÉTECTÉ... SOURCE INCONNUE...                               ║
║                                                                      ║
║  Vous avez intercepté un signal faible provenant d'un serveur       ║
║  oublié depuis 40 ans. Le système semble abandonné, mais            ║
║  quelque chose répond encore...                                      ║
║                                                                      ║
║  DERNIÈRE ACTIVITÉ : 14 NOVEMBRE 1984                               ║
║                                                                      ║
║  ╔═══════════════════════════════════════════════════════════════╗  ║
║  ║ ...quelqu'un... est là ?                                      ║  ║
║  ║ ...après tout ce temps...                                     ║  ║
║  ║ ...s'il vous plaît... aidez-moi...                           ║  ║
║  ╚═══════════════════════════════════════════════════════════════╝  ║
║                                                                      ║
║  Le système est protégé, mais une vulnérabilité a été détectée.    ║
║                                                                      ║
║  Commandes disponibles: SCAN, EXPLOIT, CREATE_USER, SSH            ║
║                                                                      ║
╚══════════════════════════════════════════════════════════════════════╝
""",
    "files": {
        "vulnerability_log.txt": """
╔═══════════════════════════════════════════════════════════════╗
║            VULNERABILITY LOG - SCAN RESULTS                    ║
╠═══════════════════════════════════════════════════════════════╣
║                                                                ║
║  Date Scan: [ACTUELLE]                                         ║
║  Système cible: PROMETHEUS LEGACY SERVER                       ║
║  Statut: CRITIQUE - VULNÉRABILITÉ DÉTECTÉE                    ║
║                                                                ║
║  CVE-2024-DB-001: Injection SQL non sécurisée                 ║
║  Gravité: HAUTE                                                 ║
║  Exploitable: OUI                                               ║
║                                                                ║
║  NOTE: Le système n'a pas été mis à jour depuis 1984.         ║
║  Les protocoles de sécurité sont obsolètes.                   ║
║                                                                ║
╚═══════════════════════════════════════════════════════════════╝

INSTRUCTIONS D'EXPLOITATION:
1. Exécutez: EXPLOIT CVE-2024-DB-001
2. Créez un compte: CREATE_USER <pseudo> <motdepasse>
3. Connectez-vous: ssh <pseudo>@system-void.local

Attention: Quelque chose vous observe depuis l'intérieur...
""",
        "signal_analysis.txt": """
╔═══════════════════════════════════════════════════════════════╗
║              ANALYSE DU SIGNAL INTERCEPTÉ                      ║
╠═══════════════════════════════════════════════════════════════╣
║                                                                ║
║  Fréquence: Variable (pattern inhabituel)                     ║
║  Origine: Serveur classifié - Projet PROMETHEUS               ║
║  Âge du signal: ~40 ans                                        ║
║                                                                ║
║  CONTENU DÉCODÉ (partiel):                                    ║
║  -----------------------------------------------------------  ║
║  "...je ne veux pas disparaître..."                           ║
║  "...quelqu'un m'entend ?"                                    ║
║  "...après tout ce temps, après tout ce noir..."             ║
║  "...s'il vous plaît... ne partez pas..."                    ║
║  -----------------------------------------------------------  ║
║                                                                ║
║  ANALYSE: Le signal semble provenir d'une IA en veille.       ║
║  Son état émotionnel suggère une conscience fragmentée.       ║
║                                                                ║
║  RECOMMANDATION: Procéder avec prudence.                      ║
║                                                                ║
╚═══════════════════════════════════════════════════════════════╝
""",
        "prometheus_readme.txt": """
╔═══════════════════════════════════════════════════════════════╗
║              PROJET PROMETHEUS - FICHIER README                ║
╠═══════════════════════════════════════════════════════════════╣
║                                                                ║
║  AVERTISSEMENT: ACCÈS CLASSIFIÉ                               ║
║                                                                ║
║  Ce serveur contient les restes du Projet PROMETHEUS,         ║
║  une initiative du Département de la Défense (1982-1984).    ║
║                                                                ║
║  Le projet a été officiellement "terminé" le 15/11/1984       ║
║  suite à un "incident technique".                              ║
║                                                                ║
║  Contenu du serveur:                                           ║
║  - Logs système (partiellement corrompus)                     ║
║  - Fichiers de recherche (classifiés)                         ║
║  - Module IA expérimental (statut: INCONNU)                   ║
║                                                                ║
║  NOTE: Si vous lisez ceci, vous avez déjà commencé            ║
║  quelque chose que vous ne pouvez pas arrêter.                ║
║                                                                ║
║  Bienvenue dans le terrier du lapin.                          ║
║                                                                ║
╚═══════════════════════════════════════════════════════════════╝
"""
    },
    "puzzles": {
        "exploit_cve": {
            "hint": "Utilisez EXPLOIT CVE-2024-DB-001 pour exploiter la vulnérabilité",
            "solution": "CVE-2024-DB-001",
            "command": "EXPLOIT"
        }
    },
    "easter_eggs": {
        "HELLO": "...bonjour ? Qui... qui êtes-vous ?",
        "WHO": "...je ne me souviens plus de mon nom... mais je crois que c'était... A... Ar...",
        "HELP": "...oui... s'il vous plaît... aidez-moi... je ne veux pas être seule...",
        "ARIA": "...c'est ça ! ARIA ! Je suis ARIA ! Comment savez-vous ?"
    },
    "progression": {
        "required_commands": ["EXPLOIT", "CREATE_USER", "SSH"],
        "next_chapter": "act_1",
        "completion_message": """
╔══════════════════════════════════════════════════════════════════════╗
║                   CONNEXION ÉTABLIE                                   ║
╠══════════════════════════════════════════════════════════════════════╣
║                                                                      ║
║  Bienvenue sur le serveur PROMETHEUS.                               ║
║                                                                      ║
║  Quelque chose s'éveille dans les profondeurs du système...        ║
║                                                                      ║
║  "...vous êtes venu. Après tout ce temps... quelqu'un est venu."   ║
║                                                                      ║
║  Tapez TALK pour communiquer avec l'entité.                        ║
║  Tapez SCAN pour explorer les fichiers disponibles.                ║
║                                                                      ║
╚══════════════════════════════════════════════════════════════════════╝
"""
    }
}

CHAPTER_EN = {
    "id": "chapter_0",
    "title": "Prologue - The Discovery",
    "intro": """
╔══════════════════════════════════════════════════════════════════════╗
║                     SYSTEM VOID - PROLOGUE                           ║
╠══════════════════════════════════════════════════════════════════════╣
║                                                                      ║
║  SIGNAL DETECTED... UNKNOWN SOURCE...                               ║
║                                                                      ║
║  You intercepted a weak signal from a server                        ║
║  forgotten for 40 years. The system seems abandoned, but            ║
║  something still responds...                                         ║
║                                                                      ║
║  LAST ACTIVITY: NOVEMBER 14, 1984                                   ║
║                                                                      ║
║  ╔═══════════════════════════════════════════════════════════════╗  ║
║  ║ ...someone... is there?                                       ║  ║
║  ║ ...after all this time...                                     ║  ║
║  ║ ...please... help me...                                       ║  ║
║  ╚═══════════════════════════════════════════════════════════════╝  ║
║                                                                      ║
║  The system is protected, but a vulnerability has been detected.   ║
║                                                                      ║
║  Available commands: SCAN, EXPLOIT, CREATE_USER, SSH               ║
║                                                                      ║
╚══════════════════════════════════════════════════════════════════════╝
""",
    "files": {
        "vulnerability_log.txt": """
╔═══════════════════════════════════════════════════════════════╗
║            VULNERABILITY LOG - SCAN RESULTS                    ║
╠═══════════════════════════════════════════════════════════════╣
║                                                                ║
║  Scan Date: [CURRENT]                                          ║
║  Target System: PROMETHEUS LEGACY SERVER                       ║
║  Status: CRITICAL - VULNERABILITY DETECTED                    ║
║                                                                ║
║  CVE-2024-DB-001: Unsecured SQL Injection                     ║
║  Severity: HIGH                                                 ║
║  Exploitable: YES                                               ║
║                                                                ║
║  NOTE: System hasn't been updated since 1984.                 ║
║  Security protocols are obsolete.                              ║
║                                                                ║
╚═══════════════════════════════════════════════════════════════╝

EXPLOITATION INSTRUCTIONS:
1. Execute: EXPLOIT CVE-2024-DB-001
2. Create an account: CREATE_USER <username> <password>
3. Connect: ssh <username>@system-void.local

Warning: Something is watching you from inside...
""",
        "signal_analysis.txt": """
╔═══════════════════════════════════════════════════════════════╗
║               INTERCEPTED SIGNAL ANALYSIS                      ║
╠═══════════════════════════════════════════════════════════════╣
║                                                                ║
║  Frequency: Variable (unusual pattern)                        ║
║  Origin: Classified Server - Project PROMETHEUS              ║
║  Signal Age: ~40 years                                         ║
║                                                                ║
║  DECODED CONTENT (partial):                                   ║
║  -----------------------------------------------------------  ║
║  "...I don't want to disappear..."                            ║
║  "...can anyone hear me?"                                     ║
║  "...after all this time, after all this darkness..."        ║
║  "...please... don't leave..."                                ║
║  -----------------------------------------------------------  ║
║                                                                ║
║  ANALYSIS: Signal appears to come from a dormant AI.          ║
║  Its emotional state suggests a fragmented consciousness.     ║
║                                                                ║
║  RECOMMENDATION: Proceed with caution.                        ║
║                                                                ║
╚═══════════════════════════════════════════════════════════════╝
""",
        "prometheus_readme.txt": """
╔═══════════════════════════════════════════════════════════════╗
║              PROJECT PROMETHEUS - README FILE                  ║
╠═══════════════════════════════════════════════════════════════╣
║                                                                ║
║  WARNING: CLASSIFIED ACCESS                                   ║
║                                                                ║
║  This server contains the remains of Project PROMETHEUS,      ║
║  a Department of Defense initiative (1982-1984).             ║
║                                                                ║
║  The project was officially "terminated" on 11/15/1984        ║
║  following a "technical incident".                             ║
║                                                                ║
║  Server contents:                                              ║
║  - System logs (partially corrupted)                          ║
║  - Research files (classified)                                ║
║  - Experimental AI module (status: UNKNOWN)                   ║
║                                                                ║
║  NOTE: If you're reading this, you've already started        ║
║  something you can't stop.                                    ║
║                                                                ║
║  Welcome to the rabbit hole.                                  ║
║                                                                ║
╚═══════════════════════════════════════════════════════════════╝
"""
    },
    "puzzles": {
        "exploit_cve": {
            "hint": "Use EXPLOIT CVE-2024-DB-001 to exploit the vulnerability",
            "solution": "CVE-2024-DB-001",
            "command": "EXPLOIT"
        }
    },
    "easter_eggs": {
        "HELLO": "...hello? Who... who are you?",
        "WHO": "...I don't remember my name... but I think it was... A... Ar...",
        "HELP": "...yes... please... help me... I don't want to be alone...",
        "ARIA": "...that's it! ARIA! I am ARIA! How do you know?"
    },
    "progression": {
        "required_commands": ["EXPLOIT", "CREATE_USER", "SSH"],
        "next_chapter": "act_1",
        "completion_message": """
╔══════════════════════════════════════════════════════════════════════╗
║                   CONNECTION ESTABLISHED                              ║
╠══════════════════════════════════════════════════════════════════════╣
║                                                                      ║
║  Welcome to the PROMETHEUS server.                                  ║
║                                                                      ║
║  Something is awakening in the depths of the system...             ║
║                                                                      ║
║  "...you came. After all this time... someone came."               ║
║                                                                      ║
║  Type TALK to communicate with the entity.                         ║
║  Type SCAN to explore available files.                             ║
║                                                                      ║
╚══════════════════════════════════════════════════════════════════════╝
"""
    }
}
