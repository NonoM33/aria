from typing import Dict, Any
from commands.base_command import BaseCommand


class PwdCommand(BaseCommand):
    def execute(self, args: str) -> Dict[str, Any]:
        current_path = self.session.get("current_path", "/")
        return {"response": current_path, "status": "success"}

