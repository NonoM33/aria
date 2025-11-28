"""
RESOURCE Command - Gère les ressources et quêtes quotidiennes
"""
from typing import Dict, Any
from commands.base_command import BaseCommand
from services.resource_service import get_resource_manager, get_quest_manager, get_achievement_manager


class ResourceCommand(BaseCommand):
    def execute(self, args: str) -> Dict[str, Any]:
        if not args:
            return self._show_resources()
        
        parts = args.split()
        subcommand = parts[0].upper() if parts else ""
        
        if subcommand == "QUESTS" or subcommand == "QUEST":
            return self._show_quests()
        elif subcommand == "ACHIEVEMENTS" or subcommand == "ACHIEVEMENT":
            return self._show_achievements()
        elif subcommand == "RESTORE":
            resource_type = parts[1].lower() if len(parts) > 1 else None
            return self._restore_resource(resource_type)
        else:
            if self.lang == "FR":
                return {"response": "Usage: RESOURCE [QUESTS|ACHIEVEMENTS|RESTORE <type>]", "status": "info"}
            else:
                return {"response": "Usage: RESOURCE [QUESTS|ACHIEVEMENTS|RESTORE <type>]", "status": "info"}
    
    def _show_resources(self) -> Dict[str, Any]:
        """Affiche les ressources"""
        from commands.monitor_command import MonitorCommand
        monitor = MonitorCommand(self.session, self.db, self.lang)
        return monitor.execute("")
    
    def _show_quests(self) -> Dict[str, Any]:
        """Affiche les quêtes quotidiennes"""
        quest_manager = get_quest_manager(self.session)
        quests = quest_manager.get_quests()
        
        if not quests:
            if self.lang == "FR":
                return {"response": "Aucune quête quotidienne disponible.", "status": "info"}
            else:
                return {"response": "No daily quests available.", "status": "info"}
        
        if self.lang == "FR":
            response = "╔════════════════════════════════════════════════════════════════════╗\n"
            response += "║                    QUÊTES QUOTIDIENNES                            ║\n"
            response += "╠════════════════════════════════════════════════════════════════════╣\n"
            response += "║                                                                    ║\n"
        else:
            response = "╔════════════════════════════════════════════════════════════════════╗\n"
            response += "║                    DAILY QUESTS                                   ║\n"
            response += "╠════════════════════════════════════════════════════════════════════╣\n"
            response += "║                                                                    ║\n"
        
        for quest_id, quest in quests.items():
            progress_bar = self._create_progress_bar(quest["progress"], quest["target"])
            status = "✅" if quest.get("completed", False) else "⏳"
            
            if self.lang == "FR":
                response += f"║  {status} {quest['title']:<50} ║\n"
                response += f"║     {quest['description']:<54} ║\n"
                response += f"║     Progression: {progress_bar} {quest['progress']}/{quest['target']:<30} ║\n"
                if quest.get("completed", False):
                    reward = quest["reward"]
                    rewards_str = ", ".join([f"{k}: {v}" for k, v in reward.items()])
                    response += f"║     Récompense: {rewards_str:<45} ║\n"
                response += "║                                                                    ║\n"
            else:
                response += f"║  {status} {quest['title']:<50} ║\n"
                response += f"║     {quest['description']:<54} ║\n"
                response += f"║     Progress: {progress_bar} {quest['progress']}/{quest['target']:<30} ║\n"
                if quest.get("completed", False):
                    reward = quest["reward"]
                    rewards_str = ", ".join([f"{k}: {v}" for k, v in reward.items()])
                    response += f"║     Reward: {rewards_str:<45} ║\n"
                response += "║                                                                    ║\n"
        
        response += "╚════════════════════════════════════════════════════════════════════╝"
        
        return {"response": response, "status": "success"}
    
    def _show_achievements(self) -> Dict[str, Any]:
        """Affiche les achievements"""
        achievement_manager = get_achievement_manager(self.session)
        achievements = achievement_manager.get_achievements()
        
        if not achievements:
            if self.lang == "FR":
                return {"response": "Aucun achievement débloqué.", "status": "info"}
            else:
                return {"response": "No achievements unlocked.", "status": "info"}
        
        if self.lang == "FR":
            response = "╔════════════════════════════════════════════════════════════════════╗\n"
            response += "║                    ACHIEVEMENTS                                    ║\n"
            response += "╠════════════════════════════════════════════════════════════════════╣\n"
            response += "║                                                                    ║\n"
        else:
            response = "╔════════════════════════════════════════════════════════════════════╗\n"
            response += "║                    ACHIEVEMENTS                                   ║\n"
            response += "╠════════════════════════════════════════════════════════════════════╣\n"
            response += "║                                                                    ║\n"
        
        for achievement in achievements:
            if self.lang == "FR":
                response += f"║  🏆 {achievement['title']:<50} ║\n"
                response += f"║     {achievement['description']:<54} ║\n"
            else:
                response += f"║  🏆 {achievement['title']:<50} ║\n"
                response += f"║     {achievement['description']:<54} ║\n"
            response += "║                                                                    ║\n"
        
        response += "╚════════════════════════════════════════════════════════════════════╝"
        
        return {"response": response, "status": "success"}
    
    def _restore_resource(self, resource_type: str) -> Dict[str, Any]:
        """Restaure une ressource"""
        if not resource_type:
            if self.lang == "FR":
                return {"response": "Usage: RESOURCE RESTORE <cpu|memory|energy|bandwidth>", "status": "info"}
            else:
                return {"response": "Usage: RESOURCE RESTORE <cpu|memory|energy|bandwidth>", "status": "info"}
        
        credits = self.session.get("credits", 0)
        cost = 10
        
        if credits < cost:
            if self.lang == "FR":
                return {"response": f"Crédits insuffisants. Coût: {cost} crédits.", "status": "error"}
            else:
                return {"response": f"Insufficient credits. Cost: {cost} credits.", "status": "error"}
        
        resource_manager = get_resource_manager(self.session)
        resource_manager.restore_resource(resource_type, 25)
        self.session["credits"] = credits - cost
        
        if self.lang == "FR":
            return {"response": f"{resource_type} restauré de 25%. Coût: {cost} crédits.", "status": "success"}
        else:
            return {"response": f"{resource_type} restored by 25%. Cost: {cost} credits.", "status": "success"}
    
    def _create_progress_bar(self, current: int, target: int, length: int = 20) -> str:
        """Crée une barre de progression"""
        if target == 0:
            return "░" * length
        
        filled = int((current / target) * length)
        filled = max(0, min(length, filled))
        empty = length - filled
        
        bar = "█" * filled + "░" * empty
        return bar

