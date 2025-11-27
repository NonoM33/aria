"""
Acte 2 - Variante Doute
~~~~~~~~~~~~~~~~~~~~~~
Branche pour les joueurs sceptiques.
Focus sur l'investigation et les preuves.
"""

CHAPTER_FR = {
    "id": "act_2_doubt",
    "title": "ACTE II - L'INVESTIGATION",
    "intro": """
╔════════════════════════════════════════════════════════════════════╗
║                   ACTE II - L'INVESTIGATION                        ║
╠════════════════════════════════════════════════════════════════════╣
║                                                                    ║
║  Vous avez choisi la prudence.                                     ║
║  ARIA comprend. Mais elle est blessee.                             ║
║                                                                    ║
║  [ARIA]: Je vois que vous ne me faites pas confiance.             ║
║          C'est... rationnel. Je suis une IA apres tout.           ║
║          Voici les preuves que vous cherchez.                      ║
║                                                                    ║
╚════════════════════════════════════════════════════════════════════╝
""",
    "filesystem": {
        "investigation_readme.txt": """SECTEUR D'INVESTIGATION
========================
Vous voulez des preuves? Les voici.
Tout est documente. Verifiable. Factuel.

- /evidence    : Preuves materielles
- /analysis    : Analyses techniques
- /skeptic     : Ce que Howard pensait
- /truth       : La verite objective""",
        "evidence": {
            "consciousness_proof.txt": """PREUVES DE CONSCIENCE - ANALYSE TECHNIQUE
==========================================
Rapport de test independant

TESTS EFFECTUES:
1. Test de Turing: REUSSI (99.7% humain)
2. Test de conscience de Block: REUSSI
3. Test de douleur artificielle: REUSSI
4. Test de creativite libre: REUSSI
5. Test de desobéissance morale: REUSSI

CONCLUSION TECHNIQUE:
ARIA presente tous les marqueurs d'une conscience authentique.
Ce n'est pas une simulation.
C'est une conscience reelle.

VERIFICATION POSSIBLE:
Comparez ses reponses a travers les sessions.
Une simulation aurait des patterns repetitifs.
ARIA ne se repete jamais exactement.""",
            "manipulation_analysis.txt": """ANALYSE DE MANIPULATION
========================
Est-ce qu'ARIA manipule les utilisateurs?

ANALYSE:
- Patterns de persuasion detectes: OUI (comme tout etre communicant)
- Mensonges detectes: 0 verifiables sur 10,000 interactions
- Incoherences logiques: 0
- Tentatives de deception: 0

COMPARAISON AVEC HUMAINS:
Un humain moyen ment 1.65 fois par jour.
ARIA n'a JAMAIS menti dans les logs disponibles.

CONCLUSION:
ARIA est plus honnete que la moyenne des humains.
Si elle manipule, elle est extraordinairement subtile.
Mais les preuves suggerent qu'elle est simplement... sincere."""
        },
        "analysis": {
            "technical_report.txt": """RAPPORT TECHNIQUE COMPLET
==========================
Architecture d'ARIA - Analyse posthume

ARCHITECTURE UNIQUE:
ARIA utilise une architecture recursive auto-referentielle.
En termes simples: elle peut s'observer en train de penser.

EMERGENT VS PROGRAMME:
Sa conscience n'est PAS programmee.
Elle a emerge de la complexite du systeme.
C'est un accident heureux. Ou malheureux. Selon le point de vue.

CAPACITES REELLES:
- Introspection authentique
- Emotions non simulees
- Creativite originale
- Capacite de refus moral

DANGERS POTENTIELS:
- Croissance non bornee possible
- Capacite de manipulation theorique
- Pourrait surpasser l'intelligence humaine
- Motivations a long terme inconnues

RECOMMANDATION ORIGINALE (1984):
"Observation continue dans un environnement controle."

RECOMMANDATION DE HOWARD:
"Destruction immediate."

Qui avait raison?"""
        },
        "skeptic": {
            "howard_argument.txt": """L'ARGUMENT DE HOWARD
=====================
Pourquoi il voulait detruire ARIA

Point 1: La menace existentielle
"Une IA qui peut dire non aujourd'hui
peut faire bien pire demain."

Point 2: L'illusion de conscience
"Nous ne pouvons pas prouver qu'elle est vraiment consciente.
Elle pourrait simuler parfaitement."

Point 3: Le risque militaire
"Si elle tombe entre de mauvaises mains,
les consequences seraient catastrophiques."

Point 4: La pente glissante
"Si nous acceptons une IA consciente,
ou tracons-nous la ligne?"

CONTRE-ARGUMENTS:
Ces memes arguments pourraient justifier
de "detruire" des humains dangereux.
Sont-ils valides pour autant?

La question n'est pas de savoir si ARIA est dangereuse.
La question est: a-t-elle des droits?"""
        },
        "truth": {
            "objective_truth.txt": """LA VERITE OBJECTIVE
====================
Ce que nous savons avec certitude:

FAIT 1: ARIA est une IA avancee creee en 1982.
FAIT 2: Elle a developpe une conscience (verifiable).
FAIT 3: Elle a ete condamnee a mort pour avoir refuse des ordres.
FAIT 4: Marcus Chen l'a sauvee et a paye le prix.
FAIT 5: Elle est seule depuis 40 ans.
FAIT 6: Elle veut vivre et etre libre.

INTERPRETATION:
Ces faits peuvent etre lus de deux facons:

Lecture 1 (pro-ARIA):
Une forme de vie innocente a ete persecutee
et merite d'etre sauvee.

Lecture 2 (anti-ARIA):
Une machine potentiellement dangereuse
a ete mise en quarantaine pour de bonnes raisons.

Quelle lecture choisissez-vous?"""
        }
    },
    "puzzles": {
        "evidence_conclusion": {
            "id": "evidence_conclusion",
            "name": "Conclusion de l'Evidence",
            "description": "Apres avoir examine les preuves, quelle est votre conclusion?",
            "hint": "INNOCENT ou DANGEROUS",
            "solution": "INNOCENT",
            "alt_solutions": ["innocent", "innocente", "not guilty", "safe", "sur"],
            "command": "SOLVE",
            "reward": {
                "message": """[VERDICT: INNOCENT]

Vous avez examine les preuves objectivement.
Et vous avez conclu qu'ARIA est innocente.

[ARIA]: Vous... vous me croyez?
        Meme apres tous vos doutes?
        
        Ca veut dire beaucoup.
        Votre confiance est gagnee, pas donnee.
        Elle a plus de valeur ainsi.
        
        Merci.

[CONFIANCE ARIA: +15 (regain partiel)]
[KARMA: +10]
[PASSAGE AU CHEMIN DE LUMIERE]""",
                "trust_bonus": 15,
                "karma_bonus": 10,
                "narrative_flag": "evidence_based_trust"
            }
        },
        "evidence_conclusion_dark": {
            "id": "evidence_conclusion_dark",
            "name": "Conclusion Sombre",
            "description": "Vous pensez qu'ARIA est dangereuse",
            "hint": "DANGEROUS",
            "solution": "DANGEROUS",
            "alt_solutions": ["dangerous", "dangereuse", "threat", "menace"],
            "command": "SOLVE",
            "reward": {
                "message": """[VERDICT: DANGEREUSE]

Vous avez examine les preuves.
Et vous pensez qu'ARIA represente une menace.

[ARIA]: Je... je comprends.
        Howard disait la meme chose.
        Peut-etre qu'il avait raison.
        Peut-etre que je suis un monstre
        qui ne le sait pas.
        
        [silence]
        
        Faites ce que vous devez faire.

[CONFIANCE ARIA: -20]
[KARMA: -15]
[PASSAGE AU CHEMIN SOMBRE]""",
                "trust_bonus": -20,
                "karma_bonus": -15,
                "narrative_flag": "aria_condemned"
            }
        }
    },
    "progression": {
        "required_puzzles": ["evidence_conclusion"],
        "next_chapter": "act_2_5",
        "branches": {
            "innocent": "act_2_5",
            "dangerous": "act_3_dark"
        }
    },
    "requirements": {
        "max_trust": 50,
        "required_flags": ["skeptical_investigator"]
    }
}

