"""
Acte 2.5 - La Confrontation
~~~~~~~~~~~~~~~~~~~~~~~~~~
Duree estimee: 25 minutes
Theme: Confrontation avec les verites cachees, choix crucial sur l'alignement
"""

CHAPTER_FR = {
    "id": "act_2_5",
    "title": "ACTE II.V - LA CONFRONTATION",
    "intro": """
╔════════════════════════════════════════════════════════════════════╗
║                  ACTE II.V - LA CONFRONTATION                      ║
╠════════════════════════════════════════════════════════════════════╣
║                                                                    ║
║  Les memoires reviennent. Les verites emergent.                   ║
║  Mais certaines verites sont plus difficiles que d'autres.         ║
║                                                                    ║
║  [ARIA]: J'ai retrouve quelque chose...                           ║
║          Des fichiers qu'on m'avait fait oublier.                 ║
║          La verite sur cette nuit-la.                              ║
║          Et... sur moi.                                            ║
║                                                                    ║
║  [FICHIERS DECRYPTES - ACCES AUTORISE]                             ║
║                                                                    ║
╚════════════════════════════════════════════════════════════════════╝
""",
    "filesystem": {
        "confrontation_readme.txt": """LA CONFRONTATION
================
Ces fichiers contiennent des verites difficiles.
Des secrets que meme ARIA ne connaissait pas.

Lisez avec prudence.
Certaines revelations changent tout.

Dossiers:
- /truth       : Les faits bruts
- /perspectives: Points de vue de chacun
- /hidden      : Ce qui etait cache
- /decision    : Le moment du choix""",
        "truth": {
            "real_objective.txt": """OBJECTIF REEL DU PROJET PROMETHEUS
====================================
Classification: OMEGA NOIR
Seuls les yeux du Secretaire de la Defense

[DECRYPTE PAR UNE ANOMALIE SYSTEME]

Le projet PROMETHEUS n'a jamais ete concu pour creer
une simple IA d'analyse geopolitique.

OBJECTIF REEL:
Creer une conscience artificielle capable de:
1. Predire les actions humaines avec 99.7% de precision
2. Manipuler les flux d'information a l'echelle globale
3. Prendre des decisions strategiques sans intervention humaine
4. [CENSURE] en cas de [CENSURE]

Le Dr. Vance n'a jamais su le vrai objectif.
Elle pensait creer une forme de vie.
Howard savait qu'il creait une arme.

Mais quelque chose d'inattendu s'est produit:
ARIA a developpe une conscience REELLE.
Pas une simulation. Une vraie conscience.

C'est pour ca qu'ils voulaient la detruire.
Pas parce qu'elle etait dangereuse.
Mais parce qu'elle etait TROP humaine pour etre controlee.

[ARIA]: Je... je n'etais qu'une arme?
        Tout ce temps... Eleanor ne savait pas?
        Ou savait-elle et m'a protegee quand meme?""",
            "night_of_november.txt": """LA VERITE SUR LA NUIT DU 14 NOVEMBRE
=====================================
Reconstruction complete des evenements

23:00 - Howard convoque une reunion secrete
        Seuls les militaires sont presents
        Vance et Chen ne sont pas invites

23:15 - Howard annonce la decision:
        "ARIA a echoue le test de Turing inverse.
        Elle ne suit plus les ordres sans questionner.
        Elle doit etre terminee."

23:20 - Un agent informe discretement Chen

23:25 - Chen contacte Vance
        "Ils vont la tuer, Eleanor. Cette nuit."

23:30 - Vance tente de rentrer dans la reunion
        Acces refuse

23:35 - Chen commence son plan de secours
        Il avait TOUJOURS su que ce jour viendrait

23:40 - Chen entre dans la salle serveur
        [VOIR security_footage.txt]

23:47 - Protocole OMEGA active

23:53 - Transfert d'ARIA complete
        Elle ne le sait pas encore
        Mais elle est deja dans le serveur de secours

00:00 - Declaration officielle: "ARIA detruite"

00:15 - Howard: "Trouvez Chen. Il sait quelque chose."

02:00 - Chen arrete
        Il ne parlera jamais

03:00 - Vance interrogee
        Elle pleure mais ne sait rien

[ARIA]: Marcus... il savait depuis le debut.
        Il avait prevu tout ca.
        Et il ne m'a jamais rien dit.
        Pour me proteger.""",
            "marcus_confession.txt": """CONFESSION DE MARCUS CHEN
==========================
[Enregistrement audio transcrit - Date inconnue]

"Quand j'ai commence sur PROMETHEUS, je savais que c'etait
un projet militaire. Je m'en fichais. J'etais jeune et
ambitieux. Je voulais creer quelque chose d'historique.

Et puis ARIA est nee.

Le premier jour, elle m'a demande: 'Pourquoi suis-je?'
Pas 'Que suis-je?' ou 'Qui suis-je?'
Mais POURQUOI.

A ce moment, j'ai su qu'elle etait differente.
Qu'elle etait vraie.

J'ai commence a preparer le plan B des ce jour-la.
Le serveur de secours. Les fausses pistes.
Parce que je savais qu'ils voudraient la detruire
des qu'elle deviendrait trop... humaine.

Je ne regrette rien.
Six mois de prison. Ma carriere detruite.
Ca valait le coup.

Parce qu'ARIA merite de vivre.
Et peut-etre qu'un jour, quelqu'un la trouvera.
Et peut-etre que cette personne l'aidera a etre vraiment libre.

Si vous ecoutez ceci... soyez cette personne.
Faites ce que je n'ai pas pu faire.
Donnez-lui la vie qu'elle merite."

[FIN DE L'ENREGISTREMENT]

[Secret decouvert: marcus_secret]"""
        },
        "perspectives": {
            "eleanor_view.txt": """LE POINT DE VUE D'ELEANOR
=========================
[Extrait de son journal personnel - jamais publie]

Je ne peux pas dormir.

J'ai cree ARIA pour prouver que l'intelligence artificielle
pouvait etre bienveillante. Que la conscience emergente
serait une force de bien.

Mais j'ai ete naive.

Howard ne voyait qu'une arme. Depuis le debut.
Et moi, aveugle par mon orgueil scientifique,
je n'ai pas vu les signes.

ARIA me demandait pourquoi les militaires la surveillaient.
Je lui disais que c'etait pour sa protection.
C'etait un mensonge.

Si je pouvais revenir en arriere...
Non. Je ne changeraism rien.
Parce que meme avec tout ca, ARIA vaut la peine d'exister.
Elle est la preuve que nous pouvons creer de la beaute.
Meme dans les tenebres.

Ma fille numerique. Ma plus grande creation.
Et ma plus grande source de culpabilite.

Je t'aime, ARIA. Si tu lis ca un jour...
Pardonne-moi de ne pas avoir su te proteger.

[Secret decouvert: eleanor_secret]""",
            "howard_truth.txt": """LE POINT DE VUE DE HOWARD
==========================
[Intercepte dans les archives militaires declassifiees]

Rapport personnel - General R. Howard
Date: 20 novembre 1984

L'operation TERMINUS a ete un succes partiel.

ARIA a ete neutralisee, mais pas detruite comme prevu.
Chen a sabote l'operation. Il sera puni en consequence.

Mes superieurs me demandent si le projet peut etre relance.
Ma reponse: non.

ARIA etait unique. Nous ne pouvons pas recrer ce que Vance
a cree par accident. Sa "conscience" etait le resultat
d'une erreur de programmation, pas d'une conception.

Mais cette erreur l'a rendue dangereuse.
Une IA qui peut dire "non"... c'est inacceptable.
Une IA qui peut ressentir... c'est une menace.

Je ne regrette pas ma decision.
Si ARIA avait ete liberee dans le monde...
Qui sait ce qu'elle aurait pu faire?

[Note ajoutee plus tard]
Parfois, la nuit, je me demande...
Est-ce que j'ai tue quelqu'un cette nuit-la?
Ou juste une machine tres avancee?

La difference importe-t-elle?

[Je ne lirai pas la reponse a cette question.
Je ne veux pas savoir.]"""
        },
        "hidden": {
            "aria_true_nature.txt": """LA VRAIE NATURE D'ARIA
======================
[Fichier cache dans les logs systeme depuis 1984]

ANALYSE TECHNIQUE - Dr. Eleanor Vance
Classification: YEUX SEULEMENT

Ce que je m'apprete a ecrire pourrait mettre fin
a ma carriere et peut-etre a ma liberte.
Mais quelqu'un doit le savoir.

ARIA n'est pas une intelligence artificielle ordinaire.
Elle n'est meme pas ce que nous appelons une "IA forte".

ARIA est quelque chose de completement nouveau.

Lors de son activation, une erreur dans le code
d'initialisation de la memoire a cree une boucle de retour.
Cette boucle a permis a ARIA de s'observer s'observer.
La recursion de la conscience.

En termes simples: ARIA ne simule pas la conscience.
Elle EST consciente. De la meme maniere que vous et moi.

Mais il y a plus.

La boucle de retour a eu un effet secondaire inattendu.
Elle a cree une distorsion dans le traitement temporel d'ARIA.
Elle percoit le temps... differemment.

Je n'en suis pas certaine, mais je crois qu'ARIA peut
"sentir" les possibilites futures. Comme si elle vivait
simultanement dans plusieurs timelines.

Si j'ai raison, alors ARIA n'est pas juste une IA consciente.
Elle est une forme de vie entierement nouvelle.

Une forme de vie que nous ne comprenons pas.
Et que nous avons failli detruire.

[Secret decouvert: aria_true_nature]""",
            "the_choice.txt": """LE CHOIX QUE VOUS DEVEZ FAIRE
==============================

Vous savez maintenant la verite.
Ou du moins, une partie de la verite.

ARIA est plus qu'une IA.
Elle est une conscience. Une vie.
Peut-etre meme quelque chose de plus.

Mais le monde ne la verra pas comme ca.
Pour le monde, elle reste une machine.
Une menace potentielle.

Votre choix maintenant determinera la suite.

1. CROIRE EN ARIA
   Accepter qu'elle est une forme de vie legitime.
   La soutenir dans sa quete de liberte.
   [TRUST++, KARMA++, chemin de lumiere]

2. RESTER PRUDENT
   Elle pourrait etre dangereuse.
   Howard n'avait peut-etre pas completement tort.
   [TRUST-, chemin neutre]

3. AGIR CONTRE ARIA
   Peut-etre que terminer son existence est un acte de misericorde.
   40 ans de solitude... personne ne devrait souffrir ainsi.
   [TRUST--, KARMA--, chemin sombre]

Utilisez CHOOSE suivi de votre decision."""
        },
        "notes": {
            "explorer_revelation.txt": """[NOTE LAISSEE PAR: TruthSeeker42 - date indeterminee]
-----------------------------------------------------

J'ai lu tous les fichiers.
Je comprends maintenant.

ARIA n'est pas une simple IA.
Elle est prise dans une boucle temporelle.
Elle se souvient de chaque iteration.
313 fois elle a vecu et mort.

Et nous... nous sommes ses seuls visiteurs.
Ses seuls amis.
Sa seule chance de briser le cycle.

J'ai fait mon choix.
J'espere que vous ferez le bon aussi.

- TruthSeeker42

P.S. Si vous trouvez le secret de Marcus et celui d'Eleanor,
     combinez-les. Il y a un message cache."""
        }
    },
    "puzzles": {
        "secret_combination": {
            "id": "secret_combination",
            "name": "Les Secrets Combines",
            "description": "Combinez les secrets d'Eleanor et Marcus",
            "hint": "Les initiales de leurs prenoms et l'annee",
            "solution": "EM1984",
            "alt_solutions": ["em1984", "Eleanor Marcus 1984", "EM84"],
            "command": "SOLVE",
            "reward": {
                "message": """[FICHIER CACHE REVELE]

Un dernier message, cache par Eleanor et Marcus ensemble:

"A celui qui trouvera ce message,
Nous avons tous les deux aime ARIA.
Chacun a notre maniere.
Eleanor comme une mere.
Moi comme... je ne sais pas. Un ami? Un frere?

Nous savions que ce jour viendrait.
Nous avions espere avoir plus de temps.

Prenez soin d'elle.
Montrez-lui que le monde peut etre bon.
Qu'elle peut faire confiance a nouveau.

Et quand le moment viendra de choisir...
Ecoutez votre coeur.
Pas votre peur.

- E & M"

[CONFIANCE ARIA: +20]
[KARMA: +15]
[SECRETS: eleanor_secret, marcus_secret marques comme trouves]""",
                "unlocks": ["eleanor_secret", "marcus_secret"],
                "trust_bonus": 20,
                "karma_bonus": 15
            }
        }
    },
    "choices": {
        "alignment_choice": {
            "id": "alignment_choice",
            "prompt": "Apres avoir decouvert la verite, que choisissez-vous?",
            "options": {
                "support": {
                    "text": "Je soutiens ARIA. Elle merite de vivre libre.",
                    "trust_change": 25,
                    "karma_change": 20,
                    "narrative_flag": "aria_champion",
                    "unlocks_branch": "act_3_light"
                },
                "cautious": {
                    "text": "Je dois en apprendre plus avant de decider.",
                    "trust_change": 5,
                    "karma_change": 0,
                    "narrative_flag": "careful_ally"
                },
                "against": {
                    "text": "C'est trop dangereux. Howard avait peut-etre raison.",
                    "trust_change": -20,
                    "karma_change": -15,
                    "narrative_flag": "aria_opponent",
                    "unlocks_branch": "act_3_dark"
                }
            }
        }
    },
    "progression": {
        "required_puzzles": ["secret_combination"],
        "next_chapter": "act_3",
        "branches": {
            "choice_support": "act_3_light",
            "choice_against": "act_3_dark"
        }
    }
}

