from typing import Dict, Any
from commands.base_command import BaseCommand
from adventures.adventure_data import get_adventure_data

class AnalyzeCommand(BaseCommand):
    def execute(self, args: str) -> Dict[str, Any]:
        if not self.check_level(2):
            if self.lang == "FR":
                return {"response": "Niveau d'accès insuffisant.", "status": "error"}
            else:
                return {"response": "Insufficient access level.", "status": "error"}
        
        if not args:
            if self.lang == "FR":
                return {"response": "Usage: ANALYZE <sujet>\nExemples: ANALYZE security, ANALYZE network", "status": "info"}
            else:
                return {"response": "Usage: ANALYZE <subject>\nExamples: ANALYZE security, ANALYZE network", "status": "info"}
        
        subject = args.lower().strip()
        if subject == "security" or subject == "sécurité":
            adventure_data = get_adventure_data(self.lang)
            data = adventure_data.get(self.lang, {})
            chapter_3 = data.get("chapters", {}).get("chapter_3", {})
            files = chapter_3.get("files", {})
            security_log = files.get("security_log.txt", "")
            if self.lang == "FR":
                return {"response": f"Analyse de sécurité:\n\n{security_log}", "status": "success"}
            else:
                return {"response": f"Security analysis:\n\n{security_log}", "status": "success"}
        elif subject == "network" or subject == "réseau":
            if self.lang == "FR":
                return {"response": "Utilisez la commande NETWORK pour voir la carte du réseau.", "status": "info"}
            else:
                return {"response": "Use NETWORK command to see network map.", "status": "info"}
        else:
            if self.lang == "FR":
                return {"response": f"Analyse de '{subject}' non disponible.", "status": "error"}
            else:
                return {"response": f"Analysis of '{subject}' not available.", "status": "error"}

