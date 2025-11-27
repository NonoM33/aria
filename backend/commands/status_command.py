from typing import Dict, Any
from commands.base_command import BaseCommand
from adventures.adventure_loader import get_chapter

class StatusCommand(BaseCommand):
    def execute(self, args: str) -> Dict[str, Any]:
        level = self.session.get("level", 0)
        integrity = 34 + (level * 15)
        if level >= 5:
            integrity = 100
        
        chapter_id = self.session.get("chapter", "chapter_0")
        chapter = get_chapter(chapter_id, self.lang)
        chapter_title = chapter.get("title", "N/A") if chapter else "N/A"
        current_path = self.session.get("current_path", "/")
        
        if level == 0:
            if self.lang == "FR":
                status_msg = f"""STATUT SYSTEME
==============
Integrite: {integrity}%
Securite: CRITIQUE
Chemin: {current_path}

Message: Le vide attend... 2024"""
            else:
                status_msg = f"""SYSTEM STATUS
=============
Integrity: {integrity}%
Security: CRITICAL
Path: {current_path}

Message: The void awaits... 2024"""
        else:
            security = "CRITIQUE" if level < 3 else "BRECHE"
            security_en = "CRITICAL" if level < 3 else "BREACHED"
            
            if self.lang == "FR":
                status_msg = f"""STATUT SYSTEME
==============
Integrite: {integrity}%
Securite: {security}
Niveau d'acces: {level}
Chapitre: {chapter_title}
Chemin: {current_path}"""
            else:
                status_msg = f"""SYSTEM STATUS
=============
Integrity: {integrity}%
Security: {security_en}
Access Level: {level}
Chapter: {chapter_title}
Path: {current_path}"""
        
        return {"response": status_msg, "status": "success"}
