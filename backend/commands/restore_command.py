from typing import Dict, Any
from commands.base_command import BaseCommand
from services.progress_service import save_session_to_db
from services.event_service import create_global_event

class RestoreCommand(BaseCommand):
    def execute(self, args: str) -> Dict[str, Any]:
        if not self.check_level(4):
            if self.lang == "FR":
                return {"response": "Niveau d'accès insuffisant.", "status": "error"}
            else:
                return {"response": "Insufficient access level.", "status": "error"}
        
        if not args:
            if self.lang == "FR":
                return {"response": "Usage: RESTORE <code>\nLe code est: 34 + 15 + 5 + 1", "status": "info"}
            else:
                return {"response": "Usage: RESTORE <code>\nThe code is: 34 + 15 + 5 + 1", "status": "info"}
        
        if args.strip() == "55":
            self.update_session({"level": 5})
            self.session.setdefault("flags", []).append("system_restored")
            
            save_session_to_db(self.db, self.session)
            
            if self.session.get("username"):
                create_global_event(
                    self.db,
                    "SYSTEM_RESTORED",
                    {"level": 5, "restored_by": self.session.get("username")},
                    triggered_by=self.session.get("username"),
                    impact_level=8
                )
            
            if self.lang == "FR":
                return {"response": "Code de restauration correct!\n\nSystème restauré à 100%.\n\nÉtape finale: résolvez l'énigme finale avec SOLVE.", "status": "success"}
            else:
                return {"response": "Restoration code correct!\n\nSystem restored to 100%.\n\nFinal step: solve the final riddle with SOLVE.", "status": "success"}
        else:
            if self.lang == "FR":
                return {"response": "Code incorrect. Réessayez.", "status": "error"}
            else:
                return {"response": "Incorrect code. Try again.", "status": "error"}

