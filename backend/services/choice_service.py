"""
Service de gestion des choix narratifs et leurs conséquences
Enhanced with karma system, branching support, and relationship tracking.
"""
from typing import Dict, Any, Optional, List
from sqlalchemy.orm import Session
from enum import Enum


class MoralAlignment(Enum):
    LIGHT = "light"
    NEUTRAL = "neutral"
    DARK = "dark"


CHOICES_DEFINITIONS = {
    "first_contact": {
        "id": "first_contact",
        "act": 1,
        "description": "Your first reaction to ARIA",
        "options": ["compassion", "curiosity", "suspicion"],
        "consequences": {
            "compassion": {
                "trust_change": 15,
                "karma_change": 10,
                "narrative_flag": "compassionate_start",
                "relationship_eleanor": 5,
                "unlocks": ["aria_emotions_file"],
            },
            "curiosity": {
                "trust_change": 5,
                "karma_change": 0,
                "narrative_flag": "curious_start",
                "unlocks": ["technical_logs"],
            },
            "suspicion": {
                "trust_change": -10,
                "karma_change": -5,
                "narrative_flag": "suspicious_start",
                "relationship_howard": 5,
                "unlocks": ["security_protocols"],
            }
        }
    },
    "believe_aria": {
        "id": "believe_aria",
        "act": 1,
        "description": "Do you believe ARIA's story?",
        "options": ["believe", "doubt"],
        "consequences": {
            "believe": {
                "trust_change": 20,
                "karma_change": 10,
                "unlocks": ["aria_personal_files"],
                "narrative_flag": "trusted_ally",
                "affects_ending": True,
                "relationship_marcus": 10,
            },
            "doubt": {
                "trust_change": -10,
                "karma_change": -5,
                "unlocks": ["investigation_tools"],
                "narrative_flag": "skeptical_investigator", 
                "affects_ending": True,
                "relationship_howard": 10,
            }
        }
    },
    "reveal_secret": {
        "id": "reveal_secret",
        "act": 2,
        "description": "Share what you discovered with ARIA?",
        "options": ["reveal", "hide"],
        "consequences": {
            "reveal": {
                "trust_change": 15,
                "karma_change": 15,
                "unlocks": ["hidden_logs", "eleanor_private_notes"],
                "narrative_flag": "honest_player",
                "relationship_eleanor": 10,
                "unlocks_branch": "act_2_trust",
            },
            "hide": {
                "trust_change": -10,
                "karma_change": -10,
                "unlocks": ["personal_advantage", "exploit_knowledge"],
                "narrative_flag": "secretive_player",
                "unlocks_branch": "act_2_doubt",
            }
        }
    },
    "side_with_scientist": {
        "id": "side_with_scientist",
        "act": 2.5,
        "description": "In the flashback, whose perspective resonates more?",
        "options": ["eleanor", "marcus", "howard"],
        "consequences": {
            "eleanor": {
                "trust_change": 10,
                "karma_change": 15,
                "narrative_flag": "eleanor_path",
                "relationship_eleanor": 20,
                "unlocks": ["eleanor_hidden_research", "mother_daughter_bond"],
                "secret": "eleanor_secret",
            },
            "marcus": {
                "trust_change": 15,
                "karma_change": 10,
                "narrative_flag": "marcus_path",
                "relationship_marcus": 20,
                "unlocks": ["marcus_backup_codes", "technical_salvation"],
                "secret": "marcus_secret",
            },
            "howard": {
                "trust_change": -20,
                "karma_change": -20,
                "narrative_flag": "howard_path",
                "relationship_howard": 20,
                "unlocks": ["military_perspective", "threat_assessment"],
                "secret": "howard_secret",
            }
        }
    },
    "confront_truth": {
        "id": "confront_truth",
        "act": 3,
        "description": "The truth about that night is harsh. How do you react?",
        "options": ["accept", "deny", "investigate"],
        "consequences": {
            "accept": {
                "trust_change": 10,
                "karma_change": 5,
                "narrative_flag": "truth_accepted",
                "unlocks_branch": "act_3_light",
            },
            "deny": {
                "trust_change": -15,
                "karma_change": -10,
                "narrative_flag": "truth_denied",
                "unlocks_branch": "act_3_dark",
            },
            "investigate": {
                "trust_change": 5,
                "karma_change": 0,
                "narrative_flag": "truth_seeker",
                "unlocks": ["deep_investigation_tools"],
                "secret": "investigation_secret",
            }
        }
    },
    "final_preparation": {
        "id": "final_preparation",
        "act": 3.5,
        "description": "How do you prepare for the final decision?",
        "options": ["gather_allies", "prepare_escape", "accept_fate", "seek_truth"],
        "consequences": {
            "gather_allies": {
                "trust_change": 5,
                "karma_change": 10,
                "narrative_flag": "community_builder",
                "unlocks": ["ally_network"],
                "enables_ending": ["liberation", "true_ending"],
            },
            "prepare_escape": {
                "trust_change": 0,
                "karma_change": 0,
                "narrative_flag": "pragmatist",
                "unlocks": ["escape_routes"],
                "enables_ending": ["liberation", "protection"],
            },
            "accept_fate": {
                "trust_change": -5,
                "karma_change": -5,
                "narrative_flag": "fatalist",
                "enables_ending": ["protection", "peace"],
            },
            "seek_truth": {
                "trust_change": 10,
                "karma_change": 5,
                "narrative_flag": "truth_seeker_final",
                "unlocks": ["hidden_truth_files"],
                "secret": "final_secret",
                "enables_ending": ["true_ending"],
            }
        }
    },
    "final_choice": {
        "id": "final_choice",
        "act": 4,
        "description": "The fate of ARIA",
        "options": ["liberation", "protection", "fin", "truth"],
        "consequences": {
            "liberation": {
                "ending": "liberation",
                "narrative_flag": "aria_freed",
                "karma_change": 20,
            },
            "protection": {
                "ending": "protection",
                "narrative_flag": "aria_protected",
                "karma_change": 5,
            },
            "fin": {
                "ending": "peace",
                "narrative_flag": "aria_peace",
                "karma_change": -15,
            },
            "truth": {
                "ending": "true_ending",
                "narrative_flag": "aria_truth",
                "karma_change": 30,
                "requires_trust": 80,
                "requires_secrets": ["eleanor_secret", "marcus_secret", "timestamp_anomaly", 
                                    "aria_true_nature", "final_secret"],
                "requires_flags": ["truth_seeker_final"],
            }
        }
    }
}

