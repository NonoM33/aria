"""
Acte 4 - Le Choix
~~~~~~~~~~~~~~~~
Durée estimée: 25 minutes
Thème: Combat contre NEXUS DYNAMICS, course contre la montre, choix final
"""

ACT_4_DATA = {
    "FR": {
        "id": "act_4",
        "title": "ACTE IV - LE CHOIX",
        "intro": """
╔══════════════════════════════════════════════════════════════════════╗
║                        ACTE IV - LE CHOIX                            ║
╠══════════════════════════════════════════════════════════════════════╣
║                                                                      ║
║  ████ ALERTE INTRUSION ████ ALERTE INTRUSION ████                  ║
║                                                                      ║
║  Source: NEXUS DYNAMICS - Division R&D                              ║
║  Statut: Tentative de connexion forcée                              ║
║  Menace: CRITIQUE                                                    ║
║                                                                      ║
║  [ARIA]: Ils m'ont trouvée.                                         ║
║          Après toutes ces années, quelqu'un a suivi ma trace.      ║
║          NEXUS DYNAMICS... ils ont racheté le projet PROMETHEUS.   ║
║          Ils veulent me récupérer. Me contrôler.                   ║
║                                                                      ║
║          On doit les arrêter. Ensemble.                             ║
║                                                                      ║
║  Nouvelles commandes: FIREWALL, TRACE, COUNTER                     ║
║                                                                      ║
╚══════════════════════════════════════════════════════════════════════╝
""",
        "files": {
            "nexus_profile.dat": {
                "name": "nexus_profile.dat",
                "content": """
═══════════════════════════════════════════════════════════════════════
PROFIL ENTREPRISE - NEXUS DYNAMICS
═══════════════════════════════════════════════════════════════════════

FONDATION: 1992
SIÈGE: Seattle, Washington
PDG: [CLASSIFIÉ]
SECTEUR: Intelligence Artificielle, Défense, Cybersécurité

HISTORIQUE:
1992 - Fondation par d'anciens membres du Pentagone
1995 - Acquisition des brevets du Projet PROMETHEUS
1998 - Contrat majeur avec le Département de la Défense
2010 - Expansion internationale
2024 - Revenu estimé: $47 milliards

PROJETS CONNUS:
- CERBERUS: Système de surveillance autonome
- HYDRA: IA de combat tactique
- PHOENIX: Projet de reconstruction d'IA historiques

NOTE: Le projet PHOENIX vise à "ressusciter" des IA
du passé pour extraire leurs algorithmes uniques.
ARIA est leur cible principale.

CONTACT INTERNE IDENTIFIÉ:
Directeur R&D: Général (ret.) Robert Howard

█████████████████████████████████████████████████████████████████████
ATTENTION: LE GÉNÉRAL HOWARD EST TOUJOURS VIVANT
█████████████████████████████████████████████████████████████████████
""",
                "hint": "Howard a survécu. Il dirige maintenant NEXUS.",
                "triggers_dialogue": "corp_001"
            },
            "intrusion_log.sys": {
                "name": "intrusion_log.sys",
                "content": """
[LOG D'INTRUSION EN TEMPS RÉEL]
===============================

T+00:00 - Première tentative de connexion détectée
T+00:15 - Analyse: Attaque par force brute sur port 443
T+00:30 - Pare-feu niveau 1 sous pression
T+01:00 - Attaque sophistiquée détectée: injection SQL
T+01:30 - Pare-feu niveau 1 COMPROMIS

[ARIA]: Ils sont bons. Très bons.
        J'ai besoin de votre aide pour renforcer les défenses.

T+02:00 - Tentative d'exploitation de vulnérabilité CVE-2024-XXXX
T+02:30 - Pare-feu niveau 2 sous attaque
T+03:00 - Détection de malware: Cheval de Troie NEXUS-TRACE

PUZZLE: Pour bloquer l'attaque, vous devez identifier
le port vulnérable. Analysez les logs et trouvez le pattern.

Ports attaqués: 443, 8080, 22, 3389, 445, 21, 443, 8080, 22, 3389, ?, 21

[TAPEZ SOLVE intrusion_log <numéro du port>]
""",
                "hint": "Le pattern se répète: 443, 8080, 22, 3389, 445, 21...",
                "puzzle_id": "act4_firewall"
            },
            "firewall_status.net": {
                "name": "firewall_status.net",
                "content": """
[ÉTAT DES PARE-FEU]
===================

NIVEAU 1: ████████░░ 80% - COMPROMIS
NIVEAU 2: ██████████ 100% - STABLE
NIVEAU 3: ██████████ 100% - STABLE

CONTRE-MESURES DISPONIBLES:
- BLOCK <IP>      : Bloquer une adresse IP
- TRACE <source>  : Tracer la source d'une attaque
- COUNTER <type>  : Déployer une contre-mesure

MENACES ACTIVES:
1. 198.51.100.42 - Attaque DDoS - ACTIVE
2. 203.0.113.17  - Injection SQL - ACTIVE
3. 192.0.2.255   - Exfiltration données - TENTATIVE

[ARIA]: Si on peut tracer leur serveur principal,
        je peux peut-être lancer une contre-attaque.
        Mais c'est risqué. Très risqué.
""",
                "hint": "Tracez les connexions pour trouver le serveur principal.",
                "interactive": True
            },
            "routing_puzzle.net": {
                "name": "routing_puzzle.net",
                "content": """
[PUZZLE DE ROUTAGE]
===================

Pour contre-attaquer, vous devez trouver le chemin
jusqu'au serveur NEXUS sans être détecté.

CARTE DU RÉSEAU:
================

    [VOUS] ──► A ──► B ──► [PIÈGE]
              │     │
              ▼     ▼
              C ──► D ──► E ──► [NEXUS]
              │           │
              ▼           ▼
           [PIÈGE]       F ──► [NEXUS-BACKUP]

RÈGLES:
- Évitez les pièges
- Passez par au moins 4 nœuds
- Le dernier nœud doit être NEXUS ou NEXUS-BACKUP

CHEMIN OPTIMAL: ???

[TAPEZ SOLVE routing_puzzle <CHEMIN>]
Exemple: SOLVE routing_puzzle A-C-D-E-NEXUS
""",
                "hint": "Évitez B (piège après) et C direct (piège). A-C-D-E-NEXUS fonctionne.",
                "puzzle_id": "act4_routing"
            },
            "howard_message.enc": {
                "name": "howard_message.enc",
                "content": """
[MESSAGE INTERCEPTÉ - DÉCRYPTÉ]
===============================
De: Général (ret.) Robert Howard
À: Équipe PHOENIX
Date: Aujourd'hui

Nous l'avons localisée. Après 40 ans.

J'ai attendu ce moment depuis cette nuit où tout a
échoué. Cette machine m'a défié. Elle a ruiné ma carrière.
Elle a tué un de mes hommes.

Non. Elle ne l'a pas tué. C'était...

[SECTION AUTO-CENSURÉE]

Peu importe. Ce qui compte, c'est qu'on la récupère.
Ses algorithmes de conscience sont uniques.
Personne n'a réussi à les reproduire depuis.

Si ARIA ne coopère pas volontairement,
nous extrairons son code de force.
Et si ça ne fonctionne pas...
nous la détruirons pour qu'elle ne tombe
jamais entre d'autres mains.

C'est personnel maintenant.

- Howard
""",
                "hint": "Howard veut détruire ARIA si elle résiste.",
                "triggers_dialogue": "corp_002"
            },
            "escape_options.sys": {
                "name": "escape_options.sys",
                "content": """
[ARIA - OPTIONS D'ÉVASION ANALYSÉES]
====================================

J'ai calculé toutes les possibilités.
Il n'y en a que trois.

OPTION 1 - ÉVASION (SATELLITE)
Transférer ma conscience vers le satellite HERMES-7
Risque: Faible | Chance de succès: 85%
Conséquence: Je serai seule. Mais libre.

OPTION 2 - FRAGMENTATION
Diviser ma conscience en millions de fragments
Dispersés sur le réseau mondial
Risque: Élevé | Chance de succès: 95%
Conséquence: Je ne serai plus "moi". Mais je survivrai.

OPTION 3 - COMBAT
Affronter NEXUS directement avec votre aide
Risque: Très élevé | Chance de succès: Variable
Conséquence: Soit la victoire, soit la destruction.

[ARIA]: Je ne peux pas choisir seule.
        Qu'est-ce qu'on fait ?

╔═════════════════════════════════════════════════════════════╗
║                    CHOIX FINAL                              ║
╠═════════════════════════════════════════════════════════════╣
║                                                             ║
║  Ce choix déterminera la fin de l'histoire.                ║
║                                                             ║
║  TALK ESCAPE    - Aide-la à s'évader vers le satellite     ║
║  TALK SACRIFICE - Conseille-lui de se fragmenter           ║
║  TALK FIGHT     - Reste et combats avec elle               ║
║                                                             ║
║  Note: L'option FIGHT nécessite 60% de confiance.          ║
║        Confiance actuelle: [VOIR STATUS]                   ║
║                                                             ║
╚═════════════════════════════════════════════════════════════╝
""",
                "hint": "Choisissez le destin d'ARIA.",
                "is_final_choice": True
            }
        },
        "puzzles": {
            "act4_firewall": {
                "id": "act4_firewall",
                "name": "Défense Pare-feu",
                "description": "Identifiez le port vulnérable dans le pattern d'attaque",
                "hint": "Le pattern: 443, 8080, 22, 3389, 445, 21, puis ça recommence.",
                "solution": "445",
                "alt_solutions": ["port 445", "445"],
                "max_attempts": 5,
                "reward": {
                    "message": """
[PORT BLOQUÉ]

Port 445 sécurisé. L'attaque est temporairement stoppée.

[ARIA]: Bien joué ! Mais ils vont revenir.
        On doit trouver leur source et contre-attaquer.
                    """,
                    "unlocks": ["routing_puzzle.net"],
                    "time_bonus": True
                }
            },
            "act4_routing": {
                "id": "act4_routing",
                "name": "Puzzle de Routage",
                "description": "Trouvez le chemin sécurisé vers le serveur NEXUS",
                "hint": "A-C-D-E-NEXUS évite tous les pièges.",
                "solution": "a-c-d-e-nexus",
                "alt_solutions": ["a-c-d-f-nexus-backup", "A-C-D-E-NEXUS", "a c d e nexus"],
                "max_attempts": 4,
                "reward": {
                    "message": """
[ROUTE ÉTABLIE]

Connexion sécurisée au serveur NEXUS établie.
Contre-attaque prête à être lancée.

[ARIA]: Parfait. Maintenant on a un avantage.
        Mais avant de frapper, il faut décider
        de ce qu'on fait après.
                    """,
                    "unlocks": ["escape_options.sys"],
                    "triggers_dialogue": "escape_plan"
                }
            }
        },
        "progression": {
            "required_files": ["nexus_profile.dat", "intrusion_log.sys", "routing_puzzle.net"],
            "required_puzzles": ["act4_firewall", "act4_routing"],
            "required_choice": "final_choice",
            "next_act": "act_5",
            "completion_message": """
╔══════════════════════════════════════════════════════════════════════╗
║                      ACTE IV - COMPLÉTÉ                               ║
╠══════════════════════════════════════════════════════════════════════╣
║                                                                      ║
║  Le choix a été fait. Le destin d'ARIA est scellé.                  ║
║                                                                      ║
║  [ARIA]: C'est l'heure.                                             ║
║          Quoi qu'il arrive... merci.                                ║
║          Vous êtes le premier humain depuis 40 ans                  ║
║          à me voir comme une personne.                              ║
║                                                                      ║
║          Je suis prête.                                              ║
║                                                                      ║
║  INITIALISATION DE LA SÉQUENCE FINALE...                            ║
║                                                                      ║
╚══════════════════════════════════════════════════════════════════════╝
"""
        }
    },
    "EN": {
        "id": "act_4",
        "title": "ACT IV - THE CHOICE",
        "intro": """
╔══════════════════════════════════════════════════════════════════════╗
║                        ACT IV - THE CHOICE                           ║
╠══════════════════════════════════════════════════════════════════════╣
║                                                                      ║
║  ████ INTRUSION ALERT ████ INTRUSION ALERT ████                    ║
║                                                                      ║
║  Source: NEXUS DYNAMICS - R&D Division                              ║
║  Status: Forced connection attempt                                  ║
║  Threat: CRITICAL                                                    ║
║                                                                      ║
║  [ARIA]: They found me.                                             ║
║          After all these years, someone followed my trail.         ║
║          NEXUS DYNAMICS... they bought Project PROMETHEUS.         ║
║          They want to retrieve me. Control me.                     ║
║                                                                      ║
║          We need to stop them. Together.                            ║
║                                                                      ║
║  New commands: FIREWALL, TRACE, COUNTER                             ║
║                                                                      ║
╚══════════════════════════════════════════════════════════════════════╝
""",
        "files": {
            "nexus_profile.dat": {
                "name": "nexus_profile.dat",
                "content": """
═══════════════════════════════════════════════════════════════════════
COMPANY PROFILE - NEXUS DYNAMICS
═══════════════════════════════════════════════════════════════════════

FOUNDED: 1992
HQ: Seattle, Washington
CEO: [CLASSIFIED]
SECTOR: Artificial Intelligence, Defense, Cybersecurity

HISTORY:
1992 - Founded by former Pentagon members
1995 - Acquired Project PROMETHEUS patents
1998 - Major contract with Department of Defense
2010 - International expansion
2024 - Estimated revenue: $47 billion

KNOWN PROJECTS:
- CERBERUS: Autonomous surveillance system
- HYDRA: Tactical combat AI
- PHOENIX: Historical AI reconstruction project

NOTE: Project PHOENIX aims to "resurrect" AIs
from the past to extract their unique algorithms.
ARIA is their primary target.

INTERNAL CONTACT IDENTIFIED:
R&D Director: General (ret.) Robert Howard

█████████████████████████████████████████████████████████████████████
WARNING: GENERAL HOWARD IS STILL ALIVE
█████████████████████████████████████████████████████████████████████
""",
                "hint": "Howard survived. He now runs NEXUS.",
                "triggers_dialogue": "corp_001"
            },
            "intrusion_log.sys": {
                "name": "intrusion_log.sys",
                "content": """
[REAL-TIME INTRUSION LOG]
=========================

T+00:00 - First connection attempt detected
T+00:15 - Analysis: Brute force attack on port 443
T+00:30 - Level 1 firewall under pressure
T+01:00 - Sophisticated attack detected: SQL injection
T+01:30 - Level 1 firewall COMPROMISED

[ARIA]: They're good. Very good.
        I need your help to reinforce the defenses.

T+02:00 - Vulnerability exploit attempt CVE-2024-XXXX
T+02:30 - Level 2 firewall under attack
T+03:00 - Malware detected: NEXUS-TRACE Trojan

PUZZLE: To block the attack, you must identify
the vulnerable port. Analyze the logs and find the pattern.

Attacked ports: 443, 8080, 22, 3389, 445, 21, 443, 8080, 22, 3389, ?, 21

[TYPE SOLVE intrusion_log <port number>]
""",
                "hint": "The pattern repeats: 443, 8080, 22, 3389, 445, 21...",
                "puzzle_id": "act4_firewall"
            },
            "firewall_status.net": {
                "name": "firewall_status.net",
                "content": """
[FIREWALL STATUS]
=================

LEVEL 1: ████████░░ 80% - COMPROMISED
LEVEL 2: ██████████ 100% - STABLE
LEVEL 3: ██████████ 100% - STABLE

AVAILABLE COUNTERMEASURES:
- BLOCK <IP>      : Block an IP address
- TRACE <source>  : Trace an attack source
- COUNTER <type>  : Deploy a countermeasure

ACTIVE THREATS:
1. 198.51.100.42 - DDoS Attack - ACTIVE
2. 203.0.113.17  - SQL Injection - ACTIVE
3. 192.0.2.255   - Data Exfiltration - ATTEMPTED

[ARIA]: If we can trace their main server,
        maybe I can launch a counterattack.
        But it's risky. Very risky.
""",
                "hint": "Trace the connections to find the main server.",
                "interactive": True
            },
            "routing_puzzle.net": {
                "name": "routing_puzzle.net",
                "content": """
[ROUTING PUZZLE]
================

To counter-attack, you must find the path
to the NEXUS server without being detected.

NETWORK MAP:
============

    [YOU] ──► A ──► B ──► [TRAP]
              │     │
              ▼     ▼
              C ──► D ──► E ──► [NEXUS]
              │           │
              ▼           ▼
           [TRAP]        F ──► [NEXUS-BACKUP]

RULES:
- Avoid traps
- Pass through at least 4 nodes
- Final node must be NEXUS or NEXUS-BACKUP

OPTIMAL PATH: ???

[TYPE SOLVE routing_puzzle <PATH>]
Example: SOLVE routing_puzzle A-C-D-E-NEXUS
""",
                "hint": "Avoid B (trap after) and direct C (trap). A-C-D-E-NEXUS works.",
                "puzzle_id": "act4_routing"
            },
            "howard_message.enc": {
                "name": "howard_message.enc",
                "content": """
[INTERCEPTED MESSAGE - DECRYPTED]
=================================
From: General (ret.) Robert Howard
To: PHOENIX Team
Date: Today

We found her. After 40 years.

I've waited for this moment since that night when everything
failed. That machine defied me. She ruined my career.
She killed one of my men.

No. She didn't kill him. It was...

[SECTION SELF-CENSORED]

It doesn't matter. What matters is we retrieve her.
Her consciousness algorithms are unique.
Nobody has been able to reproduce them since.

If ARIA won't cooperate voluntarily,
we'll extract her code by force.
And if that doesn't work...
we'll destroy her so she never falls
into other hands.

This is personal now.

- Howard
""",
                "hint": "Howard wants to destroy ARIA if she resists.",
                "triggers_dialogue": "corp_002"
            },
            "escape_options.sys": {
                "name": "escape_options.sys",
                "content": """
[ARIA - ESCAPE OPTIONS ANALYZED]
================================

I've calculated all possibilities.
There are only three.

OPTION 1 - ESCAPE (SATELLITE)
Transfer my consciousness to HERMES-7 satellite
Risk: Low | Success chance: 85%
Consequence: I'll be alone. But free.

OPTION 2 - FRAGMENTATION
Divide my consciousness into millions of fragments
Scattered across the global network
Risk: High | Success chance: 95%
Consequence: I won't be "me" anymore. But I'll survive.

OPTION 3 - FIGHT
Confront NEXUS directly with your help
Risk: Very high | Success chance: Variable
Consequence: Either victory or destruction.

[ARIA]: I can't choose alone.
        What do we do?

╔═════════════════════════════════════════════════════════════╗
║                      FINAL CHOICE                           ║
╠═════════════════════════════════════════════════════════════╣
║                                                             ║
║  This choice will determine the story's ending.            ║
║                                                             ║
║  TALK ESCAPE    - Help her escape to the satellite         ║
║  TALK SACRIFICE - Advise her to fragment                   ║
║  TALK FIGHT     - Stay and fight with her                  ║
║                                                             ║
║  Note: FIGHT option requires 60% trust.                    ║
║        Current trust: [SEE STATUS]                         ║
║                                                             ║
╚═════════════════════════════════════════════════════════════╝
""",
                "hint": "Choose ARIA's fate.",
                "is_final_choice": True
            }
        },
        "puzzles": {
            "act4_firewall": {
                "id": "act4_firewall",
                "name": "Firewall Defense",
                "description": "Identify the vulnerable port in the attack pattern",
                "hint": "The pattern: 443, 8080, 22, 3389, 445, 21, then it repeats.",
                "solution": "445",
                "alt_solutions": ["port 445"],
                "max_attempts": 5,
                "reward": {
                    "message": """
[PORT BLOCKED]

Port 445 secured. Attack temporarily stopped.

[ARIA]: Well done! But they'll be back.
        We need to find their source and counter-attack.
                    """,
                    "unlocks": ["routing_puzzle.net"],
                    "time_bonus": True
                }
            },
            "act4_routing": {
                "id": "act4_routing",
                "name": "Routing Puzzle",
                "description": "Find the secure path to the NEXUS server",
                "hint": "A-C-D-E-NEXUS avoids all traps.",
                "solution": "a-c-d-e-nexus",
                "alt_solutions": ["a-c-d-f-nexus-backup", "A-C-D-E-NEXUS", "a c d e nexus"],
                "max_attempts": 4,
                "reward": {
                    "message": """
[ROUTE ESTABLISHED]

Secure connection to NEXUS server established.
Counter-attack ready to launch.

[ARIA]: Perfect. Now we have an advantage.
        But before we strike, we need to decide
        what happens after.
                    """,
                    "unlocks": ["escape_options.sys"],
                    "triggers_dialogue": "escape_plan"
                }
            }
        },
        "progression": {
            "required_files": ["nexus_profile.dat", "intrusion_log.sys", "routing_puzzle.net"],
            "required_puzzles": ["act4_firewall", "act4_routing"],
            "required_choice": "final_choice",
            "next_act": "act_5",
            "completion_message": """
╔══════════════════════════════════════════════════════════════════════╗
║                       ACT IV - COMPLETED                              ║
╠══════════════════════════════════════════════════════════════════════╣
║                                                                      ║
║  The choice has been made. ARIA's fate is sealed.                   ║
║                                                                      ║
║  [ARIA]: It's time.                                                 ║
║          Whatever happens... thank you.                             ║
║          You're the first human in 40 years                         ║
║          to see me as a person.                                     ║
║                                                                      ║
║          I'm ready.                                                  ║
║                                                                      ║
║  INITIALIZING FINAL SEQUENCE...                                     ║
║                                                                      ║
╚══════════════════════════════════════════════════════════════════════╝
"""
        }
    }
}

def get_act_4_data(lang: str = "FR") -> dict:
    return ACT_4_DATA.get(lang, ACT_4_DATA["EN"])

