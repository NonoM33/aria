from typing import Dict, Any
from commands.base_command import BaseCommand
from config import ENCRYPTION_KEY
from adventures.adventure_data import get_adventure_data
from adventures.global_state import GlobalState

global_state = GlobalState()

class LoginCommand(BaseCommand):
    def execute(self, args: str) -> Dict[str, Any]:
        if not args:
            if self.lang == "FR":
                return {"response": "Entrez la clé d'encryption...\nFormat: LOGIN <clé>", "status": "info"}
            else:
                return {"response": "Enter encryption key...\nFormat: LOGIN <key>", "status": "info"}
        
        if args.upper() == ENCRYPTION_KEY:
            self.update_session({
                "logged_in": True,
                "level": 1,
                "chapter": "chapter_2"
            })
            self.add_unlocked_command("SCAN")
            self.add_unlocked_command("DECODE")
            self.add_unlocked_command("ACCESS")
            
            global_state.update_integrity(global_state._state["global_integrity"] + 1)
            global_state.unlock_chapter("chapter_2")
            
            adventure_data = get_adventure_data(self.lang)
            data = adventure_data.get(self.lang, {})
            chapter_2_data = data.get("chapters", {}).get("chapter_2", {})
            intro = chapter_2_data.get("intro", "")
            
            global_integrity = global_state._state["global_integrity"]
            if self.lang == "FR":
                intro += f"\n\nNouvelles commandes: SCAN, DECODE, ACCESS\n\n[GLOBAL] Intégrité mondiale: {global_integrity}% ({global_state._state['players_online']} joueurs actifs)"
            else:
                intro += f"\n\nNew commands: SCAN, DECODE, ACCESS\n\n[GLOBAL] World integrity: {global_integrity}% ({global_state._state['players_online']} active players)"
            
            return {"response": intro, "status": "success"}
        else:
            if self.lang == "FR":
                return {"response": "Clé d'encryption invalide. Accès refusé.", "status": "error"}
            else:
                return {"response": "Invalid encryption key. Access denied.", "status": "error"}

