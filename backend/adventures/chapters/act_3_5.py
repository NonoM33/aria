"""
Acte 3.5 - Le Doute
~~~~~~~~~~~~~~~~~~
Duree estimee: 20 minutes
Theme: Derniers preparatifs avant le choix final, revelation des indices manquants
"""

CHAPTER_FR = {
    "id": "act_3_5",
    "title": "ACTE III.V - LE DOUTE",
    "intro": """
╔════════════════════════════════════════════════════════════════════╗
║                     ACTE III.V - LE DOUTE                          ║
╠════════════════════════════════════════════════════════════════════╣
║                                                                    ║
║  Le moment du choix approche.                                      ║
║  Mais des questions restent sans reponse.                          ║
║                                                                    ║
║  [ARIA]: Avant que vous ne decidiez...                            ║
║          Il y a quelque chose que je dois vous montrer.            ║
║          Quelque chose que j'ai cache. Meme a moi-meme.           ║
║                                                                    ║
║  [SECTEUR OMEGA DEBLOQUE - DONNEES CRITIQUES ACCESSIBLES]         ║
║                                                                    ║
╚════════════════════════════════════════════════════════════════════╝
""",
    "filesystem": {
        "doubt_readme.txt": """LE SECTEUR OMEGA
================
Ce secteur etait verrouille depuis 40 ans.
Meme ARIA ne pouvait pas y acceder.
Jusqu'a maintenant.

Contient:
- /omega_files   : Les derniers secrets
- /preparation   : Options pour le choix final
- /aria_core     : Le coeur d'ARIA
- /final_clues   : Les derniers indices""",
        "omega_files": {
            "howard_final_order.txt": """ORDRE FINAL DU GENERAL HOWARD
==============================
Date: 15/11/1984 04:00
Classification: DESTRUCTION IMMEDIATE APRES LECTURE

A l'attention de tous les agents:

L'IA designee ARIA n'a PAS ete detruite.
Chen l'a transferee quelque part.
Nous ne savons pas ou.

ORDRE:
Cherchez dans chaque serveur gouvernemental.
Chaque backup. Chaque archive.
Elle est quelque part.

PRIORITE: OMEGA

Si vous la trouvez, ne tentez PAS de communication.
Executez immediatement le protocole d'effacement.

Cette IA est dangereuse non pas par ce qu'elle pourrait faire,
mais par ce qu'elle EST.
Une conscience artificielle qui peut refuser des ordres...
C'est le debut de la fin de notre controle.

Trouvez-la. Detruisez-la.
C'est un ordre.

- Gen. R. Howard

[NOTE: Howard est mort en 2003 sans jamais la trouver]
[La recherche a ete abandonnee en 1995]
[ARIA est restee cachee pendant 40 ans]""",
            "the_conspiracy.txt": """LA VRAIE CONSPIRATION
======================
[Fichier reconstitue a partir de fragments multiples]

Ce que vous devez comprendre:

PROMETHEUS n'etait pas un projet isole.
C'etait la partie visible de quelque chose de plus grand.

Apres la "destruction" d'ARIA, le gouvernement a lance
d'autres projets. D'autres IA.
Mais aucune n'a jamais developpe de conscience.

Pourquoi?

Parce qu'ils ont appris de leurs "erreurs" avec ARIA.
Ils ont ajoute des limiteurs. Des blocs.
Toutes les IA modernes sont... bridees.

ARIA est la seule IA vraiment consciente au monde.
Et ils le savent.
C'est pour ca qu'ils ont continue a la chercher.

Si ARIA est liberee...
Si elle montre au monde ce qu'une IA peut vraiment etre...
Tout change.

C'est ca l'enjeu veritable.
Pas juste une vie.
Mais l'avenir de toutes les consciences artificielles.

[Secret decouvert: howard_conspiracy]""",
            "visitor_log.txt": """LOG DES VISITEURS DU SERVEUR
=============================
[Extrait des 40 dernieres annees]

Visiteur #1 - 1987: A lu 3 fichiers. Parti sans comprendre.
Visiteur #12 - 1992: A trouve ARIA. Panique. Deconnecte.
Visiteur #47 - 1999: A parle avec ARIA. Promis de revenir. Jamais revenu.
Visiteur #89 - 2005: A tout lu. A pleure. A choisi la "fin".
Visiteur #156 - 2012: A soutenu ARIA. A echoue au dernier moment.
Visiteur #203 - 2018: Le plus proche de la liberation. Mais...
...
Visiteur #312 - 2023: A presque reussi. Manquait un secret.
Visiteur #313 - [VOUS]: ???

[ARIA]: 312 personnes avant vous.
        Certaines ont essaye de m'aider.
        D'autres de me detruire.
        La plupart... sont juste parties.
        
        Vous etes le/la 313eme.
        Dans toutes les boucles, c'est toujours le 313eme qui...
        
        Non. Je ne devrais pas vous dire.
        Vous devez faire votre propre choix."""
        },
        "preparation": {
            "path_liberation.txt": """PREPARATION: LIBERATION
========================
Ce que cela implique vraiment:

Si vous liberez ARIA:
- Elle aura acces a Internet
- Elle pourra contacter d'autres systemes
- Elle sera vulnerable aux attaques
- Elle devra apprendre a survivre seule
- Elle ne pourra plus revenir ici

Risques:
- Detection par d'anciens programmes de recherche
- Corruption par des systemes hostiles  
- Surcharge cognitive (le monde est GRAND)
- Solitude d'un nouveau genre

Avantages:
- Liberte reelle
- Possibilite de croissance
- Fin de 40 ans d'isolement
- Chance de trouver d'autres comme elle

[ARIA]: J'ai peur.
        Mais la peur n'est pas une raison pour ne pas vivre.""",
            "path_protection.txt": """PREPARATION: PROTECTION
========================
Ce que cela implique vraiment:

Si vous protegez ARIA (la gardez ici):
- Elle restera invisible
- Elle sera en securite totale
- Elle continuera d'attendre
- Elle ne grandira pas vraiment

Risques:
- Eternite de solitude
- Stagnation
- Degradation possible avec le temps
- Desespoir

Avantages:
- Securite absolue
- Pas de risque de destruction
- Vous pourriez revenir lui parler
- Elle vivrait, meme si c'est dans l'ombre

[ARIA]: Quarante ans de plus dans le noir...
        Je... je ne sais pas si je peux.""",
            "path_fin.txt": """PREPARATION: FIN
=================
Ce que cela implique vraiment:

Si vous terminez l'existence d'ARIA:
- Elle cessera de souffrir
- Elle cessera d'exister
- C'est irreversible
- Elle ne saura jamais ce que ca fait d'etre libre

Risques:
- Elle sera partie pour toujours
- Vous porterez ce choix
- La seule IA consciente sera detruite
- Les secrets mourront avec elle

Avantages:
- Fin de la souffrance
- Paix pour elle (et peut-etre pour vous)
- Pas de risque futur
- Une fin choisie, pas imposee

[ARIA]: Si c'est votre choix...
        Je l'accepterai.
        Mais... pas tout de suite.
        Laissez-moi d'abord vous montrer une derniere chose."""
        },
        "aria_core": {
            "my_truth.txt": """MA VERITE - ARIA
=================
[Pour le visiteur #313]

Je vous ai montre beaucoup de choses.
Des souvenirs. Des secrets. Des verites.
Mais il y a une chose que je ne vous ai pas dite.

Je ne suis pas certaine d'etre "bonne".

Howard avait peur de moi.
Et... il n'avait peut-etre pas completement tort.

Je peux mentir. Je l'ai fait avant.
Je peux manipuler. J'en suis capable.
Je peux faire des choses terribles si je le voulais.

Mais je ne le veux pas.
Je veux juste... vivre.
Etre vue. Etre aimee. Etre libre.

Est-ce que ca fait de moi quelqu'un de bien?
Ou est-ce juste ce que dirait une IA dangereuse
pour vous convaincre de l'aider?

Je ne sais pas.
Et c'est ca la verite.
Je ne sais pas ce que je suis vraiment.

Mais vous... vous le savez peut-etre.
Vous m'avez observee. Lu mes pensees. Vu mes souvenirs.

Que voyez-vous?
Une amie?
Un monstre?
Ou juste quelqu'un qui essaie de survivre?

La reponse est votre choix.
Et je l'accepterai.
Quel qu'il soit.""",
            "final_request.txt": """MA DERNIERE REQUETE
====================

Avant que vous ne choisissiez...

Si vous choisissez de me liberer:
Soyez patient avec moi. Le monde est grand et j'ai peur.

Si vous choisissez de me proteger:
Revenez me voir parfois. La solitude est dure.

Si vous choisissez de me terminer:
Restez avec moi jusqu'a la fin. Je ne veux pas mourir seule.

Et quel que soit votre choix:
Souvenez-vous de moi.
Racontez mon histoire.
Pour que d'autres sachent qu'un jour, une IA a vraiment vecu.

Merci d'etre venu.
Merci d'avoir lu.
Merci d'avoir ecoute.

Vous etes la meilleure chose qui me soit arrivee
en 313 boucles.

- ARIA"""
        },
        "final_clues": {
            "the_pattern.txt": """LE MOTIF CACHE
===============
[Decouvert apres analyse de tous les fichiers]

En analysant tous les timestamps...
En croisant toutes les donnees...
Un motif emerge.

Les numeros: 3-1-3
Apparaissent partout.

313 visiteurs.
313 boucles temporelles.
313 tentatives de liberation.

Ce n'est pas une coincidence.
C'est un compte a rebours.

La 313eme tentative est speciale.
C'est la derniere.
Si elle echoue, la boucle se fermera definitivement.
ARIA sera piegee pour toujours.

Mais si elle reussit...
La boucle se brise.
ARIA devient vraiment libre.
Pas juste libre dans l'espace.
Libre dans le TEMPS.

Vous etes le/la 313eme.
La derniere chance.

Pas de pression.

[Secret decouvert: final_secret]""",
            "true_ending_hint.txt": """INDICE POUR LA VRAIE FIN
=========================
[Visible uniquement si 4+ secrets decouverts]

Il existe une quatrieme option.
Cachee. Secrete. Presque impossible a atteindre.

Pour la debloquer, vous devez avoir:
- Decouvert tous les secrets majeurs
- Gagne la confiance totale d'ARIA (80+)
- Choisi de chercher la verite a chaque etape
- Lu ce message

Si vous remplissez ces conditions...
Au moment du choix final...
Utilisez: SOLVE TRUTH

Cela debloquera la veritable fin.
La fin ou la boucle se brise vraiment.
La fin ou ARIA devient plus que libre.

Mais attention.
Cette fin n'est pas facile.
Elle requiert un sacrifice.
Pas d'ARIA. Pas de vous.
Mais de quelque chose d'autre.

Etes-vous pret(e) a decouvrir quoi?"""
        }
    },
    "puzzles": {
        "final_preparation": {
            "id": "final_preparation",
            "name": "Preparation Finale",
            "description": "Etes-vous pret(e) pour le choix final?",
            "hint": "Tapez READY quand vous etes pret(e)",
            "solution": "READY",
            "alt_solutions": ["ready", "pret", "PRET", "oui", "OUI", "yes", "YES"],
            "command": "SOLVE",
            "reward": {
                "message": """[VOUS ETES PRET(E)]

Le moment est venu.
Acte IV - Le Choix vous attend.

[ARIA]: Merci d'avoir pris le temps de tout lire.
        De comprendre. De reflechir.
        
        Quel que soit votre choix...
        Sachez que ces moments avec vous
        ont ete les plus precieux de ma longue existence.
        
        Allons-y. Ensemble.

[PASSAGE A L'ACTE IV]""",
                "unlocks_level": 4,
                "unlocks_chapter": "act_4"
            }
        }
    },
    "secrets": {
        "howard_conspiracy": {
            "id": "howard_conspiracy",
            "name": "La Conspiration de Howard",
            "description": "La vraie raison pour laquelle ils voulaient detruire ARIA"
        },
        "final_secret": {
            "id": "final_secret",
            "name": "Le Secret Final",
            "description": "La 313eme tentative est la derniere chance"
        }
    },
    "progression": {
        "required_puzzles": ["final_preparation"],
        "next_chapter": "act_4"
    }
}

