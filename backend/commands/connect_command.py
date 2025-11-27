from typing import Dict, Any
from commands.base_command import BaseCommand
from adventures.adventure_data import get_adventure_data
from services.progress_service import save_session_to_db

class ConnectCommand(BaseCommand):
    def execute(self, args: str) -> Dict[str, Any]:
        if not self.check_level(3):
            if self.lang == "FR":
                return {"response": "Niveau d'accès insuffisant.", "status": "error"}
            else:
                return {"response": "Insufficient access level.", "status": "error"}
        
        if not args:
            if self.lang == "FR":
                return {"response": "Usage: CONNECT SERVER_GAMMA <mot_de_passe>", "status": "info"}
            else:
                return {"response": "Usage: CONNECT SERVER_GAMMA <password>", "status": "info"}
        
        parts = args.split(" ", 1)
        if len(parts) < 2:
            if self.lang == "FR":
                return {"response": "Format: CONNECT <serveur> <mot_de_passe>", "status": "error"}
            else:
                return {"response": "Format: CONNECT <server> <password>", "status": "error"}
        
        server = parts[0].upper()
        password = parts[1].upper()
        
        if server == "SERVER_GAMMA" and password == "DIOV":
            self.update_session({
                "logged_in": True,
                "level": 4,
                "chapter": "chapter_5"
            })
            self.add_unlocked_command("RESTORE")
            self.add_unlocked_command("SOLVE")
            
            save_session_to_db(self.db, self.session)
            
            adventure_data = get_adventure_data(self.lang)
            data = adventure_data.get(self.lang, {})
            new_chapter = data.get("chapters", {}).get("chapter_5", {})
            intro = new_chapter.get("intro", "")
            
            if self.lang == "FR":
                return {"response": f"Serveur GAMMA connecté!\n\n{intro}", "status": "success"}
            else:
                return {"response": f"Server GAMMA connected!\n\n{intro}", "status": "success"}
        else:
            if self.lang == "FR":
                return {"response": "Connexion échouée. Serveur ou mot de passe incorrect.", "status": "error"}
            else:
                return {"response": "Connection failed. Server or password incorrect.", "status": "error"}

