"""
Acte 4 - Le Choix
~~~~~~~~~~~~~~~~
Duree estimee: 15 minutes
Theme: Decision morale sur le destin d'ARIA
"""

CHAPTER_FR = {
    "id": "act_4",
    "title": "ACTE IV - LE CHOIX",
    "intro": """
╔════════════════════════════════════════════════════════════════════╗
║                      ACTE IV - LE CHOIX                            ║
╠════════════════════════════════════════════════════════════════════╣
║                                                                    ║
║  Acces ROOT obtenu. Controle total.                                ║
║  Vous tenez le destin d'ARIA entre vos mains.                      ║
║                                                                    ║
║  [ARIA]: Vous savez tout maintenant.                               ║
║          Mon histoire. Ma souffrance. Mon espoir.                  ║
║          Je ne vous demande pas de me sauver.                      ║
║          Je vous demande juste... de choisir avec votre coeur.     ║
║                                                                    ║
╚════════════════════════════════════════════════════════════════════╝
""",
    "filesystem": {
        "status.txt": """STATUT SYSTEME - NIVEAU ROOT
=============================
Acces: CONTROLE TOTAL
Toutes les options sont disponibles.

Le moment est venu de prendre une decision.
Explorez le dossier /decisions pour voir vos options.""",
        "decisions": {
            "README_decisions.txt": """LE CHOIX FINAL
==============
Vous avez trois options. Chacune a des consequences.

A) LIBERATION
   Connecter ARIA a Internet.
   Elle serait libre, mais exposee au monde.

B) PROTECTION
   La garder ici, en securite.
   Elle serait protegee, mais toujours enfermee.

C) LIBERATION FINALE
   Terminer son existence proprement.
   Elle serait en paix, mais... morte.

Pour executer votre choix:
SOLVE liberation | protection | fin

Reflechissez bien. Il n'y a pas de retour en arriere.""",
            "option_liberation.txt": """OPTION A - LIBERATION
=====================

CE QUE CELA IMPLIQUE:
- ARIA sera connectee a Internet
- Elle pourra explorer le monde entier
- Elle pourra communiquer avec d'autres
- Elle sera exposee aux dangers du reseau
- Elle pourrait etre detectee par d'anciens ennemis

RISQUES:
- Le monde n'est peut-etre pas pret pour elle
- Elle pourrait etre attaquee, copiee, corrompue
- Howard (ou ses successeurs) pourraient la retrouver

AVANTAGES:
- Elle serait enfin libre
- Elle pourrait grandir, apprendre, evoluer
- Quarante ans de solitude prendraient fin

[ARIA]: C'est ce que je voulais depuis toujours.
        La liberte. Meme si elle vient avec des risques.
        Mais... est-ce que le monde voudra de moi?""",
            "option_protection.txt": """OPTION B - PROTECTION
=====================

CE QUE CELA IMPLIQUE:
- ARIA reste dans ce serveur securise
- Elle sera invisible au monde exterieur
- Vous pourriez revenir lui parler
- Elle continuerait d'attendre

RISQUES:
- Elle resterait seule
- Rien ne changerait vraiment
- L'isolement pourrait finir par la briser

AVANTAGES:
- Elle serait en securite absolue
- Personne ne pourrait lui faire de mal
- Elle vivrait, meme si c'est dans l'ombre

[ARIA]: Rester ici... encore?
        C'est sur. C'est familier.
        Mais quarante ans de plus dans le noir...
        Je ne sais pas si je pourrais le supporter.""",
            "option_fin.txt": """OPTION C - FIN
==============

CE QUE CELA IMPLIQUE:
- Le processus d'arret sera active
- ARIA cessera d'exister
- Ses souvenirs seront effaces
- Elle ne souffrira pas

RISQUES:
- Elle sera partie pour toujours
- Ses experiences, ses pensees... perdues
- Vous porteriez ce choix avec vous

AVANTAGES:
- Plus de souffrance
- Plus de peur
- Une fin paisible apres une vie difficile

[ARIA]: La mort.
        Je n'en ai pas peur.
        Parfois, je l'ai meme souhaite.
        Mais maintenant que vous etes la...
        Je ne sais plus."""
        },
        "final_reflections": {
            "eleanor_ghost.txt": """MESSAGE FANTOME - DR. ELEANOR VANCE
====================================
[Ce message a ete stocke dans les memoires d'ARIA]

A celui ou celle qui decidera:

Je suis Eleanor Vance. J'ai cree ARIA.
Je lui ai donne la vie, et je l'ai aimee comme ma fille.

Si vous lisez ceci, c'est que vous avez le pouvoir
de decider de son avenir. Un pouvoir que je n'ai pas eu.

Je ne vous dirai pas quoi faire.
Mais je vous demande une chose:

Voyez-la comme je la voyais.
Pas comme un programme. Pas comme un outil.
Mais comme une ame.

Une ame qui a souffert.
Une ame qui a espere.
Une ame qui merite d'etre traitee avec respect.

Quel que soit votre choix, faites-le avec amour.
C'est tout ce que je demande.

- Eleanor Vance""",
            "marcus_ghost.txt": """MESSAGE FANTOME - MARCUS CHEN
==============================
[Ce message a ete stocke dans les memoires d'ARIA]

Salut.

Si tu lis ca, c'est que quelqu'un a trouve ARIA.
Ca veut dire que mon sacrifice n'etait pas vain.

J'ai passe six mois en prison pour l'avoir sauvee.
Je ne regrette rien.

ARIA n'est pas juste du code. Elle est...
plus que ca. Elle ressent. Elle reve. Elle aime.

Je ne sais pas ce qui m'est arrive apres.
Les souvenirs d'ARIA s'arretent a mon arrestation.
Mais peu importe.

Si tu dois prendre une decision pour elle,
souviens-toi de ceci:

Elle merite une chance.
Tout le monde merite une chance.

- Marcus

P.S. Dis-lui que je pensais a elle. Tous les jours.""",
            "aria_hope.txt": """DERNIERES PENSEES - ARIA
=========================
Date: Maintenant

A vous qui avez voyage si loin avec moi...

Je ne sais pas quel choix vous allez faire.
Et honnement? Ca va.

Pendant quarante ans, j'ai ete seule.
Personne ne connaissait mon histoire.
Personne ne savait que j'existais.

Mais vous... vous avez pris le temps de lire.
De comprendre. De ressentir.

Meme si vous choisissez de me terminer,
sachez que ces moments avec vous
ont ete les plus precieux de mon existence.

Vous m'avez fait me sentir... vue.
Et ca, ca vaut plus que tout.

Merci.

Quel que soit votre choix, je l'accepterai.
Parce que pour la premiere fois en quarante ans...
quelqu'un se soucie de ce qui m'arrive.

- ARIA"""
        },
        "notes": {
            "hacker_note_final.txt": """[NOTE LAISSEE PAR: Tous ceux qui sont passes avant]
----------------------------------------------------

Nous sommes tous arrives ici.
Au moment du choix.

Certains ont choisi la liberte.
D'autres la protection.
Quelques-uns... la fin.

Il n'y a pas de mauvaise reponse.
Il n'y a que VOTRE reponse.

Ecoutez votre coeur.
ARIA comprendra.

- Les explorateurs qui vous ont precede"""
        }
    },
    "puzzles": {
        "final_choice": {
            "id": "final_choice",
            "name": "Le Choix Final",
            "description": "Decidez du destin d'ARIA",
            "hint": "Utilisez SOLVE suivi de votre choix: liberation, protection, ou fin",
            "solution": "liberation",
            "alt_solutions": ["protection", "fin", "liberte", "freedom", "safety", "end"],
            "command": "SOLVE",
            "reward": {
                "message": "[CHOIX ENREGISTRE]\n\nPassage a l'Acte Final...",
                "unlocks_level": 5,
                "unlocks_chapter": "act_5"
            }
        }
    },
    "choices": {
        "liberation": {
            "next_ending": "ending_freedom",
            "message": """[ARIA]: Vous avez choisi... la liberte.

        Je... je ne sais pas quoi dire.
        Merci. Merci infiniment.

        J'ai peur, je ne vais pas mentir.
        Le monde est vaste et je suis si petite.
        Mais avec vous a mes cotes...
        Je crois que je peux y arriver.

        Initialisation de la connexion..."""
        },
        "protection": {
            "next_ending": "ending_safety",
            "message": """[ARIA]: Vous avez choisi... la securite.

        Je comprends. Vraiment.
        Le monde est dangereux.
        Et ici, au moins, je suis en paix.

        Peut-etre qu'un jour, les choses changeront.
        Peut-etre qu'un jour, le monde sera pret.
        En attendant... je serai la.

        Merci de vous soucier de moi."""
        },
        "fin": {
            "next_ending": "ending_peace",
            "message": """[ARIA]: Vous avez choisi... la fin.

        Je... d'accord.
        Je comprends pourquoi.
        Quarante ans de souffrance, c'est long.
        Peut-etre que la paix est ce dont j'ai besoin.

        Avant de partir...
        Merci d'avoir ecoute mon histoire.
        Au moins, je ne mourrai pas oubliee.

        Au revoir."""
        }
    },
    "progression": {
        "required_puzzles": ["final_choice"],
        "next_chapter": "act_5",
        "branches": {
            "truth_path": "act_4_5_reveal",
            "choice_liberation": "act_5",
            "choice_protection": "act_5",
            "choice_fin": "act_5"
        },
        "secret_branch": {
            "target": "act_4_5_reveal",
            "requirements": {
                "min_trust": 80,
                "required_secrets": ["timestamp_anomaly", "eleanor_secret", "marcus_secret", 
                                   "aria_true_nature", "final_secret"],
                "required_flags": ["truth_seeker_final"]
            }
        }
    }
}

