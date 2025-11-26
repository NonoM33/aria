ADVENTURE_DATA = {
    "FR": {
        "chapters": {
            "chapter_1": {
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
            },
            "chapter_2": {
                "title": "Le Décodage",
                "intro": "Accès niveau 1 obtenu.\n\nNouvelles commandes disponibles: SCAN, DECODE, ACCESS\n\nVous devez maintenant scanner le système pour trouver les fichiers corrompus.",
                "files": {
                    "corrupted_data.b64": "VGhlIG5leHQgc3RlcCBpcyB0byBkZWNvZGUgdGhlIGZpbGUgY29kZWQgaW4gYmFzZTY0LgpUaGUgYW5zd2VyIGlzOiBQUk9UT0NPTF9YWVo=",
                    "protocol_xyz.txt": """PROTOCOL XYZ
==============

Ce protocole permet d'accéder au niveau 2.

Pour activer le protocole, vous devez:
1. Décoder le fichier corrupted_data.b64
2. Utiliser la commande: ACTIVATE <protocol_name>

Le nom du protocole est dans le fichier décodé.""",
                    "hint_sequence.txt": """SÉQUENCE D'ACTIVATION
=====================

Les fichiers doivent être lus dans un ordre spécifique:
1. corrupted_data.b64 -> Décoder avec DECODE
2. protocol_xyz.txt -> Lire le contenu
3. Utiliser ACTIVATE avec le nom du protocole trouvé

Indice: Le protocole commence par PROTOCOL_""",
                }
            },
            "chapter_3": {
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
            },
            "chapter_4": {
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
            },
            "chapter_5": {
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
            },
            "chapter_6": {
                "title": "L'Exploration",
                "intro": "Système restauré partiellement.\n\nVous avez maintenant accès à un gestionnaire de fichiers avancé.\nNouvelles commandes: NVIM, MAN\n\nUtilisez NVIM pour explorer le système de fichiers.",
                "files": {
                    "file_structure.txt": """STRUCTURE DES FICHIERS
=====================

/system/
  /core/
    - kernel.bin (LOCKED)
    - config.enc (ENCRYPTED)
  /logs/
    - access.log
    - security.log
    - error.log
  /data/
    - users.db
    - secrets.enc
  /scripts/
    - exploit.sh
    - decrypt.py

Utilisez NVIM pour naviguer dans cette structure.""",
                    "nvim_help.txt": """AIDE NVIM
==========

Commandes de base:
- h, j, k, l : Navigation (gauche, bas, haut, droite)
- i : Mode insertion
- ESC : Mode normal
- :q : Quitter
- :w : Sauvegarder
- / : Rechercher
- :e <fichier> : Ouvrir un fichier""",
                }
            },
            "chapter_7": {
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
            },
            "chapter_8": {
                "title": "La Multi-tâche",
                "intro": "Niveau 7 débloqué.\n\nMaîtrisez l'art de la multi-tâche avec les terminaux splités.\nCommandes: SPLIT, JOBS\n\nCréez plusieurs terminaux pour exécuter des tâches en parallèle.",
                "files": {
                    "multitask_guide.txt": """GUIDE MULTI-TÂCHE
==================

Raccourcis terminaux splités:
- Ctrl+B puis % : Split vertical
- Ctrl+B puis " : Split horizontal
- Ctrl+B puis flèches : Naviguer entre panneaux
- Ctrl+B puis x : Fermer le panneau actuel

Exemples:
1. Terminal 1: PORTSCAN 192.168.1.100
2. Terminal 2: BRUTEFORCE admin wordlist.txt
3. Terminal 3: MONITOR network""",
                }
            },
            "chapter_9": {
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
            },
            "chapter_10": {
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
        },
        "system_messages": {
            "welcome": "SYSTEM_VOID v2.0 initialisé.\nTapez HELP pour commencer.",
            "level_up": "Niveau {level} débloqué!",
            "file_accessed": "Fichier {filename} ouvert.",
            "puzzle_solved": "Énigme résolue!",
            "chapter_complete": "Chapitre '{title}' terminé!"
        }
    },
    "EN": {
        "chapters": {
            "chapter_1": {
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
            },
            "chapter_2": {
                "title": "The Decoding",
                "intro": "Level 1 access obtained.\n\nNew commands available: SCAN, DECODE, ACCESS\n\nYou must now scan the system to find corrupted files.",
                "files": {
                    "corrupted_data.b64": "VGhlIG5leHQgc3RlcCBpcyB0byBkZWNvZGUgdGhlIGZpbGUgY29kZWQgaW4gYmFzZTY0LgpUaGUgYW5zd2VyIGlzOiBQUk9UT0NPTF9YWVo=",
                    "protocol_xyz.txt": """PROTOCOL XYZ
==============

This protocol allows access to level 2.

To activate the protocol, you must:
1. Decode the corrupted_data.b64 file
2. Use command: ACTIVATE <protocol_name>

The protocol name is in the decoded file.""",
                    "hint_sequence.txt": """ACTIVATION SEQUENCE
====================

Files must be read in a specific order:
1. corrupted_data.b64 -> Decode with DECODE
2. protocol_xyz.txt -> Read content
3. Use ACTIVATE with found protocol name

Hint: Protocol starts with PROTOCOL_""",
                }
            },
            "chapter_3": {
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
            },
            "chapter_4": {
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
            },
            "chapter_5": {
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
            },
            "chapter_6": {
                "title": "The Exploration",
                "intro": "System partially restored.\n\nYou now have access to an advanced file manager.\nNew commands: NVIM, MAN\n\nUse NVIM to explore the file system.",
                "files": {
                    "file_structure.txt": """FILE STRUCTURE
================

/system/
  /core/
    - kernel.bin (LOCKED)
    - config.enc (ENCRYPTED)
  /logs/
    - access.log
    - security.log
    - error.log
  /data/
    - users.db
    - secrets.enc
  /scripts/
    - exploit.sh
    - decrypt.py

Use NVIM to navigate this structure.""",
                    "nvim_help.txt": """NVIM HELP
==========

Basic commands:
- h, j, k, l : Navigation (left, down, up, right)
- i : Insert mode
- ESC : Normal mode
- :q : Quit
- :w : Save
- / : Search
- :e <file> : Open a file""",
                }
            },
            "chapter_7": {
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
            },
            "chapter_8": {
                "title": "Multi-tasking",
                "intro": "Level 7 unlocked.\n\nMaster the art of multi-tasking with split terminals.\nCommands: SPLIT, JOBS\n\nCreate multiple terminals to execute tasks in parallel.",
                "files": {
                    "multitask_guide.txt": """MULTI-TASK GUIDE
================

Split terminal shortcuts:
- Ctrl+B then % : Vertical split
- Ctrl+B then " : Horizontal split
- Ctrl+B then arrows : Navigate between panels
- Ctrl+B then x : Close current panel

Examples:
1. Terminal 1: PORTSCAN 192.168.1.100
2. Terminal 2: BRUTEFORCE admin wordlist.txt
3. Terminal 3: MONITOR network""",
                }
            },
            "chapter_9": {
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
            },
            "chapter_10": {
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
        },
        "system_messages": {
            "welcome": "SYSTEM_VOID v2.0 initialized.\nType HELP to start.",
            "level_up": "Level {level} unlocked!",
            "file_accessed": "File {filename} opened.",
            "puzzle_solved": "Riddle solved!",
            "chapter_complete": "Chapter '{title}' completed!"
        }
    }
}

