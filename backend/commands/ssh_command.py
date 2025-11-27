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
        password = None
        
        if " " in username:
            username, password = username.split(" ", 1)
        
        if not self.db:
            if self.lang == "FR":
                return {"response": "Base de données non disponible.", "status": "error"}
            else:
                return {"response": "Database not available.", "status": "error"}
        
        token = None
        if self.session.get("ssh_token"):
            token = self.session.get("ssh_token")
        
        result = ssh_connect(self.db, username, password, token)
        
        if result.get("success"):
            new_token = result.get("token")
            self.update_session({
                "username": result["username"],
                "player_id": result.get("player_id"),
                "logged_in": True,
                "ssh_token": new_token,
                "chapter": "chapter_1"
            })
            
            if self.lang == "FR":
                return {
                    "response": f"Connexion SSH établie avec {username}@system-void.local\n\nBienvenue, {username}!\n\nVous êtes maintenant connecté. Votre progression est sauvegardée.",
                    "status": "success",
                    "token": new_token
                }
            else:
                return {
                    "response": f"SSH connection established with {username}@system-void.local\n\nWelcome, {username}!\n\nYou are now connected. Your progress is saved.",
                    "status": "success",
                    "token": new_token
                }
        else:
            if self.lang == "FR":
                return {"response": f"Échec de la connexion SSH: {result.get('message', 'Identifiants invalides')}", "status": "error"}
            else:
                return {"response": f"SSH connection failed: {result.get('message', 'Invalid credentials')}", "status": "error"}

