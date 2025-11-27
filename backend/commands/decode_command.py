import base64
from typing import Dict, Any
from commands.base_command import BaseCommand
from adventures.adventure_data import get_adventure_data

class DecodeCommand(BaseCommand):
    def execute(self, args: str) -> Dict[str, Any]:
        if not self.check_level(1):
            if self.lang == "FR":
                return {"response": "Niveau d'accès insuffisant.", "status": "error"}
            else:
                return {"response": "Insufficient access level.", "status": "error"}
        
        if not args:
            if self.lang == "FR":
                return {"response": "Usage: DECODE <texte_base64> ou DECODE <nom_fichier>\nExemple: DECODE VGhpcyBpcyBhIHRlc3Q=\nExemple: DECODE corrupted_data.b64", "status": "info"}
            else:
                return {"response": "Usage: DECODE <base64_text> or DECODE <filename>\nExample: DECODE VGhpcyBpcyBhIHRlc3Q=\nExample: DECODE corrupted_data.b64", "status": "info"}
        
        adventure_data = get_adventure_data(self.lang)
        data = adventure_data.get(self.lang, {})
        chapter = self.get_chapter_data(data)
        files = chapter.get("files", {})
        filename = args.lower().strip()
        
        if filename in files:
            file_content = files[filename]
            try:
                decoded = base64.b64decode(file_content).decode('utf-8')
                if self.lang == "FR":
                    return {"response": f"Fichier {filename} décodé:\n\n{decoded}", "status": "success"}
                else:
                    return {"response": f"File {filename} decoded:\n\n{decoded}", "status": "success"}
            except:
                if self.lang == "FR":
                    return {"response": f"Le fichier {filename} ne contient pas de Base64 valide.", "status": "error"}
                else:
                    return {"response": f"File {filename} does not contain valid Base64.", "status": "error"}
        else:
            try:
                decoded = base64.b64decode(args).decode('utf-8')
                if self.lang == "FR":
                    return {"response": f"Décodé: {decoded}", "status": "success"}
                else:
                    return {"response": f"Decoded: {decoded}", "status": "success"}
            except:
                if self.lang == "FR":
                    return {"response": "Échec du décodage. Format invalide ou fichier introuvable.", "status": "error"}
                else:
                    return {"response": "Decoding failed. Invalid format or file not found.", "status": "error"}

