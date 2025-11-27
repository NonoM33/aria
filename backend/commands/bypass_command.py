from typing import Dict, Any
from commands.base_command import BaseCommand
from adventures.adventure_data import get_adventure_data

class BypassCommand(BaseCommand):
    def execute(self, args: str) -> Dict[str, Any]:
        if not self.check_level(2):
            if self.lang == "FR":
                return {"response": "Niveau d'accès insuffisant.", "status": "error"}
            else:
                return {"response": "Insufficient access level.", "status": "error"}
        
        if not args:
            if self.lang == "FR":
                return {"response": "Usage: BYPASS <code>\nLe code est la réponse à l'énigme du carré magique.", "status": "info"}
            else:
                return {"response": "Usage: BYPASS <code>\nThe code is the answer to the magic square riddle.", "status": "info"}
        
        adventure_data = get_adventure_data(self.lang)
        data = adventure_data.get(self.lang, {})
        chapter = self.get_chapter_data(data)
        puzzles = chapter.get("puzzles", {})
        puzzle = puzzles.get("magic_square", {})
        
        if args.strip() == puzzle.get("solution", ""):
            self.update_session({
                "logged_in": True,
                "level": 3,
                "chapter": "chapter_4"
            })
            self.add_unlocked_command("CONNECT")
            self.add_solved_puzzle("magic_square")
            
            new_chapter = data.get("chapters", {}).get("chapter_4", {})
            intro = new_chapter.get("intro", "")
            
            if self.lang == "FR":
                return {"response": f"Code correct!\n\n{intro}", "status": "success"}
            else:
                return {"response": f"Correct code!\n\n{intro}", "status": "success"}
        else:
            if self.lang == "FR":
                return {"response": "Code incorrect. Réessayez.", "status": "error"}
            else:
                return {"response": "Incorrect code. Try again.", "status": "error"}