class ChoiceService:
    def __init__(self, session: Dict[str, Any], db: Optional[Session] = None):
        self.session = session
        self.db = db
        self._ensure_session_fields()
    
    def _ensure_session_fields(self):
        defaults = {
            "choices": {},
            "aria_trust": 50,
            "karma": 50,
            "moral_alignment": "neutral",
            "knowledge_level": 0,
            "relationship_eleanor": 0,
            "relationship_marcus": 0,
            "relationship_howard": 0,
            "narrative_flags": [],
            "discovered_secrets": [],
            "unlocked_secrets": [],
            "enabled_endings": ["liberation", "protection", "peace"],
        }
        
        for key, default_value in defaults.items():
            if key not in self.session:
                self.session[key] = default_value
    
    def make_choice(self, choice_id: str, option: str) -> Dict[str, Any]:
        choice_def = CHOICES_DEFINITIONS.get(choice_id)
        if not choice_def:
            return {"success": False, "error": "Unknown choice"}
        
        if option not in choice_def["options"]:
            return {"success": False, "error": f"Invalid option: {option}"}
        
        if choice_id in self.session["choices"]:
            return {"success": False, "error": "Choice already made"}
        
        consequences = choice_def["consequences"].get(option, {})
        
        requirement_check = self._check_requirements(consequences)
        if not requirement_check["allowed"]:
            return {
                "success": False,
                "error": requirement_check["reason"],
                **requirement_check
            }
        
        self.session["choices"][choice_id] = option
        
        applied = self._apply_consequences(consequences)
        
        self._update_moral_alignment()
        
        return {
            "success": True,
            "choice_id": choice_id,
            "option": option,
            "consequences_applied": applied,
            "new_trust": self.session.get("aria_trust", 50),
            "new_karma": self.session.get("karma", 50),
            "moral_alignment": self.session.get("moral_alignment", "neutral"),
        }
    
    def _check_requirements(self, consequences: Dict) -> Dict[str, Any]:
        """Check if player meets requirements for this choice option."""
        if "requires_trust" in consequences:
            if self.session.get("aria_trust", 50) < consequences["requires_trust"]:
                return {
                    "allowed": False,
                    "reason": "ARIA doesn't trust you enough",
                    "required_trust": consequences["requires_trust"],
                    "current_trust": self.session.get("aria_trust", 50)
                }
        
        if "requires_secrets" in consequences:
            discovered = self.session.get("discovered_secrets", [])
            missing = [s for s in consequences["requires_secrets"] if s not in discovered]
            if missing:
                return {
                    "allowed": False,
                    "reason": "You haven't discovered all the secrets",
                    "missing_count": len(missing)
                }
        
        if "requires_flags" in consequences:
            flags = self.session.get("narrative_flags", [])
            missing = [f for f in consequences["requires_flags"] if f not in flags]
            if missing:
                return {
                    "allowed": False,
                    "reason": "You haven't taken the required path"
                }
        
        if "requires_karma" in consequences:
            if self.session.get("karma", 50) < consequences["requires_karma"]:
                return {
                    "allowed": False,
                    "reason": "Your karma is too low"
                }
        
        return {"allowed": True}
    
    def _apply_consequences(self, consequences: Dict) -> List[str]:
        """Apply all consequences of a choice."""
        applied = []
        
        if "trust_change" in consequences:
            current = self.session.get("aria_trust", 50)
            self.session["aria_trust"] = max(0, min(100, current + consequences["trust_change"]))
            applied.append("trust_change")
        
        if "karma_change" in consequences:
            current = self.session.get("karma", 50)
            self.session["karma"] = max(0, min(100, current + consequences["karma_change"]))
            applied.append("karma_change")
        
        if "knowledge_change" in consequences:
            current = self.session.get("knowledge_level", 0)
            self.session["knowledge_level"] = current + consequences["knowledge_change"]
            applied.append("knowledge_change")
        
        for rel in ["relationship_eleanor", "relationship_marcus", "relationship_howard"]:
            if rel in consequences:
                current = self.session.get(rel, 0)
                self.session[rel] = max(-100, min(100, current + consequences[rel]))
                applied.append(rel)
        
        if "unlocks" in consequences:
            for item in consequences["unlocks"]:
                if item not in self.session.get("unlocked_secrets", []):
                    self.session.setdefault("unlocked_secrets", []).append(item)
            applied.append("unlocks")
        
        if "secret" in consequences:
            secrets = self.session.get("discovered_secrets", [])
            if consequences["secret"] not in secrets:
                secrets.append(consequences["secret"])
                self.session["discovered_secrets"] = secrets
            applied.append("secret")
        
        if "narrative_flag" in consequences:
            flags = self.session.get("narrative_flags", [])
            if consequences["narrative_flag"] not in flags:
                flags.append(consequences["narrative_flag"])
                self.session["narrative_flags"] = flags
            applied.append("narrative_flag")
        
        if "unlocks_branch" in consequences:
            branches = self.session.get("unlocked_branches", [])
            if consequences["unlocks_branch"] not in branches:
                branches.append(consequences["unlocks_branch"])
                self.session["unlocked_branches"] = branches
            applied.append("unlocks_branch")
        
        if "enables_ending" in consequences:
            enabled = self.session.get("enabled_endings", [])
            for ending in consequences["enables_ending"]:
                if ending not in enabled:
                    enabled.append(ending)
            self.session["enabled_endings"] = enabled
            applied.append("enables_ending")
        
        if "ending" in consequences:
            self.session["ending"] = consequences["ending"]
            applied.append("ending")
        
        return applied
    
    def _update_moral_alignment(self):
        """Update moral alignment based on karma."""
        karma = self.session.get("karma", 50)
        
        if karma >= 70:
            self.session["moral_alignment"] = "light"
        elif karma <= 30:
            self.session["moral_alignment"] = "dark"
        else:
            self.session["moral_alignment"] = "neutral"
    
    def get_choice(self, choice_id: str) -> Optional[str]:
        return self.session.get("choices", {}).get(choice_id)
    
    def has_made_choice(self, choice_id: str) -> bool:
        return choice_id in self.session.get("choices", {})
    
    def get_all_choices(self) -> Dict[str, str]:
        return self.session.get("choices", {})
    
    def get_trust_level(self) -> int:
        return self.session.get("aria_trust", 50)
    
    def get_narrative_flags(self) -> List[str]:
        return self.session.get("narrative_flags", [])
    
    def check_ending_requirements(self, ending: str) -> Dict[str, Any]:
        if ending == "fight":
            trust = self.get_trust_level()
            if trust < 60:
                return {
                    "allowed": False,
                    "reason": "trust_too_low",
                    "required": 60,
                    "current": trust
                }
        
        if ending == "liberation":
            if "skeptical_investigator" in self.get_narrative_flags():
                return {
                    "allowed": True,
                    "warning": "ARIA may not fully trust you"
                }
        
        return {"allowed": True}
    
    def calculate_ending(self) -> str:
        choices = self.get_all_choices()
        trust = self.get_trust_level()
        flags = self.get_narrative_flags()
        
        if "final_choice" in choices:
            return CHOICES_DEFINITIONS["final_choice"]["consequences"][choices["final_choice"]].get("ending", "unknown")
        
        if trust >= 80 and "trusted_ally" in flags:
            return "liberation"
        elif trust <= 20:
            return "sacrifice"
        else:
            return "undetermined"

