from typing import Dict, Any
from commands.base_command import BaseCommand
from adventures.global_state import GlobalState
from config import DEV_MODE

global_state = GlobalState()

class HelpCommand(BaseCommand):
    def execute(self, args: str) -> Dict[str, Any]:
        is_logged_in = self.session.get("logged_in", False)
        level = self.session.get("level", 0)
        
        if not is_logged_in:
            all_commands = {"HELP", "EXIT", "LS", "CAT", "CD", "PWD", "SCAN", "EDIT", "ALIAS"}
        else:
            all_commands = {"HELP", "EXIT", "LS", "CAT", "CD", "PWD", "SCAN", "STATUS", "EDIT", "ALIAS"}
            all_commands.update(self.session.get("unlocked_commands", []))
            
            if level >= 1:
                all_commands.update(["DECODE", "SOLVE"])
            if level >= 2:
                all_commands.update(["ANALYZE"])
            if level >= 3:
                all_commands.update(["BYPASS"])
            if level >= 4:
                all_commands.update(["RESTORE"])
            if level >= 5:
                all_commands.update(["MAN"])
            if DEV_MODE:
                all_commands.add("DEV")
        
        sorted_commands = sorted(all_commands)
        available = ", ".join(sorted_commands)
        
        if self.lang == "FR":
            help_msg = f"Commandes disponibles: {available}"
            if not is_logged_in:
                help_msg += "\n\nAcces restreint. Explorez le systeme avec LS et CD..."
            else:
                help_msg += f"\n\nNiveau d'acces: {level}"
                help_msg += "\nTapez STATUS pour voir l'etat du systeme."
                help_msg += "\nARIA vous parlera automatiquement..."
                help_msg += f"\n\n[GLOBAL] Integrite mondiale: {global_state._state['global_integrity']}%"
        else:
            help_msg = f"Commands available: {available}"
            if not is_logged_in:
                help_msg += "\n\nAccess restricted. Explore the system with LS and CD..."
            else:
                help_msg += f"\n\nAccess level: {level}"
                help_msg += "\nType STATUS to see system status."
                help_msg += "\nARIA will speak to you automatically..."
                help_msg += f"\n\n[GLOBAL] World integrity: {global_state._state['global_integrity']}%"
        
        return {"response": help_msg, "status": "success"}
