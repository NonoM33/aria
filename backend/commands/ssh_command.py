from typing import Dict, Any
from commands.base_command import BaseCommand
from auth.ssh_auth import ssh_connect

class SshCommand(BaseCommand):
    def execute(self, args: str) -> Dict[str, Any]:
        if not args:
            if self.lang == "FR":
                return {"response": "Usage: ssh <username> <password>@system-void.local\nExemple: ssh hacker motdepasse123@system-void.local\n\nNote: Le mot de passe est requis pour la connexion SSH.", "status": "info"}
            else:
                return {"response": "Usage: ssh <username> <password>@system-void.local\nExample: ssh hacker password123@system-void.local\n\nNote: Password is required for SSH connection.", "status": "info"}
        
        parts = args.split("@")
        if len(parts) != 2 or parts[1] not in ["system-void.local", "localhost"]:
            if self.lang == "FR":
                return {"response": "Format invalide. Utilisez: ssh <username> <password>@system-void.local", "status": "error"}
            else:
                return {"response": "Invalid format. Use: ssh <username> <password>@system-void.local", "status": "error"}
        
        username_part = parts[0].strip()
        password = None
        
        username_parts = username_part.split(" ", 1)
        if len(username_parts) == 2:
            username = username_parts[0].strip()
            password = username_parts[1].strip()
        else:
            username = username_parts[0].strip()
        
        if not self.db:
            if self.lang == "FR":
                return {"response": "Base de données non disponible.", "status": "error"}
            else:
                return {"response": "Database not available.", "status": "error"}
        
        token = None
        if hasattr(self, 'token') and self.token:
            token = self.token
        elif self.session.get("ssh_token"):
            token = self.session.get("ssh_token")
        
        if not password and not token:
            if self.lang == "FR":
                return {"response": "Erreur: Mot de passe requis pour la connexion SSH.\n\nFormat: ssh <username> <password>@system-void.local\nExemple: ssh hacker motdepasse123@system-void.local", "status": "error"}
            else:
                return {"response": "Error: Password required for SSH connection.\n\nFormat: ssh <username> <password>@system-void.local\nExample: ssh hacker password123@system-void.local", "status": "error"}
        
        try:
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
                        "token": new_token,
                        "username": result["username"]
                    }
                else:
                    return {
                        "response": f"SSH connection established with {username}@system-void.local\n\nWelcome, {username}!\n\nYou are now connected. Your progress is saved.",
                        "status": "success",
                        "token": new_token,
                        "username": result["username"]
                    }
            else:
                if self.lang == "FR":
                    return {"response": f"Échec de la connexion SSH: {result.get('message', 'Identifiants invalides')}", "status": "error"}
                else:
                    return {"response": f"SSH connection failed: {result.get('message', 'Invalid credentials')}", "status": "error"}
        except Exception as e:
            if self.lang == "FR":
                return {"response": f"Erreur lors de la connexion SSH: {str(e)}", "status": "error"}
            else:
                return {"response": f"SSH connection error: {str(e)}", "status": "error"}

