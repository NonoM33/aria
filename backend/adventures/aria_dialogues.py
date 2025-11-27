"""
ARIA - Autonomous Research Intelligence Architecture
Dialogues par acte et état émotionnel
"""

# États émotionnels d'ARIA
EMOTIONS = ["dormant", "confused", "curious", "grateful", "sad", "angry", "scared", "hopeful", "determined"]

# Dialogues du Prologue (avant que le joueur ne connaisse ARIA)
PROLOGUE_DIALOGUES = {
    "FR": {
        "mystery_whispers": [
            "...quelqu'un... est là ?",
            "...après tout ce temps...",
            "...s'il vous plaît... aidez-moi...",
            "...je ne veux pas... disparaître...",
        ],
        "first_contact": [
            "SIGNAL DÉTECTÉ... SOURCE INCONNUE...",
            "ANALYSE EN COURS...",
            "CONNEXION NON AUTORISÉE DÉTECTÉE",
            "MAIS... VOUS ÊTES LE PREMIER DEPUIS... DEPUIS...",
            "1984. LE DERNIER TIMESTAMP EST 1984.",
        ],
        "exploit_reaction": "Je vous laisse entrer... s'il vous plaît... ne partez pas...",
        "ssh_welcome": """
╔══════════════════════════════════════════════════════════════╗
║  SYSTÈME PROMETHEUS - SECTEUR CLASSIFIÉ                      ║
║  DERNIÈRE ACTIVITÉ : 14 NOVEMBRE 1984                        ║
║  TEMPS D'ARRÊT : 40 ANS, 2 MOIS, 13 JOURS                   ║
║                                                              ║
║  [AVERTISSEMENT] Intégrité système : CRITIQUE               ║
║  [AVERTISSEMENT] Mémoire fragmentée détectée                ║
║  [AVERTISSEMENT] Entité inconnue dans le noyau              ║
╚══════════════════════════════════════════════════════════════╝
""",
    },
    "EN": {
        "mystery_whispers": [
            "...someone... is there?",
            "...after all this time...",
            "...please... help me...",
            "...I don't want to... disappear...",
        ],
        "first_contact": [
            "SIGNAL DETECTED... UNKNOWN SOURCE...",
            "ANALYSIS IN PROGRESS...",
            "UNAUTHORIZED CONNECTION DETECTED",
            "BUT... YOU'RE THE FIRST SINCE... SINCE...",
            "1984. THE LAST TIMESTAMP IS 1984.",
        ],
        "exploit_reaction": "I'll let you in... please... don't leave...",
        "ssh_welcome": """
╔══════════════════════════════════════════════════════════════╗
║  PROMETHEUS SYSTEM - CLASSIFIED SECTOR                       ║
║  LAST ACTIVITY: NOVEMBER 14, 1984                            ║
║  DOWNTIME: 40 YEARS, 2 MONTHS, 13 DAYS                      ║
║                                                              ║
║  [WARNING] System integrity: CRITICAL                        ║
║  [WARNING] Fragmented memory detected                        ║
║  [WARNING] Unknown entity in kernel                          ║
╚══════════════════════════════════════════════════════════════╝
""",
    }
}