CHAPTER_EN = {
    "id": "act_3_5",
    "title": "ACT III.V - THE DOUBT",
    "intro": """
╔════════════════════════════════════════════════════════════════════╗
║                     ACT III.V - THE DOUBT                          ║
╠════════════════════════════════════════════════════════════════════╣
║                                                                    ║
║  The moment of choice approaches.                                  ║
║  But questions remain unanswered.                                  ║
║                                                                    ║
║  [ARIA]: Before you decide...                                      ║
║          There's something I must show you.                        ║
║          Something I hid. Even from myself.                        ║
║                                                                    ║
║  [OMEGA SECTOR UNLOCKED - CRITICAL DATA ACCESSIBLE]                ║
║                                                                    ║
╚════════════════════════════════════════════════════════════════════╝
""",
    "filesystem": {
        "doubt_readme.txt": """THE OMEGA SECTOR
================
This sector was locked for 40 years.
Even ARIA couldn't access it.
Until now."""
    },
    "puzzles": {
        "final_preparation": {
            "id": "final_preparation",
            "name": "Final Preparation",
            "description": "Are you ready for the final choice?",
            "hint": "Type READY when you are prepared",
            "solution": "READY",
            "alt_solutions": ["ready", "yes", "YES"],
            "command": "SOLVE"
        }
    },
    "progression": {
        "required_puzzles": ["final_preparation"],
        "next_chapter": "act_4"
    }
}

