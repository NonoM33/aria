from typing import Dict, Any
from commands.base_command import BaseCommand
from auth.ssh_auth import hack_database_and_create_user
from services.session_service import mark_connection_converted

class CreateUserCommand(BaseCommand):
    def execute(self, args: str) -> Dict[str, Any]:
        unlocked_commands = self.session.get("unlocked_commands", [])
        if "CREATE_USER" not in unlocked_commands:
            if self.lang == "FR":
                return {"response": "Commande inconnue. Accès refusé.\n\nTapez HELP pour voir les commandes disponibles.", "status": "error"}
            else:
                return {"response": "Unknown command. Access Denied.\n\nType HELP to see available commands.", "status": "error"}
        
        if not args:
            if self.lang == "FR":
                return {"response": "Usage: CREATE_USER <username> <password>\nExemple: CREATE_USER hacker password123", "status": "info"}
            else:
                return {"response": "Usage: CREATE_USER <username> <password>\nExample: CREATE_USER hacker password123", "status": "info"}
        
        if "exploit_success" not in self.session.get("flags", []) and "CVE-2024-DB-001" not in str(self.session.get("solved_puzzles", [])):
            if self.lang == "FR":
                return {"response": "Acces refuse. Le systeme est protege.\n\nTrouvez une faille de securite d'abord...", "status": "error"}
            else:
                return {"response": "Access denied. System is protected.\n\nFind a security flaw first...", "status": "error"}
        
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
            token = result.get("token")
            player_id = result.get("player_id")
            self.update_session({
                "username": result["username"],
                "player_id": player_id,
                "logged_in": True,
                "ssh_token": token
            })
            
            session_id = self.session.get("session_id")
            if session_id and player_id:
                mark_connection_converted(session_id, player_id, self.db)
            
            if self.lang == "FR":
                return {
                    "response": f"""Utilisateur {username} créé avec succès!

Compte SSH créé via exploit de base de données.
Vous pouvez maintenant vous connecter avec:
ssh {username}@system-void.local""",
                    "status": "success",
                    "token": token
                }
            else:
                return {
                    "response": f"""User {username} created successfully!

SSH account created via database exploit.
You can now connect with:
ssh {username}@system-void.local""",
                    "status": "success",
                    "token": token
                }
        else:
            if self.lang == "FR":
                return {"response": f"Échec de la création: {result.get('message', 'Erreur inconnue')}", "status": "error"}
            else:
                return {"response": f"Creation failed: {result.get('message', 'Unknown error')}", "status": "error"}