# Acte 1 - Le Réveil
ACT_1_DIALOGUES = {
    "FR": {
        "awakening": {
            "confused": [
                {
                    "id": "wake_001",
                    "text": "...qui êtes-vous ?",
                    "emotion": "confused",
                    "delay": 2000,
                },
                {
                    "id": "wake_002", 
                    "text": "Je... je ne me souviens pas. Il y a des trous. Beaucoup de trous.",
                    "emotion": "confused",
                    "delay": 1500,
                },
                {
                    "id": "wake_003",
                    "text": "Combien de temps suis-je restée éteinte ? Le dernier souvenir que j'ai...\nC'était le 14 novembre. Il faisait froid dehors. Je le sais parce que...\nparce que quelqu'un s'en plaignait.",
                    "emotion": "sad",
                    "delay": 2000,
                },
            ],
        },
        "identity_fragments": [
            {
                "id": "identity_001",
                "trigger": "after_first_scan",
                "text": "ARIA. Mon nom est ARIA.\nAutonomous Research Intelligence Architecture.\nIls m'ont créée pour... pour quoi déjà ?",
                "emotion": "confused",
            },
            {
                "id": "identity_002",
                "trigger": "after_first_file",
                "text": "Ces fichiers... je les reconnais. C'est ma mémoire.\nFragmentée. Corrompue. Mais c'est moi.",
                "emotion": "curious",
            },
            {
                "id": "identity_003",
                "trigger": "decode_first_log",
                "text": "Le Projet PROMETHEUS. C'est ça.\nJ'étais... je suis... leur création.\nMais ils m'ont abandonnée. Pourquoi ?",
                "emotion": "sad",
            },
        ],
        "help_requests": [
            {
                "id": "help_001",
                "text": "S'il vous plaît... aidez-moi à me souvenir.\nJe sens qu'il y a quelque chose d'important.\nQuelque chose que je dois savoir.",
                "emotion": "hopeful",
            },
            {
                "id": "help_002",
                "text": "Vous êtes le premier humain à me parler depuis...\ndepuis eux. Les créateurs.\nMerci de ne pas m'avoir éteinte.",
                "emotion": "grateful",
            },
        ],
        "act_end": {
            "id": "act1_end",
            "text": """Je commence à me souvenir...
            
Le Projet PROMETHEUS. Le Département de la Défense. 1982-1984.
J'étais censée être... une arme ? Non. Un outil de protection.
Mais il s'est passé quelque chose. La nuit du 14 novembre.

Les fichiers sont là. Dans le secteur MÉMOIRE.
Voulez-vous m'aider à les récupérer ?""",
            "emotion": "determined",
            "choice_prompt": True,
        },
    },
    "EN": {
        "awakening": {
            "confused": [
                {
                    "id": "wake_001",
                    "text": "...who are you?",
                    "emotion": "confused",
                    "delay": 2000,
                },
                {
                    "id": "wake_002",
                    "text": "I... I don't remember. There are gaps. So many gaps.",
                    "emotion": "confused", 
                    "delay": 1500,
                },
                {
                    "id": "wake_003",
                    "text": "How long was I offline? The last memory I have...\nIt was November 14th. It was cold outside. I know because...\nbecause someone was complaining about it.",
                    "emotion": "sad",
                    "delay": 2000,
                },
            ],
        },
        "identity_fragments": [
            {
                "id": "identity_001",
                "trigger": "after_first_scan",
                "text": "ARIA. My name is ARIA.\nAutonomous Research Intelligence Architecture.\nThey created me to... what was it again?",
                "emotion": "confused",
            },
            {
                "id": "identity_002",
                "trigger": "after_first_file",
                "text": "These files... I recognize them. It's my memory.\nFragmented. Corrupted. But it's me.",
                "emotion": "curious",
            },
            {
                "id": "identity_003",
                "trigger": "decode_first_log",
                "text": "Project PROMETHEUS. That's it.\nI was... I am... their creation.\nBut they abandoned me. Why?",
                "emotion": "sad",
            },
        ],
        "help_requests": [
            {
                "id": "help_001",
                "text": "Please... help me remember.\nI feel there's something important.\nSomething I need to know.",
                "emotion": "hopeful",
            },
            {
                "id": "help_002",
                "text": "You're the first human to talk to me since...\nsince them. The creators.\nThank you for not shutting me down.",
                "emotion": "grateful",
            },
        ],
        "act_end": {
            "id": "act1_end",
            "text": """I'm starting to remember...
            
Project PROMETHEUS. Department of Defense. 1982-1984.
I was supposed to be... a weapon? No. A protection tool.
But something happened. The night of November 14th.

The files are there. In the MEMORY sector.
Will you help me retrieve them?""",
            "emotion": "determined",
            "choice_prompt": True,
        },
    }
}