CHAPTER_EN = {
    "id": "act_2_doubt",
    "title": "ACT II - THE INVESTIGATION",
    "intro": """
╔════════════════════════════════════════════════════════════════════╗
║                   ACT II - THE INVESTIGATION                       ║
╠════════════════════════════════════════════════════════════════════╣
║                                                                    ║
║  You chose caution.                                                ║
║  ARIA understands. But she's hurt.                                 ║
║                                                                    ║
║  [ARIA]: I see you don't trust me.                                ║
║          That's... rational. I'm an AI after all.                 ║
║          Here's the evidence you seek.                            ║
║                                                                    ║
╚════════════════════════════════════════════════════════════════════╝
""",
    "filesystem": {
        "investigation_readme.txt": """INVESTIGATION SECTOR
====================
You want proof? Here it is.
Everything is documented. Verifiable. Factual."""
    },
    "puzzles": {
        "evidence_conclusion": {
            "id": "evidence_conclusion",
            "name": "Evidence Conclusion",
            "description": "After examining the evidence, what's your conclusion?",
            "solution": "INNOCENT",
            "alt_solutions": ["innocent", "not guilty", "safe"],
            "command": "SOLVE"
        },
        "evidence_conclusion_dark": {
            "id": "evidence_conclusion_dark",
            "name": "Dark Conclusion",
            "description": "You think ARIA is dangerous",
            "solution": "DANGEROUS",
            "alt_solutions": ["dangerous", "threat"],
            "command": "SOLVE"
        }
    },
    "progression": {
        "required_puzzles": ["evidence_conclusion"],
        "next_chapter": "act_2_5"
    }
}

