from typing import Dict, Any
from commands.base_command import BaseCommand
from adventures.aria_dialogues import get_random_idle_message
from services.aria_service import handle_aria_choice, is_aria_choice_command


class TalkCommand(BaseCommand):
    def execute(self, args: str) -> Dict[str, Any]:
        if not self.session.get("logged_in"):
            if self.lang == "FR":
                return {
                    "response": "...",
                    "status": "info",
                    "aria_state": "dormant"
                }
            else:
                return {
                    "response": "...",
                    "status": "info", 
                    "aria_state": "dormant"
                }
        
        if args and is_aria_choice_command(args.strip()):
            result = handle_aria_choice(self.session, args.strip(), self.lang)
            if result:
                return {"response": "", "status": "success", **result}
        
        idle_msg = get_random_idle_message(self.lang)
        
        return {
            "response": f"[ARIA]\n{idle_msg}",
            "status": "info",
            "aria_state": "idle",
            "aria_emotion": "curious"
        }


class AriaCommand(BaseCommand):
    def execute(self, args: str) -> Dict[str, Any]:
        talk_cmd = TalkCommand(self.session, self.db, self.lang)
        return talk_cmd.execute(args)
