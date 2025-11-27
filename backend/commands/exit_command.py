from typing import Dict, Any
from commands.base_command import BaseCommand

class ExitCommand(BaseCommand):
    def execute(self, args: str) -> Dict[str, Any]:
        if not self.session.get("logged_in") or not self.session.get("username"):
            if self.lang == "FR":
                return {"response": "Vous n'êtes pas connecté.", "status": "info"}
            else:
                return {"response": "You are not connected.", "status": "info"}
        
        username = self.session.get("username")
        
        self.update_session({
            "logged_in": False,
            "username": None,
            "player_id": None,
            "ssh_token": None
        })
        
        if self.lang == "FR":
            return {
                "response": f"Déconnexion réussie. Au revoir, {username}!",
                "status": "success",
                "logout": True,
                "username": None
            }
        else:
            return {
                "response": f"Logout successful. Goodbye, {username}!",
                "status": "success",
                "logout": True,
                "username": None
            }

