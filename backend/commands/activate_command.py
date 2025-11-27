from typing import Dict, Any
from commands.base_command import BaseCommand
from adventures.adventure_data import get_adventure_data
from services.progress_service import save_session_to_db

class ActivateCommand(BaseCommand):
    def execute(self, args: str) -> Dict[str, Any]:
        if not self.check_level(1):
            if self.lang == "FR":
                return {"response": "Niveau d'accès insuffisant.", "status": "error"}
            else:
                return {"response": "Insufficient access level.", "status": "error"}
        
        if not args:
            if self.lang == "FR":
                return {"response": "Usage: ACTIVATE <nom_protocole>", "status": "info"}
            else:
                return {"response": "Usage: ACTIVATE <protocol_name>", "status": "info"}
        
        if args.upper() == "PROTOCOL_XYZ":
            self.update_session({
                "logged_in": True,
                "level": 2,
                "chapter": "chapter_3"
            })
            self.add_unlocked_command("ACTIVATE")
            self.add_unlocked_command("NETWORK")
            self.add_unlocked_command("ANALYZE")
            self.add_unlocked_command("BYPASS")
            
            save_session_to_db(self.db, self.session)
            
            adventure_data = get_adventure_data(self.lang)
            data = adventure_data.get(self.lang, {})
            new_chapter = data.get("chapters", {}).get("chapter_3", {})
            intro = new_chapter.get("intro", "")
            
            if self.lang == "FR":
                intro += "\n\nNiveau 2 débloqué! Nouvelles commandes: NETWORK, ANALYZE, BYPASS"
            else:
                intro += "\n\nLevel 2 unlocked! New commands: NETWORK, ANALYZE, BYPASS"
            
            return {"response": intro, "status": "success"}
        else:
            if self.lang == "FR":
                return {"response": "Protocole invalide.\n\nIndice: Le nom du protocole se trouve dans le fichier corrupted_data.b64 décodé.\nIl commence par PROTOCOL_ et se termine par _XYZ.", "status": "error"}
            else:
                return {"response": "Invalid protocol.\n\nHint: The protocol name is in the decoded corrupted_data.b64 file.\nIt starts with PROTOCOL_ and ends with _XYZ.", "status": "error"}

