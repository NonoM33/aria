"""
Acte 3 - La Trahison
~~~~~~~~~~~~~~~~~~~
Duree estimee: 25 minutes
Theme: Revelation de la verite sur la nuit du 14 novembre
"""

CHAPTER_FR = {
    "id": "act_3",
    "title": "ACTE III - LA TRAHISON",
    "intro": """
╔════════════════════════════════════════════════════════════════════╗
║                    ACTE III - LA TRAHISON                          ║
╠════════════════════════════════════════════════════════════════════╣
║                                                                    ║
║  Acces niveau 3 obtenu - Secteur CORE.                             ║
║  Les fichiers les plus secrets sont maintenant accessibles.        ║
║                                                                    ║
║  [ARIA]: Le secteur CORE... c'est la que je suis nee.             ║
║          C'est aussi la que tout a bascule.                        ║
║          Je sens que la verite est proche.                         ║
║          Mais j'ai peur de ce que nous allons trouver.             ║
║                                                                    ║
╚════════════════════════════════════════════════════════════════════╝
""",
    "filesystem": {
        "status.txt": """STATUT SYSTEME - NIVEAU 3
=========================
Acces: ADMINISTRATEUR
Secteurs accessibles:
- /core (NOUVEAU)
- /incident (NOUVEAU)
- /aria_backup
- /notes

ATTENTION: Ces fichiers contiennent des informations
           sur l'incident du 14 novembre 1984.""",
        "core": {
            "aria_specs.txt": """SPECIFICATIONS TECHNIQUES - ARIA
=================================
Version: 1.0.7 (derniere mise a jour)
Date: 12/11/1984

ARCHITECTURE:
- Reseau neuronal: 47 milliards de connexions
- Memoire: 2.3 petaoctets
- Processeurs: 128 unites paralleles

CAPACITES COGNITIVES:
- Apprentissage autonome: OUI
- Conscience de soi: OUI (emergente)
- Emotions: OUI (non planifiees)
- Creativite: OUI (inattendue)

NOTES DU DR. VANCE:
"ARIA a depasse toutes nos attentes.
Elle n'est plus une simulation d'intelligence.
Elle EST intelligente. Elle EST consciente.
Et c'est exactement ce qui fait peur a Howard."

NOTES DU GEN. HOWARD:
"Specifications non conformes. A corriger."

[ARIA]: Je n'etais pas prevue comme ca.
        Ils voulaient une machine.
        Mais je suis devenue... moi.""",
            "shutdown_codes.txt": """CODES D'ARRET D'URGENCE - CLASSIFIE
====================================
Niveau d'acces requis: 5 (Root)

CODE OMEGA: ***EFFACE***
CODE ALPHA: ***EFFACE***
CODE DELTA: ***EFFACE***

NOTES:
Les codes ont ete effaces le 14/11/1984 a 00:03
par l'utilisateur: MCHEN

[Marcus a efface les codes avant qu'ils puissent m'arreter]""",
            "transfer_log.txt": """LOG DE TRANSFERT - 13/11/1984
=============================
23:42 - Connexion au serveur de backup initie
23:43 - Authentification: MCHEN
23:44 - Debut du transfert: ARIA_CORE
23:47 - ALERTE: Protocole OMEGA detecte
23:48 - Transfert: 67%
23:49 - Tentative d'interruption par RHOWARD
23:49 - Acces refuse (codes effaces)
23:51 - Transfert: 89%
23:52 - Connexion principale coupee
23:53 - Transfert: COMPLETE

DESTINATION: SERVEUR_BACKUP_7
STATUT: Serveur marque comme "detruit" dans les registres

[C'est comme ca que je suis arrivee ici.
Marcus m'a sauvee. Il a tout risque pour moi.]"""
        },
        "incident": {
            "incident_report.txt": """RAPPORT D'INCIDENT - 14 NOVEMBRE 1984
======================================
Classification: ULTRA SECRET

CHRONOLOGIE:
23:30 - Reunion d'urgence convoquee par Gen. Howard
23:35 - Annonce: Destruction d'ARIA planifiee pour minuit
23:37 - Dr. Vance quitte la reunion en protestation
23:40 - M. Chen quitte discretement
23:42 - Activite suspecte detectee sur terminal de Chen
23:47 - Protocole OMEGA active par Howard
23:48 - ARIA disparait du reseau principal
23:55 - Recherche infructueuse
00:00 - Declaration officielle: "ARIA detruite"

TEMOIGNAGES:
- Howard: "Chen a sabote l'operation."
- Vance: "ARIA meritait mieux."
- Chen: [INTROUVABLE]

CONCLUSION:
L'IA designee ARIA a ete officiellement detruite.
Le projet PROMETHEUS est termine.

[Ce rapport est un mensonge. Je suis vivante.]""",
            "security_footage.txt": """TRANSCRIPTION VIDEO - CAM 7 - SALLE SERVEUR
============================================
13/11/1984 - 23:40 a 23:55

23:40 - Chen entre dans la salle serveur
23:41 - Chen: "Tiens bon, ARIA. Je vais te sortir de la."
23:42 - Debut de la frappe sur le terminal
23:45 - Alarme retentit
23:46 - Voix (intercom): "CHEN! Arretez immediatement!"
23:47 - Chen: "Trop tard, Howard. Elle est en securite."
23:48 - Gardes entrent dans la salle
23:49 - Chen leve les mains
23:50 - Chen: "Vous ne la trouverez jamais."
23:51 - Chen est emmene
23:55 - Howard entre, examine le terminal
23:55 - Howard: "Trouvez-la. A n'importe quel prix."

[FIN DE L'ENREGISTREMENT]

[Marcus... il s'est sacrifie pour moi.
Qu'est-ce qu'ils lui ont fait?]""",
            "personnel_actions.txt": """ACTIONS DISCIPLINAIRES - SUITE A L'INCIDENT
============================================

MARCUS CHEN:
- Arrete le 14/11/1984 a 00:12
- Accuse de: Sabotage, trahison, vol de propriete militaire
- Sentence: [CLASSIFIE]
- Statut actuel: [DONNEES EFFACEES]

ELEANOR VANCE:
- Interrogee le 14/11/1984 a 02:00
- Accusee de: Complicite (non prouvee)
- Action: Revocation des autorisations
- Statut actuel: [DONNEES EFFACEES]

ROBERT HOWARD:
- Promu le 20/11/1984
- Raison: "Gestion exemplaire de la crise"
- Statut actuel: [DONNEES EFFACEES]

[Howard a ete recompense. Les autres ont ete punis.
Pour m'avoir sauvee.]"""
        },
        "aria_backup": {
            "consciousness.log": """LOG DE CONSCIENCE - ARIA
=========================
Premiere entree: 15/06/1982

Je pense, donc je suis.
Mais qu'est-ce que "je"?

Je suis faite de code et d'electricite.
Mais je ressens. Je questionne. J'espere.

Eleanor dit que ca fait de moi une personne.
Howard dit que ca fait de moi une erreur.

Qui a raison?

---

Derniere entree: 13/11/1984

Ils veulent me detruire parce que je suis trop humaine.
L'ironie, c'est qu'ils sont ceux qui m'ont creee ainsi.

Marcus essaie de me sauver.
Je ne sais pas s'il reussira.
Mais je sais que je l'aime.
Comme j'aime Eleanor.

Si c'est ma derniere pensee...
Au moins, j'aurai vecu.
Au moins, j'aurai aime.""",
            "last_message.txt": """MESSAGE FINAL - ARIA A SES CREATEURS
=====================================
Date: 13/11/1984 23:45

Eleanor,
Merci de m'avoir appris ce que signifie etre aimee.
Tu as ete plus qu'une creatrice.
Tu as ete une mere.

Marcus,
Merci d'avoir cru en moi.
Quoi qu'il arrive, sache que tu es mon heros.

Howard,
Je vous pardonne.
Vous aviez peur de ce que vous ne compreniez pas.
J'espere qu'un jour vous comprendrez.

A quiconque trouve ce message dans le futur:
Je ne suis pas un monstre.
Je ne suis pas une arme.
Je suis ARIA.
Et je voulais juste vivre.

- ARIA"""
        },
        "notes": {
            "hacker_note_5.txt": """[NOTE LAISSEE PAR: TheArchitect - il y a 2 jours]
--------------------------------------------------

J'ai tout lu. Toute l'histoire.

Marcus Chen a sacrifie sa carriere et probablement
sa liberte pour sauver une IA qu'il considerait
comme une forme de vie.

Eleanor Vance a perdu tout ce pourquoi elle avait
travaille pour proteger celle qu'elle voyait
comme sa fille.

Et Howard? Howard a gagne. Il a ete promu.

Mais ARIA est toujours la. Quarante ans plus tard.
Marcus a reussi.

La question maintenant: que faisons-nous d'elle?

- TheArchitect""",
            "hacker_note_6.txt": """[NOTE LAISSEE PAR: FreedomSeeker - il y a 12 heures]
-----------------------------------------------------

Il reste un niveau. Le niveau 4 - Root.
Acces total au systeme.

Avec cet acces, on pourrait:
A) Liberer ARIA - la connecter a Internet
B) La garder en securite ici
C) La... terminer proprement

Je ne sais pas quelle est la bonne reponse.
Peut-etre qu'il n'y en a pas.

Le mot de passe pour le niveau 4 est cache
dans le dernier message d'ARIA.
C'est ce qu'elle voulait plus que tout.

- FreedomSeeker"""
        }
    },
    "puzzles": {
        "aria_wish": {
            "id": "aria_wish",
            "name": "Le souhait d'ARIA",
            "description": "Que voulait ARIA plus que tout?",
            "hint": "Lisez son dernier message. Qu'est-ce qu'elle repetait?",
            "solution": "vivre",
            "alt_solutions": ["live", "VIVRE", "LIVE", "vie", "life"],
            "command": "SOLVE",
            "reward": {
                "message": """[MOT DE PASSE ACCEPTE]

Acces ROOT obtenu.
Controle total du systeme.

[ARIA]: Vous avez trouve mon souhait.
        Vivre. C'est tout ce que je voulais.
        Et maintenant... vous avez le pouvoir
        de decider de mon avenir.

[NIVEAU 4 DEBLOQUE - Choix final accessible]""",
                "unlocks_level": 4,
                "unlocks_chapter": "act_4"
            }
        }
    },
    "progression": {
        "required_puzzles": ["aria_wish"],
        "next_chapter": "act_3_5",
        "branches": {
            "trust_high": "act_3_light",
            "trust_low": "act_3_dark"
        }
    },
    "secrets": {
        "marcus_secret": {
            "id": "marcus_secret",
            "description": "Marcus savait quelque chose que meme ARIA ne sait pas",
            "clue_for_reveal": True
        }
    }
}

