from typing import Dict, Any
from commands.base_command import BaseCommand
from adventures.adventure_loader import get_chapter_filesystem

class ScanCommand(BaseCommand):
    def execute(self, args: str) -> Dict[str, Any]:
        chapter_id = self.session.get("chapter", "chapter_0")
        filesystem = get_chapter_filesystem(chapter_id, self.lang)
        
        if not filesystem:
            filesystem = {}
        
        current_path = self.session.get("current_path", "/")
        
        contents = self._get_directory_contents(filesystem, current_path)
        
        dirs = []
        files = []
        if contents:
            for name, value in contents.items():
                if isinstance(value, dict):
                    dirs.append(f"[DIR]  {name}/")
                else:
                    files.append(f"       {name}")
        
        dirs.sort()
        files.sort()
        
        items = dirs + files
        item_list = "\n".join(items) if items else "(vide)" if self.lang == "FR" else "(empty)"
        
        if self.lang == "FR":
            response = f"Scan en cours... [{current_path}]\n\n{item_list}"
        else:
            response = f"Scanning... [{current_path}]\n\n{item_list}"
        
        return {"response": response, "status": "success"}
    
    def _get_directory_contents(self, filesystem: dict, path: str) -> dict:
        if path == "/":
            return filesystem
        parts = path.strip("/").split("/")
        current = filesystem
        for part in parts:
            if isinstance(current, dict) and part in current:
                current = current[part]
            else:
                return {}
        if isinstance(current, dict):
            return current
        return {}
