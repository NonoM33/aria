from typing import Dict, Any
from commands.base_command import BaseCommand
from adventures.global_state import GlobalState
from config import DEV_MODE

global_state = GlobalState()

class HelpCommand(BaseCommand):
    def execute(self, args: str) -> Dict[str, Any]:
        all_commands = set(self.session.get("unlocked_commands", []))
        
        if self.session.get("level", 0) >= 1:
            all_commands.update(["SCAN", "DECODE", "ACCESS"])
        if self.session.get("level", 0) >= 2:
            all_commands.update(["ACTIVATE", "NETWORK", "ANALYZE", "BYPASS"])
        if self.session.get("level", 0) >= 3:
            all_commands.update(["CONNECT", "RESTORE", "SOLVE"])
        if self.session.get("level", 0) >= 6:
            all_commands.update(["NVIM", "MAN"])
        if DEV_MODE:
            all_commands.add("DEV")
        
        sorted_commands = sorted(all_commands)
        available = ", ".join(sorted_commands)
        
        help_msg = f"Commands available: {available}"
        if self.lang == "FR":
            help_msg += "\n\nTapez STATUS pour voir l'état du système."
            help_msg += f"\n[GLOBAL] Intégrité mondiale: {global_state._state['global_integrity']}%"
        else:
            help_msg += "\n\nType STATUS to see system status."
            help_msg += f"\n[GLOBAL] World integrity: {global_state._state['global_integrity']}%"
        
        return {"response": help_msg, "status": "success"}

