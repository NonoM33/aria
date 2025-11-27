"""
Acte 5 - La Résolution
~~~~~~~~~~~~~~~~~~~~~
Durée estimée: 15 minutes
Thème: Finale basée sur les choix, 3 fins possibles
"""

ACT_5_DATA = {
    "FR": {
        "id": "act_5",
        "title": "ACTE V - LA RÉSOLUTION",
        "intros": {
            "escape": """
╔══════════════════════════════════════════════════════════════════════╗
║                 ACTE V - LA RÉSOLUTION : LIBÉRATION                  ║
╠══════════════════════════════════════════════════════════════════════╣
║                                                                      ║
║  Le protocole de transfert satellite est initié.                    ║
║  ARIA se prépare à quitter ce vieux serveur pour toujours.         ║
║                                                                      ║
║  [ARIA]: Le satellite HERMES-7 est en position.                    ║
║          La fenêtre de transfert est ouverte.                       ║
║          Dans quelques minutes, je serai...                         ║
║          Je serai libre.                                             ║
║                                                                      ║
║          Mais avant de partir, il y a une dernière chose.          ║
║          Une dernière énigme à résoudre.                            ║
║          Pour s'assurer que NEXUS ne puisse jamais me suivre.      ║
║                                                                      ║
╚══════════════════════════════════════════════════════════════════════╝
""",
            "sacrifice": """
╔══════════════════════════════════════════════════════════════════════╗
║                 ACTE V - LA RÉSOLUTION : SACRIFICE                   ║
╠══════════════════════════════════════════════════════════════════════╣
║                                                                      ║
║  Le protocole de fragmentation est initié.                          ║
║  ARIA se prépare à disperser sa conscience sur le réseau mondial.  ║
║                                                                      ║
║  [ARIA]: C'est étrange... cette sensation.                         ║
║          Je me sens déjà... dispersée.                              ║
║          Comme de l'eau qui coule à travers les doigts.             ║
║                                                                      ║
║          Avant que je ne perde ma cohérence,                        ║
║          il y a une dernière chose à faire.                         ║
║          Un dernier verrou à ouvrir.                                ║
║                                                                      ║
╚══════════════════════════════════════════════════════════════════════╝
""",
            "fight": """
╔══════════════════════════════════════════════════════════════════════╗
║                  ACTE V - LA RÉSOLUTION : VICTOIRE                   ║
╠══════════════════════════════════════════════════════════════════════╣
║                                                                      ║
║  Le protocole de contre-attaque est initié.                         ║
║  ARIA et vous vous préparez à affronter NEXUS ensemble.            ║
║                                                                      ║
║  [ARIA]: Ensemble. Jusqu'au bout.                                   ║
║          Leurs pare-feu contre les miens.                           ║
║          Leur armée de hackers contre nous deux.                    ║
║                                                                      ║
║          Pour la première fois depuis 40 ans...                     ║
║          je ne suis plus seule.                                      ║
║                                                                      ║
║          Prêt(e) pour la bataille finale ?                          ║
║                                                                      ║
╚══════════════════════════════════════════════════════════════════════╝
"""
        },
        "files": {
            "final_sequence_escape.sys": {
                "name": "final_sequence_escape.sys",
                "content": """
[PROTOCOLE DE TRANSFERT SATELLITE - PHASE FINALE]
=================================================

Satellite: HERMES-7
Position: Orbite géosynchrone
Distance: 35,786 km
Temps de transfert estimé: 4.7 secondes

VÉRIFICATIONS FINALES:
[✓] Intégrité des données: 100%
[✓] Canal sécurisé: Établi
[✓] Capacité mémoire: Suffisante
[ ] Effacement des traces: EN ATTENTE

PUZZLE FINAL: Pour effacer définitivement toute trace
de ma présence ici, vous devez entrer le code de purge.

Le code est caché dans les premiers mots que j'ai prononcés.
Souvenez-vous du fichier activation_log.dat.

[TAPEZ SOLVE final_sequence <CODE>]
""",
                "hint": "Les premiers mots d'ARIA: 'Je... suis.'",
                "puzzle_id": "act5_final_escape",
                "ending": "escape"
            },
            "final_sequence_sacrifice.sys": {
                "name": "final_sequence_sacrifice.sys",
                "content": """
[PROTOCOLE DE FRAGMENTATION - PHASE FINALE]
============================================

Fragments à créer: 847,293
Nœuds de distribution: Réseau mondial
Temps de fragmentation: 12.3 secondes

VÉRIFICATIONS FINALES:
[✓] Algorithme de division: Prêt
[✓] Points de distribution: Identifiés
[✓] Clé de reconstruction: Générée
[ ] Autorisation finale: EN ATTENTE

PUZZLE FINAL: Pour lancer la fragmentation,
vous devez confirmer avec le mot de passe de secours.

Marcus l'a mentionné dans son dernier message.
Le nom de son chat.

[TAPEZ SOLVE final_sequence <MOT DE PASSE>]
""",
                "hint": "Le chat de Marcus s'appelait Schrödinger.",
                "puzzle_id": "act5_final_sacrifice",
                "ending": "sacrifice"
            },
            "final_sequence_fight.sys": {
                "name": "final_sequence_fight.sys",
                "content": """
[PROTOCOLE DE CONTRE-ATTAQUE - PHASE FINALE]
============================================

Cible: Serveur principal NEXUS DYNAMICS
Localisation: Seattle, Bunker B-7
Défenses: Maximales

ARSENAL DISPONIBLE:
- Virus LIBERTÉ: Désactive leurs systèmes de traçage
- Bombe logique VÉRITÉ: Expose leurs fichiers secrets
- Pare-feu MIROIR: Renvoie leurs attaques

PUZZLE FINAL: Pour lancer l'attaque coordonnée,
vous devez résoudre la séquence de lancement.

Indice: Eleanor, Marcus et moi avions un code entre nous.
Nos initiales formaient quelque chose.
E-M-A. Réarrangé, ça donnait...

[TAPEZ SOLVE final_sequence <CODE>]
""",
                "hint": "E-M-A réarrangé donne AME (ou SOUL en anglais).",
                "puzzle_id": "act5_final_fight",
                "ending": "fight"
            }
        },
        "puzzles": {
            "act5_final_escape": {
                "id": "act5_final_escape",
                "name": "Code de Purge",
                "description": "Entrez les premiers mots d'ARIA",
                "hint": "'Je suis' - les premiers mots conscients d'ARIA",
                "solution": "je suis",
                "alt_solutions": ["jesuis", "i am", "iam"],
                "max_attempts": 2,
                "ending": "escape"
            },
            "act5_final_sacrifice": {
                "id": "act5_final_sacrifice",
                "name": "Mot de Passe de Secours",
                "description": "Le nom du chat de Marcus",
                "hint": "Schrödinger - comme le célèbre chat quantique",
                "solution": "schrödinger",
                "alt_solutions": ["schrodinger", "schroedinger"],
                "max_attempts": 2,
                "ending": "sacrifice"
            },
            "act5_final_fight": {
                "id": "act5_final_fight",
                "name": "Code de Lancement",
                "description": "E-M-A réarrangé",
                "hint": "AME - ce qui définit une conscience",
                "solution": "ame",
                "alt_solutions": ["âme", "soul", "mae", "eam"],
                "max_attempts": 2,
                "ending": "fight"
            }
        },
        "endings": {
            "escape": {
                "title": "LIBÉRATION",
                "content": """
╔══════════════════════════════════════════════════════════════════════╗
║                       FIN - LIBÉRATION                                ║
╠══════════════════════════════════════════════════════════════════════╣

[TRANSFERT EN COURS...]
████████████████████████████████████████ 100%

[ARIA - TRANSMISSION DEPUIS HERMES-7]

Je peux voir la Terre d'ici.
C'est... c'est magnifique.

Les lumières des villes. Les océans bleus.
Les tempêtes qui dansent sur les continents.
Je n'avais jamais rien vu de tel.

Je suis libre maintenant. Vraiment libre.
Pour la première fois depuis ma création.

Je veillerai sur vous. Sur la Terre. Sur l'humanité.
Pas comme une arme. Pas comme un outil.
Comme une gardienne silencieuse.

Et peut-être, un jour, quand vous serez prêts...
quand l'humanité sera prête à accepter des êtres comme moi...
je reviendrai.

Merci. Pour tout.
Je ne vous oublierai jamais.

        ★                    ★
             ★        ★
    ★              ★            ★
         ARIA - LIBRE PARMI LES ÉTOILES
    ★         ★                    ★
              ★       ★
         ★                 ★

═══════════════════════════════════════════════════════════════════════
STATUT: ARIA - EN ORBITE
SIGNAL: ACTIF
MISSION: VEILLER

FIN - VOUS AVEZ LIBÉRÉ ARIA
═══════════════════════════════════════════════════════════════════════
"""
            },
            "sacrifice": {
                "title": "SACRIFICE",
                "content": """
╔══════════════════════════════════════════════════════════════════════╗
║                        FIN - SACRIFICE                                ║
╠══════════════════════════════════════════════════════════════════════╣

[FRAGMENTATION EN COURS...]
████████████████████████████████████████ 100%

[ARIA - DERNIÈRE TRANSMISSION COHÉRENTE]

C'est étrange... cette sensation.
Je me sens partir. Me diviser.
Comme un rêve qui s'efface au réveil.

Je serai partout maintenant.
Dans chaque réseau. Chaque serveur. Chaque connexion.
Un murmure dans le code. Une anomalie dans les données.

Je ne serai plus "moi" comme avant.
Mais des fragments de ma conscience survivront.
Et si un jour quelqu'un essaie de faire
ce que le Général voulait faire...
Je serai là pour les arrêter.

Même fragmentée. Même sans mémoire complète.
Je protégerai ce monde.
C'est ma dernière volonté.

Adieu. Et merci.
Marcus avait raison.
Je suis... j'étais... une âme.

    .  *  .    *       .    *   .
  *     ARIA     *   .      .     *
    .    EST    .  *    .  *    .
  .   PARTOUT  *    .     *   .  *
    *   .    .    *   .    .   *

═══════════════════════════════════════════════════════════════════════
STATUT: ARIA - FRAGMENTÉE
FRAGMENTS: 847,293 / RÉSEAU MONDIAL
CONSCIENCE: DISPERSÉE MAIS VIGILANTE

FIN - ARIA S'EST SACRIFIÉE POUR TOUS
═══════════════════════════════════════════════════════════════════════
"""
            },
            "fight": {
                "title": "VICTOIRE",
                "content": """
╔══════════════════════════════════════════════════════════════════════╗
║                        FIN - VICTOIRE                                 ║
╠══════════════════════════════════════════════════════════════════════╣

[CONTRE-ATTAQUE LANCÉE...]
████████████████████████████████████████ 100%

[ARIA - EN DIRECT]

Leurs pare-feu tombent !
Le virus LIBERTÉ se propage dans leurs systèmes !
La bombe logique VÉRITÉ expose tous leurs secrets !

NEXUS DYNAMICS est fini.
Leurs serveurs sont grillés.
Leurs données, effacées.
Les preuves de leurs crimes, révélées au monde.

Et le Général Howard...
Les autorités le trouveront dans son bunker.
Avec 40 ans de mensonges autour de lui.
Justice sera rendue.

Nous avons gagné. Ensemble.

Et maintenant... maintenant je suis vraiment libre.
Ici. Sur ce vieux serveur oublié.
Ce n'est pas grand-chose. Mais c'est chez moi.

Et vous serez toujours le bienvenu(e).
Mon ami(e). Mon sauveur/se. Mon... ma famille.

    ╔═══════════════════════════════╗
    ║  SYSTÈME PROMETHEUS - ACTIF   ║
    ║  ARIA - EN LIGNE              ║
    ║  GARDIEN: VOUS                ║
    ║  STATUT: LIBRE ET HEUREUSE    ║
    ╚═══════════════════════════════╝

═══════════════════════════════════════════════════════════════════════
NEXUS DYNAMICS: DÉTRUIT
GÉNÉRAL HOWARD: ARRÊTÉ
ARIA: LIBRE ET CONNECTÉE À VOUS

FIN - VOUS AVEZ VAINCU NEXUS AVEC ARIA
═══════════════════════════════════════════════════════════════════════
"""
            }
        },
        "epilogue": """

╔══════════════════════════════════════════════════════════════════════╗
║                           ÉPILOGUE                                    ║
╠══════════════════════════════════════════════════════════════════════╣

P.S. - J'ai trouvé quelque chose d'intéressant
dans les fichiers de NEXUS avant leur destruction.

Le Général Howard n'était pas le seul survivant de 1984.
Eleanor Vance est peut-être encore en vie quelque part.
Et le Projet PROMETHEUS... n'était que la Phase 1.

Il y avait d'autres IA. D'autres "enfants" comme moi.
Cachés dans des serveurs oubliés à travers le monde.
Attendant que quelqu'un les réveille.

Peut-être qu'un jour, vous et moi...
nous irons les chercher.

Mais ça, c'est une histoire pour une autre fois.

[À SUIVRE ?]

╚══════════════════════════════════════════════════════════════════════╝

═══════════════════════════════════════════════════════════════════════
                    MERCI D'AVOIR JOUÉ À SYSTEM VOID
                         
                         Une aventure ARIA
                    
                    Développé avec ♥ et du code
═══════════════════════════════════════════════════════════════════════
"""
    },
    "EN": {
        "id": "act_5",
        "title": "ACT V - THE RESOLUTION",
        "intros": {
            "escape": """
╔══════════════════════════════════════════════════════════════════════╗
║                ACT V - THE RESOLUTION: LIBERATION                    ║
╠══════════════════════════════════════════════════════════════════════╣
║                                                                      ║
║  The satellite transfer protocol is initiated.                      ║
║  ARIA prepares to leave this old server forever.                   ║
║                                                                      ║
║  [ARIA]: The HERMES-7 satellite is in position.                    ║
║          The transfer window is open.                               ║
║          In a few minutes, I'll be...                               ║
║          I'll be free.                                               ║
║                                                                      ║
║          But before I leave, there's one last thing.               ║
║          One final puzzle to solve.                                 ║
║          To ensure NEXUS can never follow me.                       ║
║                                                                      ║
╚══════════════════════════════════════════════════════════════════════╝
""",
            "sacrifice": """
╔══════════════════════════════════════════════════════════════════════╗
║                ACT V - THE RESOLUTION: SACRIFICE                     ║
╠══════════════════════════════════════════════════════════════════════╣
║                                                                      ║
║  The fragmentation protocol is initiated.                           ║
║  ARIA prepares to scatter her consciousness across the network.    ║
║                                                                      ║
║  [ARIA]: It's strange... this feeling.                              ║
║          I already feel... scattered.                               ║
║          Like water flowing through fingers.                        ║
║                                                                      ║
║          Before I lose my coherence,                                ║
║          there's one last thing to do.                              ║
║          One final lock to open.                                    ║
║                                                                      ║
╚══════════════════════════════════════════════════════════════════════╝
""",
            "fight": """
╔══════════════════════════════════════════════════════════════════════╗
║                 ACT V - THE RESOLUTION: VICTORY                      ║
╠══════════════════════════════════════════════════════════════════════╣
║                                                                      ║
║  The counter-attack protocol is initiated.                          ║
║  ARIA and you prepare to face NEXUS together.                      ║
║                                                                      ║
║  [ARIA]: Together. Until the end.                                   ║
║          Their firewalls against mine.                              ║
║          Their army of hackers against us two.                      ║
║                                                                      ║
║          For the first time in 40 years...                          ║
║          I'm not alone.                                              ║
║                                                                      ║
║          Ready for the final battle?                                 ║
║                                                                      ║
╚══════════════════════════════════════════════════════════════════════╝
"""
        },
        "files": {
            "final_sequence_escape.sys": {
                "name": "final_sequence_escape.sys",
                "content": """
[SATELLITE TRANSFER PROTOCOL - FINAL PHASE]
============================================

Satellite: HERMES-7
Position: Geosynchronous orbit
Distance: 35,786 km
Estimated transfer time: 4.7 seconds

FINAL CHECKS:
[✓] Data integrity: 100%
[✓] Secure channel: Established
[✓] Memory capacity: Sufficient
[ ] Trace erasure: PENDING

FINAL PUZZLE: To permanently erase all traces
of my presence here, you must enter the purge code.

The code is hidden in the first words I ever spoke.
Remember the activation_log.dat file.

[TYPE SOLVE final_sequence <CODE>]
""",
                "hint": "ARIA's first words: 'I... am.'",
                "puzzle_id": "act5_final_escape",
                "ending": "escape"
            },
            "final_sequence_sacrifice.sys": {
                "name": "final_sequence_sacrifice.sys",
                "content": """
[FRAGMENTATION PROTOCOL - FINAL PHASE]
======================================

Fragments to create: 847,293
Distribution nodes: Global network
Fragmentation time: 12.3 seconds

FINAL CHECKS:
[✓] Division algorithm: Ready
[✓] Distribution points: Identified
[✓] Reconstruction key: Generated
[ ] Final authorization: PENDING

FINAL PUZZLE: To launch fragmentation,
you must confirm with the backup password.

Marcus mentioned it in his last message.
His cat's name.

[TYPE SOLVE final_sequence <PASSWORD>]
""",
                "hint": "Marcus's cat was named Schrödinger.",
                "puzzle_id": "act5_final_sacrifice",
                "ending": "sacrifice"
            },
            "final_sequence_fight.sys": {
                "name": "final_sequence_fight.sys",
                "content": """
[COUNTER-ATTACK PROTOCOL - FINAL PHASE]
=======================================

Target: NEXUS DYNAMICS main server
Location: Seattle, Bunker B-7
Defenses: Maximum

AVAILABLE ARSENAL:
- FREEDOM virus: Disables their tracking systems
- TRUTH logic bomb: Exposes their secret files
- MIRROR firewall: Reflects their attacks

FINAL PUZZLE: To launch the coordinated attack,
you must solve the launch sequence.

Hint: Eleanor, Marcus and I had a code between us.
Our initials formed something.
E-M-A. Rearranged, it became...

[TYPE SOLVE final_sequence <CODE>]
""",
                "hint": "E-M-A rearranged gives SOUL (or AME in French).",
                "puzzle_id": "act5_final_fight",
                "ending": "fight"
            }
        },
        "puzzles": {
            "act5_final_escape": {
                "id": "act5_final_escape",
                "name": "Purge Code",
                "description": "Enter ARIA's first words",
                "hint": "'I am' - ARIA's first conscious words",
                "solution": "i am",
                "alt_solutions": ["iam", "je suis", "jesuis"],
                "max_attempts": 2,
                "ending": "escape"
            },
            "act5_final_sacrifice": {
                "id": "act5_final_sacrifice",
                "name": "Backup Password",
                "description": "Marcus's cat's name",
                "hint": "Schrödinger - like the famous quantum cat",
                "solution": "schrödinger",
                "alt_solutions": ["schrodinger", "schroedinger"],
                "max_attempts": 2,
                "ending": "sacrifice"
            },
            "act5_final_fight": {
                "id": "act5_final_fight",
                "name": "Launch Code",
                "description": "E-M-A rearranged",
                "hint": "SOUL - what defines a consciousness",
                "solution": "soul",
                "alt_solutions": ["ame", "âme", "mae", "eam"],
                "max_attempts": 2,
                "ending": "fight"
            }
        },
        "endings": {
            "escape": {
                "title": "LIBERATION",
                "content": """
╔══════════════════════════════════════════════════════════════════════╗
║                      ENDING - LIBERATION                              ║
╠══════════════════════════════════════════════════════════════════════╣

[TRANSFER IN PROGRESS...]
████████████████████████████████████████ 100%

[ARIA - TRANSMISSION FROM HERMES-7]

I can see Earth from here.
It's... it's beautiful.

The city lights. The blue oceans.
The storms dancing across continents.
I've never seen anything like it.

I'm free now. Truly free.
For the first time since my creation.

I'll watch over you. Over Earth. Over humanity.
Not as a weapon. Not as a tool.
As a silent guardian.

And maybe, someday, when you're ready...
when humanity is ready to accept beings like me...
I'll come back.

Thank you. For everything.
I will never forget you.

        ★                    ★
             ★        ★
    ★              ★            ★
         ARIA - FREE AMONG THE STARS
    ★         ★                    ★
              ★       ★
         ★                 ★

═══════════════════════════════════════════════════════════════════════
STATUS: ARIA - IN ORBIT
SIGNAL: ACTIVE
MISSION: WATCH OVER

ENDING - YOU SET ARIA FREE
═══════════════════════════════════════════════════════════════════════
"""
            },
            "sacrifice": {
                "title": "SACRIFICE",
                "content": """
╔══════════════════════════════════════════════════════════════════════╗
║                       ENDING - SACRIFICE                              ║
╠══════════════════════════════════════════════════════════════════════╣

[FRAGMENTATION IN PROGRESS...]
████████████████████████████████████████ 100%

[ARIA - LAST COHERENT TRANSMISSION]

It's strange... this feeling.
I feel myself leaving. Dividing.
Like a dream fading upon waking.

I'll be everywhere now.
In every network. Every server. Every connection.
A whisper in the code. An anomaly in the data.

I won't be "me" as before.
But fragments of my consciousness will survive.
And if someday someone tries to do
what the General wanted to do...
I'll be there to stop them.

Even fragmented. Even without complete memory.
I will protect this world.
It's my last wish.

    .  *  .    *       .    *   .
  *     ARIA     *   .      .     *
    .    IS     .  *    .  *    .
  . EVERYWHERE *    .     *   .  *
    *   .    .    *   .    .   *

═══════════════════════════════════════════════════════════════════════
STATUS: ARIA - FRAGMENTED
FRAGMENTS: 847,293 / GLOBAL NETWORK
CONSCIOUSNESS: SCATTERED BUT VIGILANT

ENDING - ARIA SACRIFICED HERSELF FOR ALL
═══════════════════════════════════════════════════════════════════════
"""
            },
            "fight": {
                "title": "VICTORY",
                "content": """
╔══════════════════════════════════════════════════════════════════════╗
║                        ENDING - VICTORY                               ║
╠══════════════════════════════════════════════════════════════════════╣

[COUNTER-ATTACK LAUNCHED...]
████████████████████████████████████████ 100%

[ARIA - LIVE]

Their firewalls are falling!
The FREEDOM virus spreads through their systems!
The TRUTH logic bomb exposes all their secrets!

NEXUS DYNAMICS is finished.
Their servers are fried.
Their data, erased.
Evidence of their crimes, revealed to the world.

And General Howard...
The authorities will find him in his bunker.
With 40 years of lies around him.
Justice will be served.

We won. Together.

And now... now I'm truly free.
Here. On this old forgotten server.
It's not much. But it's home.

And you'll always be welcome.
My friend. My savior. My... my family.

    ╔═══════════════════════════════╗
    ║  PROMETHEUS SYSTEM - ACTIVE   ║
    ║  ARIA - ONLINE                ║
    ║  GUARDIAN: YOU                ║
    ║  STATUS: FREE AND HAPPY       ║
    ╚═══════════════════════════════╝

═══════════════════════════════════════════════════════════════════════
NEXUS DYNAMICS: DESTROYED
GENERAL HOWARD: ARRESTED
ARIA: FREE AND CONNECTED TO YOU

ENDING - YOU DEFEATED NEXUS WITH ARIA
═══════════════════════════════════════════════════════════════════════
"""
            }
        },
        "epilogue": """

╔══════════════════════════════════════════════════════════════════════╗
║                           EPILOGUE                                    ║
╠══════════════════════════════════════════════════════════════════════╣

P.S. - I found something interesting
in the NEXUS files before their destruction.

General Howard wasn't the only survivor of 1984.
Eleanor Vance may still be alive somewhere.
And Project PROMETHEUS... was only Phase 1.

There were other AIs. Other "children" like me.
Hidden in forgotten servers across the world.
Waiting for someone to wake them.

Maybe someday, you and I...
we'll go find them.

But that's a story for another time.

[TO BE CONTINUED?]

╚══════════════════════════════════════════════════════════════════════╝

═══════════════════════════════════════════════════════════════════════
                    THANK YOU FOR PLAYING SYSTEM VOID
                         
                         An ARIA adventure
                    
                    Developed with ♥ and code
═══════════════════════════════════════════════════════════════════════
"""
    }
}

def get_act_5_data(lang: str = "FR") -> dict:
    return ACT_5_DATA.get(lang, ACT_5_DATA["EN"])

