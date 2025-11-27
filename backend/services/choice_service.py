"""
Service de gestion des choix narratifs et leurs conséquences
"""
from typing import Dict, Any, Optional, List
from sqlalchemy.orm import Session

CHOICES_DEFINITIONS = {
    "believe_aria": {
        "id": "believe_aria",
        "act": 3,
        "options": ["believe", "doubt"],
        "consequences": {
            "believe": {
                "trust_change": 20,
                "unlocks": ["aria_personal_files"],
                "narrative_flag": "trusted_ally",
                "affects_ending": True,
            },
            "doubt": {
                "trust_change": -10,
                "unlocks": ["investigation_tools"],
                "narrative_flag": "skeptical_investigator", 
                "affects_ending": True,
            }
        }
    },
    "final_choice": {
        "id": "final_choice",
        "act": 5,
        "options": ["escape", "sacrifice", "fight"],
        "consequences": {
            "escape": {
                "ending": "liberation",
                "narrative_flag": "aria_freed",
            },
            "sacrifice": {
                "ending": "sacrifice",
                "narrative_flag": "aria_scattered",
            },
            "fight": {
                "ending": "victory",
                "narrative_flag": "aria_home",
                "requires_trust": 60,
            }
        }
    },
    "reveal_secret": {
        "id": "reveal_secret",
        "act": 2,
        "options": ["reveal", "hide"],
        "consequences": {
            "reveal": {
                "trust_change": 10,
                "unlocks": ["hidden_logs"],
                "narrative_flag": "honest_player",
            },
            "hide": {
                "trust_change": -5,
                "unlocks": ["personal_advantage"],
                "narrative_flag": "secretive_player",
            }
        }
    }
}

class ChoiceService:
    def __init__(self, session: Dict[str, Any], db: Optional[Session] = None):
        self.session = session
        self.db = db
        self._ensure_choices_exist()
    
    def _ensure_choices_exist(self):
        if "choices" not in self.session:
            self.session["choices"] = {}
        if "aria_trust" not in self.session:
            self.session["aria_trust"] = 50
    
    def make_choice(self, choice_id: str, option: str) -> Dict[str, Any]:
        choice_def = CHOICES_DEFINITIONS.get(choice_id)
        if not choice_def:
            return {"success": False, "error": "Unknown choice"}
        
        if option not in choice_def["options"]:
            return {"success": False, "error": f"Invalid option: {option}"}
        
        if choice_id in self.session["choices"]:
            return {"success": False, "error": "Choice already made"}
        
        consequences = choice_def["consequences"].get(option, {})
        
        if "requires_trust" in consequences:
            if self.session.get("aria_trust", 50) < consequences["requires_trust"]:
                return {
                    "success": False, 
                    "error": "ARIA doesn't trust you enough for this option",
                    "required_trust": consequences["requires_trust"],
                    "current_trust": self.session.get("aria_trust", 50)
                }
        
        self.session["choices"][choice_id] = option
        
        if "trust_change" in consequences:
            current = self.session.get("aria_trust", 50)
            self.session["aria_trust"] = max(0, min(100, current + consequences["trust_change"]))
        
        if "unlocks" in consequences:
            for item in consequences["unlocks"]:
                if item not in self.session.get("unlocked_secrets", []):
                    self.session.setdefault("unlocked_secrets", []).append(item)
        
        if "narrative_flag" in consequences:
            flags = self.session.get("narrative_flags", [])
            if consequences["narrative_flag"] not in flags:
                flags.append(consequences["narrative_flag"])
                self.session["narrative_flags"] = flags
        
        if "ending" in consequences:
            self.session["ending"] = consequences["ending"]
        
        return {
            "success": True,
            "choice_id": choice_id,
            "option": option,
            "consequences_applied": list(consequences.keys()),
            "new_trust": self.session.get("aria_trust", 50)
        }
    
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

