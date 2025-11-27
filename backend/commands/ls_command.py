from typing import Dict, Any
from commands.base_command import BaseCommand
from adventures.adventure_loader import get_chapter_filesystem

class LsCommand(BaseCommand):
    def execute(self, args: str) -> Dict[str, Any]:
        chapter_id = self.session.get("chapter", "chapter_0")
        filesystem = get_chapter_filesystem(chapter_id, self.lang)
        
        if not filesystem:
            filesystem = {}
        
        current_path = self.session.get("current_path", "/")
        
        if args and args.strip():
            target_path = args.strip()
            if target_path.startswith("/"):
                path_to_list = target_path
            else:
                if current_path == "/":
                    path_to_list = "/" + target_path
                else:
                    path_to_list = current_path + "/" + target_path
        else:
            path_to_list = current_path
        
        path_to_list = path_to_list.replace("//", "/")
        
        contents = self._get_directory_contents(filesystem, path_to_list)
        
        if contents is None:
            if self.lang == "FR":
                return {"response": f"ls: impossible d'acceder a '{args.strip()}': Aucun fichier ou dossier de ce type", "status": "error"}
            else:
                return {"response": f"ls: cannot access '{args.strip()}': No such file or directory", "status": "error"}
        
        if not contents:
            if self.lang == "FR":
                return {"response": "(dossier vide)", "status": "success"}
            else:
                return {"response": "(empty directory)", "status": "success"}
        
        dirs = []
        files = []
        for name, value in contents.items():
            if isinstance(value, dict):
                dirs.append(f"[DIR]  {name}/")
            else:
                files.append(f"       {name}")
        
        dirs.sort()
        files.sort()
        
        result_lines = dirs + files
        result = "\n".join(result_lines)
        
        return {"response": result, "status": "success"}
    
    def _get_directory_contents(self, filesystem: Dict, path: str) -> Dict:
        if path == "/":
            return filesystem
        
        parts = path.strip("/").split("/")
        current = filesystem
        
        for part in parts:
            if isinstance(current, dict) and part in current:
                current = current[part]
            else:
                return None
        
        if isinstance(current, dict):
            return current
        else:
            return None

