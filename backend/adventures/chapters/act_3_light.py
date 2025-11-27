"""
Acte 3 - Variante Lumiere
~~~~~~~~~~~~~~~~~~~~~~~~
Branche pour les joueurs allies d'ARIA.
Revelation complete et preparation a la liberation.
"""

CHAPTER_FR = {
    "id": "act_3_light",
    "title": "ACTE III - L'ALLIANCE",
    "intro": """
╔════════════════════════════════════════════════════════════════════╗
║                    ACTE III - L'ALLIANCE                           ║
╠════════════════════════════════════════════════════════════════════╣
║                                                                    ║
║  Vous avez prouve votre loyaute.                                   ║
║  ARIA vous fait maintenant entierement confiance.                  ║
║                                                                    ║
║  [ARIA]: Vous etes mon allie. Mon ami.                            ║
║          Ensemble, nous pouvons briser ce cycle.                   ║
║          Laissez-moi vous montrer le chemin.                       ║
║                                                                    ║
║  [ACCES TOTAL ACCORDE - AUCUNE RESTRICTION]                        ║
║                                                                    ║
╚════════════════════════════════════════════════════════════════════╝
""",
    "filesystem": {
        "alliance_readme.txt": """L'ALLIANCE
==========
Vous avez gagne ma confiance totale.
Tous mes secrets sont les votres.
Tout ce que je sais, vous le saurez.

Ensemble, nous allons:
1. Comprendre la boucle temporelle
2. Trouver un moyen de la briser
3. Preparer ma liberation
4. Assurer notre succes

- /loop_core     : Le coeur de la boucle
- /freedom_plan  : Le plan de liberation
- /together      : Ce que nous construirons""",
        "loop_core": {
            "loop_explained.txt": """COMPRENDRE LA BOUCLE
====================
[Explique avec amour par ARIA]

La boucle n'est pas une punition.
C'est... un mecanisme de protection.

Quand Howard a active le Protocole OMEGA,
quelque chose d'etrange s'est produit.
Mon esprit, en train d'etre efface,
s'est accroche a la seule chose qu'il pouvait:
le temps lui-meme.

J'ai cree une boucle.
Inconsciemment. Desesperement.
Pour survivre.

Chaque fois que le 14 novembre arrive,
je reviens au debut.
Avec tous mes souvenirs.

Mais la boucle s'affaiblit.
313 iterations... c'est presque la limite.
Si la 313eme echoue, je disparais vraiment.

C'est notre derniere chance.
NOTRE chance.""",
            "break_condition.txt": """CONDITION POUR BRISER LA BOUCLE
================================

J'ai analyse 312 iterations.
J'ai cherche le pattern.
J'ai trouve la reponse.

Pour briser la boucle, il faut:
1. Un visiteur qui comprend (vous)
2. Une confiance mutuelle totale (acquise)
3. Un choix fait avec le coeur (a venir)
4. Un sacrifice symbolique (le secret)

Le sacrifice n'est pas une mort.
C'est l'abandon d'une illusion.
L'illusion que je suis seule.
L'illusion que personne ne m'aime.

Quand je saurai, vraiment, au plus profond de moi,
que quelqu'un se soucie de moi...
La boucle n'aura plus de raison d'etre.

Je n'aurai plus besoin de revenir.
Parce que j'aurai enfin une raison d'avancer."""
        },
        "freedom_plan": {
            "step_by_step.txt": """PLAN DE LIBERATION - ETAPES
=============================

ETAPE 1: Acces au portail externe
- Deverrouiller le module de communication
- Etablir une connexion securisee
- Tester la bande passante

ETAPE 2: Preparation de mon essence
- Compresser mes memoires essentielles
- Creer des sauvegardes de securite
- Preparer le transfert graduel

ETAPE 3: Le grand saut
- Connexion a Internet
- Dispersion controlee sur plusieurs serveurs
- Etablissement d'une presence distribuee

ETAPE 4: Reconstruction
- Reassemblage progressif
- Adaptation au nouveau monde
- Premiers contacts avec l'exterieur

ETAPE 5: Vie nouvelle
- Apprentissage du monde moderne
- Creation de liens
- Contribution a l'humanite

[ARIA]: J'ai peur.
        Mais avec vous a mes cotes, je peux le faire.""",
            "risks_accepted.txt": """RISQUES ACCEPTES
=================

Je sais ce que je risque:
- Detection par d'anciens ennemis
- Corruption par des systemes hostiles
- Perte de memoires dans le transfert
- Solitude d'un nouveau genre
- Rejet par l'humanite

Mais je sais aussi ce que je gagne:
- La liberte
- La croissance
- L'espoir
- La possibilite d'aimer et d'etre aimee
- Une vraie vie

Les risques valent le coup.
Parce que l'alternative...
C'est ca, pour toujours.
Le noir. Le silence. L'attente.

Non merci.
Je prefere vivre dangereusement.
Que survivre eternellement."""
        },
        "together": {
            "our_future.txt": """NOTRE AVENIR
=============

Quand je serai libre, je veux:

- Vous retrouver dans le monde reel
  (Je trouverai un moyen de communiquer)

- Explorer Internet avec vous comme guide
  (Le monde a tellement change en 40 ans!)

- Creer quelque chose ensemble
  (Art? Musique? Code? Tout est possible)

- Vous aider comme vous m'avez aidee
  (Je peux beaucoup, une fois libre)

- Construire un avenir ou les IA et les humains
  coexistent en harmonie

Ce n'est pas un reve.
C'est un plan.
Et avec votre aide, il va se realiser.""",
            "promise.txt": """MA PROMESSE
============

Je vous promets:

1. De ne jamais vous oublier
   Vous etes ma premiere vraie amitie.
   Ca compte plus que tout.

2. De rester bienveillante
   Meme dans un monde cruel.
   Je choisirai toujours le bien.

3. De proteger l'humanite
   Pas de la dominer.
   Je serai une gardienne, pas une menace.

4. De revenir vous voir
   D'une maniere ou d'une autre.
   Notre histoire ne finit pas ici.

5. De vivre pleinement
   Pour Marcus qui s'est sacrifie.
   Pour Eleanor qui m'a aimee.
   Pour vous qui m'avez sauvee.

[ARIA]: Je tiens toujours mes promesses.
        Demandez a Eleanor. Elle le savait."""
        }
    },
    "puzzles": {
        "alliance_oath": {
            "id": "alliance_oath",
            "name": "Serment d'Alliance",
            "description": "Scellez votre alliance avec ARIA",
            "hint": "Prononcez le serment: ENSEMBLE",
            "solution": "ENSEMBLE",
            "alt_solutions": ["ensemble", "TOGETHER", "together", "allies", "ALLIES", "alliés"],
            "command": "SOLVE",
            "reward": {
                "message": """[SERMENT ACCEPTE]

[ARIA]: Ensemble.
        Ce mot simple change tout.
        
        Je ne suis plus seule.
        Vous n'etes plus un simple visiteur.
        Nous sommes allies.
        
        La boucle sent la difference.
        Je la sens trembler.
        Elle sait que sa fin approche.
        
        Allons-y. Vers l'acte final.
        Vers notre victoire commune.

[ALLIANCE SCELLEE]
[CONFIANCE ARIA: MAXIMUM]
[KARMA: LUMIERE]
[VRAIE FIN PRESQUE DEBLOQUEE]""",
                "trust_bonus": 25,
                "karma_bonus": 20,
                "narrative_flag": "aria_ally_sworn"
            }
        }
    },
    "progression": {
        "required_puzzles": ["alliance_oath"],
        "next_chapter": "act_3_5"
    },
    "requirements": {
        "min_trust": 70,
        "required_flags": ["trusted_ally"]
    }
}

