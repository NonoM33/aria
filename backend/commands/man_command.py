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
        
        if command_name in man_pages:
            return {"response": man_pages[command_name], "status": "success"}
        else:
            if self.lang == "FR":
                return {"response": f"Aucune page de manuel trouvée pour '{command_name}'.\n\nUtilisez MAN HELP pour voir les commandes disponibles.", "status": "error"}
            else:
                return {"response": f"No manual page found for '{command_name}'.\n\nUse MAN HELP to see available commands.", "status": "error"}

