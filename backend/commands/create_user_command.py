from typing import Dict, Any
from commands.base_command import BaseCommand
from auth.ssh_auth import hack_database_and_create_user

class CreateUserCommand(BaseCommand):
    def execute(self, args: str) -> Dict[str, Any]:
        if not args:
            if self.lang == "FR":
                return {"response": "Usage: CREATE_USER <username> <password>\nExemple: CREATE_USER hacker password123", "status": "info"}
            else:
                return {"response": "Usage: CREATE_USER <username> <password>\nExample: CREATE_USER hacker password123", "status": "info"}
        
        parts = args.split(" ", 1)
        if len(parts) < 2:
            if self.lang == "FR":
                return {"response": "Format: CREATE_USER <username> <password>", "status": "error"}
            else:
                return {"response": "Format: CREATE_USER <username> <password>", "status": "error"}
        
        username = parts[0].strip()
        password = parts[1].strip()
        
        if not self.db:
            if self.lang == "FR":
                return {"response": "Base de données non disponible.", "status": "error"}
            else:
                return {"response": "Database not available.", "status": "error"}
        
        result = hack_database_and_create_user(self.db, username, password)
        
        if result.get("success"):
            self.update_session({
                "username": result["username"],
                "player_id": result.get("player_id"),
                "logged_in": True
            })
            
            if self.lang == "FR":
                return {
                    "response": f"""Utilisateur {username} créé avec succès!

Compte SSH créé via exploit de base de données.
Vous pouvez maintenant vous connecter avec:
ssh {username}@system-void.local""",
                    "status": "success",
                    "token": result.get("token")
                }
            else:
                return {
                    "response": f"""User {username} created successfully!

SSH account created via database exploit.
You can now connect with:
ssh {username}@system-void.local""",
                    "status": "success",
                    "token": result.get("token")
                }
        else:
            if self.lang == "FR":
                return {"response": f"Échec de la création: {result.get('message', 'Erreur inconnue')}", "status": "error"}
            else:
                return {"response": f"Creation failed: {result.get('message', 'Unknown error')}", "status": "error"}

