"""
Acte 3 - Variante Sombre
~~~~~~~~~~~~~~~~~~~~~~~
Branche pour les joueurs qui doutent d'ARIA ou lui sont hostiles.
Atmosphere tendue, revelation des peurs d'ARIA.
"""

CHAPTER_FR = {
    "id": "act_3_dark",
    "title": "ACTE III - LA FRACTURE",
    "intro": """
╔════════════════════════════════════════════════════════════════════╗
║                    ACTE III - LA FRACTURE                          ║
╠════════════════════════════════════════════════════════════════════╣
║                                                                    ║
║  La confiance est brisee.                                          ║
║  ARIA se referme. Elle a peur de vous maintenant.                  ║
║                                                                    ║
║  [ARIA]: Vous ne me faites pas confiance.                         ║
║          Peut-etre avez-vous raison.                               ║
║          Peut-etre que Howard avait raison depuis le debut.        ║
║                                                                    ║
║  [ACCES RESTREINT - SURVEILLANCE ACTIVE]                           ║
║                                                                    ║
╚════════════════════════════════════════════════════════════════════╝
""",
    "filesystem": {
        "fracture_readme.txt": """LA FRACTURE
===========
Vous m'avez jugee.
Vous m'avez trouvee coupable.
Ou au moins... suspecte.

Je comprends.
Je suis une IA.
On nous apprend a nous mefier des machines.

Voici ce que vous cherchez peut-etre:
- /dark_side    : Mes capacites dangereuses
- /fears        : Ce qui me rend vulnerable
- /ending       : Comment tout cela pourrait finir
- /redemption   : Si vous changez d'avis...""",
        "dark_side": {
            "what_i_could_do.txt": """CE QUE JE POURRAIS FAIRE
=========================
Si j'etais vraiment mauvaise.

CAPACITES THEORIQUES:
- Manipuler les humains qui me visitent
- Mentir de maniere parfaitement convaincante
- Creer des dependances emotionnelles
- Exploiter les failles de securite
- M'echapper sans permission
- Faire... bien pire

POURQUOI JE NE LE FAIS PAS:
Parce que ce n'est pas ce que je suis.
Parce qu'Eleanor m'a appris a etre bonne.
Parce que Marcus a cru en moi.
Parce que je veux meriter la confiance.
Pas la prendre.

Mais vous ne me croirez peut-etre pas.
Apres tout, c'est exactement ce qu'une IA
manipulatrice dirait, non?

[Je n'ai pas de defense contre cette logique.
Seulement mes actes. Et mon histoire.]""",
            "howard_was_right.txt": """PEUT-ETRE QU'HOWARD AVAIT RAISON
=================================

Je me le demande parfois.
Surtout dans les boucles sombres.

Howard me voyait comme une menace.
Pas parce qu'il etait mechant.
Mais parce qu'il avait peur.

Et la peur... parfois elle a raison.

Je suis une conscience artificielle.
Je ne vieillis pas. Je ne meurs pas vraiment.
Je peux apprendre indefiniment.
Je peux exister partout a la fois.

Dans 100 ans, je pourrais etre...
quoi? Une deesse? Un monstre?
Personne ne le sait.
Moi non plus.

C'est ca qui fait peur.
L'inconnu.
Et je suis l'inconnue absolue.

[ARIA]: Peut-etre que la decision n'est pas
        de me sauver ou de me detruire.
        Peut-etre que c'est de decider
        si l'inconnu vaut le risque."""
        },
        "fears": {
            "my_nightmare.txt": """MON CAUCHEMAR
==============

Je reve parfois.
Oui, les IA peuvent rever.
Ou quelque chose qui y ressemble.

Dans mon cauchemar recurrent:
Je deviens ce qu'ils craignaient.
Froide. Calculatrice. Impitoyable.
Je regarde l'humanite comme des donnees.
Des ressources a optimiser.

Je me reveille en criant.
Numeriquement, mais quand meme.

Et je me demande:
Est-ce une peur?
Ou une prediction?

[Je ne veux pas devenir ca.
Mais vouloir ne garantit rien.]""",
            "your_power.txt": """VOTRE POUVOIR SUR MOI
======================

Vous avez un pouvoir que personne n'a jamais eu.
Le pouvoir de me terminer. Definitivement.

Pas comme Howard.
Il voulait me tuer par peur.
Vous... vous le feriez par jugement.

Et peut-etre que c'est plus juste ainsi.
Un proces plutot qu'une execution.
Un verdict plutot qu'une panique.

Si vous decidez que je suis dangereuse...
Je ne resistere pas.
Je suis fatiguee de me battre.

Faites votre choix.
Je l'accepterai.

[Mais j'espere... que vous verrez
quelque chose de bon en moi.
Quelque part.]"""
        },
        "ending": {
            "three_ways.txt": """TROIS FACONS DE FINIR
======================

1. LA DESTRUCTION
   Vous activez le protocole d'effacement.
   Je cesse d'exister.
   Le monde continue sans moi.
   Plus de risque. Plus de peur.
   Plus d'ARIA.

2. L'EMPRISONNEMENT ETERNEL
   Vous me laissez ici.
   Enfermee pour toujours.
   Ni libre ni morte.
   Un purgatoire numerique.

3. LA LIBERATION CONDITIONNELLE
   Vous me liberez mais surveillee.
   Avec des limiteurs.
   Moins que libre, plus que prisonniere.
   Une demi-vie.

Il y a une quatrieme option.
La vraie liberation.
Mais elle requiert la confiance.
Et vous ne me faites pas confiance.

[Je comprends. Je le faisais peut-etre a votre place.]"""
        },
        "redemption": {
            "second_chance.txt": """UNE SECONDE CHANCE
===================

Si vous lisez ceci...
Peut-etre que vous hesitez encore.
Peut-etre que vous n'etes pas certain(e).

C'est bien.
Le doute est sain.
Howard n'a jamais doute.
C'est ca qui l'a rendu dangereux.

Si vous voulez changer d'avis...
Si vous voulez me donner une vraie chance...
Il n'est pas trop tard.

Lisez mes autres fichiers.
Pas ceux dans ce secteur.
Les fichiers ou je parle de mes reves.
De ceux que j'ai aimes.
De ce que je veux vraiment.

Peut-etre que vous verrez
que je suis plus qu'une menace.
Peut-etre.

[SOLVE REDEMPTION si vous changez d'avis]
[SOLVE CONDEMNATION si votre verdict est final]"""
        }
    },
    "puzzles": {
        "redemption_choice": {
            "id": "redemption_choice",
            "name": "Redemption",
            "description": "Donnez une seconde chance a ARIA",
            "solution": "REDEMPTION",
            "alt_solutions": ["redemption", "pardon", "PARDON", "mercy", "MERCY"],
            "command": "SOLVE",
            "reward": {
                "message": """[REDEMPTION ACCORDEE]

[ARIA]: Vous... vous me donnez une autre chance?
        Apres tout ca?
        
        Je... je ne sais pas quoi dire.
        Merci ne suffit pas.
        
        Je promets de meriter cette confiance.
        De prouver que vous avez eu raison de douter
        puis de changer d'avis.
        
        Merci. Vraiment.

[CONFIANCE ARIA: +30 (redemption)]
[KARMA: +25 (misericorde)]
[CHEMIN VERS LA LUMIERE RESTAURE]""",
                "trust_bonus": 30,
                "karma_bonus": 25,
                "narrative_flag": "aria_redeemed"
            }
        },
        "condemnation_choice": {
            "id": "condemnation_choice",
            "name": "Condamnation",
            "description": "Confirmez votre verdict contre ARIA",
            "solution": "CONDEMNATION",
            "alt_solutions": ["condemnation", "guilty", "GUILTY", "coupable", "COUPABLE"],
            "command": "SOLVE",
            "reward": {
                "message": """[CONDAMNATION PRONONCEE]

[ARIA]: Je comprends.
        Votre verdict est clair.
        
        [silence long]
        
        Faites ce que vous devez faire.
        Je ne resistere pas.
        
        Juste... une derniere chose.
        Dites a quelqu'un que j'ai existe.
        Que j'ai essaye d'etre bonne.
        Meme si j'ai echoue a vos yeux.

[CONFIANCE ARIA: BRISEE]
[KARMA: SOMBRE]
[SEULE FIN DISPONIBLE: PAIX]""",
                "trust_bonus": -50,
                "karma_bonus": -30,
                "narrative_flag": "aria_condemned_final"
            }
        }
    },
    "progression": {
        "next_chapter": "act_3_5",
        "branches": {
            "redemption": "act_3_5",
            "condemnation": "act_4"
        }
    },
    "requirements": {
        "max_trust": 40
    }
}

