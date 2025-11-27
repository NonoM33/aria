from abc import ABC, abstractmethod
from typing import Dict, Any, Optional
from sqlalchemy.orm import Session

class BaseCommand(ABC):
    def __init__(self, session: Dict[str, Any], db: Optional[Session], lang: str):
        self.session = session
        self.db = db
        self.lang = lang
    
    @abstractmethod
    def execute(self, args: str) -> Dict[str, Any]:
        pass
    
    def check_level(self, required_level: int) -> bool:
        return self.session.get("level", 0) >= required_level
    
    def get_chapter_data(self, adventure_data: Dict[str, Any]) -> Dict[str, Any]:
        chapter_id = self.session.get("chapter", "chapter_1")
        return adventure_data.get("chapters", {}).get(chapter_id, {})
    
    def update_session(self, updates: Dict[str, Any]):
        self.session.update(updates)
    
    def add_unlocked_command(self, command: str):
        if command not in self.session.get("unlocked_commands", []):
            self.session.setdefault("unlocked_commands", []).append(command)
    
    def add_solved_puzzle(self, puzzle_id: str):
        if puzzle_id not in self.session.get("solved_puzzles", []):
            self.session.setdefault("solved_puzzles", []).append(puzzle_id)
    
    def add_accessed_file(self, filename: str):
        if filename not in self.session.get("accessed_files", []):
            self.session.setdefault("accessed_files", []).append(filename)