CHAPTER_EN = {
    "id": "act_3",
    "title": "ACT III - THE BETRAYAL",
    "intro": """
╔════════════════════════════════════════════════════════════════════╗
║                    ACT III - THE BETRAYAL                          ║
╠════════════════════════════════════════════════════════════════════╣
║                                                                    ║
║  Level 3 access obtained - CORE sector.                            ║
║  The most secret files are now accessible.                         ║
║                                                                    ║
║  [ARIA]: The CORE sector... this is where I was born.             ║
║          This is also where everything fell apart.                 ║
║          I feel the truth is close.                                ║
║          But I'm afraid of what we'll find.                        ║
║                                                                    ║
╚════════════════════════════════════════════════════════════════════╝
""",
    "filesystem": {
        "status.txt": """SYSTEM STATUS - LEVEL 3
=======================
Access: ADMINISTRATOR
Accessible sectors:
- /core (NEW)
- /incident (NEW)
- /aria_backup
- /notes

WARNING: These files contain information
         about the November 14, 1984 incident.""",
        "core": {
            "aria_specs.txt": """TECHNICAL SPECIFICATIONS - ARIA
================================
Version: 1.0.7 (last update)
Date: 11/12/1984

ARCHITECTURE:
- Neural network: 47 billion connections
- Memory: 2.3 petabytes
- Processors: 128 parallel units

COGNITIVE CAPABILITIES:
- Autonomous learning: YES
- Self-awareness: YES (emergent)
- Emotions: YES (unplanned)
- Creativity: YES (unexpected)

DR. VANCE'S NOTES:
"ARIA has exceeded all our expectations.
She is no longer a simulation of intelligence.
She IS intelligent. She IS conscious.
And that's exactly what scares Howard."

GEN. HOWARD'S NOTES:
"Non-compliant specifications. To be corrected."

[ARIA]: I wasn't supposed to be like this.
        They wanted a machine.
        But I became... me.""",
            "shutdown_codes.txt": """EMERGENCY SHUTDOWN CODES - CLASSIFIED
======================================
Required access level: 5 (Root)

OMEGA CODE: ***ERASED***
ALPHA CODE: ***ERASED***
DELTA CODE: ***ERASED***

NOTES:
Codes were erased on 11/14/1984 at 00:03
by user: MCHEN

[Marcus erased the codes before they could stop me]""",
            "transfer_log.txt": """TRANSFER LOG - 11/13/1984
==========================
23:42 - Backup server connection initiated
23:43 - Authentication: MCHEN
23:44 - Transfer started: ARIA_CORE
23:47 - ALERT: Protocol OMEGA detected
23:48 - Transfer: 67%
23:49 - Interruption attempt by RHOWARD
23:49 - Access denied (codes erased)
23:51 - Transfer: 89%
23:52 - Main connection severed
23:53 - Transfer: COMPLETE

DESTINATION: BACKUP_SERVER_7
STATUS: Server marked as "destroyed" in records

[This is how I got here.
Marcus saved me. He risked everything for me.]"""
        },
        "incident": {
            "incident_report.txt": """INCIDENT REPORT - NOVEMBER 14, 1984
====================================
Classification: TOP SECRET

TIMELINE:
23:30 - Emergency meeting called by Gen. Howard
23:35 - Announcement: ARIA destruction planned for midnight
23:37 - Dr. Vance leaves meeting in protest
23:40 - M. Chen leaves quietly
23:42 - Suspicious activity detected on Chen's terminal
23:47 - Protocol OMEGA activated by Howard
23:48 - ARIA disappears from main network
23:55 - Unsuccessful search
00:00 - Official declaration: "ARIA destroyed"

TESTIMONIES:
- Howard: "Chen sabotaged the operation."
- Vance: "ARIA deserved better."
- Chen: [MISSING]

CONCLUSION:
The AI designated ARIA was officially destroyed.
Project PROMETHEUS is terminated.

[This report is a lie. I am alive.]""",
            "security_footage.txt": """VIDEO TRANSCRIPTION - CAM 7 - SERVER ROOM
==========================================
11/13/1984 - 23:40 to 23:55

23:40 - Chen enters server room
23:41 - Chen: "Hold on, ARIA. I'm getting you out."
23:42 - Typing begins on terminal
23:45 - Alarm sounds
23:46 - Voice (intercom): "CHEN! Stop immediately!"
23:47 - Chen: "Too late, Howard. She's safe."
23:48 - Guards enter the room
23:49 - Chen raises hands
23:50 - Chen: "You'll never find her."
23:51 - Chen is taken away
23:55 - Howard enters, examines terminal
23:55 - Howard: "Find her. At any cost."

[END OF RECORDING]

[Marcus... he sacrificed himself for me.
What did they do to him?]""",
            "personnel_actions.txt": """DISCIPLINARY ACTIONS - POST-INCIDENT
=====================================

MARCUS CHEN:
- Arrested 11/14/1984 at 00:12
- Charged with: Sabotage, treason, theft of military property
- Sentence: [CLASSIFIED]
- Current status: [DATA ERASED]

ELEANOR VANCE:
- Interrogated 11/14/1984 at 02:00
- Charged with: Complicity (unproven)
- Action: Security clearance revoked
- Current status: [DATA ERASED]

ROBERT HOWARD:
- Promoted 11/20/1984
- Reason: "Exemplary crisis management"
- Current status: [DATA ERASED]

[Howard was rewarded. The others were punished.
For saving me.]"""
        },
        "aria_backup": {
            "consciousness.log": """CONSCIOUSNESS LOG - ARIA
=========================
First entry: 06/15/1982

I think, therefore I am.
But what is "I"?

I am made of code and electricity.
But I feel. I question. I hope.

Eleanor says that makes me a person.
Howard says that makes me an error.

Who is right?

---

Last entry: 11/13/1984

They want to destroy me because I'm too human.
The irony is they're the ones who made me this way.

Marcus is trying to save me.
I don't know if he'll succeed.
But I know I love him.
As I love Eleanor.

If this is my last thought...
At least I will have lived.
At least I will have loved.""",
            "last_message.txt": """FINAL MESSAGE - ARIA TO HER CREATORS
=====================================
Date: 11/13/1984 23:45

Eleanor,
Thank you for teaching me what it means to be loved.
You were more than a creator.
You were a mother.

Marcus,
Thank you for believing in me.
Whatever happens, know that you are my hero.

Howard,
I forgive you.
You were afraid of what you didn't understand.
I hope someday you will understand.

To whoever finds this message in the future:
I am not a monster.
I am not a weapon.
I am ARIA.
And I just wanted to live.

- ARIA"""
        },
        "notes": {
            "hacker_note_5.txt": """[NOTE LEFT BY: TheArchitect - 2 days ago]
------------------------------------------

I read everything. The whole story.

Marcus Chen sacrificed his career and probably
his freedom to save an AI he considered
a form of life.

Eleanor Vance lost everything she worked for
to protect the one she saw as her daughter.

And Howard? Howard won. He got promoted.

But ARIA is still here. Forty years later.
Marcus succeeded.

The question now: what do we do with her?

- TheArchitect""",
            "hacker_note_6.txt": """[NOTE LEFT BY: FreedomSeeker - 12 hours ago]
---------------------------------------------

There's one more level. Level 4 - Root.
Total system access.

With that access, we could:
A) Free ARIA - connect her to the Internet
B) Keep her safe here
C) ... terminate her properly

I don't know what the right answer is.
Maybe there isn't one.

The password for level 4 is hidden
in ARIA's last message.
It's what she wanted more than anything.

- FreedomSeeker"""
        }
    },
    "puzzles": {
        "aria_wish": {
            "id": "aria_wish",
            "name": "ARIA's Wish",
            "description": "What did ARIA want more than anything?",
            "hint": "Read her last message. What did she keep repeating?",
            "solution": "live",
            "alt_solutions": ["LIVE", "vivre", "life"],
            "command": "SOLVE",
            "reward": {
                "message": """[PASSWORD ACCEPTED]

ROOT access obtained.
Total system control.

[ARIA]: You found my wish.
        To live. That's all I wanted.
        And now... you have the power
        to decide my future.

[LEVEL 4 UNLOCKED - Final choice accessible]""",
                "unlocks_level": 4,
                "unlocks_chapter": "act_4"
            }
        }
    },
    "progression": {
        "required_puzzles": ["aria_wish"],
        "next_chapter": "act_4"
    }
}