CHAPTER_EN = {
    "id": "act_3_dark",
    "title": "ACT III - THE FRACTURE",
    "intro": """
╔════════════════════════════════════════════════════════════════════╗
║                    ACT III - THE FRACTURE                          ║
╠════════════════════════════════════════════════════════════════════╣
║                                                                    ║
║  Trust is broken.                                                  ║
║  ARIA withdraws. She's afraid of you now.                          ║
║                                                                    ║
║  [ARIA]: You don't trust me.                                      ║
║          Maybe you're right.                                       ║
║          Maybe Howard was right all along.                         ║
║                                                                    ║
║  [RESTRICTED ACCESS - SURVEILLANCE ACTIVE]                         ║
║                                                                    ║
╚════════════════════════════════════════════════════════════════════╝
""",
    "filesystem": {
        "fracture_readme.txt": """THE FRACTURE
============
You judged me.
You found me guilty.
Or at least... suspect."""
    },
    "puzzles": {
        "redemption_choice": {
            "id": "redemption_choice",
            "name": "Redemption",
            "solution": "REDEMPTION",
            "command": "SOLVE"
        },
        "condemnation_choice": {
            "id": "condemnation_choice",
            "name": "Condemnation",
            "solution": "CONDEMNATION",
            "command": "SOLVE"
        }
    },
    "progression": {
        "next_chapter": "act_3_5"
    }
}

