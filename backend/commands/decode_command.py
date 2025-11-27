import base64
import codecs
from typing import Dict, Any
from commands.base_command import BaseCommand
from adventures.adventure_loader import get_chapter_filesystem

class DecodeCommand(BaseCommand):
    def execute(self, args: str) -> Dict[str, Any]:
        if not args:
            if self.lang == "FR":
                return {"response": "Usage: DECODE <texte>\nDecode du texte en Base64 ou ROT13.\nExemple: DECODE SGVsbG8gV29ybGQ=", "status": "info"}
            else:
                return {"response": "Usage: DECODE <text>\nDecodes Base64 or ROT13 text.\nExample: DECODE SGVsbG8gV29ybGQ=", "status": "info"}
        
        text = args.strip()
        
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
