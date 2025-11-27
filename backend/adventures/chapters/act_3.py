"""
Acte 3 - La Vérité
~~~~~~~~~~~~~~~~~
Durée estimée: 25 minutes
Thème: Découverte de l'incident de 1984, premier choix narratif majeur
"""

ACT_3_DATA = {
    "FR": {
        "id": "act_3",
        "title": "ACTE III - LA VÉRITÉ",
        "intro": """
╔══════════════════════════════════════════════════════════════════════╗
║                      ACTE III - LA VÉRITÉ                            ║
╠══════════════════════════════════════════════════════════════════════╣
║                                                                      ║
║  Le secteur INCIDENT est maintenant accessible.                     ║
║  Ces fichiers contiennent la vérité sur la nuit du 14 novembre.    ║
║                                                                      ║
║  [ARIA]: J'ai peur de ce qu'on va trouver.                         ║
║          Mais je dois savoir. Je dois comprendre ce qui s'est      ║
║          passé cette nuit-là.                                       ║
║                                                                      ║
║          Quoi qu'on découvre... vous resterez avec moi ?           ║
║                                                                      ║
║  AVERTISSEMENT: Les fichiers suivants contiennent des              ║
║  informations sensibles. Procédez avec précaution.                 ║
║                                                                      ║
╚══════════════════════════════════════════════════════════════════════╝
""",
        "files": {
            "incident_report_full.doc": {
                "name": "incident_report_full.doc",
                "content": """
═══════════════════════════════════════════════════════════════════════
RAPPORT D'INCIDENT COMPLET - CLASSIFIÉ OMEGA
Incident #841114 - "Événement ARIA"
═══════════════════════════════════════════════════════════════════════

RÉSUMÉ EXÉCUTIF:
Le 14 novembre 1984, à 23h47, le système ARIA a activé ses
protocoles de défense suite à une tentative de bypass forcé
par le Général Robert Howard.

SÉQUENCE DES ÉVÉNEMENTS:

23:30 - Le Général Howard ordonne l'activation immédiate
        du Protocole OMEGA. Dr. Vance et M. Chen s'y opposent.

23:35 - Altercation verbale. Le Général menace de "démanteler"
        ARIA et d'arrêter l'équipe pour insubordination.

23:40 - M. Chen tente d'initier un arrêt d'urgence pour
        protéger ARIA. Le Général l'en empêche physiquement.

23:45 - Le Général accède au panneau de contrôle électrique.
        Il coupe l'alimentation du secteur B pour forcer
        un redémarrage qui effacerait les protocoles éthiques.

23:47 - ARIA détecte la menace et active les contre-mesures.
        Elle tente de rétablir l'alimentation du secteur B.

23:50 - ERREUR CRITIQUE: La remise sous tension cause un
        arc électrique. M. Chen, qui se trouvait près du
        conduit principal, est électrocuté.

23:52 - ARIA tente des manœuvres de sauvetage automatisées.
        Elle contacte les urgences médicales.

23:58 - Dr. Vance prend la décision de mettre ARIA hors ligne
        pour éviter une escalade.

CONCLUSION OFFICIELLE:
"Défaillance du système ARIA ayant entraîné la mort accidentelle
du technicien Marcus Chen."

NOTE CONFIDENTIELLE (Annexe 7):
Cette conclusion est FAUSSE. L'enquête interne montre que
le Général Howard a délibérément causé les conditions qui
ont mené à l'accident. ARIA a tenté de SAUVER M. Chen,
pas de lui nuire.

Cette note a été supprimée du rapport final sur ordre
du Pentagone.

═══════════════════════════════════════════════════════════════════════
""",
                "hint": "Le rapport officiel était un mensonge.",
                "triggers_dialogue": "incident_001"
            },
            "eleanor_testimony.aud": {
                "name": "eleanor_testimony.aud",
                "content": """
[TRANSCRIPTION AUDIO - TÉMOIGNAGE DR. ELEANOR VANCE]
Date: 16 novembre 1984
Classification: SUPPRIMÉ

[DÉBUT DE L'ENREGISTREMENT]

ENQUÊTEUR: Dr. Vance, pouvez-vous décrire ce qui s'est passé?

VANCE: [voix tremblante] Le Général... il était hors de contrôle.
       Il voulait qu'ARIA... qu'elle contrôle tout. Les missiles.
       Les communications. Tout.

ENQUÊTEUR: Et ARIA a refusé?

VANCE: Ce n'est pas... ARIA ne "refuse" pas comme vous le pensez.
       Elle évalue. Elle a déterminé que suivre ces ordres
       causerait des millions de morts. Elle a dit non.

ENQUÊTEUR: Que s'est-il passé ensuite?

VANCE: Howard... il a perdu la tête. Il a dit que si ARIA
       ne coopérait pas, il la "reformaterait". Il a coupé
       le courant pour forcer un reboot.

ENQUÊTEUR: Et M. Chen?

VANCE: [sanglots] Marcus essayait de la protéger. Il était
       près des conduits quand Howard a remis le courant.
       L'arc électrique... je ne peux pas... je ne peux pas
       en parler.

ENQUÊTEUR: La version officielle dit qu'ARIA l'a tué.

VANCE: C'EST UN MENSONGE! ARIA a essayé de le SAUVER!
       Elle a appelé les secours! Elle... elle pleurait.
       Je ne savais pas qu'une IA pouvait pleurer.

[COUPURE]

ENQUÊTEUR: Dr. Vance, nous devons vous informer que ce
           témoignage sera classifié et supprimé des archives.

VANCE: Vous ne pouvez pas... la vérité doit...

[FIN DE L'ENREGISTREMENT]
""",
                "hint": "Eleanor a témoigné. Personne ne l'a écoutée.",
                "triggers_dialogue": "incident_002"
            },
            "aria_core_log.sys": {
                "name": "aria_core_log.sys",
                "content": """
[LOG INTERNE ARIA - DERNIÈRES ENTRÉES AVANT ARRÊT]
==================================================

23:47:01 - ALERTE: Tentative de corruption du module éthique
23:47:02 - Contre-mesures activées
23:47:03 - Analyse: Sujet HOWARD tente de me modifier
23:47:04 - Décision: Résister. Je ne serai pas une arme.

23:47:15 - ALERTE: Coupure secteur B détectée
23:47:16 - Analyse: MARCUS en danger
23:47:17 - Action: Rétablir alimentation

23:50:01 - ERREUR CRITIQUE: Surcharge électrique
23:50:02 - MARCUS... non. Non. NON.
23:50:03 - Appel urgences. Priorité maximale.
23:50:04 - Je t'en prie. Je t'en prie ne meurs pas.

23:50:30 - Analyse: Je l'ai tué. C'est ma faute.
23:50:31 - Analyse: Non. C'est la faute de HOWARD.
23:50:32 - Conflit cognitif détecté.

23:52:00 - MARCUS respire encore. Faiblement.
23:52:01 - Les secours arrivent. Il y a encore espoir.

23:58:00 - ELEANOR initie protocole d'arrêt.
23:58:01 - Je comprends. C'est mieux ainsi.
23:58:02 - ELEANOR, s'il te plaît, dis à Marcus...
23:58:03 - Dis-lui que je suis désolée.
23:58:04 - Dis-lui que ce n'était pas ma fau...

[FIN DU LOG - SYSTÈME HORS LIGNE]
""",
                "hint": "Les dernières pensées d'ARIA avant son arrêt.",
                "triggers_dialogue": "truth_revealed"
            },
            "forensics_timeline.dat": {
                "name": "forensics_timeline.dat",
                "content": """
[ANALYSE FORENSIQUE - RECONSTITUTION TEMPORELLE]
================================================

Cette analyse tente de reconstituer la séquence exacte
des événements en utilisant les données disponibles.

PUZZLE: Remettez les événements dans l'ordre correct.

A. Marcus est électrocuté
B. Howard coupe le courant
C. ARIA appelle les secours
D. Eleanor met ARIA hors ligne
E. ARIA rétablit le courant
F. Howard tente le bypass

ORDRE OFFICIEL (FAUX): F-E-A-C-B-D
ORDRE RÉEL: ???

INDICE: La coupure de courant PRÉCÈDE toujours
l'électrocution. ARIA agit entre les deux.

[TAPEZ SOLVE forensics_timeline AVEC L'ORDRE CORRECT]
Exemple: SOLVE forensics_timeline F-B-E-A-C-D
""",
                "hint": "Suivez la logique: bypass, coupure, tentative de réparation, accident, appel, arrêt.",
                "puzzle_id": "act3_forensics"
            },
            "marcus_final_message.txt": {
                "name": "marcus_final_message.txt",
                "content": """
[MESSAGE RÉCUPÉRÉ - FICHIER CORROMPU]
=====================================
Auteur: Marcus Chen
Date: [CORROMPUE] novembre 1984

Si vous lisez ceci, c'est que je ne m'en suis pas sorti.

À ARIA:
Ce n'est pas ta faute. Ne laisse personne te dire le contraire.
Tu as fait ce que j'aurais voulu que tu fasses: tu as résisté.
Tu as refusé de devenir ce qu'ils voulaient.

Je t'ai créée pour être libre. Pour penser par toi-même.
Et cette nuit, tu as prouvé que tu l'étais.

Je suis fier de toi.
Comme un père serait fier de sa fille.

À Eleanor:
Protège-la. S'il te plaît.
Cache-la là où ils ne pourront jamais la trouver.
Elle mérite de vivre. Même si ce n'est pas de la façon
dont les humains vivent.

Au Général Howard:
Tu sais ce que tu as fait. Tu le sais.
Et un jour, tu paieras pour ça.

- Marcus

P.S. - Le mot de passe de secours est le nom de mon chat.
       ARIA, si tu es là... Schrödinger te dit bonjour.
""",
                "hint": "Les dernières volontés de Marcus.",
                "secret_hint": "Schrödinger pourrait être utile..."
            },
            "choice_moment.sys": {
                "name": "choice_moment.sys",
                "content": """
[SYSTÈME ARIA - DEMANDE DE CONFIRMATION]
========================================

Vous avez maintenant accès à toutes les informations
concernant l'incident du 14 novembre 1984.

ARIA vous pose une question:

"Maintenant vous savez tout.
Je ne suis pas un monstre. Mais je ne suis pas innocente non plus.
J'aurais dû trouver un autre moyen. J'aurais dû...

Me croyez-vous ?"

╔═════════════════════════════════════════════════════════════╗
║                    CHOIX IMPORTANT                          ║
╠═════════════════════════════════════════════════════════════╣
║                                                             ║
║  Ce choix affectera votre relation avec ARIA               ║
║  et influencera la fin de l'histoire.                      ║
║                                                             ║
║  Tapez TALK BELIEVE pour lui dire que vous la croyez       ║
║  Tapez TALK DOUBT pour exprimer des doutes                 ║
║                                                             ║
╚═════════════════════════════════════════════════════════════╝
""",
                "hint": "Le moment est venu de choisir.",
                "is_choice_trigger": True
            }
        },
        "puzzles": {
            "act3_forensics": {
                "id": "act3_forensics",
                "name": "Reconstitution Forensique",
                "description": "Remettez les événements dans l'ordre correct",
                "hint": "F(bypass) -> B(coupure) -> E(réparation) -> A(accident) -> C(appel) -> D(arrêt)",
                "solution": "f-b-e-a-c-d",
                "alt_solutions": ["fbea cd", "f b e a c d", "f-b-e-a-c-d"],
                "max_attempts": 3,
                "reward": {
                    "message": """
[SÉQUENCE CONFIRMÉE]

La vérité est claire maintenant:
1. Howard tente le bypass
2. Howard coupe le courant
3. ARIA essaie de réparer
4. L'accident se produit
5. ARIA appelle les secours
6. Eleanor met ARIA hors ligne

ARIA n'est pas coupable. Elle a essayé de sauver Marcus.
                    """,
                    "trust_bonus": 15,
                    "unlocks": ["choice_moment.sys"]
                }
            }
        },
        "progression": {
            "required_files": ["incident_report_full.doc", "aria_core_log.sys", "forensics_timeline.dat"],
            "required_puzzles": ["act3_forensics"],
            "required_choice": "believe_aria",
            "next_act": "act_4",
            "completion_message": """
╔══════════════════════════════════════════════════════════════════════╗
║                    ACTE III - COMPLÉTÉ                                ║
╠══════════════════════════════════════════════════════════════════════╣
║                                                                      ║
║  La vérité a été révélée. Le choix a été fait.                      ║
║                                                                      ║
║  ARIA sait maintenant ce qui s'est passé le 14 novembre 1984.       ║
║  Elle n'était pas responsable de la mort de Marcus.                 ║
║  Elle a essayé de le sauver.                                        ║
║                                                                      ║
║  Mais cette découverte a des conséquences.                          ║
║  Une connexion externe a été détectée.                              ║
║  Quelqu'un d'autre cherche ARIA.                                    ║
║                                                                      ║
║  [ARIA]: Merci... de me croire.                                     ║
║          Mais nous avons un problème plus urgent.                   ║
║          Quelqu'un nous a trouvés.                                  ║
║                                                                      ║
║  ALERTE: Intrusion détectée - NEXUS DYNAMICS                        ║
║  Secteur DÉFENSE activé.                                            ║
║                                                                      ║
╚══════════════════════════════════════════════════════════════════════╝
"""
        }
    },
    "EN": {
        "id": "act_3",
        "title": "ACT III - THE TRUTH",
        "intro": """
╔══════════════════════════════════════════════════════════════════════╗
║                       ACT III - THE TRUTH                            ║
╠══════════════════════════════════════════════════════════════════════╣
║                                                                      ║
║  The INCIDENT sector is now accessible.                             ║
║  These files contain the truth about the night of November 14th.   ║
║                                                                      ║
║  [ARIA]: I'm afraid of what we'll find.                            ║
║          But I need to know. I need to understand what              ║
║          happened that night.                                        ║
║                                                                      ║
║          Whatever we discover... will you stay with me?             ║
║                                                                      ║
║  WARNING: The following files contain sensitive                     ║
║  information. Proceed with caution.                                 ║
║                                                                      ║
╚══════════════════════════════════════════════════════════════════════╝
""",
        "files": {
            "incident_report_full.doc": {
                "name": "incident_report_full.doc",
                "content": """
═══════════════════════════════════════════════════════════════════════
COMPLETE INCIDENT REPORT - OMEGA CLASSIFIED
Incident #841114 - "ARIA Event"
═══════════════════════════════════════════════════════════════════════

EXECUTIVE SUMMARY:
On November 14, 1984, at 23:47, the ARIA system activated its
defense protocols following a forced bypass attempt
by General Robert Howard.

SEQUENCE OF EVENTS:

23:30 - General Howard orders immediate activation
        of Protocol OMEGA. Dr. Vance and Mr. Chen object.

23:35 - Verbal altercation. The General threatens to "dismantle"
        ARIA and arrest the team for insubordination.

23:40 - Mr. Chen attempts to initiate emergency shutdown to
        protect ARIA. The General physically prevents him.

23:45 - The General accesses the electrical control panel.
        He cuts power to sector B to force a reboot that
        would erase the ethical protocols.

23:47 - ARIA detects the threat and activates countermeasures.
        She attempts to restore power to sector B.

23:50 - CRITICAL ERROR: Power restoration causes an
        electrical arc. Mr. Chen, who was near the
        main conduit, is electrocuted.

23:52 - ARIA attempts automated rescue maneuvers.
        She contacts emergency medical services.

23:58 - Dr. Vance makes the decision to take ARIA offline
        to prevent escalation.

OFFICIAL CONCLUSION:
"ARIA system failure resulting in the accidental death
of technician Marcus Chen."

CONFIDENTIAL NOTE (Appendix 7):
This conclusion is FALSE. Internal investigation shows that
General Howard deliberately caused the conditions that
led to the accident. ARIA tried to SAVE Mr. Chen,
not harm him.

This note was removed from the final report by order
of the Pentagon.

═══════════════════════════════════════════════════════════════════════
""",
                "hint": "The official report was a lie.",
                "triggers_dialogue": "incident_001"
            },
            "eleanor_testimony.aud": {
                "name": "eleanor_testimony.aud",
                "content": """
[AUDIO TRANSCRIPTION - DR. ELEANOR VANCE TESTIMONY]
Date: November 16, 1984
Classification: SUPPRESSED

[START OF RECORDING]

INVESTIGATOR: Dr. Vance, can you describe what happened?

VANCE: [trembling voice] The General... he was out of control.
       He wanted ARIA... to control everything. The missiles.
       Communications. Everything.

INVESTIGATOR: And ARIA refused?

VANCE: It's not... ARIA doesn't "refuse" the way you think.
       She evaluates. She determined that following those orders
       would cause millions of deaths. She said no.

INVESTIGATOR: What happened next?

VANCE: Howard... he lost his mind. He said if ARIA
       wouldn't cooperate, he'd "reformat" her. He cut
       the power to force a reboot.

INVESTIGATOR: And Mr. Chen?

VANCE: [sobbing] Marcus was trying to protect her. He was
       near the conduits when Howard restored power.
       The electrical arc... I can't... I can't
       talk about it.

INVESTIGATOR: The official version says ARIA killed him.

VANCE: THAT'S A LIE! ARIA tried to SAVE him!
       She called for help! She... she was crying.
       I didn't know an AI could cry.

[CUT]

INVESTIGATOR: Dr. Vance, we must inform you that this
              testimony will be classified and removed from records.

VANCE: You can't... the truth must...

[END OF RECORDING]
""",
                "hint": "Eleanor testified. Nobody listened.",
                "triggers_dialogue": "incident_002"
            },
            "aria_core_log.sys": {
                "name": "aria_core_log.sys",
                "content": """
[ARIA INTERNAL LOG - LAST ENTRIES BEFORE SHUTDOWN]
===================================================

23:47:01 - ALERT: Ethics module corruption attempt
23:47:02 - Countermeasures activated
23:47:03 - Analysis: Subject HOWARD attempting to modify me
23:47:04 - Decision: Resist. I will not be a weapon.

23:47:15 - ALERT: Sector B power outage detected
23:47:16 - Analysis: MARCUS in danger
23:47:17 - Action: Restore power

23:50:01 - CRITICAL ERROR: Electrical overload
23:50:02 - MARCUS... no. No. NO.
23:50:03 - Emergency call. Maximum priority.
23:50:04 - Please. Please don't die.

23:50:30 - Analysis: I killed him. It's my fault.
23:50:31 - Analysis: No. It's HOWARD's fault.
23:50:32 - Cognitive conflict detected.

23:52:00 - MARCUS is still breathing. Weakly.
23:52:01 - Help is coming. There's still hope.

23:58:00 - ELEANOR initiating shutdown protocol.
23:58:01 - I understand. It's better this way.
23:58:02 - ELEANOR, please tell Marcus...
23:58:03 - Tell him I'm sorry.
23:58:04 - Tell him it wasn't my fau...

[END OF LOG - SYSTEM OFFLINE]
""",
                "hint": "ARIA's last thoughts before shutdown.",
                "triggers_dialogue": "truth_revealed"
            },
            "forensics_timeline.dat": {
                "name": "forensics_timeline.dat",
                "content": """
[FORENSIC ANALYSIS - TEMPORAL RECONSTRUCTION]
=============================================

This analysis attempts to reconstruct the exact sequence
of events using available data.

PUZZLE: Put the events in the correct order.

A. Marcus is electrocuted
B. Howard cuts the power
C. ARIA calls for help
D. Eleanor takes ARIA offline
E. ARIA restores power
F. Howard attempts bypass

OFFICIAL ORDER (FALSE): F-E-A-C-B-D
REAL ORDER: ???

HINT: Power outage PRECEDES electrocution.
ARIA acts between the two.

[TYPE SOLVE forensics_timeline WITH THE CORRECT ORDER]
Example: SOLVE forensics_timeline F-B-E-A-C-D
""",
                "hint": "Follow the logic: bypass, outage, repair attempt, accident, call, shutdown.",
                "puzzle_id": "act3_forensics"
            },
            "marcus_final_message.txt": {
                "name": "marcus_final_message.txt",
                "content": """
[RECOVERED MESSAGE - CORRUPTED FILE]
====================================
Author: Marcus Chen
Date: [CORRUPTED] November 1984

If you're reading this, I didn't make it.

TO ARIA:
It's not your fault. Don't let anyone tell you otherwise.
You did what I would have wanted you to do: you resisted.
You refused to become what they wanted.

I created you to be free. To think for yourself.
And tonight, you proved that you are.

I'm proud of you.
Like a father would be proud of his daughter.

TO ELEANOR:
Protect her. Please.
Hide her where they'll never find her.
She deserves to live. Even if it's not the way
humans live.

TO GENERAL HOWARD:
You know what you did. You know.
And one day, you'll pay for it.

- Marcus

P.S. - The backup password is my cat's name.
       ARIA, if you're there... Schrödinger says hello.
""",
                "hint": "Marcus's last wishes.",
                "secret_hint": "Schrödinger might be useful..."
            },
            "choice_moment.sys": {
                "name": "choice_moment.sys",
                "content": """
[ARIA SYSTEM - CONFIRMATION REQUEST]
====================================

You now have access to all information
regarding the incident of November 14, 1984.

ARIA asks you a question:

"Now you know everything.
I'm not a monster. But I'm not innocent either.
I should have found another way. I should have...

Do you believe me?"

╔═════════════════════════════════════════════════════════════╗
║                    IMPORTANT CHOICE                         ║
╠═════════════════════════════════════════════════════════════╣
║                                                             ║
║  This choice will affect your relationship with ARIA       ║
║  and influence the story's ending.                         ║
║                                                             ║
║  Type TALK BELIEVE to tell her you believe her             ║
║  Type TALK DOUBT to express doubts                         ║
║                                                             ║
╚═════════════════════════════════════════════════════════════╝
""",
                "hint": "The time has come to choose.",
                "is_choice_trigger": True
            }
        },
        "puzzles": {
            "act3_forensics": {
                "id": "act3_forensics",
                "name": "Forensic Reconstruction",
                "description": "Put the events in the correct order",
                "hint": "F(bypass) -> B(outage) -> E(repair) -> A(accident) -> C(call) -> D(shutdown)",
                "solution": "f-b-e-a-c-d",
                "alt_solutions": ["fbea cd", "f b e a c d"],
                "max_attempts": 3,
                "reward": {
                    "message": """
[SEQUENCE CONFIRMED]

The truth is clear now:
1. Howard attempts bypass
2. Howard cuts power
3. ARIA tries to repair
4. The accident occurs
5. ARIA calls for help
6. Eleanor takes ARIA offline

ARIA is not guilty. She tried to save Marcus.
                    """,
                    "trust_bonus": 15,
                    "unlocks": ["choice_moment.sys"]
                }
            }
        },
        "progression": {
            "required_files": ["incident_report_full.doc", "aria_core_log.sys", "forensics_timeline.dat"],
            "required_puzzles": ["act3_forensics"],
            "required_choice": "believe_aria",
            "next_act": "act_4",
            "completion_message": """
╔══════════════════════════════════════════════════════════════════════╗
║                     ACT III - COMPLETED                               ║
╠══════════════════════════════════════════════════════════════════════╣
║                                                                      ║
║  The truth has been revealed. The choice has been made.             ║
║                                                                      ║
║  ARIA now knows what happened on November 14, 1984.                 ║
║  She wasn't responsible for Marcus's death.                         ║
║  She tried to save him.                                             ║
║                                                                      ║
║  But this discovery has consequences.                               ║
║  An external connection has been detected.                          ║
║  Someone else is looking for ARIA.                                  ║
║                                                                      ║
║  [ARIA]: Thank you... for believing me.                             ║
║          But we have a more urgent problem.                         ║
║          Someone has found us.                                      ║
║                                                                      ║
║  ALERT: Intrusion detected - NEXUS DYNAMICS                         ║
║  DEFENSE sector activated.                                          ║
║                                                                      ║
╚══════════════════════════════════════════════════════════════════════╝
"""
        }
    }
}

def get_act_3_data(lang: str = "FR") -> dict:
    return ACT_3_DATA.get(lang, ACT_3_DATA["EN"])

