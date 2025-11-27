from typing import Dict, Any
from commands.base_command import BaseCommand
from adventures.adventure_loader import get_chapter_filesystem


class CdCommand(BaseCommand):
    def execute(self, args: str) -> Dict[str, Any]:
        chapter_id = self.session.get("chapter", "chapter_0")
        filesystem = get_chapter_filesystem(chapter_id, self.lang)
        
        if not filesystem:
            filesystem = {}
        
        current_path = self.session.get("current_path", "/")
        
        if not args or args.strip() == "":
            self.session["current_path"] = "/"
            return {"response": "/", "status": "success"}
        
        target = args.strip()
        
        if target == "..":
            if current_path == "/":
                return {"response": "/", "status": "success"}
            parts = current_path.rstrip("/").split("/")
            parts = [p for p in parts if p]
            if len(parts) > 0:
                parts.pop()
            new_path = "/" + "/".join(parts)
            if new_path == "":
                new_path = "/"
            self.session["current_path"] = new_path
            return {"response": new_path, "status": "success"}
        
        if target == ".":
            return {"response": current_path, "status": "success"}
        
        if target.startswith("/"):
            new_path = target
        else:
            if current_path == "/":
                new_path = "/" + target
            else:
                new_path = current_path + "/" + target
        
        new_path = new_path.replace("//", "/")
        if new_path != "/" and new_path.endswith("/"):
            new_path = new_path.rstrip("/")
        
        if self._path_exists(filesystem, new_path):
            self.session["current_path"] = new_path
            return {"response": new_path, "status": "success"}
        else:
            if self.lang == "FR":
                return {"response": f"cd: {target}: Aucun fichier ou dossier de ce type", "status": "error"}
            else:
                return {"response": f"cd: {target}: No such file or directory", "status": "error"}
    
    def _path_exists(self, filesystem: Dict, path: str) -> bool:
        if path == "/":
            return True
        
        parts = path.strip("/").split("/")
        current = filesystem
        
        for part in parts:
            if isinstance(current, dict) and part in current:
                current = current[part]
            else:
                return False
        
        return isinstance(current, dict)
