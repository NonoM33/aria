"""
Resource Management Service
Gère les ressources système (CPU, mémoire, énergie, bande passante)
et les mécaniques addictives (daily quests, achievements, progression)
"""
from typing import Dict, Any, List, Optional
from datetime import datetime, timedelta
import random
import json


class ResourceManager:
    """Gère les ressources système du joueur"""
    
    def __init__(self, session: Dict[str, Any]):
        self.session = session
        self._init_resources()
    
    def _init_resources(self):
        """Initialise les ressources si elles n'existent pas"""
        if "resources" not in self.session:
            self.session["resources"] = {
                "cpu": 100,
                "memory": 100,
                "energy": 100,
                "bandwidth": 100,
                "storage": 1000,
                "used_storage": 0,
                "last_update": datetime.utcnow().isoformat()
            }
        
        if "resource_upgrades" not in self.session:
            self.session["resource_upgrades"] = {
                "cpu_level": 1,
                "memory_level": 1,
                "energy_level": 1,
                "bandwidth_level": 1,
                "storage_level": 1
            }
        
        if "resource_history" not in self.session:
            self.session["resource_history"] = []
    
    def update_resources(self):
        """Met à jour les ressources (consommation naturelle)"""
        resources = self.session["resources"]
        last_update = datetime.fromisoformat(resources.get("last_update", datetime.utcnow().isoformat()))
        now = datetime.utcnow()
        elapsed = (now - last_update).total_seconds()
        
        if elapsed < 1:
            return
        
        energy_level = self.session["resource_upgrades"]["energy_level"]
        energy_drain = 0.1 / energy_level
        
        resources["energy"] = max(0, resources["energy"] - energy_drain * elapsed / 60)
        resources["last_update"] = now.isoformat()
        
        if resources["energy"] <= 0:
            resources["cpu"] = max(0, resources["cpu"] - 0.5 * elapsed / 60)
            resources["memory"] = max(0, resources["memory"] - 0.3 * elapsed / 60)
    
    def consume_resource(self, resource_type: str, amount: float) -> bool:
        """Consomme une ressource"""
        resources = self.session["resources"]
        
        if resource_type not in resources:
            return False
        
        if resources[resource_type] < amount:
            return False
        
        resources[resource_type] -= amount
        return True
    
    def restore_resource(self, resource_type: str, amount: float):
        """Restaure une ressource"""
        resources = self.session["resources"]
        
        if resource_type not in resources:
            return
        
        max_value = 100
        if resource_type == "storage":
            max_value = 1000 + (self.session["resource_upgrades"]["storage_level"] - 1) * 500
        
        resources[resource_type] = min(max_value, resources[resource_type] + amount)
    
    def get_resources(self) -> Dict[str, Any]:
        """Retourne l'état actuel des ressources"""
        self.update_resources()
        return self.session["resources"].copy()
    
    def can_perform_action(self, cpu_cost: float = 0, memory_cost: float = 0, 
                          energy_cost: float = 0) -> bool:
        """Vérifie si une action peut être effectuée"""
        resources = self.session["resources"]
        
        if resources["cpu"] < cpu_cost:
            return False
        if resources["memory"] < memory_cost:
            return False
        if resources["energy"] < energy_cost:
            return False
        
        return True
    
    def upgrade_resource(self, resource_type: str) -> Dict[str, Any]:
        """Améliore une ressource"""
        upgrades = self.session["resource_upgrades"]
        level = upgrades.get(f"{resource_type}_level", 1)
        
        if level >= 10:
            return {"success": False, "message": "Niveau maximum atteint"}
        
        cost = level * 100
        credits = self.session.get("credits", 0)
        
        if credits < cost:
            return {"success": False, "message": f"Crédits insuffisants ({cost} requis)"}
        
        self.session["credits"] = credits - cost
        upgrades[f"{resource_type}_level"] = level + 1
        
        if resource_type == "cpu":
            self.session["resources"]["cpu"] = min(100, self.session["resources"]["cpu"] + 10)
        elif resource_type == "memory":
            self.session["resources"]["memory"] = min(100, self.session["resources"]["memory"] + 10)
        elif resource_type == "energy":
            self.session["resources"]["energy"] = min(100, self.session["resources"]["energy"] + 10)
        elif resource_type == "storage":
            self.session["resources"]["storage"] += 500
        
        return {"success": True, "level": level + 1, "message": f"{resource_type} amélioré au niveau {level + 1}"}


