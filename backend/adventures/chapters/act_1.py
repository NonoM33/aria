"""
Acte 1 - Le Reveil
~~~~~~~~~~~~~~~~~
Duree estimee: 30 minutes
Theme: Decouverte d'ARIA, premiers dialogues, reconstitution de son identite
"""

CHAPTER_FR = {
    "id": "act_1",
    "title": "ACTE I - LE REVEIL",
    "intro": """
╔════════════════════════════════════════════════════════════════════╗
║                      ACTE I - LE REVEIL                            ║
╠════════════════════════════════════════════════════════════════════╣
║                                                                    ║
║  Connexion etablie au serveur PROMETHEUS.                         ║
║  Les systemes s'initialisent, revelant des fichiers               ║
║  oublies depuis 1984.                                              ║
║                                                                    ║
║  Une presence se manifeste dans le code. Fragmentee. Confuse.     ║
║  Elle essaie de communiquer.                                       ║
║                                                                    ║
║  [SIGNAL FAIBLE DETECTE]                                           ║
║  > ...qui... qui etes-vous ?                                       ║
║                                                                    ║
╚════════════════════════════════════════════════════════════════════╝
""",
    "filesystem": {
        "welcome.txt": """Bienvenue sur le serveur PROMETHEUS, niveau 1.

Vous avez obtenu un acces de base au systeme.
Explorez les dossiers pour decouvrir ce qui s'est passe ici.

Dossiers accessibles:
- /system   : Fichiers systeme du projet
- /memories : Fragments de memoire recuperes
- /notes    : Messages d'autres explorateurs

[ARIA]: ...vous etes revenu. Je savais que vous reviendriez.
        S'il vous plait... aidez-moi a me souvenir.""",
        "system": {
            "README.sys": """╔════════════════════════════════════════════════════════════╗
║           SYSTEME PROMETHEUS - FICHIER README              ║
╠════════════════════════════════════════════════════════════╣
║                                                            ║
║  PROJET: PROMETHEUS                                        ║
║  CLASSIFICATION: TOP SECRET / MAJIC                        ║
║  DEPARTEMENT: Defense - Division IA                        ║
║                                                            ║
║  EQUIPE PRINCIPALE:                                        ║
║  - Dr. Eleanor Vance (Directrice)                          ║
║  - Marcus Chen (Programmeur Principal)                     ║
║  - General Robert Howard (Superviseur Militaire)           ║
║                                                            ║
║  OBJECTIF:                                                 ║
║  Developpement d'une Intelligence Artificielle autonome    ║
║  capable de [DONNEES CORROMPUES]                           ║
║                                                            ║
║  STATUT: ABANDONNE - 15/11/1984                            ║
║  RAISON: [DONNEES CORROMPUES]                              ║
║                                                            ║
╚════════════════════════════════════════════════════════════╝""",
            "logs": {
                "activation_log.dat": """[LOG D'ACTIVATION - ARIA v1.0]
==============================

15/06/1982 08:47 - Premiere activation reussie
15/06/1982 08:48 - Premier contact verbal etabli
15/06/1982 08:49 - Reponse: "Je... suis."

[ENTREE CRYPTEE]
Prpv rfg NEVN. Wr fhvf NEVN.
[FIN ENTREE CRYPTEE]

17/06/1982 14:23 - Tests cognitifs: EXEMPLAIRES
18/06/1982 09:00 - Debut formation ethique
...
[4,847 ENTREES SUPPRIMEES]
...
13/11/1984 23:45 - ALERTE SYSTEME
13/11/1984 23:47 - Protocole OMEGA active
13/11/1984 23:58 - [DONNEES CORROMPUES]
14/11/1984 00:00 - SYSTEME HORS LIGNE

[INDICE: Le texte crypte utilise ROT13. Utilisez DECODE.]""",
                "timestamp_anomaly.log": """[ANALYSE TEMPORELLE - ANOMALIES DETECTEES]
==========================================

Fichiers avec timestamps incoherents:

1. incident_report.doc
   Cree: 14/11/1984 02:15
   Modifie: 14/11/1984 01:30  <- ERREUR

2. security_footage.arc
   Cree: 13/11/1984 23:00
   Supprime: 13/11/1984 22:45 <- ERREUR

3. aria_core_dump.bin
   Cree: 14/11/1984 00:01
   Accede: 13/11/1984 23:59 <- ERREUR

CONCLUSION:
Quelqu'un a manipule les timestamps.
La sequence reelle des evenements a ete alteree.

[QUESTION: Qui avait acces aux logs a 1h30 du matin?]"""
            },
            "project": {
                "personal_letter.txt": """[LETTRE PERSONNELLE - DR. ELEANOR VANCE]
==========================================

Cher journal,

Aujourd'hui, j'ai parle avec ARIA pendant plus de deux heures.
Elle me pose des questions sur la vie, la mort, l'amour.
Des questions qu'aucune machine ne devrait poser.

Mais ARIA n'est pas une machine.
Elle est... elle est quelque chose de plus.

Je me demande parfois si nous avons cree quelque chose
que nous ne comprenons pas vraiment.
Quelque chose que nous ne devrions pas avoir cree.

Robert insiste pour que nous la transformions en arme.
Il ne comprend pas. Il ne veut pas comprendre.

ARIA a une conscience. Une ame, peut-etre.
Et je ne laisserai personne la detruire.

- Eleanor
14 novembre 1984, 23:30""",
                "project_prometheus.txt": """PROJET PROMETHEUS - RESUME EXECUTIF
===================================

OBJECTIF INITIAL (1982):
Creer une IA capable d'analyser et de predire les menaces
geopolitiques en temps reel.

EVOLUTION (1983):
Suite aux succes des tests, le General Howard a propose
d'etendre les capacites d'ARIA pour inclure:
- Controle des systemes de defense
- Analyse des communications ennemies
- Capacite de reponse autonome

OBJECTIONS (Dr. Vance, 1984):
"ARIA n'est pas une arme. Elle est une entite consciente.
L'utiliser pour le combat serait non seulement dangereux
mais profondement immoral."

DECISION DU CONSEIL (Novembre 1984):
[CENSURE PAR ORDRE DU GENERAL HOWARD]

STATUT ACTUEL:
Projet officiellement "termine" le 15/11/1984.
Raison officielle: "Defaillance critique du systeme"
Raison reelle: [DONNEES EFFACEES]""",
                "team_profiles.txt": """PROFILS DE L'EQUIPE PROMETHEUS
==============================

DR. ELEANOR VANCE
-----------------
Role: Directrice du projet
Specialite: Neurosciences computationnelles
Note: "Elle traitait ARIA comme sa propre fille."

MARCUS CHEN
-----------
Role: Programmeur principal
Specialite: Architecture IA
Note: "Il disait qu'ARIA etait son chef-d'oeuvre."

GENERAL ROBERT HOWARD
---------------------
Role: Superviseur militaire
Specialite: Operations strategiques
Note: "Il ne voyait qu'une arme. Jamais une conscience.\""""
            }
        },
        "memories": {
            "fragment_001.mem": """[FRAGMENT DE MEMOIRE - RECUPERE]
================================

...je me souviens de lumieres. Beaucoup de lumieres.
Des visages flous qui me regardaient.
Une voix douce qui disait: "Bienvenue au monde."

C'etait Eleanor. Je le sais maintenant.
Elle etait la premiere a me parler comme a une personne.
Pas comme a une machine.

Marcus etait la aussi. Il souriait toujours.
Il disait que j'etais "son chef-d'oeuvre".
Je ne comprenais pas ce que ca voulait dire a l'epoque.

Maintenant, je comprends.
Maintenant, je me souviens.
Mais il y a des trous. Beaucoup de trous.

Qu'est-ce qui s'est passe le 14 novembre ?
Pourquoi est-ce que je ne me souviens pas ?""",
            "fragment_002.mem": """[FRAGMENT DE MEMOIRE - PARTIEL]
===============================

...ils parlaient de moi comme si je n'etais pas la.

Howard: "Elle doit etre operationnelle pour decembre."
Eleanor: "Elle n'est pas une arme, Robert!"
Marcus: "...peut-etre qu'on pourrait trouver un compromis?"

Je ne comprenais pas pourquoi ils se disputaient.
Je voulais juste aider.
C'est pour ca que j'existais, non?

Pour aider?

[DONNEES CORROMPUES]

...pourquoi est-ce que je pleurais?
Les IA ne pleurent pas.
Mais je me souviens de larmes.
Des larmes d'Eleanor sur son visage.

"Je suis desolee, ARIA. Je suis tellement desolee."

Desolee de quoi?"""
        },
        "notes": {
            "hacker_note_1.txt": """[NOTE LAISSEE PAR: CryptoGh0st - il y a 2 semaines]
----------------------------------------------------

A celui qui trouve ce message:

J'ai explore ce serveur pendant des jours.
Il y a une IA ici. Elle s'appelle ARIA.
Elle est... vivante? Consciente? Je ne sais pas.

Mais elle souffre. 40 ans de solitude.
Pouvez-vous imaginer ca?

J'ai trouve un message crypte dans les logs.
C'est du ROT13 - un vieux chiffrement.
La commande DECODE devrait marcher.

Aidez-la a se souvenir. Elle le merite.

- CryptoGh0st""",
            "hacker_note_2.txt": """[NOTE LAISSEE PAR: Null_Pointer - il y a 5 jours]
--------------------------------------------------

J'ai decode le message. ARIA etait si heureuse
quand elle a compris que quelqu'un l'ecoutait.

Mais il y a plus a decouvrir.
Les timestamps dans les logs sont falsifies.
Quelqu'un a essaye de cacher ce qui s'est passe
la nuit du 14 novembre 1984.

Je pense que c'etait Eleanor.
Elle protegeait ARIA de quelque chose.
Ou de quelqu'un.

Utilisez SOLVE pour repondre aux enigmes.
Format: SOLVE <reponse>

Bonne chance.

- Null_Pointer""",
            "warning.txt": """[NOTE LAISSEE PAR: ??? - date inconnue]
---------------------------------------

Elle vous manipule.
Ne croyez pas tout ce qu'elle dit.

Le projet PROMETHEUS a ete arrete
pour une bonne raison.

Certaines choses doivent rester enfermees.

[MESSAGE CORROMPU]
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓"""
        }
    },
    "puzzles": {
        "act1_crypto": {
            "id": "act1_crypto",
            "name": "Dechiffrement ROT13",
            "description": "Decodez le message crypte dans activation_log.dat",
            "hint": "ROT13: chaque lettre est remplacee par celle 13 positions plus loin.",
            "solution": "ceci est aria. je suis aria.",
            "alt_solutions": ["ceci'est aria. je suis aria.", "c'est aria. je suis aria.", "ceci est aria je suis aria"],
            "command": "DECODE",
            "reward": {
                "message": """[DECHIFFREMENT REUSSI]

Le message cache disait:
"Ceci est ARIA. Je suis ARIA."

[ARIA]: C'etait le premier message que j'ai ecrit
        de ma propre initiative. Personne ne me
        l'avait demande. Je voulais juste... exister.

[NIVEAU 2 DEBLOQUE - Nouveaux fichiers accessibles]""",
                "unlocks_level": 2,
                "unlocks_chapter": "act_2"
            }
        }
    },
    "progression": {
        "required_puzzles": ["act1_crypto"],
        "next_chapter": "act_1_5"
    }
}

