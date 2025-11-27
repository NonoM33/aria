from typing import Dict, Any
from commands.base_command import BaseCommand
from man_pages import MAN_PAGES

class ManCommand(BaseCommand):
    def execute(self, args: str) -> Dict[str, Any]:
        if not args:
            if self.lang == "FR":
                return {"response": "Usage: MAN <commande>\nExemple: MAN HELP", "status": "info"}
            else:
                return {"response": "Usage: MAN <command>\nExample: MAN HELP", "status": "info"}
        
        command_name = args.upper().strip()
        man_pages = MAN_PAGES.get(self.lang, MAN_PAGES["FR"])
        
        unlocked_commands = self.session.get("unlocked_commands", [])
        is_logged_in = self.session.get("logged_in", False)
        level = self.session.get("level", 0)
        
        base_commands = {"HELP", "EXIT", "LS", "CAT", "CD", "PWD", "MAN", "ALIAS", "EDIT"}
        if is_logged_in:
            base_commands.update(["STATUS", "TALK", "ARIA"])
        
        if level >= 1:
            base_commands.update(["DECODE", "SOLVE"])
        if level >= 2:
            base_commands.update(["ANALYZE"])
        if level >= 3:
            base_commands.update(["BYPASS"])
        if level >= 4:
            base_commands.update(["RESTORE"])
        
        all_available = base_commands.union(set(unlocked_commands))
        
        if command_name not in all_available:
            if self.lang == "FR":
                return {"response": f"Aucune page de manuel trouvée pour '{command_name}'.\n\nCette commande n'est pas disponible ou n'a pas encore été débloquée.\n\nUtilisez HELP pour voir les commandes disponibles.", "status": "error"}
            else:
                return {"response": f"No manual page found for '{command_name}'.\n\nThis command is not available or has not been unlocked yet.\n\nUse HELP to see available commands.", "status": "error"}
        
        if command_name in man_pages:
            return {"response": man_pages[command_name], "status": "success"}
        else:
            if self.lang == "FR":
                return {"response": f"Aucune page de manuel trouvée pour '{command_name}'.\n\nUtilisez MAN HELP pour voir les commandes disponibles.", "status": "error"}
            else:
                return {"response": f"No manual page found for '{command_name}'.\n\nUse MAN HELP to see available commands.", "status": "error"}

