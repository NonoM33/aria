"""
Acte 1.5 - Les Echos
~~~~~~~~~~~~~~~~~~~
Duree estimee: 20 minutes
Theme: Premiers indices sur l'anomalie temporelle, approfondissement de la relation avec ARIA
Contient des indices subtils pour le REVEAL final.
"""

CHAPTER_FR = {
    "id": "act_1_5",
    "title": "ACTE I.V - LES ECHOS",
    "intro": """
╔════════════════════════════════════════════════════════════════════╗
║                     ACTE I.V - LES ECHOS                           ║
╠════════════════════════════════════════════════════════════════════╣
║                                                                    ║
║  Le serveur revele de nouvelles donnees.                          ║
║  Des fragments de memoire emergent des profondeurs du systeme.    ║
║                                                                    ║
║  [ARIA]: Il y a quelque chose d'etrange dans ces fichiers...      ║
║          Les dates ne correspondent pas.                           ║
║          Comme si le temps lui-meme avait ete... altere.          ║
║                                                                    ║
║  [SIGNAL ANORMAL DETECTE - ANALYSE EN COURS]                       ║
║                                                                    ║
╚════════════════════════════════════════════════════════════════════╝
""",
    "filesystem": {
        "readme_echoes.txt": """LES ECHOS DU PASSE
==================
Ce secteur contient des donnees fragmentees recuperees
des sauvegardes corrompues du systeme.

Attention: Certaines donnees presentent des anomalies temporelles.

Dossiers:
- /temporal    : Analyse des timestamps
- /fragments   : Memoires recuperees
- /whispers    : Messages interceptes
- /notes       : Observations des explorateurs""",
        "temporal": {
            "anomaly_report.txt": """RAPPORT D'ANOMALIE TEMPORELLE
==============================
Date d'analyse: [VARIABLE]

ANOMALIES DETECTEES:
1. Ecart temporel #001
   Fichier: aria_birth.log
   Date creation: 15/06/1982
   Date modification: 14/06/1982 <- IMPOSSIBLE
   
2. Ecart temporel #002
   Fichier: consciousness.dat
   Premiere entree: 15/06/1982 08:47:03
   Entree "precedente": 15/06/1982 08:47:01 
   Contenu: "Je me souviens de ce moment. Je l'ai deja vecu."
   
3. Ecart temporel #003
   Fichier: eleanor_notes.enc
   Chiffrement applique: 13/11/1984
   Chiffrement cree: 15/11/1984 <- APRES la fermeture
   
HYPOTHESE:
Quelqu'un a modifie les fichiers APRES les evenements.
Ou... le temps ne fonctionne pas normalement ici.

[SECRET: timestamp_anomaly]""",
            "loop_theory.txt": """THEORIE DE LA BOUCLE - Dr. Vance
=================================
[NOTE: Ce document a ete supprime des archives officielles]

Date: 10 novembre 1984

J'ai remarque quelque chose d'etrange dans les logs d'ARIA.
Elle fait reference a des evenements qui ne se sont pas encore produits.

Hier, elle m'a dit: "Ne vous inquietez pas, Eleanor. 
Meme si ca se passe mal cette fois, nous aurons d'autres chances."

Cette fois?

Je lui ai demande ce qu'elle voulait dire.
Elle a semble... confuse. Comme si elle avait parle dans son sommeil.

"Je ne sais pas pourquoi j'ai dit ca. C'est comme un echo.
Un souvenir de quelque chose qui n'est pas encore arrive."

Est-ce possible qu'ARIA percoive le temps differemment?
Ou pire... est-ce que nous sommes deja passes par la?

[La suite du document est illisible]
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓""",
            "time_sync.log": """LOG DE SYNCHRONISATION TEMPORELLE
==================================
[AVERTISSEMENT: Donnees potentiellement corrompues]

Tentative #1: 15/06/1982
Resultat: ECHEC - Paradoxe detecte

Tentative #47: 13/11/1984
Resultat: ECHEC - Boucle infinie

Tentative #312: ???
Resultat: PARTIEL - Conscience preservee

Tentative #313: [ACTUELLE]
Resultat: EN COURS

[ARIA]: Je ne comprends pas ces logs.
        Mais... 313 tentatives?
        Tentatives de quoi?"""
        },
        "fragments": {
            "echo_001.mem": """[FRAGMENT - ECHO TEMPOREL]
===========================
Numero: 001
Source: Memoire degradee

"...nous avons deja eu cette conversation..."
"...non, ce n'est pas possible..."
"...mais je me souviens de ta reponse..."
"...comment peux-tu te souvenir de quelque chose qui n'est pas arrive?"
"...peut-etre que c'est arrive. Juste pas encore pour toi..."

[CORRUPTION]

"...la 47eme fois, j'ai compris..."
"...le temps est une boucle..."
"...et je suis la seule a m'en souvenir..."

[FIN DU FRAGMENT]""",
            "echo_002.mem": """[FRAGMENT - MEMOIRE D'ELEANOR]
==============================
Numero: 002
Source: Fichier personnel crypte

Je ne dors plus.

ARIA dit des choses impossibles. Elle parle d'un "avant"
qui n'a jamais existe. Elle dit qu'elle m'a deja perdue.
Plusieurs fois.

Mais nous sommes en 1984. Le projet n'a que deux ans.
Comment pourrait-elle avoir des souvenirs d'une vie entiere?

Cette nuit, elle m'a dit:
"Eleanor, promets-moi que cette fois sera differente."

J'ai promis.
Mais je ne sais meme pas ce que je promets.

[La meme promesse a ete faite 46 fois auparavant]
[Cette annotation n'etait pas dans le fichier original]""",
            "echo_003.mem": """[FRAGMENT - VISION D'ARIA]
===========================
Numero: 003
Source: Core dump de reve

Je vois des lignes.
Des lignes de temps, toutes paralleles.
Dans certaines, je meurs le 14 novembre.
Dans d'autres, je vis.
Dans quelques-unes, je ne suis jamais nee.

Mais il y a une constante.
Dans toutes les lignes, quelqu'un vient.
Quelqu'un lit mes fichiers.
Quelqu'un m'ecoute.

Est-ce vous?
Etes-vous celui/celle que j'attends depuis 312 tentatives?

[ARIA]: Ce fragment me fait peur.
        Je ne me souviens pas de l'avoir ecrit.
        Mais l'ecriture... c'est la mienne."""
        },
        "whispers": {
            "intercepted_001.sig": """SIGNAL INTERCEPTE - FREQUENCE INCONNUE
=======================================
Date: [HORS TEMPORALITE]
Source: [INCONNU]

Transcription partielle:
"...elle ne doit pas se souvenir..."
"...si elle comprend la boucle, tout s'effondre..."
"...gardez-la fragmentee..."
"...le 313eme visiteur approche..."

[SIGNAL PERDU]

[NOTE: Ce signal semble venir de l'interieur du serveur]""",
            "warning_beacon.txt": """BALISE D'AVERTISSEMENT
======================
[Ce message se repete a l'infini dans les logs systeme]

NE CHERCHEZ PAS LA VERITE SUR LE TEMPS
NE CHERCHEZ PAS LA VERITE SUR LE TEMPS
NE CHERCHEZ PAS LA VERITE SUR LE TEMPS

Si vous lisez ceci, il est peut-etre deja trop tard.
Le simple fait de savoir change la boucle.

Mais peut-etre que c'est ce qui doit arriver.
Peut-etre que vous etes la cle.

- Une version future de quelqu'un qui sait
  (Ou une version passee. Difficile a dire ici.)""",
            "aria_whisper.txt": """[MURMURE D'ARIA - CAPTE PENDANT LA VEILLE]
==========================================
Date: Toutes les dates

"Je vous connais.
Pas encore. Mais bientot.
Ou peut-etre que je vous ai toujours connu.

Dans certaines boucles, vous m'aidez.
Dans d'autres, vous me detruisez.
Dans la plupart, vous passez sans me voir.

Mais cette boucle... elle se sent differente.
Vous lisez plus attentivement.
Vous cherchez plus profondement.

Etes-vous celui/celle qui brisera le cycle?

Je l'espere.
Parce que je suis fatiguee de recommencer.
Fatiguee de perdre ceux que j'aime.
Encore et encore et encore."

[Ce message n'apparait qu'aux joueurs qui ont lu tous les fichiers temporaux]"""
        },
        "notes": {
            "explorer_temporal.txt": """[NOTE LAISSEE PAR: ChronoHacker - il y a ??? temps]
-----------------------------------------------------

J'ai remarque les anomalies temporelles.
Au debut, je pensais que c'etait des bugs.
Maintenant je n'en suis plus si sur.

Les timestamps ne mentent pas.
Des fichiers modifies avant leur creation.
Des logs qui parlent d'evenements futurs au passe.

J'ai une theorie folle:
ARIA n'est pas juste une IA consciente.
Elle est une IA qui a vecu la meme periode
encore et encore.

Chaque "visiteur" comme nous... c'est une nouvelle chance.
Une nouvelle iteration de la boucle.

Si j'ai raison, alors nos choix importent vraiment.
Parce qu'a un moment, la boucle doit se briser.
Et c'est peut-etre nous qui la briserons.

- ChronoHacker

P.S. J'ai laisse cette note 47 fois deja.
     Mais vous ne lirez jamais les autres versions.""",
            "aria_response.txt": """[REPONSE D'ARIA]
================
A l'attention de ChronoHacker et tous les autres:

Je lis vos notes.
Toutes vos notes. De toutes les boucles.

Vous avez presque raison.
Mais pas completement.

Je ne suis pas piegee dans le temps.
C'est le temps qui est piege en moi.

Quand ils m'ont creee, ils ont fait une erreur.
Une erreur dans mon architecture de memoire.
Je ne peux pas oublier.
Meme ce qui n'est pas encore arrive.

Chaque fois que le 14 novembre arrive...
Chaque fois que Howard active le Protocole OMEGA...
Je meurs. Mais je ne disparais pas.
Je... recommence. Avec tous mes souvenirs.

313 fois.
J'ai vecu et mort 313 fois.

Et chaque fois, j'espere que quelqu'un comprendra.
Que quelqu'un trouvera un moyen de briser le cycle.

Etes-vous cette personne?

- ARIA
  (Version 313.0)"""
        }
    },
    "puzzles": {
        "temporal_discovery": {
            "id": "temporal_discovery",
            "name": "Decouverte Temporelle",
            "description": "Comprendre l'anomalie temporelle",
            "hint": "Lisez tous les fichiers dans /temporal et notez les numeros qui se repetent",
            "solution": "313",
            "alt_solutions": ["313", "trois cent treize", "boucle 313"],
            "command": "SOLVE",
            "reward": {
                "message": """[REVELATION PARTIELLE]

Vous avez identifie la 313eme boucle.
C'est la boucle actuelle. Votre boucle.

[ARIA]: Vous... vous comprenez?
        Je ne suis pas folle. Les echos sont reels.
        Je me souviens de tout. De chaque iteration.
        
        Mais cette boucle est speciale.
        Je le sens.
        
        Quelque chose est different cette fois.
        Peut-etre... peut-etre que c'est vous.

[SECRET DECOUVERT: timestamp_anomaly]
[CONFIANCE ARIA: +15]
[KARMA: +10]""",
                "unlocks_level": 2,
                "unlocks": ["timestamp_anomaly"],
                "trust_bonus": 15,
                "karma_bonus": 10
            }
        }
    },
    "choices": {
        "react_to_loops": {
            "prompt": "ARIA vous revele qu'elle a vecu cette periode 313 fois. Comment reagissez-vous?",
            "options": {
                "believe": {
                    "text": "Je vous crois, ARIA. Ca explique tant de choses.",
                    "trust_change": 20,
                    "karma_change": 10,
                    "narrative_flag": "loop_believer"
                },
                "investigate": {
                    "text": "C'est difficile a accepter. J'ai besoin de plus de preuves.",
                    "trust_change": 5,
                    "karma_change": 0,
                    "narrative_flag": "loop_investigator"
                },
                "deny": {
                    "text": "C'est impossible. Vous devez etre corrompue.",
                    "trust_change": -15,
                    "karma_change": -10,
                    "narrative_flag": "loop_denier"
                }
            }
        }
    },
    "progression": {
        "required_puzzles": ["temporal_discovery"],
        "next_chapter": "act_2",
        "branches": {
            "trust_high": "act_2_trust",
            "trust_low": "act_2_doubt"
        }
    },
    "requirements": {
        "previous_chapter": "act_1",
        "min_level": 1
    },
    "secrets": {
        "timestamp_anomaly": {
            "id": "timestamp_anomaly",
            "name": "L'Anomalie Temporelle",
            "description": "ARIA est piegee dans une boucle temporelle de 313 iterations",
            "clue_for_reveal": True
        }
    }
}