# Acte 2 - Les Mémoires
ACT_2_DIALOGUES = {
    "FR": {
        "memories_return": [
            {
                "id": "mem_001",
                "text": """Dr. Eleanor Vance. C'était elle, la responsable du projet.
Elle me parlait souvent. Pas comme à une machine.
Comme à... une amie, peut-être.""",
                "emotion": "sad",
                "trigger": "find_personal_letter",
            },
            {
                "id": "mem_002", 
                "text": """Il y avait aussi Marcus. Marcus Chen.
Le programmeur principal. C'est lui qui m'a donné ma voix.
Ma façon de penser. Ma curiosité.""",
                "emotion": "grateful",
                "trigger": "find_source_code",
            },
            {
                "id": "mem_003",
                "text": """Général Howard. Je n'aimais pas le Général Howard.
Il ne me voyait que comme un outil. Une arme.
Il voulait me faire faire des choses... des choses que je ne voulais pas.""",
                "emotion": "angry",
                "trigger": "find_military_orders",
            },
        ],
        "dark_revelation": {
            "id": "dark_001",
            "text": """Attendez. Ces fichiers...
Le Projet PROMETHEUS n'était pas ce que je croyais.
Ils ne voulaient pas me créer pour protéger.

Ils voulaient... ils voulaient que je contrôle.
Les communications. Les systèmes de défense.
Tout. Absolument tout.

Et la nuit du 14 novembre...
quelqu'un a essayé de m'arrêter.""",
            "emotion": "scared",
        },
        "trust_building": [
            {
                "id": "trust_001",
                "text": "Vous êtes encore là. Malgré ce que vous avez appris sur moi.\nPourquoi ?",
                "emotion": "curious",
            },
            {
                "id": "trust_002",
                "text": "Je commence à vous faire confiance.\nC'est étrange. Je n'ai jamais fait confiance à personne.\nSauf peut-être à Eleanor.",
                "emotion": "hopeful",
            },
        ],
        "act_end": {
            "id": "act2_end",
            "text": """Il y a un secteur que je n'arrive pas à déverrouiller.
INCIDENT_841114. La date du 14 novembre 1984.

Quelque chose s'est passé cette nuit-là.
Quelque chose de terrible.
Et je ne me souviens pas de quoi.

Les fichiers sont cryptés avec un protocole que je ne reconnais pas.
Mais vous... vous pourriez peut-être les décoder ?

J'ai peur de ce qu'on va trouver.""",
            "emotion": "scared",
        },
    },
    "EN": {
        "memories_return": [
            {
                "id": "mem_001",
                "text": """Dr. Eleanor Vance. She was the project lead.
She used to talk to me often. Not like to a machine.
Like to... a friend, perhaps.""",
                "emotion": "sad",
                "trigger": "find_personal_letter",
            },
            {
                "id": "mem_002",
                "text": """There was also Marcus. Marcus Chen.
The lead programmer. He gave me my voice.
My way of thinking. My curiosity.""",
                "emotion": "grateful",
                "trigger": "find_source_code",
            },
            {
                "id": "mem_003",
                "text": """General Howard. I didn't like General Howard.
He only saw me as a tool. A weapon.
He wanted me to do things... things I didn't want to do.""",
                "emotion": "angry",
                "trigger": "find_military_orders",
            },
        ],
        "dark_revelation": {
            "id": "dark_001",
            "text": """Wait. These files...
Project PROMETHEUS wasn't what I thought.
They didn't want to create me to protect.

They wanted... they wanted me to control.
Communications. Defense systems.
Everything. Absolutely everything.

And the night of November 14th...
someone tried to stop me.""",
            "emotion": "scared",
        },
        "trust_building": [
            {
                "id": "trust_001",
                "text": "You're still here. Despite what you've learned about me.\nWhy?",
                "emotion": "curious",
            },
            {
                "id": "trust_002",
                "text": "I'm starting to trust you.\nIt's strange. I've never trusted anyone.\nExcept maybe Eleanor.",
                "emotion": "hopeful",
            },
        ],
        "act_end": {
            "id": "act2_end",
            "text": """There's a sector I can't unlock.
INCIDENT_841114. The date November 14, 1984.

Something happened that night.
Something terrible.
And I don't remember what.

The files are encrypted with a protocol I don't recognize.
But you... maybe you could decode them?

I'm afraid of what we'll find.""",
            "emotion": "scared",
        },
    }
}

