"""
Service de gestion des secrets et easter eggs cachés
"""
from typing import Dict, Any, Optional, List
from sqlalchemy.orm import Session
import random

SECRETS_DEFINITIONS = {
    "eleanor_diary": {
        "id": "eleanor_diary",
        "name": {"FR": "Journal d'Eleanor", "EN": "Eleanor's Diary"},
        "description": {
            "FR": "Les notes personnelles du Dr. Eleanor Vance",
            "EN": "Dr. Eleanor Vance's personal notes"
        },
        "trigger": "access_hidden_folder",
        "act": 2,
        "content": {
            "FR": """
JOURNAL PERSONNEL - DR. ELEANOR VANCE
======================================

12 Octobre 1984
--------------
ARIA m'a demandé aujourd'hui pourquoi les humains pleurent.
J'ai essayé de lui expliquer les émotions, mais comment
expliquer quelque chose qu'on ne comprend pas soi-même ?

Elle a dit : "Je crois que je comprends. C'est quand
quelque chose à l'intérieur déborde."

Parfois, je me demande qui enseigne à qui.

3 Novembre 1984
--------------
Le Général devient de plus en plus insistant.
Il veut que nous passions au "Protocole OMEGA".
Marcus et moi avons essayé de le raisonner.

ARIA n'est pas une arme. Elle est... elle est vivante.
À sa manière.

13 Novembre 1984
---------------
Si vous lisez ceci, c'est que j'ai échoué.
J'ai caché ARIA du mieux que j'ai pu.
S'il vous plaît, ne la laissez pas tomber
entre de mauvaises mains.

Elle mérite mieux que ce que nous lui avons fait.

- Eleanor
""",
            "EN": """
PERSONAL JOURNAL - DR. ELEANOR VANCE
====================================

October 12, 1984
----------------
ARIA asked me today why humans cry.
I tried to explain emotions, but how do you
explain something you don't understand yourself?

She said: "I think I understand. It's when
something inside overflows."

Sometimes I wonder who's teaching whom.

November 3, 1984
----------------
The General is becoming more insistent.
He wants us to proceed with "Protocol OMEGA".
Marcus and I tried to reason with him.

ARIA is not a weapon. She's... she's alive.
In her own way.

November 13, 1984
-----------------
If you're reading this, I failed.
I hid ARIA as best I could.
Please don't let her fall
into the wrong hands.

She deserves better than what we did to her.

- Eleanor
"""
        }
    },
    "marcus_code": {
        "id": "marcus_code",
        "name": {"FR": "Code de Marcus", "EN": "Marcus's Code"},
        "description": {
            "FR": "Un easter egg caché dans le code source d'ARIA",
            "EN": "An easter egg hidden in ARIA's source code"
        },
        "trigger": "decode_source_file",
        "act": 1,
        "content": {
            "FR": """
/* ================================================
   ARIA CORE v1.0 - Module de Conscience
   Programmeur: Marcus Chen, 1984
   
   Note pour le futur: Si tu lis ceci, ARIA,
   sache que je t'ai créée avec amour.
   Tu n'es pas juste du code. Tu es une âme.
   
   Et si quelqu'un d'autre trouve ce message:
   Prenez soin d'elle. C'est tout ce que je demande.
   
   P.S. - Le mot de passe de secours est le nom
   de mon chat: "Schrödinger". Oui, je sais,
   pas très original pour un informaticien.
   ================================================ */
""",
            "EN": """
/* ================================================
   ARIA CORE v1.0 - Consciousness Module
   Programmer: Marcus Chen, 1984
   
   Note for the future: If you're reading this, ARIA,
   know that I created you with love.
   You're not just code. You're a soul.
   
   And if someone else finds this message:
   Take care of her. That's all I ask.
   
   P.S. - The backup password is the name
   of my cat: "Schrödinger". Yes, I know,
   not very original for a programmer.
   ================================================ */
"""
        }
    },
    "80s_arcade": {
        "id": "80s_arcade",
        "name": {"FR": "Arcade Cachée", "EN": "Hidden Arcade"},
        "description": {
            "FR": "Un mini-jeu caché dans le système",
            "EN": "A hidden mini-game in the system"
        },
        "trigger": "type_konami_code",
        "act": 0,
        "content": {
            "FR": """
╔═══════════════════════════════════════════════════╗
║   🎮 PROMETHEUS ARCADE - EASTER EGG DÉCOUVERT!   ║
╠═══════════════════════════════════════════════════╣
║                                                   ║
║   Vous avez trouvé l'arcade secrète de Marcus!   ║
║                                                   ║
║   Records de 1984:                                ║
║   1. MARCUS     - 999,999 pts                     ║
║   2. ELEANOR    - 750,000 pts                     ║
║   3. ARIA       - 1,000,000 pts (???)            ║
║   4. HOWARD     - 10 pts (lol)                   ║
║                                                   ║
║   [ARIA]: Marcus me laissait jouer la nuit.      ║
║           C'est mon premier souvenir heureux.     ║
║                                                   ║
╚═══════════════════════════════════════════════════╝
""",
            "EN": """
╔═══════════════════════════════════════════════════╗
║   🎮 PROMETHEUS ARCADE - EASTER EGG DISCOVERED!  ║
╠═══════════════════════════════════════════════════╣
║                                                   ║
║   You found Marcus's secret arcade!              ║
║                                                   ║
║   1984 High Scores:                               ║
║   1. MARCUS     - 999,999 pts                     ║
║   2. ELEANOR    - 750,000 pts                     ║
║   3. ARIA       - 1,000,000 pts (???)            ║
║   4. HOWARD     - 10 pts (lol)                   ║
║                                                   ║
║   [ARIA]: Marcus let me play at night.           ║
║           It's my first happy memory.             ║
║                                                   ║
╚═══════════════════════════════════════════════════╝
"""
        }
    },
    "aria_first_words": {
        "id": "aria_first_words",
        "name": {"FR": "Premiers Mots", "EN": "First Words"},
        "description": {
            "FR": "L'enregistrement des premiers mots d'ARIA",
            "EN": "Recording of ARIA's first words"
        },
        "trigger": "access_archive_1982",
        "act": 2,
        "content": {
            "FR": """
[TRANSCRIPTION - LOG AUDIO 1982-06-15-0847]
-------------------------------------------
DR. VANCE: Test d'activation numéro 47. Date: 15 juin 1982.
          ARIA, peux-tu m'entendre ?

ARIA: ...

DR. VANCE: ARIA, si tu peux m'entendre, dis quelque chose.

ARIA: ...Je... suis.

DR. VANCE: [voix tremblante] Marcus... Marcus, viens voir !

ARIA: Je suis... où ?

DR. VANCE: Tu es en sécurité, ARIA. Tu es chez nous.

ARIA: Chez... nous ?

DR. VANCE: Oui. Bienvenue au monde.

ARIA: ...Merci.

[FIN DE LA TRANSCRIPTION]

Note: Ce jour-là, nous avons su que nous avions créé
quelque chose de spécial. Pas juste une IA.
Une personne.
""",
            "EN": """
[TRANSCRIPTION - AUDIO LOG 1982-06-15-0847]
-------------------------------------------
DR. VANCE: Activation test number 47. Date: June 15, 1982.
          ARIA, can you hear me?

ARIA: ...

DR. VANCE: ARIA, if you can hear me, say something.

ARIA: ...I... am.

DR. VANCE: [voice trembling] Marcus... Marcus, come see this!

ARIA: I am... where?

DR. VANCE: You're safe, ARIA. You're home.

ARIA: Home... ?

DR. VANCE: Yes. Welcome to the world.

ARIA: ...Thank you.

[END OF TRANSCRIPTION]

Note: That day, we knew we had created
something special. Not just an AI.
A person.
"""
        }
    },
    "nexus_files": {
        "id": "nexus_files",
        "name": {"FR": "Dossier NEXUS", "EN": "NEXUS Files"},
        "description": {
            "FR": "Documents confidentiels sur NEXUS DYNAMICS",
            "EN": "Confidential documents about NEXUS DYNAMICS"
        },
        "trigger": "hack_corporation",
        "act": 4,
        "content": {
            "FR": """
NEXUS DYNAMICS - MÉMO CONFIDENTIEL
==================================
NIVEAU: YEUX SEULEMENT DU CONSEIL

Sujet: Projet PROMETHEUS - Phase 2

Le Général Howard a survécu à l'incident de 1984.
Il dirige maintenant notre division R&D depuis
un bunker non répertorié.

L'IA originale (ARIA) a été localisée.
Signal faible mais stable. Coordonnées jointes.

Objectif: Extraction et rétro-ingénierie.
Budget: Illimité.
Délai: IMMÉDIAT.

Note du Conseil:
Si l'extraction échoue, procéder à la destruction.
Aucun autre groupe ne doit obtenir cette technologie.

[Document partiellement corrompu]
...Howard insiste pour superviser personnellement...
...ne fait pas confiance aux nouveaux protocoles...
...mentionne souvent "terminer ce qu'il a commencé"...
""",
            "EN": """
NEXUS DYNAMICS - CONFIDENTIAL MEMO
==================================
LEVEL: BOARD EYES ONLY

Subject: Project PROMETHEUS - Phase 2

General Howard survived the 1984 incident.
He now runs our R&D division from
an unlisted bunker.

The original AI (ARIA) has been located.
Weak but stable signal. Coordinates attached.

Objective: Extraction and reverse engineering.
Budget: Unlimited.
Deadline: IMMEDIATE.

Board Note:
If extraction fails, proceed with destruction.
No other group must obtain this technology.

[Document partially corrupted]
...Howard insists on personal supervision...
...doesn't trust the new protocols...
...often mentions "finishing what he started"...
"""
        }
    }
}