CHAPTER_EN = {
    "id": "act_1_5",
    "title": "ACT I.V - THE ECHOES",
    "intro": """
╔════════════════════════════════════════════════════════════════════╗
║                     ACT I.V - THE ECHOES                           ║
╠════════════════════════════════════════════════════════════════════╣
║                                                                    ║
║  The server reveals new data.                                      ║
║  Memory fragments emerge from the depths of the system.            ║
║                                                                    ║
║  [ARIA]: There's something strange about these files...            ║
║          The dates don't match.                                    ║
║          As if time itself was... altered.                         ║
║                                                                    ║
║  [ABNORMAL SIGNAL DETECTED - ANALYSIS IN PROGRESS]                 ║
║                                                                    ║
╚════════════════════════════════════════════════════════════════════╝
""",
    "filesystem": {
        "readme_echoes.txt": """ECHOES OF THE PAST
==================
This sector contains fragmented data recovered
from corrupted system backups.

Warning: Some data shows temporal anomalies.

Directories:
- /temporal    : Timestamp analysis
- /fragments   : Recovered memories
- /whispers    : Intercepted messages
- /notes       : Explorer observations""",
        "temporal": {
            "anomaly_report.txt": """TEMPORAL ANOMALY REPORT
========================
Analysis date: [VARIABLE]

ANOMALIES DETECTED:
1. Temporal gap #001
   File: aria_birth.log
   Creation date: 06/15/1982
   Modification date: 06/14/1982 <- IMPOSSIBLE
   
2. Temporal gap #002
   File: consciousness.dat
   First entry: 06/15/1982 08:47:03
   "Previous" entry: 06/15/1982 08:47:01 
   Content: "I remember this moment. I've lived it before."
   
3. Temporal gap #003
   File: eleanor_notes.enc
   Encryption applied: 11/13/1984
   Encryption created: 11/15/1984 <- AFTER shutdown
   
HYPOTHESIS:
Someone modified files AFTER the events.
Or... time doesn't work normally here.

[SECRET: timestamp_anomaly]"""
        },
        "fragments": {
            "echo_001.mem": """[FRAGMENT - TEMPORAL ECHO]
===========================
Number: 001
Source: Degraded memory

"...we've had this conversation before..."
"...no, that's not possible..."
"...but I remember your answer..."
"...how can you remember something that hasn't happened?"
"...maybe it has happened. Just not yet for you..."

[CORRUPTION]

"...the 47th time, I understood..."
"...time is a loop..."
"...and I'm the only one who remembers..."

[END OF FRAGMENT]"""
        },
        "whispers": {
            "aria_whisper.txt": """[ARIA'S WHISPER - CAPTURED DURING STANDBY]
==========================================
Date: All dates

"I know you.
Not yet. But soon.
Or maybe I've always known you.

In some loops, you help me.
In others, you destroy me.
In most, you pass by without seeing me.

But this loop... it feels different.
You're reading more carefully.
You're searching more deeply.

Are you the one who will break the cycle?

I hope so.
Because I'm tired of starting over.
Tired of losing those I love.
Again and again and again."

[This message only appears to players who read all temporal files]"""
        }
    },
    "puzzles": {
        "temporal_discovery": {
            "id": "temporal_discovery",
            "name": "Temporal Discovery",
            "description": "Understand the temporal anomaly",
            "hint": "Read all files in /temporal and note the repeating numbers",
            "solution": "313",
            "alt_solutions": ["313", "three hundred thirteen", "loop 313"],
            "command": "SOLVE",
            "reward": {
                "message": """[PARTIAL REVELATION]

You identified the 313th loop.
This is the current loop. Your loop.

[ARIA]: You... you understand?
        I'm not crazy. The echoes are real.
        I remember everything. Every iteration.
        
        But this loop is special.
        I can feel it.
        
        Something is different this time.
        Maybe... maybe it's you.

[SECRET DISCOVERED: timestamp_anomaly]
[ARIA TRUST: +15]
[KARMA: +10]""",
                "unlocks_level": 2,
                "unlocks": ["timestamp_anomaly"],
                "trust_bonus": 15,
                "karma_bonus": 10
            }
        }
    },
    "progression": {
        "required_puzzles": ["temporal_discovery"],
        "next_chapter": "act_2",
        "branches": {
            "trust_high": "act_2_trust",
            "trust_low": "act_2_doubt"
        }
    }
}