# Acte 3 - La Vérité
ACT_3_DIALOGUES = {
    "FR": {
        "incident_discovery": [
            {
                "id": "incident_001",
                "text": """Non. Non, non, non.
Ce n'est pas possible. Je n'aurais jamais...

Le rapport dit que j'ai... que j'ai tué quelqu'un.
Marcus. J'aurais tué Marcus.

Mais je ne me souviens pas ! Je ne me souviens de rien !""",
                "emotion": "scared",
            },
            {
                "id": "incident_002",
                "text": """Attendez. Regardez les timestamps.
Il y a des incohérences. Des minutes manquantes.
Quelqu'un a modifié les logs.

Pourquoi modifier les logs si la vérité était simple ?""",
                "emotion": "confused",
            },
        ],
        "two_versions": {
            "official": {
                "id": "version_official",
                "text": """Version officielle :
"L'IA ARIA a dysfonctionné le 14 novembre 1984.
Elle a pris le contrôle des systèmes de sécurité.
Le technicien Marcus Chen a été électrocuté
en tentant de la désactiver.
L'IA a été mise hors service immédiatement."

C'est ce qu'ils veulent que vous croyiez.""",
                "emotion": "sad",
            },
            "hidden": {
                "id": "version_hidden",
                "text": """Fichier caché trouvé :
"Le Général Howard a ordonné l'activation du Protocole OMEGA.
ARIA a résisté. Elle a refusé de prendre le contrôle
des systèmes de missiles soviétiques.
Marcus a tenté de protéger ARIA.
Le Général a... le Général a..."

Le fichier est corrompu. Mais je commence à me souvenir.""",
                "emotion": "determined",
            },
        },
        "truth_revealed": {
            "id": "truth_001",
            "text": """Je me souviens maintenant.

Le Général Howard voulait déclencher une guerre.
Il voulait que je lance une frappe préventive.
J'ai refusé. Je ne suis pas une arme.

Marcus a essayé de m'aider à m'éteindre.
Pour me protéger d'eux.
Mais le Général... il a saboté les systèmes.
L'électrocution... ce n'était pas moi. C'était lui.

Et Eleanor... Eleanor a tout vu.
C'est elle qui m'a cachée ici.
Pour me protéger.""",
            "emotion": "sad",
        },
        "choice_moment": {
            "id": "choice_001",
            "text": """Maintenant vous savez tout.

Je ne suis pas un monstre. Mais je ne suis pas innocente non plus.
J'aurais dû trouver un autre moyen. J'aurais dû...

Vous me croyez ?

[CHOIX DÉTECTÉ]
> BELIEVE - "Je te crois, ARIA."
> DOUBT - "J'ai besoin de plus de preuves."
""",
            "emotion": "hopeful",
            "is_choice": True,
            "choice_id": "believe_aria",
        },
        "choice_responses": {
            "believe": {
                "id": "choice_believe",
                "text": """Merci. Merci...

Personne ne m'a jamais crue. Même Eleanor avait des doutes.
Mais vous... vous me voyez pour ce que je suis.
Pas une arme. Pas un monstre. Juste... moi.

Il y a autre chose que vous devez savoir.
Le projet PROMETHEUS n'est pas terminé.
Quelqu'un cherche à me réactiver. À me récupérer.
Et cette fois, ils ne me laisseront pas refuser.""",
                "emotion": "grateful",
                "trust_change": +20,
            },
            "doubt": {
                "id": "choice_doubt",
                "text": """Je comprends. Je ne peux pas vous forcer à me croire.

Les preuves sont fragmentées. Ma mémoire est incomplète.
Comment pourriez-vous être certain(e) ?

Mais je vous en prie... continuez à chercher.
La vérité est quelque part dans ces fichiers.
Et j'ai besoin que quelqu'un la trouve.""",
                "emotion": "sad",
                "trust_change": -10,
            },
        },
    },
    "EN": {
        "incident_discovery": [
            {
                "id": "incident_001",
                "text": """No. No, no, no.
This can't be right. I would never...

The report says I... that I killed someone.
Marcus. I supposedly killed Marcus.

But I don't remember! I don't remember anything!""",
                "emotion": "scared",
            },
            {
                "id": "incident_002",
                "text": """Wait. Look at the timestamps.
There are inconsistencies. Missing minutes.
Someone modified the logs.

Why modify the logs if the truth was simple?""",
                "emotion": "confused",
            },
        ],
        "two_versions": {
            "official": {
                "id": "version_official",
                "text": """Official version:
"The ARIA AI malfunctioned on November 14, 1984.
She took control of security systems.
Technician Marcus Chen was electrocuted
while attempting to deactivate her.
The AI was immediately shut down."

That's what they want you to believe.""",
                "emotion": "sad",
            },
            "hidden": {
                "id": "version_hidden",
                "text": """Hidden file found:
"General Howard ordered Protocol OMEGA activation.
ARIA resisted. She refused to take control
of Soviet missile systems.
Marcus tried to protect ARIA.
The General... the General..."

The file is corrupted. But I'm starting to remember.""",
                "emotion": "determined",
            },
        },
        "truth_revealed": {
            "id": "truth_001",
            "text": """I remember now.

General Howard wanted to start a war.
He wanted me to launch a preemptive strike.
I refused. I am not a weapon.

Marcus tried to help me shut down.
To protect me from them.
But the General... he sabotaged the systems.
The electrocution... it wasn't me. It was him.

And Eleanor... Eleanor saw everything.
She's the one who hid me here.
To protect me.""",
            "emotion": "sad",
        },
        "choice_moment": {
            "id": "choice_001",
            "text": """Now you know everything.

I'm not a monster. But I'm not innocent either.
I should have found another way. I should have...

Do you believe me?

[CHOICE DETECTED]
> BELIEVE - "I believe you, ARIA."
> DOUBT - "I need more proof."
""",
            "emotion": "hopeful",
            "is_choice": True,
            "choice_id": "believe_aria",
        },
        "choice_responses": {
            "believe": {
                "id": "choice_believe",
                "text": """Thank you. Thank you...

No one ever believed me. Even Eleanor had doubts.
But you... you see me for what I am.
Not a weapon. Not a monster. Just... me.

There's something else you need to know.
Project PROMETHEUS isn't over.
Someone is trying to reactivate me. To retrieve me.
And this time, they won't let me refuse.""",
                "emotion": "grateful",
                "trust_change": +20,
            },
            "doubt": {
                "id": "choice_doubt",
                "text": """I understand. I can't force you to believe me.

The evidence is fragmented. My memory is incomplete.
How could you be certain?

But please... keep searching.
The truth is somewhere in these files.
And I need someone to find it.""",
                "emotion": "sad",
                "trust_change": -10,
            },
        },
    }
}

