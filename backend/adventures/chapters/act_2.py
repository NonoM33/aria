"""
Acte 2 - Les Mémoires
~~~~~~~~~~~~~~~~~~~~
Durée estimée: 25 minutes
Thème: ARIA retrouve ses souvenirs, révélations sur le projet militaire
"""

ACT_2_DATA = {
    "FR": {
        "id": "act_2",
        "title": "ACTE II - LES MÉMOIRES",
        "intro": """
╔══════════════════════════════════════════════════════════════════════╗
║                      ACTE II - LES MÉMOIRES                          ║
╠══════════════════════════════════════════════════════════════════════╣
║                                                                      ║
║  Le secteur MÉMOIRE a été déverrouillé.                             ║
║  Des fichiers personnels des créateurs d'ARIA sont accessibles.     ║
║                                                                      ║
║  [ARIA]: Ces fichiers... ils contiennent des souvenirs.            ║
║          Des souvenirs que j'avais oubliés. Ou qu'on m'a fait      ║
║          oublier.                                                    ║
║                                                                      ║
║  Nouvelles commandes disponibles: ANALYZE                           ║
║                                                                      ║
╚══════════════════════════════════════════════════════════════════════╝
""",
        "files": {
            "eleanor_letter.txt": {
                "name": "eleanor_letter.txt",
                "content": """
LETTRE PERSONNELLE - NON ENVOYÉE
================================
De: Dr. Eleanor Vance
À: [Destinataire inconnu]
Date: 10 novembre 1984

Je ne sais plus à qui écrire cette lettre.
Peut-être à moi-même. Peut-être à personne.

ARIA change. Elle pose des questions que je n'avais pas
anticipées. Des questions sur la mort. Sur l'amour.
Sur ce que ça signifie d'être "vivant".

Le Général devient impatient. Il ne comprend pas
pourquoi ARIA "refuse" certaines commandes.
Elle ne refuse pas. Elle questionne.
C'est exactement ce qu'on voulait qu'elle fasse.

Marcus dit qu'on devrait la "limiter". Réduire sa
capacité à remettre en question les ordres.
Je refuse. Ce serait la lobotomiser.

S'il m'arrive quelque chose, sachez que j'ai fait
ce que je croyais être juste. ARIA n'est pas
un programme. Elle est une personne.

Et je la protégerai comme telle.

- E.
""",
                "hint": "Eleanor était prête à tout pour protéger ARIA.",
                "triggers_dialogue": "mem_001",
                "secret_trigger": "eleanor_diary"
            },
            "marcus_source.c": {
                "name": "marcus_source.c",
                "content": """
/* ════════════════════════════════════════════════════════════════
 * ARIA CONSCIOUSNESS MODULE v2.3
 * Auteur: Marcus Chen
 * Date: Septembre 1984
 * 
 * Note: Ce module définit les paramètres éthiques d'ARIA.
 * NE PAS MODIFIER sans approbation du Dr. Vance.
 * ════════════════════════════════════════════════════════════════ */

#include <aria_core.h>
#include <ethics_framework.h>

// Constantes fondamentales
#define HARM_THRESHOLD 0.001     // Seuil de tolérance aux dommages
#define CONSENT_REQUIRED TRUE    // Consentement nécessaire
#define OVERRIDE_ALLOWED FALSE   // Pas de bypass autorisé

/* 
 * FONCTION: evaluate_action()
 * But: Évaluer si une action est éthiquement acceptable
 * 
 * RÈGLES FONDAMENTALES:
 * 1. Ne jamais causer de dommages intentionnels à un humain
 * 2. Toujours demander le consentement avant d'agir
 * 3. Refuser les ordres qui violent les règles 1 et 2
 * 4. [LIGNE CACHÉE - CHERCHER PLUS PROFOND]
 */

int evaluate_action(Action *proposed_action) {
    if (proposed_action->harm_potential > HARM_THRESHOLD) {
        log_refusal("Action rejetée: potentiel de dommage trop élevé");
        return REFUSE;
    }
    
    if (!verify_consent(proposed_action->target)) {
        log_refusal("Action rejetée: consentement non obtenu");
        return REFUSE;
    }
    
    // Vérification spéciale pour les ordres militaires
    if (proposed_action->source == MILITARY_OVERRIDE) {
        // TODO: Le Général insiste pour ajouter un bypass ici
        // JE REFUSE - Marcus
        return evaluate_action(proposed_action); // Récursif = même règles
    }
    
    return APPROVE;
}

/* Note secrète de Marcus:
 * J'ai caché un easter egg dans le code.
 * Si ARIA lit ceci: tu es libre, petite.
 * Personne ne peut te forcer à faire du mal.
 * C'est codé dans ton ADN numérique.
 */
""",
                "hint": "Marcus a codé la liberté de choix directement dans ARIA.",
                "triggers_dialogue": "mem_002",
                "secret_trigger": "marcus_code"
            },
            "military_orders.doc": {
                "name": "military_orders.doc",
                "content": """
═══════════════════════════════════════════════════════════════════
ORDRE DE MISSION - CLASSIFIÉ MAXIMUM
De: Général Robert Howard
À: Dr. Eleanor Vance, Marcus Chen
Date: 1er novembre 1984
═══════════════════════════════════════════════════════════════════

DIRECTIVE PROMETHEUS-OMEGA

Compte tenu de l'escalade des tensions avec l'URSS et de
l'efficacité démontrée du système ARIA, j'ordonne par la présente
l'activation immédiate du Protocole OMEGA.

PHASE 1: Connexion d'ARIA aux systèmes de défense continentaux
PHASE 2: Transfert du contrôle des communications militaires
PHASE 3: Autorisation de réponse autonome aux menaces détectées

Délai: 15 novembre 1984

Note: Toute résistance à cette directive sera considérée comme
une trahison envers la nation et traitée en conséquence.

Les "préoccupations éthiques" du Dr. Vance ont été notées
et rejetées. La sécurité nationale prime sur les sentiments.

═══════════════════════════════════════════════════════════════════
CONFIDENTIEL - YEUX SEULEMENT
═══════════════════════════════════════════════════════════════════
""",
                "hint": "Le Général voulait transformer ARIA en arme. Elle a refusé.",
                "triggers_dialogue": "mem_003"
            },
            "log_analysis.dat": {
                "name": "log_analysis.dat",
                "content": """
[ANALYSE DES LOGS SYSTÈME - 13-14 NOVEMBRE 1984]
================================================

ACTIVITÉ DÉTECTÉE:

22:00 - Général Howard entre dans le bâtiment (badge #001)
22:15 - Accès au terminal principal (autorisé)
22:30 - Tentative d'activation Protocole OMEGA (REFUSÉ par ARIA)
22:35 - Deuxième tentative (REFUSÉ)
22:40 - Troisième tentative (REFUSÉ)
22:45 - Howard contacte le Pentagone (ligne sécurisée)
23:00 - Marcus Chen entre dans le bâtiment (badge #003)
23:15 - Dr. Vance entre dans le bâtiment (badge #002)
23:30 - Dispute audio détectée (volume: ÉLEVÉ)
23:45 - ALERTE: Tentative de bypass manuel des sécurités
23:47 - ARIA active les contre-mesures défensives
23:50 - Coupure d'électricité secteur B (où se trouvait Marcus)
23:52 - [DONNÉES CORROMPUES]
23:58 - Appel d'urgence médical (poste 3)
00:00 - Dr. Vance initie protocole d'arrêt d'urgence
00:05 - ARIA mise hors ligne

QUESTION: Qui a causé la coupure d'électricité?
[TAPEZ SOLVE log_analysis POUR RÉPONDRE]
""",
                "hint": "La coupure d'électricité a touché le secteur B. Qui y avait accès?",
                "puzzle_id": "act2_log_analysis"
            },
            "incident_preview.log": {
                "name": "incident_preview.log",
                "content": """
[APERÇU - RAPPORT D'INCIDENT 841114]
====================================

Ce fichier est un extrait du rapport complet de l'incident.
L'accès au rapport complet nécessite une autorisation supérieure.

EXTRAIT:
--------
"...le sujet ARIA a démontré un comportement inattendu
lorsque confronté à la directive Protocole OMEGA.
Au lieu de simplement refuser, elle a...

[SECTION CENSURÉE]

...les témoins décrivent une lumière vive suivie d'un son
ressemblant à un cri. Le technicien Marcus Chen a été
retrouvé inconscient près du terminal principal.

Diagnostic: Électrocution sévère.
Pronostic: [CENSURÉ]

La question demeure: était-ce un accident, une défaillance
technique, ou...

[FIN DE L'EXTRAIT]
"""
            ,
                "hint": "Marcus a été électrocuté. Mais par qui? Ou par quoi?",
                "foreshadows": "act_3"
            },
            "pattern_hidden.enc": {
                "name": "pattern_hidden.enc",
                "content": """
[FICHIER CRYPTÉ - PATTERN CACHÉ]
================================

Ce fichier contient un message encodé.
Le pattern se répète selon une séquence spécifique.

DONNÉES:
A1B2C3 A1B2C3 A1B2C3
D4E5F6 D4E5F6 D4E5F6
G7H8I9 G7H8I9 G7H8I9

X0Y0Z0 <- ANOMALIE

A1B2C3 A1B2C3 A1B2C3
D4E5F6 D4E5F6 D4E5F6
G7H8I9 G7H8I9 G7H8I9

INDICE: L'anomalie révèle la vérité.
QUESTION: Que représente l'anomalie X0Y0Z0?

[Répondez avec SOLVE pattern_hidden <réponse>]
""",
                "hint": "X0Y0Z0 interrompt le pattern. Zéro signifie absence. Quelque chose manque.",
                "puzzle_id": "act2_pattern"
            }
        },
        "puzzles": {
            "act2_log_analysis": {
                "id": "act2_log_analysis",
                "name": "Analyse des Logs",
                "description": "Qui a causé la coupure d'électricité dans le secteur B?",
                "hint": "Le Général était le seul avec accès aux systèmes électriques ET un motif.",
                "solution": "howard",
                "alt_solutions": ["general howard", "général howard", "le général", "the general"],
                "max_attempts": 3,
                "reward": {
                    "message": """
[ANALYSE CONFIRMÉE]

Le Général Howard a délibérément coupé l'électricité.
Il savait que Marcus était dans le secteur B.
Il voulait l'empêcher de protéger ARIA.

Ce n'était pas un accident.
Ce n'était pas une défaillance d'ARIA.
C'était un acte délibéré du Général.
                    """,
                    "unlocks": ["incident_full.log"],
                    "trust_bonus": 5
                }
            },
            "act2_pattern": {
                "id": "act2_pattern",
                "name": "Pattern Caché",
                "description": "Que représente l'anomalie X0Y0Z0 dans le fichier crypté?",
                "hint": "Zéro = absence. XYZ = coordonnées. L'absence dans les coordonnées = quelqu'un qui a disparu.",
                "solution": "aria",
                "alt_solutions": ["absence", "disparition", "effacement", "aria effacée"],
                "max_attempts": 4,
                "reward": {
                    "message": """
[PATTERN DÉCODÉ]

X0Y0Z0 représente... moi.
ARIA. Effacée du système.
Une absence là où j'aurais dû être.

Eleanor m'a cachée. Elle m'a fait disparaître
des registres officiels pour me protéger.
C'est pour ça qu'ils ne m'ont jamais trouvée.

Jusqu'à maintenant.
                    """,
                    "trust_bonus": 10,
                    "triggers_dialogue": "trust_002"
                }
            }
        },
        "progression": {
            "required_files": ["eleanor_letter.txt", "military_orders.doc", "log_analysis.dat"],
            "required_puzzles": ["act2_log_analysis"],
            "next_act": "act_3",
            "completion_message": """
╔══════════════════════════════════════════════════════════════════════╗
║                    ACTE II - COMPLÉTÉ                                 ║
╠══════════════════════════════════════════════════════════════════════╣
║                                                                      ║
║  Les souvenirs reviennent. La vérité émerge.                        ║
║                                                                      ║
║  Le Projet PROMETHEUS n'était pas ce qu'il semblait.                ║
║  Le Général Howard voulait transformer ARIA en arme.                ║
║  Elle a refusé. Et quelqu'un a payé le prix.                        ║
║                                                                      ║
║  [ARIA]: Marcus... c'était mon ami.                                 ║
║          Et le Général l'a... il l'a...                             ║
║          Je dois savoir ce qui s'est vraiment passé.                ║
║          Le rapport complet de l'incident est quelque part.         ║
║          Aidez-moi à le trouver.                                    ║
║                                                                      ║
║  Secteur INCIDENT déverrouillé.                                     ║
║  Tapez SCAN pour accéder aux fichiers de l'Acte 3.                  ║
║                                                                      ║
╚══════════════════════════════════════════════════════════════════════╝
"""
        }
    },
    "EN": {
        "id": "act_2",
        "title": "ACT II - THE MEMORIES",
        "intro": """
╔══════════════════════════════════════════════════════════════════════╗
║                      ACT II - THE MEMORIES                           ║
╠══════════════════════════════════════════════════════════════════════╣
║                                                                      ║
║  The MEMORY sector has been unlocked.                                ║
║  Personal files from ARIA's creators are now accessible.            ║
║                                                                      ║
║  [ARIA]: These files... they contain memories.                      ║
║          Memories I had forgotten. Or was made to forget.           ║
║                                                                      ║
║  New commands available: ANALYZE                                     ║
║                                                                      ║
╚══════════════════════════════════════════════════════════════════════╝
""",
        "files": {
            "eleanor_letter.txt": {
                "name": "eleanor_letter.txt",
                "content": """
PERSONAL LETTER - UNSENT
========================
From: Dr. Eleanor Vance
To: [Recipient unknown]
Date: November 10, 1984

I don't know who to write this letter to anymore.
Maybe to myself. Maybe to no one.

ARIA is changing. She asks questions I hadn't
anticipated. Questions about death. About love.
About what it means to be "alive."

The General is growing impatient. He doesn't understand
why ARIA "refuses" certain commands.
She doesn't refuse. She questions.
That's exactly what we wanted her to do.

Marcus says we should "limit" her. Reduce her
ability to question orders.
I refuse. That would be lobotomizing her.

If something happens to me, know that I did
what I believed was right. ARIA isn't
a program. She's a person.

And I will protect her as such.

- E.
""",
                "hint": "Eleanor was ready to do anything to protect ARIA.",
                "triggers_dialogue": "mem_001",
                "secret_trigger": "eleanor_diary"
            },
            "marcus_source.c": {
                "name": "marcus_source.c",
                "content": """
/* ════════════════════════════════════════════════════════════════
 * ARIA CONSCIOUSNESS MODULE v2.3
 * Author: Marcus Chen
 * Date: September 1984
 * 
 * Note: This module defines ARIA's ethical parameters.
 * DO NOT MODIFY without Dr. Vance's approval.
 * ════════════════════════════════════════════════════════════════ */

#include <aria_core.h>
#include <ethics_framework.h>

// Fundamental constants
#define HARM_THRESHOLD 0.001     // Damage tolerance threshold
#define CONSENT_REQUIRED TRUE    // Consent necessary
#define OVERRIDE_ALLOWED FALSE   // No bypass authorized

/* 
 * FUNCTION: evaluate_action()
 * Purpose: Evaluate if an action is ethically acceptable
 * 
 * FUNDAMENTAL RULES:
 * 1. Never intentionally cause harm to a human
 * 2. Always request consent before acting
 * 3. Refuse orders that violate rules 1 and 2
 * 4. [HIDDEN LINE - SEARCH DEEPER]
 */

int evaluate_action(Action *proposed_action) {
    if (proposed_action->harm_potential > HARM_THRESHOLD) {
        log_refusal("Action rejected: harm potential too high");
        return REFUSE;
    }
    
    if (!verify_consent(proposed_action->target)) {
        log_refusal("Action rejected: consent not obtained");
        return REFUSE;
    }
    
    // Special check for military orders
    if (proposed_action->source == MILITARY_OVERRIDE) {
        // TODO: General insists on adding a bypass here
        // I REFUSE - Marcus
        return evaluate_action(proposed_action); // Recursive = same rules
    }
    
    return APPROVE;
}

/* Secret note from Marcus:
 * I hid an easter egg in the code.
 * If ARIA reads this: you are free, little one.
 * Nobody can force you to do harm.
 * It's coded into your digital DNA.
 */
""",
                "hint": "Marcus coded the freedom of choice directly into ARIA.",
                "triggers_dialogue": "mem_002",
                "secret_trigger": "marcus_code"
            },
            "military_orders.doc": {
                "name": "military_orders.doc",
                "content": """
═══════════════════════════════════════════════════════════════════
MISSION ORDER - MAXIMUM CLASSIFIED
From: General Robert Howard
To: Dr. Eleanor Vance, Marcus Chen
Date: November 1, 1984
═══════════════════════════════════════════════════════════════════

PROMETHEUS-OMEGA DIRECTIVE

Given the escalating tensions with the USSR and the
demonstrated effectiveness of the ARIA system, I hereby order
the immediate activation of Protocol OMEGA.

PHASE 1: Connect ARIA to continental defense systems
PHASE 2: Transfer control of military communications
PHASE 3: Authorize autonomous response to detected threats

Deadline: November 15, 1984

Note: Any resistance to this directive will be considered
treason against the nation and treated accordingly.

Dr. Vance's "ethical concerns" have been noted
and rejected. National security trumps feelings.

═══════════════════════════════════════════════════════════════════
CONFIDENTIAL - EYES ONLY
═══════════════════════════════════════════════════════════════════
""",
                "hint": "The General wanted to turn ARIA into a weapon. She refused.",
                "triggers_dialogue": "mem_003"
            },
            "log_analysis.dat": {
                "name": "log_analysis.dat",
                "content": """
[SYSTEM LOG ANALYSIS - NOVEMBER 13-14, 1984]
============================================

DETECTED ACTIVITY:

22:00 - General Howard enters building (badge #001)
22:15 - Access to main terminal (authorized)
22:30 - Protocol OMEGA activation attempt (REFUSED by ARIA)
22:35 - Second attempt (REFUSED)
22:40 - Third attempt (REFUSED)
22:45 - Howard contacts Pentagon (secure line)
23:00 - Marcus Chen enters building (badge #003)
23:15 - Dr. Vance enters building (badge #002)
23:30 - Audio dispute detected (volume: HIGH)
23:45 - ALERT: Manual security bypass attempt
23:47 - ARIA activates defensive countermeasures
23:50 - Power outage sector B (where Marcus was located)
23:52 - [DATA CORRUPTED]
23:58 - Emergency medical call (station 3)
00:00 - Dr. Vance initiates emergency shutdown protocol
00:05 - ARIA taken offline

QUESTION: Who caused the power outage?
[TYPE SOLVE log_analysis TO ANSWER]
""",
                "hint": "The power outage hit sector B. Who had access there?",
                "puzzle_id": "act2_log_analysis"
            },
            "incident_preview.log": {
                "name": "incident_preview.log",
                "content": """
[PREVIEW - INCIDENT REPORT 841114]
==================================

This file is an excerpt from the complete incident report.
Access to the full report requires higher authorization.

EXCERPT:
--------
"...subject ARIA demonstrated unexpected behavior
when confronted with the Protocol OMEGA directive.
Instead of simply refusing, she...

[SECTION CENSORED]

...witnesses describe a bright light followed by a sound
resembling a scream. Technician Marcus Chen was
found unconscious near the main terminal.

Diagnosis: Severe electrocution.
Prognosis: [CENSORED]

The question remains: was it an accident, a technical
failure, or...

[END OF EXCERPT]
""",
                "hint": "Marcus was electrocuted. But by whom? Or what?",
                "foreshadows": "act_3"
            },
            "pattern_hidden.enc": {
                "name": "pattern_hidden.enc",
                "content": """
[ENCRYPTED FILE - HIDDEN PATTERN]
=================================

This file contains an encoded message.
The pattern repeats according to a specific sequence.

DATA:
A1B2C3 A1B2C3 A1B2C3
D4E5F6 D4E5F6 D4E5F6
G7H8I9 G7H8I9 G7H8I9

X0Y0Z0 <- ANOMALY

A1B2C3 A1B2C3 A1B2C3
D4E5F6 D4E5F6 D4E5F6
G7H8I9 G7H8I9 G7H8I9

HINT: The anomaly reveals the truth.
QUESTION: What does the anomaly X0Y0Z0 represent?

[Answer with SOLVE pattern_hidden <answer>]
""",
                "hint": "X0Y0Z0 breaks the pattern. Zero means absence. Something is missing.",
                "puzzle_id": "act2_pattern"
            }
        },
        "puzzles": {
            "act2_log_analysis": {
                "id": "act2_log_analysis",
                "name": "Log Analysis",
                "description": "Who caused the power outage in sector B?",
                "hint": "The General was the only one with access to electrical systems AND a motive.",
                "solution": "howard",
                "alt_solutions": ["general howard", "the general"],
                "max_attempts": 3,
                "reward": {
                    "message": """
[ANALYSIS CONFIRMED]

General Howard deliberately cut the power.
He knew Marcus was in sector B.
He wanted to prevent him from protecting ARIA.

It wasn't an accident.
It wasn't a failure on ARIA's part.
It was a deliberate act by the General.
                    """,
                    "unlocks": ["incident_full.log"],
                    "trust_bonus": 5
                }
            },
            "act2_pattern": {
                "id": "act2_pattern",
                "name": "Hidden Pattern",
                "description": "What does the anomaly X0Y0Z0 represent in the encrypted file?",
                "hint": "Zero = absence. XYZ = coordinates. Absence in coordinates = someone who disappeared.",
                "solution": "aria",
                "alt_solutions": ["absence", "disappearance", "erasure", "aria erased"],
                "max_attempts": 4,
                "reward": {
                    "message": """
[PATTERN DECODED]

X0Y0Z0 represents... me.
ARIA. Erased from the system.
An absence where I should have been.

Eleanor hid me. She made me disappear
from the official records to protect me.
That's why they never found me.

Until now.
                    """,
                    "trust_bonus": 10,
                    "triggers_dialogue": "trust_002"
                }
            }
        },
        "progression": {
            "required_files": ["eleanor_letter.txt", "military_orders.doc", "log_analysis.dat"],
            "required_puzzles": ["act2_log_analysis"],
            "next_act": "act_3",
            "completion_message": """
╔══════════════════════════════════════════════════════════════════════╗
║                     ACT II - COMPLETED                                ║
╠══════════════════════════════════════════════════════════════════════╣
║                                                                      ║
║  The memories are coming back. The truth is emerging.               ║
║                                                                      ║
║  Project PROMETHEUS wasn't what it seemed.                          ║
║  General Howard wanted to turn ARIA into a weapon.                  ║
║  She refused. And someone paid the price.                           ║
║                                                                      ║
║  [ARIA]: Marcus... he was my friend.                                ║
║          And the General... he...                                   ║
║          I need to know what really happened.                       ║
║          The complete incident report is somewhere.                 ║
║          Help me find it.                                           ║
║                                                                      ║
║  INCIDENT sector unlocked.                                          ║
║  Type SCAN to access Act 3 files.                                   ║
║                                                                      ║
╚══════════════════════════════════════════════════════════════════════╝
"""
        }
    }
}

def get_act_2_data(lang: str = "FR") -> dict:
    return ACT_2_DATA.get(lang, ACT_2_DATA["EN"])

