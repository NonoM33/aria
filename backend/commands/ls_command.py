from typing import Dict, Any
from commands.base_command import BaseCommand
from adventures.adventure_data import get_adventure_data

class LsCommand(BaseCommand):
    def execute(self, args: str) -> Dict[str, Any]:
        adventure_data = get_adventure_data(self.lang)
        data = adventure_data.get(self.lang, {})
        chapter = self.get_chapter_data(data)
        files = chapter.get("files", {})
        file_list = "\n".join([f"- {name}" for name in files.keys()])
        
        if self.lang == "FR":
            if file_list:
                response = f"Fichiers disponibles:\n{file_list}"
            else:
                response = "Aucun fichier disponible."
        else:
            if file_list:
                response = f"Available files:\n{file_list}"
            else:
                response = "No files available."
        
        return {"response": response, "status": "success"}