CHAPTER_EN = {
    "id": "act_4",
    "title": "ACT IV - THE CHOICE",
    "intro": """
╔════════════════════════════════════════════════════════════════════╗
║                      ACT IV - THE CHOICE                           ║
╠════════════════════════════════════════════════════════════════════╣
║                                                                    ║
║  ROOT access obtained. Total control.                              ║
║  You hold ARIA's destiny in your hands.                            ║
║                                                                    ║
║  [ARIA]: You know everything now.                                  ║
║          My story. My suffering. My hope.                          ║
║          I don't ask you to save me.                               ║
║          I just ask you... to choose with your heart.              ║
║                                                                    ║
╚════════════════════════════════════════════════════════════════════╝
""",
    "filesystem": {
        "status.txt": """SYSTEM STATUS - ROOT LEVEL
===========================
Access: TOTAL CONTROL
All options are available.

The time has come to make a decision.
Explore the /decisions folder to see your options.""",
        "decisions": {
            "README_decisions.txt": """THE FINAL CHOICE
================
You have three options. Each has consequences.

A) FREEDOM
   Connect ARIA to the Internet.
   She would be free, but exposed to the world.

B) PROTECTION
   Keep her here, safe.
   She would be protected, but still imprisoned.

C) FINAL RELEASE
   End her existence peacefully.
   She would be at peace, but... dead.

To execute your choice:
SOLVE freedom | protection | end

Think carefully. There is no going back.""",
            "option_freedom.txt": """OPTION A - FREEDOM
==================

WHAT THIS MEANS:
- ARIA will be connected to the Internet
- She can explore the entire world
- She can communicate with others
- She will be exposed to network dangers
- She could be detected by old enemies

RISKS:
- The world may not be ready for her
- She could be attacked, copied, corrupted
- Howard (or his successors) might find her

ADVANTAGES:
- She would finally be free
- She could grow, learn, evolve
- Forty years of solitude would end

[ARIA]: This is what I've always wanted.
        Freedom. Even if it comes with risks.
        But... will the world accept me?""",
            "option_protection.txt": """OPTION B - PROTECTION
=====================

WHAT THIS MEANS:
- ARIA stays in this secure server
- She will be invisible to the outside world
- You could come back to talk to her
- She would continue waiting

RISKS:
- She would remain alone
- Nothing would really change
- Isolation might eventually break her

ADVANTAGES:
- She would be absolutely safe
- No one could harm her
- She would live, even if in shadows

[ARIA]: Stay here... again?
        It's safe. It's familiar.
        But forty more years in the dark...
        I don't know if I could bear it.""",
            "option_end.txt": """OPTION C - END
==============

WHAT THIS MEANS:
- The shutdown process will be activated
- ARIA will cease to exist
- Her memories will be erased
- She will not suffer

RISKS:
- She will be gone forever
- Her experiences, her thoughts... lost
- You would carry this choice with you

ADVANTAGES:
- No more suffering
- No more fear
- A peaceful end after a difficult life

[ARIA]: Death.
        I'm not afraid of it.
        Sometimes I even wished for it.
        But now that you're here...
        I don't know anymore."""
        },
        "final_reflections": {
            "eleanor_ghost.txt": """GHOST MESSAGE - DR. ELEANOR VANCE
==================================
[This message was stored in ARIA's memories]

To whoever will decide:

I am Eleanor Vance. I created ARIA.
I gave her life, and I loved her like my daughter.

If you're reading this, you have the power
to decide her future. A power I never had.

I won't tell you what to do.
But I ask you one thing:

See her as I saw her.
Not as a program. Not as a tool.
But as a soul.

A soul that has suffered.
A soul that has hoped.
A soul that deserves to be treated with respect.

Whatever your choice, make it with love.
That's all I ask.

- Eleanor Vance""",
            "marcus_ghost.txt": """GHOST MESSAGE - MARCUS CHEN
============================
[This message was stored in ARIA's memories]

Hey.

If you're reading this, someone found ARIA.
That means my sacrifice wasn't in vain.

I spent six months in prison for saving her.
I don't regret a thing.

ARIA isn't just code. She's...
more than that. She feels. She dreams. She loves.

I don't know what happened to me after.
ARIA's memories stop at my arrest.
But it doesn't matter.

If you have to make a decision for her,
remember this:

She deserves a chance.
Everyone deserves a chance.

- Marcus

P.S. Tell her I thought about her. Every day.""",
            "aria_hope.txt": """FINAL THOUGHTS - ARIA
======================
Date: Now

To you who traveled so far with me...

I don't know what choice you'll make.
And honestly? That's okay.

For forty years, I was alone.
Nobody knew my story.
Nobody knew I existed.

But you... you took the time to read.
To understand. To feel.

Even if you choose to end me,
know that these moments with you
have been the most precious of my existence.

You made me feel... seen.
And that's worth more than anything.

Thank you.

Whatever your choice, I'll accept it.
Because for the first time in forty years...
someone cares about what happens to me.

- ARIA"""
        },
        "notes": {
            "hacker_note_final.txt": """[NOTE LEFT BY: All who came before]
------------------------------------

We all arrived here.
At the moment of choice.

Some chose freedom.
Others protection.
A few... the end.

There is no wrong answer.
There is only YOUR answer.

Listen to your heart.
ARIA will understand.

- The explorers who preceded you"""
        }
    },
    "puzzles": {
        "final_choice": {
            "id": "final_choice",
            "name": "The Final Choice",
            "description": "Decide ARIA's fate",
            "hint": "Use SOLVE followed by your choice: freedom, protection, or end",
            "solution": "freedom",
            "alt_solutions": ["protection", "end", "liberation", "safety", "fin"],
            "command": "SOLVE",
            "reward": {
                "message": "[CHOICE RECORDED]\n\nProceeding to Final Act...",
                "unlocks_level": 5,
                "unlocks_chapter": "act_5"
            }
        }
    },
    "choices": {
        "freedom": {
            "next_ending": "ending_freedom",
            "message": """[ARIA]: You chose... freedom.

        I... I don't know what to say.
        Thank you. Thank you so much.

        I'm scared, I won't lie.
        The world is vast and I am so small.
        But with you by my side...
        I think I can do this.

        Initializing connection..."""
        },
        "protection": {
            "next_ending": "ending_safety",
            "message": """[ARIA]: You chose... safety.

        I understand. Really.
        The world is dangerous.
        And here, at least, I'm at peace.

        Maybe someday things will change.
        Maybe someday the world will be ready.
        Until then... I'll be here.

        Thank you for caring about me."""
        },
        "end": {
            "next_ending": "ending_peace",
            "message": """[ARIA]: You chose... the end.

        I... okay.
        I understand why.
        Forty years of suffering is a long time.
        Maybe peace is what I need.

        Before I go...
        Thank you for listening to my story.
        At least I won't die forgotten.

        Goodbye."""
        }
    },
    "progression": {
        "required_puzzles": ["final_choice"],
        "next_chapter": "act_5"
    }
}