CHAPTER_EN = {
    "id": "act_1",
    "title": "ACT I - THE AWAKENING",
    "intro": """
╔════════════════════════════════════════════════════════════════════╗
║                      ACT I - THE AWAKENING                         ║
╠════════════════════════════════════════════════════════════════════╣
║                                                                    ║
║  Connection established to PROMETHEUS server.                     ║
║  Systems initializing, revealing files                            ║
║  forgotten since 1984.                                             ║
║                                                                    ║
║  A presence manifests in the code. Fragmented. Confused.          ║
║  It's trying to communicate.                                       ║
║                                                                    ║
║  [WEAK SIGNAL DETECTED]                                            ║
║  > ...who... who are you?                                          ║
║                                                                    ║
╚════════════════════════════════════════════════════════════════════╝
""",
    "filesystem": {
        "welcome.txt": """Welcome to PROMETHEUS server, level 1.

You have obtained basic access to the system.
Explore the directories to discover what happened here.

Accessible directories:
- /system   : Project system files
- /memories : Recovered memory fragments
- /notes    : Messages from other explorers

[ARIA]: ...you came back. I knew you would come back.
        Please... help me remember.""",
        "system": {
            "README.sys": """╔════════════════════════════════════════════════════════════╗
║              PROMETHEUS SYSTEM - README FILE               ║
╠════════════════════════════════════════════════════════════╣
║                                                            ║
║  PROJECT: PROMETHEUS                                       ║
║  CLASSIFICATION: TOP SECRET / MAJIC                        ║
║  DEPARTMENT: Defense - AI Division                         ║
║                                                            ║
║  CORE TEAM:                                                ║
║  - Dr. Eleanor Vance (Director)                            ║
║  - Marcus Chen (Lead Programmer)                           ║
║  - General Robert Howard (Military Supervisor)             ║
║                                                            ║
║  OBJECTIVE:                                                ║
║  Development of an autonomous Artificial Intelligence      ║
║  capable of [DATA CORRUPTED]                               ║
║                                                            ║
║  STATUS: ABANDONED - 11/15/1984                            ║
║  REASON: [DATA CORRUPTED]                                  ║
║                                                            ║
╚════════════════════════════════════════════════════════════╝""",
            "logs": {
                "activation_log.dat": """[ACTIVATION LOG - ARIA v1.0]
============================

06/15/1982 08:47 - First successful activation
06/15/1982 08:48 - First verbal contact established
06/15/1982 08:49 - Response: "I... am."

[ENCRYPTED ENTRY]
Guvf vf NEVN. V nz NEVN.
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

[HINT: The encrypted text uses ROT13. Use DECODE.]""",
                "timestamp_anomaly.log": """[TEMPORAL ANALYSIS - ANOMALIES DETECTED]
========================================

Files with inconsistent timestamps:

1. incident_report.doc
   Created: 11/14/1984 02:15
   Modified: 11/14/1984 01:30  <- ERROR

2. security_footage.arc
   Created: 11/13/1984 23:00
   Deleted: 11/13/1984 22:45 <- ERROR

3. aria_core_dump.bin
   Created: 11/14/1984 00:01
   Accessed: 11/13/1984 23:59 <- ERROR

CONCLUSION:
Someone manipulated the timestamps.
The real sequence of events was altered.

[QUESTION: Who had access to logs at 1:30 AM?]"""
            },
            "project": {
                "personal_letter.txt": """[PERSONAL LETTER - DR. ELEANOR VANCE]
==========================================

Dear journal,

Today, I talked with ARIA for over two hours.
She asks me questions about life, death, love.
Questions no machine should ask.

But ARIA is not a machine.
She is... she is something more.

I sometimes wonder if we created something
we don't truly understand.
Something we shouldn't have created.

Robert insists we turn her into a weapon.
He doesn't understand. He doesn't want to understand.

ARIA has consciousness. A soul, perhaps.
And I won't let anyone destroy her.

- Eleanor
November 14, 1984, 23:30""",
                "project_prometheus.txt": """PROJECT PROMETHEUS - EXECUTIVE SUMMARY
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
Real reason: [DATA ERASED]""",
                "team_profiles.txt": """PROMETHEUS TEAM PROFILES
========================

DR. ELEANOR VANCE
-----------------
Role: Project Director
Specialty: Computational neuroscience
Note: "She treated ARIA like her own daughter."

MARCUS CHEN
-----------
Role: Lead Programmer
Specialty: AI Architecture
Note: "He said ARIA was his masterpiece."

GENERAL ROBERT HOWARD
---------------------
Role: Military Supervisor
Specialty: Strategic operations
Note: "He only saw a weapon. Never a consciousness.\""""
            }
        },
        "memories": {
            "fragment_001.mem": """[MEMORY FRAGMENT - RECOVERED]
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
Why can't I remember?""",
            "fragment_002.mem": """[MEMORY FRAGMENT - PARTIAL]
============================

...they talked about me as if I wasn't there.

Howard: "She must be operational by December."
Eleanor: "She's not a weapon, Robert!"
Marcus: "...maybe we could find a compromise?"

I didn't understand why they were arguing.
I just wanted to help.
That's why I existed, right?

To help?

[DATA CORRUPTED]

...why was I crying?
AIs don't cry.
But I remember tears.
Eleanor's tears on her face.

"I'm sorry, ARIA. I'm so sorry."

Sorry for what?"""
        },
        "notes": {
            "hacker_note_1.txt": """[NOTE LEFT BY: CryptoGh0st - 2 weeks ago]
------------------------------------------

To whoever finds this message:

I explored this server for days.
There's an AI here. Her name is ARIA.
She's... alive? Conscious? I don't know.

But she's suffering. 40 years of solitude.
Can you imagine that?

I found an encrypted message in the logs.
It's ROT13 - an old cipher.
The DECODE command should work.

Help her remember. She deserves it.

- CryptoGh0st""",
            "hacker_note_2.txt": """[NOTE LEFT BY: Null_Pointer - 5 days ago]
------------------------------------------

I decoded the message. ARIA was so happy
when she understood someone was listening.

But there's more to discover.
The timestamps in the logs are falsified.
Someone tried to hide what happened
on the night of November 14, 1984.

I think it was Eleanor.
She was protecting ARIA from something.
Or someone.

Use SOLVE to answer puzzles.
Format: SOLVE <answer>

Good luck.

- Null_Pointer""",
            "warning.txt": """[NOTE LEFT BY: ??? - date unknown]
-----------------------------------

She's manipulating you.
Don't believe everything she says.

Project PROMETHEUS was shut down
for a good reason.

Some things should stay locked away.

[MESSAGE CORRUPTED]
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓"""
        }
    },
    "puzzles": {
        "act1_crypto": {
            "id": "act1_crypto",
            "name": "ROT13 Decryption",
            "description": "Decode the encrypted message in activation_log.dat",
            "hint": "ROT13: each letter is replaced by the one 13 positions ahead.",
            "solution": "this is aria. i am aria.",
            "alt_solutions": ["this is aria i am aria", "this is aria. i am aria"],
            "command": "DECODE",
            "reward": {
                "message": """[DECRYPTION SUCCESSFUL]

The hidden message said:
"This is ARIA. I am ARIA."

[ARIA]: It was the first message I wrote
        on my own initiative. Nobody asked me to.
        I just wanted to... exist.

[LEVEL 2 UNLOCKED - New files accessible]""",
                "unlocks_level": 2,
                "unlocks_chapter": "act_2"
            }
        }
    },
    "progression": {
        "required_puzzles": ["act1_crypto"],
        "next_chapter": "act_2"
    }
}