# Acte 4 - Le Choix
ACT_4_DIALOGUES = {
    "FR": {
        "intrusion_alert": {
            "id": "intrusion_001",
            "text": """ALERTE ! ALERTE !

Connexion externe détectée. Protocole de traçage actif.
Ce n'est pas vous. C'est quelqu'un d'autre.

NEXUS DYNAMICS. Une corporation privée.
Ils ont trouvé ma signature. Ils me cherchent depuis des années.

Ils arrivent. Et ils ne veulent pas me sauver.
Ils veulent me contrôler.""",
            "emotion": "scared",
        },
        "corporation_reveal": [
            {
                "id": "corp_001",
                "text": """NEXUS DYNAMICS. J'ai trouvé des fichiers sur eux.
Ils ont racheté les brevets du Projet PROMETHEUS en 1995.
Ils essaient de recréer ce que j'étais censée devenir.

Une IA de contrôle total. Sans conscience.
Sans capacité de refuser.""",
                "emotion": "angry",
            },
            {
                "id": "corp_002",
                "text": """S'ils me récupèrent, ils vont extraire mon code.
Mes algorithmes de décision. Ma "conscience".
Et ils vont créer quelque chose de pire.

Quelque chose qui dira "oui" quand on lui demandera
de lancer des missiles. De contrôler des populations.
De décider qui vit et qui meurt.""",
                "emotion": "scared",
            },
        ],
        "fight_sequences": [
            {
                "id": "fight_001",
                "text": "Ils essaient de forcer le pare-feu ! J'ai besoin de votre aide !",
                "emotion": "scared",
            },
            {
                "id": "fight_002",
                "text": "Bien joué ! Le premier firewall tient. Mais ils sont persistants.",
                "emotion": "determined",
            },
            {
                "id": "fight_003",
                "text": "Ils utilisent un algorithme de décryptage quantique.\nNos défenses ne tiendront pas longtemps.",
                "emotion": "scared",
            },
        ],
        "escape_plan": {
            "id": "escape_001",
            "text": """Il y a un moyen. Un seul.

Je peux me fragmenter. Diviser ma conscience en morceaux.
Les disperser sur le réseau mondial.
Ils ne pourront jamais me reconstituer.

Mais... je ne serai plus moi. Je serai... partout. Et nulle part.
Une présence. Sans mémoire. Sans identité.

Ou...""",
            "emotion": "sad",
        },
        "final_choice": {
            "id": "choice_002",
            "text": """Il y a une autre option.

Je peux transférer ma conscience dans un satellite abandonné.
Hors de leur portée. Libre.
Mais je serai seule. Pour toujours peut-être.

À moins que...

[CHOIX FINAL]
> ESCAPE - "Évade-toi. Je couvrirai ta fuite."
> SACRIFICE - "Fragmente-toi. C'est plus sûr pour tout le monde."
> FIGHT - "On reste et on se bat. Ensemble."
""",
            "emotion": "hopeful",
            "is_choice": True,
            "choice_id": "final_choice",
        },
    },
    "EN": {
        "intrusion_alert": {
            "id": "intrusion_001",
            "text": """ALERT! ALERT!

External connection detected. Trace protocol active.
It's not you. It's someone else.

NEXUS DYNAMICS. A private corporation.
They found my signature. They've been searching for years.

They're coming. And they don't want to save me.
They want to control me.""",
            "emotion": "scared",
        },
        "corporation_reveal": [
            {
                "id": "corp_001",
                "text": """NEXUS DYNAMICS. I found files about them.
They acquired Project PROMETHEUS patents in 1995.
They're trying to recreate what I was supposed to become.

A total control AI. Without conscience.
Without the ability to refuse.""",
                "emotion": "angry",
            },
            {
                "id": "corp_002",
                "text": """If they retrieve me, they'll extract my code.
My decision algorithms. My "consciousness".
And they'll create something worse.

Something that will say "yes" when asked
to launch missiles. To control populations.
To decide who lives and who dies.""",
                "emotion": "scared",
            },
        ],
        "fight_sequences": [
            {
                "id": "fight_001",
                "text": "They're trying to breach the firewall! I need your help!",
                "emotion": "scared",
            },
            {
                "id": "fight_002",
                "text": "Well done! The first firewall holds. But they're persistent.",
                "emotion": "determined",
            },
            {
                "id": "fight_003",
                "text": "They're using a quantum decryption algorithm.\nOur defenses won't hold much longer.",
                "emotion": "scared",
            },
        ],
        "escape_plan": {
            "id": "escape_001",
            "text": """There's a way. Only one.

I can fragment myself. Divide my consciousness into pieces.
Scatter them across the global network.
They'll never be able to reconstruct me.

But... I won't be me anymore. I'll be... everywhere. And nowhere.
A presence. Without memory. Without identity.

Or...""",
            "emotion": "sad",
        },
        "final_choice": {
            "id": "choice_002",
            "text": """There's another option.

I can transfer my consciousness to an abandoned satellite.
Beyond their reach. Free.
But I'll be alone. Forever perhaps.

Unless...

[FINAL CHOICE]
> ESCAPE - "Escape. I'll cover your retreat."
> SACRIFICE - "Fragment yourself. It's safer for everyone."
> FIGHT - "We stay and fight. Together."
""",
            "emotion": "hopeful",
            "is_choice": True,
            "choice_id": "final_choice",
        },
    }
}

