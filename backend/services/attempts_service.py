"""
Service de gestion des tentatives limitées pour les énigmes
"""
from typing import Dict, Any, Optional, Tuple
from sqlalchemy.orm import Session

MAX_ATTEMPTS_DEFAULT = 3

PUZZLE_ATTEMPTS_CONFIG = {
    "act1_crypto": {"max_attempts": 3, "penalty": "trust", "penalty_value": -5},
    "act1_timestamp": {"max_attempts": 3, "penalty": "trust", "penalty_value": -3},
    "act2_log_analysis": {"max_attempts": 3, "penalty": "corruption", "penalty_value": 1},
    "act2_pattern": {"max_attempts": 4, "penalty": "trust", "penalty_value": -5},
    "act3_forensics": {"max_attempts": 3, "penalty": "file_loss", "penalty_value": 1},
    "act3_timeline": {"max_attempts": 3, "penalty": "trust", "penalty_value": -10},
    "act4_firewall": {"max_attempts": 5, "penalty": "time", "penalty_value": 1},
    "act4_routing": {"max_attempts": 4, "penalty": "detection", "penalty_value": 1},
    "act5_final": {"max_attempts": 2, "penalty": "ending", "penalty_value": 1},
}

PENALTY_MESSAGES = {
    "FR": {
        "trust": "ARIA semble déçue. Votre relation en souffre.",
        "corruption": "Des fichiers se sont corrompus pendant la tentative.",
        "file_loss": "Un fichier important a été perdu.",
        "time": "NEXUS se rapproche. Le temps presse.",
        "detection": "Votre position a été partiellement révélée.",
        "ending": "Cette erreur aura des conséquences..."
    },
    "EN": {
        "trust": "ARIA seems disappointed. Your relationship suffers.",
        "corruption": "Files were corrupted during the attempt.",
        "file_loss": "An important file was lost.",
        "time": "NEXUS is getting closer. Time is running out.",
        "detection": "Your position has been partially revealed.",
        "ending": "This mistake will have consequences..."
    }
}

