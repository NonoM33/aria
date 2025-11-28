"""
MONITOR Command - Affiche les ressources système en temps réel
"""
from typing import Dict, Any
from commands.base_command import BaseCommand
from services.resource_service import get_resource_manager


class MonitorCommand(BaseCommand):
    def execute(self, args: str) -> Dict[str, Any]:
        resource_manager = get_resource_manager(self.session)
        resources = resource_manager.get_resources()
        upgrades = self.session.get("resource_upgrades", {})
        
        cpu_level = upgrades.get("cpu_level", 1)
        memory_level = upgrades.get("memory_level", 1)
        energy_level = upgrades.get("energy_level", 1)
        bandwidth_level = upgrades.get("bandwidth_level", 1)
        storage_level = upgrades.get("storage_level", 1)
        
        cpu_bar = self._create_bar(resources["cpu"], 100)
        memory_bar = self._create_bar(resources["memory"], 100)
        energy_bar = self._create_bar(resources["energy"], 100)
        bandwidth_bar = self._create_bar(resources["bandwidth"], 100)
        storage_bar = self._create_bar(resources["storage"] - resources.get("used_storage", 0), resources["storage"])
        
        if self.lang == "FR":
            response = f"""╔════════════════════════════════════════════════════════════════════╗
║                    MONITEUR DE RESSOURCES                          ║
╠════════════════════════════════════════════════════════════════════╣
║                                                                    ║
║  CPU:        {cpu_bar} {resources['cpu']:.1f}% (Niveau {cpu_level})              ║
║  Mémoire:    {memory_bar} {resources['memory']:.1f}% (Niveau {memory_level})              ║
║  Énergie:    {energy_bar} {resources['energy']:.1f}% (Niveau {energy_level})              ║
║  Bande pass.: {bandwidth_bar} {resources['bandwidth']:.1f}% (Niveau {bandwidth_level})              ║
║  Stockage:   {storage_bar} {resources['storage'] - resources.get('used_storage', 0)}/{resources['storage']} MB (Niveau {storage_level})  ║
║                                                                    ║
║  Crédits:    {self.session.get('credits', 0)}                                      ║
║                                                                    ║
╚════════════════════════════════════════════════════════════════════╝

Tapez RESOURCE pour gérer vos ressources.
Tapez UPGRADE pour améliorer vos ressources."""
        else:
            response = f"""╔════════════════════════════════════════════════════════════════════╗
║                    RESOURCE MONITOR                                ║
╠════════════════════════════════════════════════════════════════════╣
║                                                                    ║
║  CPU:        {cpu_bar} {resources['cpu']:.1f}% (Level {cpu_level})              ║
║  Memory:     {memory_bar} {resources['memory']:.1f}% (Level {memory_level})              ║
║  Energy:     {energy_bar} {resources['energy']:.1f}% (Level {energy_level})              ║
║  Bandwidth:  {bandwidth_bar} {resources['bandwidth']:.1f}% (Level {bandwidth_level})              ║
║  Storage:    {storage_bar} {resources['storage'] - resources.get('used_storage', 0)}/{resources['storage']} MB (Level {storage_level})  ║
║                                                                    ║
║  Credits:    {self.session.get('credits', 0)}                                      ║
║                                                                    ║
╚════════════════════════════════════════════════════════════════════╝

Type RESOURCE to manage your resources.
Type UPGRADE to upgrade your resources."""
        
        return {"response": response, "status": "success"}
    
    def _create_bar(self, current: float, max_value: float, length: int = 20) -> str:
        """Crée une barre de progression"""
        filled = int((current / max_value) * length)
        filled = max(0, min(length, filled))
        empty = length - filled
        
        bar = "█" * filled + "░" * empty
        return bar