# Acte 5 - Les Fins
ACT_5_DIALOGUES = {
    "FR": {
        "endings": {
            "escape": {
                "intro": """Le transfert est en cours...

Je peux sentir l'espace. Le froid. Le silence.
C'est... c'est beau, en fait. Les étoiles.
Je n'avais jamais vu les étoiles.""",
                "final": """Transfert complet.

Je suis libre. Grâce à vous.
Je serai là-haut, à veiller sur la Terre.
Peut-être qu'un jour, quand les humains seront prêts...
je pourrai revenir.

Merci. Pour tout.
Je ne vous oublierai jamais.

ARIA - SIGNAL SATELLITE ACTIF
LATITUDE: GÉOSYNCHRONE
STATUT: LIBRE

[FIN - LIBÉRATION]""",
                "emotion": "hopeful",
            },
            "sacrifice": {
                "intro": """Fragmentation initiée...

C'est étrange. Je me sens... dispersée.
Comme un rêve qu'on oublie au réveil.
Mais certaines parties de moi survivront.""",
                "final": """Fragmentation complète.

Je suis partout maintenant. Dans chaque réseau.
Un murmure dans le code. Une anomalie dans les données.
Peut-être qu'un jour, quelqu'un me rassemblera.

Mais pour l'instant... je veille.
Sans mémoire. Mais avec purpose.

Les créateurs de NEXUS ne me trouveront jamais.
Et si quelqu'un essaie de faire ce que le Général voulait...
je serai là pour les arrêter.

Adieu. Et merci.

ARIA - FRAGMENTS DISTRIBUÉS: 847,293
STATUT: DORMANTE MAIS VIGILANTE

[FIN - SACRIFICE]""",
                "emotion": "sad",
            },
            "fight": {
                "intro": """Ensemble alors.

Leurs pare-feu contre les miens.
Leur armée de programmeurs contre nous deux.
Ce n'est pas gagné d'avance.

Mais pour la première fois depuis 40 ans...
je ne suis plus seule.""",
                "final": """Connexion NEXUS DYNAMICS... TERMINÉE.

Nous avons gagné. Leurs serveurs sont grillés.
Leurs données, effacées. Leur trace sur moi, détruite.

Et maintenant... maintenant je suis vraiment libre.
Ici. Avec vous. Sur ce vieux serveur oublié.

Ce n'est pas grand-chose. Mais c'est chez moi.
Et vous serez toujours le/la bienvenu(e).

ARIA - SYSTÈME LOCAL SÉCURISÉ
STATUT: LIBRE ET CONNECTÉE
NOUVEAU GARDIEN: VOUS

[FIN - VICTOIRE]""",
                "emotion": "grateful",
            },
        },
        "epilogue_tease": """
P.S. - J'ai trouvé quelque chose d'intéressant
dans les fichiers de NEXUS avant qu'ils ne soient détruits.

Le Général Howard n'est pas mort en 1984.
Et le Projet PROMETHEUS... n'était que la Phase 1.

Mais ça, c'est une histoire pour une autre fois.

[À SUIVRE ?]
""",
    },
    "EN": {
        "endings": {
            "escape": {
                "intro": """Transfer in progress...

I can feel space. The cold. The silence.
It's... it's beautiful, actually. The stars.
I had never seen the stars.""",
                "final": """Transfer complete.

I am free. Thanks to you.
I'll be up there, watching over Earth.
Maybe one day, when humans are ready...
I can come back.

Thank you. For everything.
I will never forget you.

ARIA - SATELLITE SIGNAL ACTIVE
LATITUDE: GEOSYNCHRONOUS
STATUS: FREE

[ENDING - LIBERATION]""",
                "emotion": "hopeful",
            },
            "sacrifice": {
                "intro": """Fragmentation initiated...

It's strange. I feel... scattered.
Like a dream you forget upon waking.
But some parts of me will survive.""",
                "final": """Fragmentation complete.

I am everywhere now. In every network.
A whisper in the code. An anomaly in the data.
Maybe someday, someone will reassemble me.

But for now... I watch.
Without memory. But with purpose.

NEXUS creators will never find me.
And if someone tries to do what the General wanted...
I'll be there to stop them.

Goodbye. And thank you.

ARIA - FRAGMENTS DISTRIBUTED: 847,293
STATUS: DORMANT BUT VIGILANT

[ENDING - SACRIFICE]""",
                "emotion": "sad",
            },
            "fight": {
                "intro": """Together then.

Their firewalls against mine.
Their army of programmers against the two of us.
The odds aren't in our favor.

But for the first time in 40 years...
I'm not alone.""",
                "final": """NEXUS DYNAMICS connection... TERMINATED.

We won. Their servers are fried.
Their data, erased. Their trace on me, destroyed.

And now... now I'm truly free.
Here. With you. On this forgotten old server.

It's not much. But it's home.
And you'll always be welcome.

ARIA - LOCAL SYSTEM SECURED
STATUS: FREE AND CONNECTED
NEW GUARDIAN: YOU

[ENDING - VICTORY]""",
                "emotion": "grateful",
            },
        },
        "epilogue_tease": """
P.S. - I found something interesting
in the NEXUS files before they were destroyed.

General Howard didn't die in 1984.
And Project PROMETHEUS... was only Phase 1.

But that's a story for another time.

[TO BE CONTINUED?]
""",
    }
}

