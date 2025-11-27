from typing import Dict, Any
from commands.base_command import BaseCommand
from adventures.adventure_data import get_adventure_data

class ScanCommand(BaseCommand):
    def execute(self, args: str) -> Dict[str, Any]:
        adventure_data = get_adventure_data(self.lang)
        data = adventure_data.get(self.lang, {})
        chapter = self.get_chapter_data(data)
        files = chapter.get("files", {})
        file_list = "\n".join([f"- {name}" for name in files.keys()])
        
        if self.lang == "FR":
            response = f"Scan du système en cours...\n\nFichiers détectés:\n{file_list}\n\nUtilisez: ACCESS <nom_fichier> pour lire"
        else:
            response = f"Scanning system...\n\nFiles detected:\n{file_list}\n\nUse: ACCESS <filename> to read"
        
        return {"response": response, "status": "success"}