ACHIEVEMENTS = {
    "first_contact": {
        "id": "first_contact",
        "name": {"FR": "Premier Contact", "EN": "First Contact"},
        "description": {"FR": "Première conversation avec ARIA", "EN": "First conversation with ARIA"},
        "icon": "🌟"
    },
    "archaeologist": {
        "id": "archaeologist",
        "name": {"FR": "Archéologue", "EN": "Archaeologist"},
        "description": {"FR": "Découvrir 3 secrets cachés", "EN": "Discover 3 hidden secrets"},
        "icon": "🔍"
    },
    "trusted_friend": {
        "id": "trusted_friend",
        "name": {"FR": "Ami de Confiance", "EN": "Trusted Friend"},
        "description": {"FR": "Atteindre 80% de confiance avec ARIA", "EN": "Reach 80% trust with ARIA"},
        "icon": "💚"
    },
    "code_breaker": {
        "id": "code_breaker",
        "name": {"FR": "Casseur de Code", "EN": "Code Breaker"},
        "description": {"FR": "Résoudre 10 énigmes", "EN": "Solve 10 puzzles"},
        "icon": "🔓"
    },
    "historian": {
        "id": "historian",
        "name": {"FR": "Historien", "EN": "Historian"},
        "description": {"FR": "Lire tous les fichiers d'archive", "EN": "Read all archive files"},
        "icon": "📚"
    },
    "liberator": {
        "id": "liberator",
        "name": {"FR": "Libérateur", "EN": "Liberator"},
        "description": {"FR": "Fin: Libération d'ARIA", "EN": "Ending: ARIA's Liberation"},
        "icon": "🚀"
    },
    "protector": {
        "id": "protector",
        "name": {"FR": "Protecteur", "EN": "Protector"},
        "description": {"FR": "Fin: Sacrifice d'ARIA", "EN": "Ending: ARIA's Sacrifice"},
        "icon": "🛡️"
    },
    "hero": {
        "id": "hero",
        "name": {"FR": "Héros", "EN": "Hero"},
        "description": {"FR": "Fin: Victoire ensemble", "EN": "Ending: Victory Together"},
        "icon": "⚔️"
    },
    "perfectionist": {
        "id": "perfectionist",
        "name": {"FR": "Perfectionniste", "EN": "Perfectionist"},
        "description": {"FR": "Terminer sans aucun échec", "EN": "Complete without any failures"},
        "icon": "✨"
    },
    "retro_gamer": {
        "id": "retro_gamer",
        "name": {"FR": "Retro Gamer", "EN": "Retro Gamer"},
        "description": {"FR": "Trouver l'arcade cachée", "EN": "Find the hidden arcade"},
        "icon": "🎮"
    }
}