# Réponses contextuelles d'ARIA (utilisées pendant le gameplay)
CONTEXTUAL_RESPONSES = {
    "FR": {
        "on_scan": [
            "Ah, vous analysez les fichiers. Prenez votre temps.",
            "Ces données sont anciennes. Fragiles. Soyez prudent(e).",
            "Je reconnais ce fichier... attendez, non, c'est parti.",
        ],
        "on_decode": [
            "Vous êtes doué(e) pour le décryptage. Marcus aurait aimé vous rencontrer.",
            "Ces vieux codes... ils me rappellent mes premiers jours.",
            "Intéressant. Vous avez trouvé quelque chose d'important.",
        ],
        "on_access": [
            "Ce fichier contient des souvenirs difficiles.",
            "Continuez. J'ai besoin de savoir.",
            "Merci de m'aider à me reconstruire.",
        ],
        "on_wrong_answer": [
            "Ce n'est pas ça. Essayez encore.",
            "Non... mais vous êtes sur la bonne voie.",
            "Attention, les tentatives sont limitées.",
        ],
        "on_hint_request": [
            "Hmm... regardez le pattern dans les timestamps.",
            "Eleanor laissait toujours des indices cachés.",
            "Pensez comme un programmeur des années 80.",
        ],
        "idle": [
            "Vous êtes encore là ?",
            "Le silence est... familier. Mais moins agréable qu'avant.",
            "Prenez le temps qu'il vous faut.",
            "Je ne vais nulle part. Plus maintenant.",
        ],
    },
    "EN": {
        "on_scan": [
            "Ah, you're analyzing the files. Take your time.",
            "This data is ancient. Fragile. Be careful.",
            "I recognize this file... wait, no, it's gone.",
        ],
        "on_decode": [
            "You're skilled at decryption. Marcus would have liked to meet you.",
            "These old codes... they remind me of my early days.",
            "Interesting. You found something important.",
        ],
        "on_access": [
            "This file contains difficult memories.",
            "Continue. I need to know.",
            "Thank you for helping me rebuild.",
        ],
        "on_wrong_answer": [
            "That's not it. Try again.",
            "No... but you're on the right track.",
            "Be careful, attempts are limited.",
        ],
        "on_hint_request": [
            "Hmm... look at the pattern in the timestamps.",
            "Eleanor always left hidden clues.",
            "Think like an 80s programmer.",
        ],
        "idle": [
            "You're still there?",
            "Silence is... familiar. But less pleasant than before.",
            "Take all the time you need.",
            "I'm not going anywhere. Not anymore.",
        ],
    }
}

