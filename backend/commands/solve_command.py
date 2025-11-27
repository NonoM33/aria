from typing import Dict, Any
from commands.base_command import BaseCommand
from adventures.adventure_data import get_adventure_data

class SolveCommand(BaseCommand):
    def execute(self, args: str) -> Dict[str, Any]:
        if not self.check_level(4):
            if self.lang == "FR":
                return {"response": "Niveau d'accès insuffisant.", "status": "error"}
            else:
                return {"response": "Insufficient access level.", "status": "error"}
        
        if not args:
            if self.lang == "FR":
                return {"response": "Usage: SOLVE <réponse>\nRésolvez l'énigme finale du fichier final_riddle.txt", "status": "info"}
            else:
                return {"response": "Usage: SOLVE <answer>\nSolve the final riddle from final_riddle.txt file", "status": "info"}
        
        adventure_data = get_adventure_data(self.lang)
        data = adventure_data.get(self.lang, {})
        chapter = self.get_chapter_data(data)
        puzzles = chapter.get("puzzles", {})
        puzzle = puzzles.get("final_riddle", {})
        
        if args.upper().strip() == puzzle.get("solution", "").upper():
            self.update_session({
                "level": 6,
                "chapter": "chapter_6"
            })
            self.session.setdefault("flags", []).append("adventure_complete")
            self.add_unlocked_command("NVIM")
            self.add_unlocked_command("MAN")
            
            if self.lang == "FR":
                return {"response": """FÉLICITATIONS!
================

Vous avez complété la première partie de SYSTEM_VOID!
L'intégrité du système est restaurée à 50%.
Nouvelles commandes débloquées: NVIM, MAN

Chapitre 6: L'Exploration
Utilisez NVIM pour explorer le système de fichiers.

Tapez MAN NVIM pour apprendre à utiliser le gestionnaire de fichiers.""", "status": "success"}
            else:
                return {"response": """CONGRATULATIONS!
==================

You have completed the first part of SYSTEM_VOID!
System integrity restored to 50%.
New commands unlocked: NVIM, MAN

Chapter 6: The Exploration
Use NVIM to explore the file system.

Type MAN NVIM to learn how to use the file manager.""", "status": "success"}
        else:
            if self.lang == "FR":
                return {"response": "Réponse incorrecte. Réessayez.", "status": "error"}
            else:
                return {"response": "Incorrect answer. Try again.", "status": "error"}