class DailyQuestManager:
    """Gère les quêtes quotidiennes"""
    
    def __init__(self, session: Dict[str, Any]):
        self.session = session
        self._init_quests()
    
    def _init_quests(self):
        """Initialise les quêtes quotidiennes"""
        if "daily_quests" not in self.session:
            self.session["daily_quests"] = {}
        
        if "last_quest_reset" not in self.session:
            self.session["last_quest_reset"] = datetime.utcnow().isoformat()
        
        self._reset_if_needed()
    
    def _reset_if_needed(self):
        """Réinitialise les quêtes si nécessaire (nouveau jour)"""
        last_reset = datetime.fromisoformat(self.session["last_quest_reset"])
        now = datetime.utcnow()
        
        if (now - last_reset).days >= 1:
            self.session["daily_quests"] = self._generate_daily_quests()
            self.session["last_quest_reset"] = now.isoformat()
    
    def _generate_daily_quests(self) -> Dict[str, Any]:
        """Génère de nouvelles quêtes quotidiennes"""
        quest_templates = [
            {
                "id": "explore_files",
                "type": "explore",
                "title": "Explorer 10 fichiers",
                "description": "Accédez à 10 fichiers différents",
                "target": 10,
                "progress": 0,
                "reward": {"credits": 50, "energy": 20}
            },
            {
                "id": "solve_puzzles",
                "type": "puzzle",
                "title": "Résoudre 3 puzzles",
                "description": "Résolvez 3 puzzles",
                "target": 3,
                "progress": 0,
                "reward": {"credits": 100, "cpu": 10}
            },
            {
                "id": "scan_systems",
                "type": "scan",
                "title": "Scanner 5 systèmes",
                "description": "Utilisez SCAN 5 fois",
                "target": 5,
                "progress": 0,
                "reward": {"credits": 75, "bandwidth": 15}
            },
            {
                "id": "decode_files",
                "type": "decode",
                "title": "Décoder 3 fichiers",
                "description": "Utilisez DECODE sur 3 fichiers",
                "target": 3,
                "progress": 0,
                "reward": {"credits": 80, "memory": 10}
            }
        ]
        
        return {q["id"]: q for q in random.sample(quest_templates, 3)}
    
    def get_quests(self) -> Dict[str, Any]:
        """Retourne les quêtes quotidiennes"""
        self._reset_if_needed()
        return self.session["daily_quests"].copy()
    
    def update_quest_progress(self, quest_type: str, amount: int = 1):
        """Met à jour la progression d'une quête"""
        self._reset_if_needed()
        quests = self.session["daily_quests"]
        
        for quest_id, quest in quests.items():
            if quest["type"] == quest_type and quest["progress"] < quest["target"]:
                quest["progress"] = min(quest["target"], quest["progress"] + amount)
                
                if quest["progress"] >= quest["target"]:
                    self._complete_quest(quest_id, quest)
    
    def _complete_quest(self, quest_id: str, quest: Dict[str, Any]):
        """Complète une quête et donne les récompenses"""
        if quest.get("completed", False):
            return
        
        quest["completed"] = True
        reward = quest["reward"]
        
        if "credits" in reward:
            self.session["credits"] = self.session.get("credits", 0) + reward["credits"]
        
        resource_manager = ResourceManager(self.session)
        for resource, amount in reward.items():
            if resource != "credits":
                resource_manager.restore_resource(resource, amount)
        
        if "achievements" not in self.session:
            self.session["achievements"] = []
        
        achievement = f"daily_quest_{quest_id}"
        if achievement not in self.session["achievements"]:
            self.session["achievements"].append(achievement)


class AchievementManager:
    """Gère les achievements"""
    
    def __init__(self, session: Dict[str, Any]):
        self.session = session
        if "achievements" not in self.session:
            self.session["achievements"] = []
        if "achievement_progress" not in self.session:
            self.session["achievement_progress"] = {}
    
    def check_achievements(self, event_type: str, context: Dict[str, Any] = None):
        """Vérifie et débloque les achievements"""
        achievements = self.session["achievements"]
        progress = self.session["achievement_progress"]
        
        # Achievements basés sur les événements
        if event_type == "file_access":
            progress["files_accessed"] = progress.get("files_accessed", 0) + 1
            
            if progress["files_accessed"] >= 10 and "explorer_10" not in achievements:
                achievements.append("explorer_10")
                return {"unlocked": "explorer_10", "title": "Explorateur", "credits": 25}
            
            if progress["files_accessed"] >= 100 and "explorer_100" not in achievements:
                achievements.append("explorer_100")
                return {"unlocked": "explorer_100", "title": "Archiviste", "credits": 100}
        
        elif event_type == "puzzle_solved":
            progress["puzzles_solved"] = progress.get("puzzles_solved", 0) + 1
            
            if progress["puzzles_solved"] >= 5 and "solver_5" not in achievements:
                achievements.append("solver_5")
                return {"unlocked": "solver_5", "title": "Résolveur", "credits": 50}
        
        elif event_type == "level_up":
            level = context.get("level", 0) if context else 0
            
            if level >= 5 and "master_hacker" not in achievements:
                achievements.append("master_hacker")
                return {"unlocked": "master_hacker", "title": "Maître Hacker", "credits": 200}
        
        return None
    
    def get_achievements(self) -> List[Dict[str, Any]]:
        """Retourne tous les achievements"""
        achievement_definitions = {
            "explorer_10": {"title": "Explorateur", "description": "Accéder à 10 fichiers"},
            "explorer_100": {"title": "Archiviste", "description": "Accéder à 100 fichiers"},
            "solver_5": {"title": "Résolveur", "description": "Résoudre 5 puzzles"},
            "master_hacker": {"title": "Maître Hacker", "description": "Atteindre le niveau 5"},
        }
        
        unlocked = self.session["achievements"]
        return [
            {**defn, "unlocked": True, "id": aid}
            for aid, defn in achievement_definitions.items()
            if aid in unlocked
        ]


def get_resource_manager(session: Dict[str, Any]) -> ResourceManager:
    """Factory pour obtenir un ResourceManager"""
    return ResourceManager(session)


def get_quest_manager(session: Dict[str, Any]) -> DailyQuestManager:
    """Factory pour obtenir un DailyQuestManager"""
    return DailyQuestManager(session)


def get_achievement_manager(session: Dict[str, Any]) -> AchievementManager:
    """Factory pour obtenir un AchievementManager"""
    return AchievementManager(session)

