import base64
import codecs
from typing import Dict, Any
from commands.base_command import BaseCommand
from adventures.adventure_loader import get_chapter_filesystem
from services.resource_service import get_resource_manager, get_quest_manager

class DecodeCommand(BaseCommand):
    def execute(self, args: str) -> Dict[str, Any]:
        if not args:
            if self.lang == "FR":
                return {"response": "Usage: DECODE <texte>\nDecode du texte en Base64 ou ROT13.\nExemple: DECODE SGVsbG8gV29ybGQ=", "status": "info"}
            else:
                return {"response": "Usage: DECODE <text>\nDecodes Base64 or ROT13 text.\nExample: DECODE SGVsbG8gV29ybGQ=", "status": "info"}
        
        text = args.strip()
        
        # Consommer des ressources
        resource_manager = get_resource_manager(self.session)
        if not resource_manager.consume_resource("cpu", 2.0):
            if self.lang == "FR":
                return {"response": "CPU insuffisant. Utilisez RESOURCE RESTORE cpu ou attendez.", "status": "error"}
            else:
                return {"response": "Insufficient CPU. Use RESOURCE RESTORE cpu or wait.", "status": "error"}
        
        resource_manager.consume_resource("memory", 1.5)
        resource_manager.consume_resource("energy", 1.0)
        
        # Mettre à jour les quêtes
        quest_manager = get_quest_manager(self.session)
        quest_manager.update_quest_progress("decode", 1)
        
        rot13_result = codecs.decode(text, 'rot_13')
        
        try:
            base64_result = base64.b64decode(text).decode('utf-8')
            if self.lang == "FR":
                return {"response": f"[Base64 decode]\n{base64_result}\n\n[ROT13 decode]\n{rot13_result}", "status": "success"}
            else:
                return {"response": f"[Base64 decoded]\n{base64_result}\n\n[ROT13 decoded]\n{rot13_result}", "status": "success"}
        except:
            if self.lang == "FR":
                return {"response": f"[ROT13 decode]\n{rot13_result}", "status": "success"}
            else:
                return {"response": f"[ROT13 decoded]\n{rot13_result}", "status": "success"}
