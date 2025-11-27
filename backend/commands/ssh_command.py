from typing import Dict, Any
from commands.base_command import BaseCommand
from auth.ssh_auth import ssh_connect

class SshCommand(BaseCommand):
    def execute(self, args: str) -> Dict[str, Any]:
        if not args:
            if self.lang == "FR":
                return {"response": "Usage: ssh <username>@system-void.local\nExemple: ssh hacker@system-void.local", "status": "info"}
            else:
                return {"response": "Usage: ssh <username>@system-void.local\nExample: ssh hacker@system-void.local", "status": "info"}
        
        parts = args.split("@")
        if len(parts) != 2 or parts[1] not in ["system-void.local", "localhost"]:
            if self.lang == "FR":
                return {"response": "Format invalide. Utilisez: ssh <username>@system-void.local", "status": "error"}
            else:
                return {"response": "Invalid format. Use: ssh <username>@system-void.local", "status": "error"}
        
        username = parts[0].strip()
        
        if not self.db:
            if self.lang == "FR":
                return {"response": "Base de données non disponible.", "status": "error"}
            else:
                return {"response": "Database not available.", "status": "error"}
        
        result = ssh_connect(self.db, username)
        
        if result.get("success"):
            self.update_session({
                "username": result["username"],
                "player_id": result.get("player_id"),
                "logged_in": True
            })
            
            if self.lang == "FR":
                return {
                    "response": f"Connexion SSH établie avec {username}@system-void.local\n\nBienvenue, {username}!",
                    "status": "success",
                    "token": result.get("token")
                }
            else:
                return {
                    "response": f"SSH connection established with {username}@system-void.local\n\nWelcome, {username}!",
                    "status": "success",
                    "token": result.get("token")
                }
        else:
            if self.lang == "FR":
                return {"response": f"Échec de la connexion SSH: {result.get('message', 'Identifiants invalides')}", "status": "error"}
            else:
                return {"response": f"SSH connection failed: {result.get('message', 'Invalid credentials')}", "status": "error"}