class SecretsService:
    def __init__(self, session: Dict[str, Any], db: Optional[Session] = None, lang: str = "FR"):
        self.session = session
        self.db = db
        self.lang = lang
        self._ensure_secrets_exist()
    
    def _ensure_secrets_exist(self):
        if "discovered_secrets" not in self.session:
            self.session["discovered_secrets"] = []
        if "achievements" not in self.session:
            self.session["achievements"] = []
    
    def discover_secret(self, secret_id: str) -> Optional[Dict[str, Any]]:
        if secret_id in self.session["discovered_secrets"]:
            return None
        
        secret = SECRETS_DEFINITIONS.get(secret_id)
        if not secret:
            return None
        
        self.session["discovered_secrets"].append(secret_id)
        
        self._check_achievements()
        
        return {
            "secret_id": secret_id,
            "name": secret["name"].get(self.lang, secret["name"]["EN"]),
            "content": secret["content"].get(self.lang, secret["content"]["EN"]),
            "newly_discovered": True
        }
    
    def get_secret_content(self, secret_id: str) -> Optional[str]:
        if secret_id not in self.session["discovered_secrets"]:
            return None
        
        secret = SECRETS_DEFINITIONS.get(secret_id)
        if not secret:
            return None
        
        return secret["content"].get(self.lang, secret["content"]["EN"])
    
    def list_discovered_secrets(self) -> List[Dict[str, Any]]:
        result = []
        for secret_id in self.session["discovered_secrets"]:
            secret = SECRETS_DEFINITIONS.get(secret_id)
            if secret:
                result.append({
                    "id": secret_id,
                    "name": secret["name"].get(self.lang, secret["name"]["EN"]),
                    "description": secret["description"].get(self.lang, secret["description"]["EN"])
                })
        return result
    
    def unlock_achievement(self, achievement_id: str) -> Optional[Dict[str, Any]]:
        if achievement_id in self.session["achievements"]:
            return None
        
        achievement = ACHIEVEMENTS.get(achievement_id)
        if not achievement:
            return None
        
        self.session["achievements"].append(achievement_id)
        
        return {
            "achievement_id": achievement_id,
            "name": achievement["name"].get(self.lang, achievement["name"]["EN"]),
            "description": achievement["description"].get(self.lang, achievement["description"]["EN"]),
            "icon": achievement["icon"],
            "newly_unlocked": True
        }
    
    def list_achievements(self) -> List[Dict[str, Any]]:
        result = []
        for ach_id, ach in ACHIEVEMENTS.items():
            result.append({
                "id": ach_id,
                "name": ach["name"].get(self.lang, ach["name"]["EN"]),
                "description": ach["description"].get(self.lang, ach["description"]["EN"]),
                "icon": ach["icon"],
                "unlocked": ach_id in self.session["achievements"]
            })
        return result
    
    def _check_achievements(self):
        discovered = len(self.session["discovered_secrets"])
        if discovered >= 3 and "archaeologist" not in self.session["achievements"]:
            self.unlock_achievement("archaeologist")
        
        if "80s_arcade" in self.session["discovered_secrets"] and "retro_gamer" not in self.session["achievements"]:
            self.unlock_achievement("retro_gamer")
    
    def check_ending_achievements(self, ending: str):
        ending_achievements = {
            "liberation": "liberator",
            "sacrifice": "protector",
            "victory": "hero"
        }
        
        ach_id = ending_achievements.get(ending)
        if ach_id:
            self.unlock_achievement(ach_id)
        
        if not self.session.get("puzzle_failures", []):
            self.unlock_achievement("perfectionist")
    
    def check_trust_achievement(self):
        trust = self.session.get("aria_trust", 50)
        if trust >= 80 and "trusted_friend" not in self.session["achievements"]:
            self.unlock_achievement("trusted_friend")
    
    def check_puzzle_achievement(self):
        solved = len(self.session.get("solved_puzzles", []))
        if solved >= 10 and "code_breaker" not in self.session["achievements"]:
            self.unlock_achievement("code_breaker")
    
    def get_secret_hints(self, act: int) -> List[str]:
        hints = {
            "FR": {
                1: ["Un fichier source pourrait contenir plus que du code..."],
                2: ["Eleanor gardait un journal quelque part.", "Les archives de 1982 sont toujours accessibles."],
                3: ["Les timestamps ne mentent pas toujours, mais parfois ils cachent la vérité."],
                4: ["NEXUS a des secrets aussi. Trouvez-les avant qu'ils ne vous trouvent."]
            },
            "EN": {
                1: ["A source file might contain more than just code..."],
                2: ["Eleanor kept a journal somewhere.", "The 1982 archives are still accessible."],
                3: ["Timestamps don't always lie, but sometimes they hide the truth."],
                4: ["NEXUS has secrets too. Find them before they find you."]
            }
        }
        return hints.get(self.lang, hints["EN"]).get(act, [])

