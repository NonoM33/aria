from typing import Dict, Any
from commands.base_command import BaseCommand
from adventures.adventure_data import get_adventure_data

class StatusCommand(BaseCommand):
    def execute(self, args: str) -> Dict[str, Any]:
        integrity = 34 + (self.session.get("level", 0) * 15)
        if self.session.get("level", 0) >= 5:
            integrity = 100
        
        adventure_data = get_adventure_data(self.lang)
        data = adventure_data.get(self.lang, {})
        chapter_id = self.session.get("chapter", "chapter_1")
        chapter = data.get("chapters", {}).get(chapter_id, {})
        
        if self.session.get("level", 0) == 0:
            if self.lang == "FR":
                status_msg = f"Intégrité du système: {integrity}%\nNiveau de sécurité: CRITIQUE\n\nMessage système: Le vide attend... 2024"
            else:
                status_msg = f"System Integrity: {integrity}%\nSecurity Level: CRITICAL\n\nSystem Message: The void awaits... 2024"
        else:
            if self.lang == "FR":
                status_msg = f"Intégrité du système: {integrity}%\nNiveau de sécurité: {'CRITIQUE' if self.session.get('level', 0) < 3 else 'BRÈCHE'}\nNiveau d'accès: {self.session.get('level', 0)}\nChapitre: {chapter.get('title', 'N/A')}"
            else:
                status_msg = f"System Integrity: {integrity}%\nSecurity Level: {'CRITICAL' if self.session.get('level', 0) < 3 else 'BREACHED'}\nAccess Level: {self.session.get('level', 0)}\nChapter: {chapter.get('title', 'N/A')}"
        
        return {"response": status_msg, "status": "success"}

