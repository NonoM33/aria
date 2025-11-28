from typing import Dict, Any
from commands.base_command import BaseCommand
from adventures.adventure_loader import get_chapter_puzzles
from services.resource_service import get_resource_manager, get_quest_manager, get_achievement_manager

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
                # Consommer des ressources
                resource_manager = get_resource_manager(self.session)
                resource_manager.consume_resource("cpu", 3.0)
                resource_manager.consume_resource("memory", 2.0)
                resource_manager.consume_resource("energy", 1.5)
                
                # Récompense en crédits
                credits_reward = 50
                self.session["credits"] = self.session.get("credits", 0) + credits_reward
                
                self.add_solved_puzzle(puzzle_id)
                
                # Mettre à jour les quêtes et achievements
                quest_manager = get_quest_manager(self.session)
                quest_manager.update_quest_progress("puzzle", 1)
                
                achievement_manager = get_achievement_manager(self.session)
                achievement_result = achievement_manager.check_achievements("puzzle_solved", {"puzzle_id": puzzle_id})
                
                reward = puzzle.get("reward", {})
                message = reward.get("message", "")
                
                if credits_reward > 0:
                    if self.lang == "FR":
                        message += f"\n\n💰 +{credits_reward} crédits obtenus!"
                    else:
                        message += f"\n\n💰 +{credits_reward} credits earned!"
                
                if achievement_result:
                    achievement_msg = f"\n🏆 Achievement débloqué: {achievement_result['title']} (+{achievement_result.get('credits', 0)} crédits)"
                    message += achievement_msg
                
                if reward.get("unlocks_level"):
                    new_level = reward["unlocks_level"]
                    self.session["level"] = new_level
                    
                    # Vérifier achievement niveau
                    achievement_result = achievement_manager.check_achievements("level_up", {"level": new_level})
                    if achievement_result:
                        message += f"\n🏆 Achievement débloqué: {achievement_result['title']} (+{achievement_result.get('credits', 0)} crédits)"
                
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
