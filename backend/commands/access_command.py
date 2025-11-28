from typing import Dict, Any
from commands.base_command import BaseCommand
from adventures.adventure_loader import get_chapter_filesystem
from services.aria_service import get_aria_trigger
from services.resource_service import get_resource_manager, get_quest_manager, get_achievement_manager

class AccessCommand(BaseCommand):
    def execute(self, args: str) -> Dict[str, Any]:
        if not args:
            if self.lang == "FR":
                return {"response": "Usage: ACCESS <nom_fichier>\nExemple: ACCESS readme.txt", "status": "info"}
            else:
                return {"response": "Usage: ACCESS <filename>\nExample: ACCESS readme.txt", "status": "info"}
        
        chapter_id = self.session.get("chapter", "chapter_0")
        filesystem = get_chapter_filesystem(chapter_id, self.lang)
        
        if not filesystem:
            filesystem = {}
        
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
            
            # Consommer des ressources
            resource_manager = get_resource_manager(self.session)
            if not resource_manager.consume_resource("cpu", 0.5):
                if self.lang == "FR":
                    return {"response": "CPU insuffisant. Utilisez RESOURCE RESTORE cpu ou attendez.", "status": "error"}
                else:
                    return {"response": "Insufficient CPU. Use RESOURCE RESTORE cpu or wait.", "status": "error"}
            
            resource_manager.consume_resource("energy", 0.3)
            
            self.add_accessed_file(file_path)
            
            # Mettre à jour les quêtes et achievements
            quest_manager = get_quest_manager(self.session)
            quest_manager.update_quest_progress("explore", 1)
            
            achievement_manager = get_achievement_manager(self.session)
            achievement_result = achievement_manager.check_achievements("file_access", {"filename": filename})
            
            if "vulnerability_log" in filename.lower() or "vulnerability" in filename.lower():
                self.add_unlocked_command("EXPLOIT")
            
            if "crypte" in filename.lower() or "encrypted" in filename.lower() or filename.endswith(".b64"):
                if self.lang == "FR":
                    content += "\n\n[Indice: Utilisez DECODE pour decoder ce fichier]"
                else:
                    content += "\n\n[Hint: Use DECODE to decode this file]"
            
            response = {"response": content, "status": "success"}
            
            if achievement_result:
                achievement_msg = f"\n\n🏆 Achievement débloqué: {achievement_result['title']} (+{achievement_result.get('credits', 0)} crédits)"
                response["response"] += achievement_msg
            
            aria_data = get_aria_trigger(
                self.session, 
                "file_access", 
                {"filename": filename, "path": file_path},
                self.lang
            )
            if aria_data:
                if aria_data.get("aria_flag"):
                    self.session.setdefault("aria_flags", []).append(aria_data["aria_flag"])
                response.update(aria_data)
            
            return response
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