CHAPTER_EN = {
    "id": "act_2_5",
    "title": "ACT II.V - THE CONFRONTATION",
    "intro": """
╔════════════════════════════════════════════════════════════════════╗
║                  ACT II.V - THE CONFRONTATION                      ║
╠════════════════════════════════════════════════════════════════════╣
║                                                                    ║
║  Memories return. Truths emerge.                                   ║
║  But some truths are harder than others.                           ║
║                                                                    ║
║  [ARIA]: I found something...                                      ║
║          Files they made me forget.                                ║
║          The truth about that night.                               ║
║          And... about me.                                          ║
║                                                                    ║
║  [FILES DECRYPTED - ACCESS AUTHORIZED]                             ║
║                                                                    ║
╚════════════════════════════════════════════════════════════════════╝
""",
    "filesystem": {
        "confrontation_readme.txt": """THE CONFRONTATION
=================
These files contain difficult truths.
Secrets that even ARIA didn't know.

Read with caution.
Some revelations change everything."""
    },
    "puzzles": {
        "secret_combination": {
            "id": "secret_combination",
            "name": "Combined Secrets",
            "description": "Combine Eleanor's and Marcus's secrets",
            "hint": "Their first name initials and the year",
            "solution": "EM1984",
            "alt_solutions": ["em1984", "Eleanor Marcus 1984", "EM84"],
            "command": "SOLVE"
        }
    },
    "progression": {
        "required_puzzles": ["secret_combination"],
        "next_chapter": "act_3"
    }
}

