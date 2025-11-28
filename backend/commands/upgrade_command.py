"""
UPGRADE Command - Améliore les ressources système
"""
from typing import Dict, Any
from commands.base_command import BaseCommand
from services.resource_service import get_resource_manager


class UpgradeCommand(BaseCommand):
    def execute(self, args: str) -> Dict[str, Any]:
        if not args:
            return self._show_upgrades()
        
        resource_type = args.lower().strip()
        valid_types = ["cpu", "memory", "energy", "bandwidth", "storage"]
        
        if resource_type not in valid_types:
            if self.lang == "FR":
                return {"response": f"Type invalide. Types disponibles: {', '.join(valid_types)}", "status": "error"}
            else:
                return {"response": f"Invalid type. Available types: {', '.join(valid_types)}", "status": "error"}
        
        resource_manager = get_resource_manager(self.session)
        result = resource_manager.upgrade_resource(resource_type)
        
        if result["success"]:
            return {"response": result["message"], "status": "success"}
        else:
            return {"response": result["message"], "status": "error"}
    
    def _show_upgrades(self) -> Dict[str, Any]:
        """Affiche les améliorations disponibles"""
        upgrades = self.session.get("resource_upgrades", {})
        credits = self.session.get("credits", 0)
        
        if self.lang == "FR":
            response = "╔════════════════════════════════════════════════════════════════════╗\n"
            response += "║                    AMÉLIORATIONS                                  ║\n"
            response += "╠════════════════════════════════════════════════════════════════════╣\n"
            response += "║                                                                    ║\n"
            response += f"║  Crédits disponibles: {credits:<40} ║\n"
            response += "║                                                                    ║\n"
        else:
            response = "╔════════════════════════════════════════════════════════════════════╗\n"
            response += "║                    UPGRADES                                        ║\n"
            response += "╠════════════════════════════════════════════════════════════════════╣\n"
            response += "║                                                                    ║\n"
            response += f"║  Available credits: {credits:<40} ║\n"
            response += "║                                                                    ║\n"
        
        resource_types = {
            "cpu": "CPU",
            "memory": "Mémoire" if self.lang == "FR" else "Memory",
            "energy": "Énergie" if self.lang == "FR" else "Energy",
            "bandwidth": "Bande passante" if self.lang == "FR" else "Bandwidth",
            "storage": "Stockage" if self.lang == "FR" else "Storage"
        }
        
        for resource_type, display_name in resource_types.items():
            level = upgrades.get(f"{resource_type}_level", 1)
            cost = level * 100
            max_level = level >= 10
            
            if max_level:
                status = "MAX" if self.lang == "FR" else "MAX"
            else:
                status = f"{cost} crédits" if self.lang == "FR" else f"{cost} credits"
            
            if self.lang == "FR":
                response += f"║  {display_name:<15} Niveau {level:<2}  Coût: {status:<20} ║\n"
            else:
                response += f"║  {display_name:<15} Level {level:<2}  Cost: {status:<20} ║\n"
        
        response += "║                                                                    ║\n"
        response += "╚════════════════════════════════════════════════════════════════════╝\n"
        
        if self.lang == "FR":
            response += "\nUsage: UPGRADE <cpu|memory|energy|bandwidth|storage>"
        else:
            response += "\nUsage: UPGRADE <cpu|memory|energy|bandwidth|storage>"
        
        return {"response": response, "status": "success"}