class AttemptsService:
    def __init__(self, session: Dict[str, Any], db: Optional[Session] = None, lang: str = "FR"):
        self.session = session
        self.db = db
        self.lang = lang
        self._ensure_attempts_exist()
    
    def _ensure_attempts_exist(self):
        if "puzzle_attempts" not in self.session:
            self.session["puzzle_attempts"] = {}
        if "puzzle_failures" not in self.session:
            self.session["puzzle_failures"] = []
        if "corruption_level" not in self.session:
            self.session["corruption_level"] = 0
        if "detection_level" not in self.session:
            self.session["detection_level"] = 0
    
    def get_remaining_attempts(self, puzzle_id: str) -> int:
        config = PUZZLE_ATTEMPTS_CONFIG.get(puzzle_id, {"max_attempts": MAX_ATTEMPTS_DEFAULT})
        used = self.session["puzzle_attempts"].get(puzzle_id, 0)
        return max(0, config["max_attempts"] - used)
    
    def use_attempt(self, puzzle_id: str) -> Tuple[bool, int, Optional[str]]:
        config = PUZZLE_ATTEMPTS_CONFIG.get(puzzle_id, {"max_attempts": MAX_ATTEMPTS_DEFAULT})
        
        if puzzle_id not in self.session["puzzle_attempts"]:
            self.session["puzzle_attempts"][puzzle_id] = 0
        
        self.session["puzzle_attempts"][puzzle_id] += 1
        remaining = self.get_remaining_attempts(puzzle_id)
        
        if remaining <= 0:
            penalty_msg = self._apply_penalty(puzzle_id, config)
            return False, 0, penalty_msg
        
        return True, remaining, None
    
    def check_answer(self, puzzle_id: str, answer: str, correct_answer: str) -> Dict[str, Any]:
        if puzzle_id in self.session.get("solved_puzzles", []):
            return {
                "correct": True,
                "already_solved": True,
                "remaining_attempts": self.get_remaining_attempts(puzzle_id)
            }
        
        remaining_before = self.get_remaining_attempts(puzzle_id)
        
        if remaining_before <= 0:
            return {
                "correct": False,
                "out_of_attempts": True,
                "remaining_attempts": 0,
                "message": self._get_out_of_attempts_message()
            }
        
        normalized_answer = answer.strip().lower()
        normalized_correct = correct_answer.strip().lower()
        
        if normalized_answer == normalized_correct:
            self.session.setdefault("solved_puzzles", []).append(puzzle_id)
            return {
                "correct": True,
                "remaining_attempts": remaining_before,
                "message": self._get_success_message()
            }
        else:
            can_continue, remaining, penalty_msg = self.use_attempt(puzzle_id)
            
            result = {
                "correct": False,
                "remaining_attempts": remaining,
                "can_continue": can_continue
            }
            
            if penalty_msg:
                result["penalty_message"] = penalty_msg
                result["message"] = self._get_failure_message(remaining, penalty_msg)
            else:
                result["message"] = self._get_wrong_answer_message(remaining)
            
            return result
    
    def _apply_penalty(self, puzzle_id: str, config: Dict) -> str:
        penalty_type = config.get("penalty", "trust")
        penalty_value = config.get("penalty_value", -5)
        
        if puzzle_id not in self.session["puzzle_failures"]:
            self.session["puzzle_failures"].append(puzzle_id)
        
        if penalty_type == "trust":
            current = self.session.get("aria_trust", 50)
            self.session["aria_trust"] = max(0, current + penalty_value)
        
        elif penalty_type == "corruption":
            self.session["corruption_level"] += penalty_value
            if self.session["corruption_level"] >= 3:
                self._corrupt_random_file()
        
        elif penalty_type == "file_loss":
            self._lose_random_file()
        
        elif penalty_type == "detection":
            self.session["detection_level"] += penalty_value
        
        elif penalty_type == "ending":
            flags = self.session.get("narrative_flags", [])
            if "critical_failure" not in flags:
                flags.append("critical_failure")
                self.session["narrative_flags"] = flags
        
        return PENALTY_MESSAGES.get(self.lang, PENALTY_MESSAGES["EN"]).get(penalty_type, "")
    
    def _corrupt_random_file(self):
        accessed = self.session.get("accessed_files", [])
        if accessed:
            import random
            file_to_corrupt = random.choice(accessed)
            corrupted = self.session.get("corrupted_files", [])
            if file_to_corrupt not in corrupted:
                corrupted.append(file_to_corrupt)
                self.session["corrupted_files"] = corrupted
    
    def _lose_random_file(self):
        accessed = self.session.get("accessed_files", [])
        secrets = self.session.get("unlocked_secrets", [])
        combined = accessed + secrets
        if combined:
            import random
            file_to_lose = random.choice(combined)
            lost = self.session.get("lost_files", [])
            if file_to_lose not in lost:
                lost.append(file_to_lose)
                self.session["lost_files"] = lost
    
    def _get_success_message(self) -> str:
        if self.lang == "FR":
            return "Correct ! Vous avez résolu l'énigme."
        return "Correct! You solved the puzzle."
    
    def _get_wrong_answer_message(self, remaining: int) -> str:
        if self.lang == "FR":
            if remaining == 1:
                return f"Incorrect. ATTENTION: Il ne vous reste qu'UNE tentative !"
            return f"Incorrect. Tentatives restantes: {remaining}"
        else:
            if remaining == 1:
                return f"Incorrect. WARNING: You only have ONE attempt left!"
            return f"Incorrect. Remaining attempts: {remaining}"
    
    def _get_failure_message(self, remaining: int, penalty: str) -> str:
        if self.lang == "FR":
            return f"Échec. Plus de tentatives disponibles.\n{penalty}"
        return f"Failed. No more attempts available.\n{penalty}"
    
    def _get_out_of_attempts_message(self) -> str:
        if self.lang == "FR":
            return "Vous n'avez plus de tentatives pour cette énigme."
        return "You have no more attempts for this puzzle."
    
    def reset_puzzle(self, puzzle_id: str):
        if puzzle_id in self.session["puzzle_attempts"]:
            del self.session["puzzle_attempts"][puzzle_id]
    
    def get_puzzle_stats(self) -> Dict[str, Any]:
        return {
            "attempts": self.session.get("puzzle_attempts", {}),
            "failures": self.session.get("puzzle_failures", []),
            "corruption_level": self.session.get("corruption_level", 0),
            "detection_level": self.session.get("detection_level", 0),
            "corrupted_files": self.session.get("corrupted_files", []),
            "lost_files": self.session.get("lost_files", [])
        }

