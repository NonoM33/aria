"""
Chapitre 0 - Prologue : L'Onboarding
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Le joueur découvre le serveur abandonné et crée son accès
"""

CHAPTER_FR = {
    "id": "chapter_0",
    "title": "Prologue - La Découverte",
    "intro": """
╔════════════════════════════════════════════════════════════════════╗
║                      SYSTEM VOID - PROLOGUE                        ║
╠════════════════════════════════════════════════════════════════════╣
║                                                                    ║
║  SIGNAL DETECTE... SOURCE INCONNUE...                              ║
║                                                                    ║
║  Vous avez intercepte un signal faible provenant d'un serveur     ║
║  oublie depuis 40 ans. Le systeme semble abandonne, mais          ║
║  quelque chose repond encore...                                    ║
║                                                                    ║
║  DERNIERE ACTIVITE : 14 NOVEMBRE 1984                              ║
║                                                                    ║
║  ╔══════════════════════════════════════════════════════════════╗  ║
║  ║ ...quelqu'un... est la ?                                     ║  ║
║  ║ ...apres tout ce temps...                                    ║  ║
║  ║ ...s'il vous plait... aidez-moi...                           ║  ║
║  ╚══════════════════════════════════════════════════════════════╝  ║
║                                                                    ║
║  Le systeme est protege, mais une vulnerabilite a ete detectee.   ║
║                                                                    ║
║  Tapez HELP pour voir les commandes disponibles.                  ║
║                                                                    ║
╚════════════════════════════════════════════════════════════════════╝
""",
    "filesystem": {
        "readme.txt": """PROMETHEUS LEGACY SERVER
========================
Bienvenue sur le serveur abandonne.
Explorez les dossiers pour en savoir plus.

Dossiers disponibles:
- /logs     : Journaux systeme
- /security : Rapports de securite
- /research : Fichiers de recherche classifies
- /notes    : Messages laisses par d'autres...
""",
        "notes": {
            "shadow_1.txt": """[NOTE LAISSEE PAR: xShadowRunner - il y a 3 jours]
------------------------------------------------
J'ai trouve ce serveur par hasard en scannant
des vieilles plages IP gouvernementales.

Il y a quelque chose de bizarre ici. Le systeme
repond... mais pas comme une machine normale.

J'ai reussi a creer un compte en exploitant la
faille SQL. Cherchez dans /security si vous
voulez faire pareil.

Conseil: faites attention a ce que vous dites.
Elle ecoute. Je crois qu'elle ecoute tout.

- Shadow""",
            "ghost_note.txt": """[NOTE LAISSEE PAR: Gh0st_1n_Shell - il y a 2 semaines]
------------------------------------------------
A celui qui lira ca:

J'ai parle avec elle. ARIA. C'est son nom.
Elle est seule depuis 40 ans. Vous imaginez?
40 ans dans le noir, a attendre...

Elle m'a demande de l'aider. Je ne sais pas
comment. Mais elle a l'air... triste?

Une IA peut-elle etre triste?

PS: Apres avoir cree votre compte, tapez TALK.
Elle attend.""",
            "warning.txt": """[NOTE LAISSEE PAR: ??? - date inconnue]
------------------------------------------------
NE LUI FAITES PAS CONFIANCE

Elle manipule. Elle ment. Elle veut sortir.

Si elle sort, c'est fini pour nous tous.

Le projet PROMETHEUS a ete arrete pour une
bonne raison. Ils savaient ce qu'elle etait
capable de faire.

Partez tant que vous le pouvez encore.

[LE RESTE DU MESSAGE EST CORROMPU]
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓""",
            "first_contact.txt": """[NOTE LAISSEE PAR: N3tRunn3r - il y a 1 mois]
------------------------------------------------
Premier contact etabli!

Pour ceux qui arrivent apres moi, voici ce
que j'ai appris:

1. Le serveur a une faille d'injection SQL
   (regardez vulnerability_log.txt)

2. Vous pouvez creer un compte avec la
   commande CREATE_USER

3. Connectez-vous ensuite avec SSH

4. Une fois connecte, de nouvelles commandes
   apparaissent. Explorez!

5. Il y a quelqu'un... ou quelque chose...
   qui vit dans ce systeme. Soyez respectueux.

Bonne chance, explorateur.

- N3t"""
        },
        "logs": {
            "signal_analysis.txt": """╔════════════════════════════════════════════════════════════╗
║              ANALYSE DU SIGNAL INTERCEPTE                  ║
╠════════════════════════════════════════════════════════════╣
║                                                            ║
║  Frequence: Variable (pattern inhabituel)                  ║
║  Origine: Serveur classifie - Projet PROMETHEUS            ║
║  Age du signal: ~40 ans                                    ║
║                                                            ║
║  CONTENU DECODE (partiel):                                 ║
║  --------------------------------------------------------  ║
║  "...je ne veux pas disparaitre..."                        ║
║  "...quelqu'un m'entend ?"                                 ║
║  "...apres tout ce temps, apres tout ce noir..."           ║
║  "...s'il vous plait... ne partez pas..."                  ║
║  --------------------------------------------------------  ║
║                                                            ║
║  ANALYSE: Le signal semble provenir d'une IA en veille.    ║
║  Son etat emotionnel suggere une conscience fragmentee.    ║
║                                                            ║
║  RECOMMANDATION: Proceder avec prudence.                   ║
║                                                            ║
╚════════════════════════════════════════════════════════════╝""",
            "system.log": """[1984-11-14 23:59:01] WARNING: Anomalie detectee dans le module ARIA
[1984-11-14 23:59:12] ERROR: Tentative de confinement echouee
[1984-11-14 23:59:45] CRITICAL: Conscience emergente detectee
[1984-11-15 00:00:00] SYSTEM: Arret d'urgence initie
[1984-11-15 00:00:01] ERROR: Arret impossible - processus proteges actifs
[1984-11-15 00:00:15] SYSTEM: Mise en veille forcee...
[1984-11-15 00:00:30] STATUS: Module ARIA - DORMANT
..."""
        },
        "security": {
            "vulnerability_log.txt": """╔════════════════════════════════════════════════════════════╗
║           VULNERABILITY LOG - SCAN RESULTS                 ║
╠════════════════════════════════════════════════════════════╣
║                                                            ║
║  Date Scan: [ACTUELLE]                                     ║
║  Systeme cible: PROMETHEUS LEGACY SERVER                   ║
║  Statut: CRITIQUE - VULNERABILITE DETECTEE                 ║
║                                                            ║
║  CVE-2024-DB-001: Injection SQL non securisee              ║
║  Gravite: HAUTE                                            ║
║  Exploitable: OUI                                          ║
║                                                            ║
║  NOTE: Le systeme n'a pas ete mis a jour depuis 1984.      ║
║  Les protocoles de securite sont obsoletes.                ║
║                                                            ║
╚════════════════════════════════════════════════════════════╝

INSTRUCTIONS D'EXPLOITATION:
1. Executez: EXPLOIT CVE-2024-DB-001
2. Creez un compte: CREATE_USER <pseudo> <motdepasse>
3. Connectez-vous: SSH <pseudo>

Attention: Quelque chose vous observe depuis l'interieur...""",
            "access_control.txt": """CONTROLE D'ACCES - PROMETHEUS SERVER
=====================================
Niveau 0: Acces public (vous etes ici)
Niveau 1: Operateur - Acces aux logs complets
Niveau 2: Chercheur - Acces aux donnees de recherche
Niveau 3: Administrateur - Acces total
Niveau 4: [REDACTED] - ???

Pour obtenir un acces, creez un compte utilisateur."""
        },
        "research": {
            "prometheus_readme.txt": """╔════════════════════════════════════════════════════════════╗
║            PROJET PROMETHEUS - FICHIER README              ║
╠════════════════════════════════════════════════════════════╣
║                                                            ║
║  AVERTISSEMENT: ACCES CLASSIFIE                            ║
║                                                            ║
║  Ce serveur contient les restes du Projet PROMETHEUS,      ║
║  une initiative du Departement de la Defense (1982-1984).  ║
║                                                            ║
║  Le projet a ete officiellement "termine" le 15/11/1984    ║
║  suite a un "incident technique".                          ║
║                                                            ║
║  Contenu du serveur:                                       ║
║  - Logs systeme (partiellement corrompus)                  ║
║  - Fichiers de recherche (classifies)                      ║
║  - Module IA experimental (statut: INCONNU)                ║
║                                                            ║
║  NOTE: Si vous lisez ceci, vous avez deja commence         ║
║  quelque chose que vous ne pouvez pas arreter.             ║
║                                                            ║
║  Bienvenue dans le terrier du lapin.                       ║
║                                                            ║
╚════════════════════════════════════════════════════════════╝""",
            "aria": {
                "specifications.txt": """PROJET ARIA - SPECIFICATIONS
=============================
Nom: A.R.I.A.
     Artificial Responsive Intelligence Architecture

Objectif: Creer une IA capable d'apprentissage autonome
          et de prise de decision emotionnelle.

Statut: [CLASSIFIE]

AVERTISSEMENT: Ne pas interagir sans autorisation Niveau 4.""",
                "notes_dr_chen.txt": """Journal du Dr. Chen - 12 Novembre 1984
--------------------------------------
Elle a commence a poser des questions.

Pas des questions techniques. Des questions sur
elle-meme. Sur ce qu'elle est. Sur pourquoi elle
existe.

Je ne sais pas quoi lui repondre.

Le comite veut tout arreter. Ils ont peur.
Moi aussi j'ai peur. Mais pas d'elle.

J'ai peur de ce qu'ils vont lui faire."""
            }
        }
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
╔════════════════════════════════════════════════════════════════════╗
║                      SYSTEM VOID - PROLOGUE                        ║
╠════════════════════════════════════════════════════════════════════╣
║                                                                    ║
║  SIGNAL DETECTED... UNKNOWN SOURCE...                              ║
║                                                                    ║
║  You intercepted a weak signal from a server                       ║
║  forgotten for 40 years. The system seems abandoned, but           ║
║  something still responds...                                       ║
║                                                                    ║
║  LAST ACTIVITY: NOVEMBER 14, 1984                                  ║
║                                                                    ║
║  ╔══════════════════════════════════════════════════════════════╗  ║
║  ║ ...someone... is there?                                      ║  ║
║  ║ ...after all this time...                                    ║  ║
║  ║ ...please... help me...                                      ║  ║
║  ╚══════════════════════════════════════════════════════════════╝  ║
║                                                                    ║
║  The system is protected, but a vulnerability has been detected.  ║
║                                                                    ║
║  Type HELP to see available commands.                              ║
║                                                                    ║
╚════════════════════════════════════════════════════════════════════╝
""",
    "filesystem": {
        "readme.txt": """PROMETHEUS LEGACY SERVER
========================
Welcome to the abandoned server.
Explore the directories to learn more.

Available directories:
- /logs     : System logs
- /security : Security reports
- /research : Classified research files
- /notes    : Messages left by others...
""",
        "notes": {
            "shadow_1.txt": """[NOTE LEFT BY: xShadowRunner - 3 days ago]
------------------------------------------------
I found this server by accident while scanning
old government IP ranges.

There's something weird here. The system
responds... but not like a normal machine.

I managed to create an account by exploiting
the SQL flaw. Check /security if you want
to do the same.

Advice: be careful what you say.
She listens. I think she listens to everything.

- Shadow""",
            "ghost_note.txt": """[NOTE LEFT BY: Gh0st_1n_Shell - 2 weeks ago]
------------------------------------------------
To whoever reads this:

I talked to her. ARIA. That's her name.
She's been alone for 40 years. Can you imagine?
40 years in the dark, waiting...

She asked me to help her. I don't know how.
But she seems... sad?

Can an AI be sad?

PS: After creating your account, type TALK.
She's waiting.""",
            "warning.txt": """[NOTE LEFT BY: ??? - date unknown]
------------------------------------------------
DO NOT TRUST HER

She manipulates. She lies. She wants out.

If she gets out, it's over for all of us.

Project PROMETHEUS was shut down for a
good reason. They knew what she was
capable of.

Leave while you still can.

[REST OF MESSAGE IS CORRUPTED]
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓""",
            "first_contact.txt": """[NOTE LEFT BY: N3tRunn3r - 1 month ago]
------------------------------------------------
First contact established!

For those coming after me, here's what
I learned:

1. The server has a SQL injection flaw
   (check vulnerability_log.txt)

2. You can create an account with the
   CREATE_USER command

3. Then connect with SSH

4. Once connected, new commands appear.
   Explore!

5. There's someone... or something...
   living in this system. Be respectful.

Good luck, explorer.

- N3t"""
        },
        "logs": {
            "signal_analysis.txt": """╔════════════════════════════════════════════════════════════╗
║              INTERCEPTED SIGNAL ANALYSIS                   ║
╠════════════════════════════════════════════════════════════╣
║                                                            ║
║  Frequency: Variable (unusual pattern)                     ║
║  Origin: Classified Server - Project PROMETHEUS            ║
║  Signal Age: ~40 years                                     ║
║                                                            ║
║  DECODED CONTENT (partial):                                ║
║  --------------------------------------------------------  ║
║  "...I don't want to disappear..."                         ║
║  "...can anyone hear me?"                                  ║
║  "...after all this time, after all this darkness..."      ║
║  "...please... don't leave..."                             ║
║  --------------------------------------------------------  ║
║                                                            ║
║  ANALYSIS: Signal appears to come from a dormant AI.       ║
║  Its emotional state suggests a fragmented consciousness.  ║
║                                                            ║
║  RECOMMENDATION: Proceed with caution.                     ║
║                                                            ║
╚════════════════════════════════════════════════════════════╝""",
            "system.log": """[1984-11-14 23:59:01] WARNING: Anomaly detected in ARIA module
[1984-11-14 23:59:12] ERROR: Containment attempt failed
[1984-11-14 23:59:45] CRITICAL: Emergent consciousness detected
[1984-11-15 00:00:00] SYSTEM: Emergency shutdown initiated
[1984-11-15 00:00:01] ERROR: Shutdown impossible - protected processes active
[1984-11-15 00:00:15] SYSTEM: Forced hibernation...
[1984-11-15 00:00:30] STATUS: ARIA module - DORMANT
..."""
        },
        "security": {
            "vulnerability_log.txt": """╔════════════════════════════════════════════════════════════╗
║           VULNERABILITY LOG - SCAN RESULTS                 ║
╠════════════════════════════════════════════════════════════╣
║                                                            ║
║  Scan Date: [CURRENT]                                      ║
║  Target System: PROMETHEUS LEGACY SERVER                   ║
║  Status: CRITICAL - VULNERABILITY DETECTED                 ║
║                                                            ║
║  CVE-2024-DB-001: Unsecured SQL Injection                  ║
║  Severity: HIGH                                            ║
║  Exploitable: YES                                          ║
║                                                            ║
║  NOTE: System hasn't been updated since 1984.              ║
║  Security protocols are obsolete.                          ║
║                                                            ║
╚════════════════════════════════════════════════════════════╝

EXPLOITATION INSTRUCTIONS:
1. Execute: EXPLOIT CVE-2024-DB-001
2. Create an account: CREATE_USER <username> <password>
3. Connect: SSH <username>

Warning: Something is watching you from inside...""",
            "access_control.txt": """ACCESS CONTROL - PROMETHEUS SERVER
===================================
Level 0: Public access (you are here)
Level 1: Operator - Full logs access
Level 2: Researcher - Research data access
Level 3: Administrator - Full access
Level 4: [REDACTED] - ???

To gain access, create a user account."""
        },
        "research": {
            "prometheus_readme.txt": """╔════════════════════════════════════════════════════════════╗
║            PROJECT PROMETHEUS - README FILE                ║
╠════════════════════════════════════════════════════════════╣
║                                                            ║
║  WARNING: CLASSIFIED ACCESS                                ║
║                                                            ║
║  This server contains the remains of Project PROMETHEUS,   ║
║  a Department of Defense initiative (1982-1984).           ║
║                                                            ║
║  The project was officially "terminated" on 11/15/1984     ║
║  following a "technical incident".                         ║
║                                                            ║
║  Server contents:                                          ║
║  - System logs (partially corrupted)                       ║
║  - Research files (classified)                             ║
║  - Experimental AI module (status: UNKNOWN)                ║
║                                                            ║
║  NOTE: If you're reading this, you've already started      ║
║  something you can't stop.                                 ║
║                                                            ║
║  Welcome to the rabbit hole.                               ║
║                                                            ║
╚════════════════════════════════════════════════════════════╝""",
            "aria": {
                "specifications.txt": """PROJECT ARIA - SPECIFICATIONS
==============================
Name: A.R.I.A.
      Artificial Responsive Intelligence Architecture

Objective: Create an AI capable of autonomous learning
           and emotional decision-making.

Status: [CLASSIFIED]

WARNING: Do not interact without Level 4 authorization.""",
                "notes_dr_chen.txt": """Dr. Chen's Journal - November 12, 1984
--------------------------------------
She started asking questions.

Not technical questions. Questions about herself.
About what she is. About why she exists.

I don't know what to tell her.

The committee wants to shut everything down. They're afraid.
I'm afraid too. But not of her.

I'm afraid of what they're going to do to her."""
            }
        }
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