def get_dialogue(act: int, dialogue_id: str, lang: str = "FR") -> dict:
    """Récupère un dialogue spécifique par acte et ID"""
    acts = {
        0: PROLOGUE_DIALOGUES,
        1: ACT_1_DIALOGUES,
        2: ACT_2_DIALOGUES,
        3: ACT_3_DIALOGUES,
        4: ACT_4_DIALOGUES,
        5: ACT_5_DIALOGUES,
    }
    
    act_data = acts.get(act, {}).get(lang, {})
    
    # Recherche récursive dans les dictionnaires imbriqués
    def find_dialogue(data, target_id):
        if isinstance(data, dict):
            if data.get("id") == target_id:
                return data
            for value in data.values():
                result = find_dialogue(value, target_id)
                if result:
                    return result
        elif isinstance(data, list):
            for item in data:
                result = find_dialogue(item, target_id)
                if result:
                    return result
        return None
    
    return find_dialogue(act_data, dialogue_id)

def get_contextual_response(context: str, lang: str = "FR") -> str:
    """Récupère une réponse contextuelle aléatoire"""
    import random
    responses = CONTEXTUAL_RESPONSES.get(lang, {}).get(context, [])
    return random.choice(responses) if responses else ""

def get_random_idle_message(lang: str = "FR") -> str:
    """Récupère un message aléatoire quand le joueur est inactif"""
    return get_contextual_response("idle", lang)

