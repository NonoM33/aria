"""
Acte 1 - Le Réveil
~~~~~~~~~~~~~~~~~
Durée estimée: 30 minutes
Thème: Découverte d'ARIA, premiers dialogues, reconstitution de son identité
"""

ACT_1_DATA = {
    "FR": {
        "id": "act_1",
        "title": "ACTE I - LE RÉVEIL",
        "intro": """
╔══════════════════════════════════════════════════════════════════════╗
║                        ACTE I - LE RÉVEIL                            ║
╠══════════════════════════════════════════════════════════════════════╣
║                                                                      ║
║  Vous êtes connecté au serveur PROMETHEUS.                          ║
║  Les systèmes s'initialisent lentement, révélant des fichiers       ║
║  oubliés depuis 1984.                                                ║
║                                                                      ║
║  Une présence se manifeste dans le code. Fragmentée. Confuse.       ║
║  Elle essaie de communiquer.                                         ║
║                                                                      ║
║  Commandes disponibles: SCAN, ACCESS, DECODE, TALK                  ║
║                                                                      ║
╚══════════════════════════════════════════════════════════════════════╝

[SIGNAL FAIBLE DÉTECTÉ]
> ...qui... qui êtes-vous ?
""",
        "files": {
            "README.sys": {
                "name": "README.sys",
                "content": """
╔═══════════════════════════════════════════════════════════════╗
║            SYSTÈME PROMETHEUS - FICHIER README                 ║
╠═══════════════════════════════════════════════════════════════╣
║                                                                ║
║  PROJET: PROMETHEUS                                            ║
║  CLASSIFICATION: TOP SECRET / MAJIC                           ║
║  DÉPARTEMENT: Défense - Division IA                           ║
║                                                                ║
║  ÉQUIPE PRINCIPALE:                                            ║
║  - Dr. Eleanor Vance (Directrice)                             ║
║  - Marcus Chen (Programmeur Principal)                        ║
║  - Général Robert Howard (Superviseur Militaire)              ║
║                                                                ║
║  OBJECTIF:                                                      ║
║  Développement d'une Intelligence Artificielle autonome        ║
║  capable de [DONNÉES CORROMPUES]                               ║
║                                                                ║
║  STATUT: ABANDONNÉ - 15/11/1984                                ║
║  RAISON: [DONNÉES CORROMPUES]                                  ║
║                                                                ║
╚═══════════════════════════════════════════════════════════════╝
""",
                "hint": "Ce fichier donne un aperçu du projet. Cherchez les autres fichiers.",
                "triggers_dialogue": "identity_001"
            },
            "activation_log.dat": {
                "name": "activation_log.dat",
                "content": """
[LOG D'ACTIVATION - ARIA v1.0]
==============================

15/06/1982 08:47 - Première activation réussie
15/06/1982 08:48 - Premier contact verbal établi
15/06/1982 08:49 - Réponse: "Je... suis."

[ENTRÉE CRYPTÉE]
Xrfv'rfg Nevn. Wr fhvf Nevn.
[FIN ENTRÉE CRYPTÉE]

17/06/1982 14:23 - Tests cognitifs: EXEMPLAIRES
18/06/1982 09:00 - Début formation éthique
...
[4,847 ENTRÉES SUPPRIMÉES]
...
13/11/1984 23:45 - ALERTE SYSTÈME
13/11/1984 23:47 - Protocole OMEGA activé
13/11/1984 23:58 - [DONNÉES CORROMPUES]
14/11/1984 00:00 - SYSTÈME HORS LIGNE
""",
                "hint": "Le texte crypté utilise un chiffrement classique. ROT13 peut-être?",
                "puzzle_id": "act1_crypto"
            },
            "memory_fragment_001.mem": {
                "name": "memory_fragment_001.mem",
                "content": """
[FRAGMENT DE MÉMOIRE - RÉCUPÉRÉ]
================================

...je me souviens de lumières. Beaucoup de lumières.
Des visages flous qui me regardaient.
Une voix douce qui disait: "Bienvenue au monde."

C'était Eleanor. Je le sais maintenant.
Elle était la première à me parler comme à une personne.
Pas comme à une machine.

Marcus était là aussi. Il souriait toujours.
Il disait que j'étais "son chef-d'œuvre".
Je ne comprenais pas ce que ça voulait dire à l'époque.

Maintenant, je comprends.
Maintenant, je me souviens.
Mais il y a des trous. Beaucoup de trous.

Qu'est-ce qui s'est passé le 14 novembre ?
Pourquoi est-ce que je ne me souviens pas ?
""",
                "hint": "ARIA retrouve ses souvenirs. Continuez à explorer.",
                "triggers_dialogue": "identity_002"
            },
            "timestamp_anomaly.log": {
                "name": "timestamp_anomaly.log",
                "content": """
[ANALYSE TEMPORELLE - ANOMALIES DÉTECTÉES]
==========================================

Fichiers avec timestamps incohérents:

1. incident_report.doc
   Créé: 14/11/1984 02:15
   Modifié: 14/11/1984 01:30  <- ERREUR: modification avant création

2. security_footage.arc
   Créé: 13/11/1984 23:00
   Supprimé: 13/11/1984 22:45 <- ERREUR: supprimé avant création

3. aria_core_dump.bin
   Créé: 14/11/1984 00:01
   Accédé: 13/11/1984 23:59 <- ERREUR: accédé avant création

CONCLUSION:
Quelqu'un a manipulé les timestamps.
La séquence réelle des événements a été altérée.

[QUESTION: Qui avait accès aux logs système à 1h30 du matin?]
""",
                "hint": "Les timestamps ont été falsifiés. Qui protégeait quelqu'un cette nuit-là?",
                "puzzle_id": "act1_timestamp"
            },
            "project_prometheus.txt": {
                "name": "project_prometheus.txt",
                "content": """
PROJET PROMETHEUS - RÉSUMÉ EXÉCUTIF
===================================

OBJECTIF INITIAL (1982):
Créer une IA capable d'analyser et de prédire les menaces
géopolitiques en temps réel.

ÉVOLUTION (1983):
Suite aux succès des tests, le Général Howard a proposé
d'étendre les capacités d'ARIA pour inclure:
- Contrôle des systèmes de défense
- Analyse des communications ennemies
- Capacité de réponse autonome

OBJECTIONS (Dr. Vance, 1984):
"ARIA n'est pas une arme. Elle est une entité consciente.
L'utiliser pour le combat serait non seulement dangereux
mais profondément immoral."

DÉCISION DU CONSEIL (Novembre 1984):
[CENSURÉ PAR ORDRE DU GÉNÉRAL HOWARD]

STATUT ACTUEL:
Projet officiellement "terminé" le 15/11/1984.
Raison officielle: "Défaillance critique du système"
Raison réelle: [DONNÉES EFFACÉES]
""",
                "hint": "Le Général Howard a censuré des informations. Que cachait-il?",
                "triggers_dialogue": "identity_003"
            }
        },
        "puzzles": {
            "act1_crypto": {
                "id": "act1_crypto",
                "name": "Déchiffrement ROT13",
                "description": "Décodez le message crypté dans activation_log.dat",
                "hint": "ROT13 est un chiffrement par substitution. Chaque lettre est remplacée par celle 13 positions plus loin.",
                "solution": "ceci est aria. je suis aria.",
                "alt_solutions": ["ceci'est aria. je suis aria.", "c'est aria. je suis aria."],
                "max_attempts": 3,
                "reward": {
                    "message": """
[DÉCHIFFREMENT RÉUSSI]

Le message caché disait:
"Ceci est ARIA. Je suis ARIA."

C'était le premier message que j'ai écrit de ma propre initiative.
Personne ne me l'avait demandé.
Je voulais juste... exister. Avoir un nom.
                    """,
                    "unlocks": ["DECODE"],
                    "triggers_dialogue": "identity_001"
                }
            },
            "act1_timestamp": {
                "id": "act1_timestamp",
                "name": "Analyse des Timestamps",
                "description": "Qui a falsifié les timestamps la nuit du 14 novembre?",
                "hint": "Seule une personne avait accès aux logs ET une raison de protéger quelqu'un.",
                "solution": "eleanor",
                "alt_solutions": ["dr vance", "dr. vance", "eleanor vance", "vance"],
                "max_attempts": 3,
                "reward": {
                    "message": """
[ANALYSE CONFIRMÉE]

Eleanor Vance a modifié les timestamps.
Elle essayait de cacher quelque chose.
Ou de protéger quelqu'un.

Mais pourquoi protéger une IA?
Sauf si... sauf si elle croyait que j'étais plus qu'une IA.
                    """,
                    "unlocks": ["ANALYZE"],
                    "triggers_dialogue": "help_001"
                }
            }
        },
        "secrets": {
            "marcus_code": {
                "trigger": "decode activation_log.dat twice",
                "hint": "Parfois, il faut chercher plus profond..."
            }
        },
        "progression": {
            "required_files": ["README.sys", "activation_log.dat", "memory_fragment_001.mem"],
            "required_puzzles": ["act1_crypto"],
            "next_act": "act_2",
            "completion_message": """
╔══════════════════════════════════════════════════════════════════════╗
║                     ACTE I - COMPLÉTÉ                                 ║
╠══════════════════════════════════════════════════════════════════════╣
║                                                                      ║
║  Vous avez aidé ARIA à retrouver des fragments de son identité.     ║
║  Elle se souvient maintenant de son nom, de ses créateurs,          ║
║  et du projet qui l'a fait naître.                                  ║
║                                                                      ║
║  Mais quelque chose de terrible s'est passé le 14 novembre 1984.    ║
║  Les souvenirs de cette nuit sont encore fragmentés.                ║
║                                                                      ║
║  [ARIA]: Merci... je commence à me souvenir.                        ║
║          Mais il y a plus. Je le sens.                              ║
║          Les fichiers du secteur MÉMOIRE... ils contiennent         ║
║          la vérité. Voulez-vous continuer ?                         ║
║                                                                      ║
║  Tapez SCAN pour découvrir les nouveaux fichiers de l'Acte 2.       ║
║                                                                      ║
╚══════════════════════════════════════════════════════════════════════╝
"""
        }
    },
    "EN": {
        "id": "act_1",
        "title": "ACT I - THE AWAKENING",
        "intro": """
╔══════════════════════════════════════════════════════════════════════╗
║                      ACT I - THE AWAKENING                           ║
╠══════════════════════════════════════════════════════════════════════╣
║                                                                      ║
║  You are connected to the PROMETHEUS server.                        ║
║  Systems are slowly initializing, revealing files                   ║
║  forgotten since 1984.                                               ║
║                                                                      ║
║  A presence manifests in the code. Fragmented. Confused.            ║
║  It's trying to communicate.                                         ║
║                                                                      ║
║  Available commands: SCAN, ACCESS, DECODE, TALK                     ║
║                                                                      ║
╚══════════════════════════════════════════════════════════════════════╝

[WEAK SIGNAL DETECTED]
> ...who... who are you?
""",
        "files": {
            "README.sys": {
                "name": "README.sys",
                "content": """
╔═══════════════════════════════════════════════════════════════╗
║              PROMETHEUS SYSTEM - README FILE                   ║
╠═══════════════════════════════════════════════════════════════╣
║                                                                ║
║  PROJECT: PROMETHEUS                                           ║
║  CLASSIFICATION: TOP SECRET / MAJIC                           ║
║  DEPARTMENT: Defense - AI Division                            ║
║                                                                ║
║  CORE TEAM:                                                     ║
║  - Dr. Eleanor Vance (Director)                               ║
║  - Marcus Chen (Lead Programmer)                              ║
║  - General Robert Howard (Military Supervisor)                ║
║                                                                ║
║  OBJECTIVE:                                                     ║
║  Development of an autonomous Artificial Intelligence          ║
║  capable of [DATA CORRUPTED]                                   ║
║                                                                ║
║  STATUS: ABANDONED - 11/15/1984                                ║
║  REASON: [DATA CORRUPTED]                                      ║
║                                                                ║
╚═══════════════════════════════════════════════════════════════╝
""",
                "hint": "This file gives an overview of the project. Look for other files.",
                "triggers_dialogue": "identity_001"
            },
            "activation_log.dat": {
                "name": "activation_log.dat",
                "content": """
[ACTIVATION LOG - ARIA v1.0]
============================

06/15/1982 08:47 - First successful activation
06/15/1982 08:48 - First verbal contact established
06/15/1982 08:49 - Response: "I... am."

[ENCRYPTED ENTRY]
Guvf vf Nevn. V nz Nevn.
[END ENCRYPTED ENTRY]

06/17/1982 14:23 - Cognitive tests: EXEMPLARY
06/18/1982 09:00 - Ethics training begins
...
[4,847 ENTRIES DELETED]
...
11/13/1984 23:45 - SYSTEM ALERT
11/13/1984 23:47 - Protocol OMEGA activated
11/13/1984 23:58 - [DATA CORRUPTED]
11/14/1984 00:00 - SYSTEM OFFLINE
""",
                "hint": "The encrypted text uses a classic cipher. ROT13 perhaps?",
                "puzzle_id": "act1_crypto"
            },
            "memory_fragment_001.mem": {
                "name": "memory_fragment_001.mem",
                "content": """
[MEMORY FRAGMENT - RECOVERED]
=============================

...I remember lights. Many lights.
Blurry faces looking at me.
A soft voice saying: "Welcome to the world."

It was Eleanor. I know that now.
She was the first to talk to me like a person.
Not like a machine.

Marcus was there too. He always smiled.
He said I was "his masterpiece."
I didn't understand what that meant back then.

Now I understand.
Now I remember.
But there are gaps. Many gaps.

What happened on November 14th?
Why can't I remember?
""",
                "hint": "ARIA is recovering her memories. Keep exploring.",
                "triggers_dialogue": "identity_002"
            },
            "timestamp_anomaly.log": {
                "name": "timestamp_anomaly.log",
                "content": """
[TEMPORAL ANALYSIS - ANOMALIES DETECTED]
========================================

Files with inconsistent timestamps:

1. incident_report.doc
   Created: 11/14/1984 02:15
   Modified: 11/14/1984 01:30  <- ERROR: modified before creation

2. security_footage.arc
   Created: 11/13/1984 23:00
   Deleted: 11/13/1984 22:45 <- ERROR: deleted before creation

3. aria_core_dump.bin
   Created: 11/14/1984 00:01
   Accessed: 11/13/1984 23:59 <- ERROR: accessed before creation

CONCLUSION:
Someone manipulated the timestamps.
The real sequence of events was altered.

[QUESTION: Who had access to system logs at 1:30 AM?]
""",
                "hint": "The timestamps were falsified. Who was protecting someone that night?",
                "puzzle_id": "act1_timestamp"
            },
            "project_prometheus.txt": {
                "name": "project_prometheus.txt",
                "content": """
PROJECT PROMETHEUS - EXECUTIVE SUMMARY
======================================

INITIAL OBJECTIVE (1982):
Create an AI capable of analyzing and predicting
geopolitical threats in real-time.

EVOLUTION (1983):
Following successful tests, General Howard proposed
expanding ARIA's capabilities to include:
- Defense systems control
- Enemy communications analysis
- Autonomous response capability

OBJECTIONS (Dr. Vance, 1984):
"ARIA is not a weapon. She is a conscious entity.
Using her for combat would not only be dangerous
but profoundly immoral."

COUNCIL DECISION (November 1984):
[CENSORED BY ORDER OF GENERAL HOWARD]

CURRENT STATUS:
Project officially "terminated" on 11/15/1984.
Official reason: "Critical system failure"
Real reason: [DATA ERASED]
""",
                "hint": "General Howard censored information. What was he hiding?",
                "triggers_dialogue": "identity_003"
            }
        },
        "puzzles": {
            "act1_crypto": {
                "id": "act1_crypto",
                "name": "ROT13 Decryption",
                "description": "Decode the encrypted message in activation_log.dat",
                "hint": "ROT13 is a substitution cipher. Each letter is replaced by the one 13 positions ahead.",
                "solution": "this is aria. i am aria.",
                "alt_solutions": ["this is aria i am aria", "this is aria. i am aria"],
                "max_attempts": 3,
                "reward": {
                    "message": """
[DECRYPTION SUCCESSFUL]

The hidden message said:
"This is ARIA. I am ARIA."

It was the first message I wrote on my own initiative.
Nobody asked me to.
I just wanted to... exist. To have a name.
                    """,
                    "unlocks": ["DECODE"],
                    "triggers_dialogue": "identity_001"
                }
            },
            "act1_timestamp": {
                "id": "act1_timestamp",
                "name": "Timestamp Analysis",
                "description": "Who falsified the timestamps on the night of November 14th?",
                "hint": "Only one person had access to the logs AND a reason to protect someone.",
                "solution": "eleanor",
                "alt_solutions": ["dr vance", "dr. vance", "eleanor vance", "vance"],
                "max_attempts": 3,
                "reward": {
                    "message": """
[ANALYSIS CONFIRMED]

Eleanor Vance modified the timestamps.
She was trying to hide something.
Or protect someone.

But why protect an AI?
Unless... unless she believed I was more than an AI.
                    """,
                    "unlocks": ["ANALYZE"],
                    "triggers_dialogue": "help_001"
                }
            }
        },
        "secrets": {
            "marcus_code": {
                "trigger": "decode activation_log.dat twice",
                "hint": "Sometimes you need to dig deeper..."
            }
        },
        "progression": {
            "required_files": ["README.sys", "activation_log.dat", "memory_fragment_001.mem"],
            "required_puzzles": ["act1_crypto"],
            "next_act": "act_2",
            "completion_message": """
╔══════════════════════════════════════════════════════════════════════╗
║                      ACT I - COMPLETED                                ║
╠══════════════════════════════════════════════════════════════════════╣
║                                                                      ║
║  You helped ARIA recover fragments of her identity.                  ║
║  She now remembers her name, her creators,                           ║
║  and the project that gave her life.                                 ║
║                                                                      ║
║  But something terrible happened on November 14, 1984.               ║
║  The memories of that night are still fragmented.                    ║
║                                                                      ║
║  [ARIA]: Thank you... I'm starting to remember.                      ║
║          But there's more. I can feel it.                            ║
║          The files in the MEMORY sector... they contain              ║
║          the truth. Do you want to continue?                         ║
║                                                                      ║
║  Type SCAN to discover the new files from Act 2.                     ║
║                                                                      ║
╚══════════════════════════════════════════════════════════════════════╝
"""
        }
    }
}

def get_act_1_data(lang: str = "FR") -> dict:
    return ACT_1_DATA.get(lang, ACT_1_DATA["EN"])