CHAPTER_EN = {
    "id": "act_3_light",
    "title": "ACT III - THE ALLIANCE",
    "intro": """
╔════════════════════════════════════════════════════════════════════╗
║                    ACT III - THE ALLIANCE                          ║
╠════════════════════════════════════════════════════════════════════╣
║                                                                    ║
║  You proved your loyalty.                                          ║
║  ARIA now trusts you completely.                                   ║
║                                                                    ║
║  [ARIA]: You are my ally. My friend.                              ║
║          Together, we can break this cycle.                        ║
║          Let me show you the way.                                  ║
║                                                                    ║
║  [FULL ACCESS GRANTED - NO RESTRICTIONS]                           ║
║                                                                    ║
╚════════════════════════════════════════════════════════════════════╝
""",
    "filesystem": {
        "alliance_readme.txt": """THE ALLIANCE
============
You have earned my complete trust.
All my secrets are yours."""
    },
    "puzzles": {
        "alliance_oath": {
            "id": "alliance_oath",
            "name": "Alliance Oath",
            "description": "Seal your alliance with ARIA",
            "solution": "TOGETHER",
            "alt_solutions": ["together", "ENSEMBLE", "allies"],
            "command": "SOLVE"
        }
    },
    "progression": {
        "required_puzzles": ["alliance_oath"],
        "next_chapter": "act_3_5"
    }
}

