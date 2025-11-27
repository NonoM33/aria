from typing import Dict, Any
from commands.base_command import BaseCommand
from adventures.adventure_loader import get_chapter_filesystem

class AccessCommand(BaseCommand):
    def execute(self, args: str) -> Dict[str, Any]:
        if not args:
            if self.lang == "FR":
                return {"response": "Usage: CAT <nom_fichier>\nExemple: CAT readme.txt", "status": "info"}
            else:
                return {"response": "Usage: CAT <filename>\nExample: CAT readme.txt", "status": "info"}
        
        adventure_data = get_adventure_data(self.lang)
        data = adventure_data.get(self.lang, {})
        chapter = self.get_chapter_data(data)
        filesystem = chapter.get("filesystem", {})
        
        current_path = self.session.get("current_path", "/")
        target = args.strip()
        
        if target.startswith("/"):
            file_path = target
        else:
            if current_path == "/":
                file_path = "/" + target
            else:
                file_path = current_path + "/" + target
        
        file_path = file_path.replace("//", "/")
        
        content = self._get_file_content(filesystem, file_path)
        
        if content is not None:
            filename = target.split("/")[-1]
            self.add_accessed_file(file_path)
            
            if filename == "corrupted_data.b64":
                if self.lang == "FR":
                    content += "\n\n[Indice: Utilisez DECODE pour decoder ce fichier]"
                else:
                    content += "\n\n[Hint: Use DECODE to decode this file]"
            
            return {"response": content, "status": "success"}
        else:
            if self.lang == "FR":
                return {"response": f"cat: {target}: Aucun fichier ou dossier de ce type", "status": "error"}
            else:
                return {"response": f"cat: {target}: No such file or directory", "status": "error"}
    
    def _get_file_content(self, filesystem: Dict, path: str) -> str:
        parts = path.strip("/").split("/")
        current = filesystem
        
        for part in parts:
            if isinstance(current, dict) and part in current:
                current = current[part]
            else:
                return None
        
        if isinstance(current, str):
            return current
        else:
            return None

