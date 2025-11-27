from typing import Dict, Any
from commands.base_command import BaseCommand
from adventures.adventure_data import get_adventure_data

class AccessCommand(BaseCommand):
    def execute(self, args: str) -> Dict[str, Any]:
        if not args:
            if self.lang == "FR":
                return {"response": "Usage: ACCESS <nom_fichier>\nExemple: ACCESS mission.txt", "status": "info"}
            else:
                return {"response": "Usage: ACCESS <filename>\nExample: ACCESS mission.txt", "status": "info"}
        
        filename = args.lower().strip()
        adventure_data = get_adventure_data(self.lang)
        data = adventure_data.get(self.lang, {})
        chapter = self.get_chapter_data(data)
        files = chapter.get("files", {})
        
        if filename in files:
            self.add_accessed_file(filename)
            content = files[filename]
            
            if filename == "corrupted_data.b64":
                if self.lang == "FR":
                    content += "\n\n[Indice: Utilisez DECODE pour décoder ce fichier]"
                else:
                    content += "\n\n[Hint: Use DECODE to decode this file]"
            
            return {"response": f"Fichier: {filename}\n\n{content}", "status": "success"}
        else:
            if self.lang == "FR":
                return {"response": f"Fichier '{filename}' introuvable ou accès refusé.", "status": "error"}
            else:
                return {"response": f"File '{filename}' not found or access denied.", "status": "error"}

