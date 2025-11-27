from typing import Dict, Any
from commands.base_command import BaseCommand
from adventures.adventure_loader import get_chapter_puzzles

class SolveCommand(BaseCommand):
    def execute(self, args: str) -> Dict[str, Any]:
        if not args:
            if self.lang == "FR":
                return {"response": "Usage: SOLVE <reponse>\nResolvez les enigmes pour progresser.", "status": "info"}
            else:
                return {"response": "Usage: SOLVE <answer>\nSolve puzzles to progress.", "status": "info"}
        
        chapter_id = self.session.get("chapter", "chapter_0")
        puzzles = get_chapter_puzzles(chapter_id, self.lang)
        
        if not puzzles:
            if self.lang == "FR":
                return {"response": "Aucune enigme disponible dans ce chapitre.", "status": "info"}
            else:
                return {"response": "No puzzles available in this chapter.", "status": "info"}
        
        answer = args.strip().lower()
        solved_puzzles = self.session.get("solved_puzzles", [])
        
        for puzzle_id, puzzle in puzzles.items():
            if puzzle_id in solved_puzzles:
                continue
            
            solution = puzzle.get("solution", "").lower()
            alt_solutions = [s.lower() for s in puzzle.get("alt_solutions", [])]
            
            if answer == solution or answer in alt_solutions:
                self.add_solved_puzzle(puzzle_id)
                
                reward = puzzle.get("reward", {})
                message = reward.get("message", "")
                
                if reward.get("unlocks_level"):
                    self.session["level"] = reward["unlocks_level"]
                
                if reward.get("unlocks_chapter"):
                    self.session["chapter"] = reward["unlocks_chapter"]
                    self.session["current_path"] = "/"
                
                for cmd in reward.get("unlocks", []):
                    self.add_unlocked_command(cmd)
                
                return {"response": message, "status": "success"}
        
        if self.lang == "FR":
            return {"response": "Reponse incorrecte. Continuez a explorer les fichiers pour trouver des indices.", "status": "error"}
        else:
            return {"response": "Incorrect answer. Keep exploring files for clues.", "status": "error"}
