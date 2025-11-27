from typing import Dict, Any, Optional
from sqlalchemy.orm import Session
from database import Player
from auth.player_service import get_player_by_id, save_player_progress

def save_session_to_db(db: Session, session: Dict[str, Any], player: Optional[Player] = None) -> bool:
    if not db:
        return False
    
    if not player and session.get("player_id"):
        try:
            player = get_player_by_id(db, session["player_id"])
        except:
            pass
    
    if not player:
        return False
    
    try:
        player.level = session.get("level", 0)
        player.chapter = session.get("chapter", "chapter_1")
        player.logged_in = session.get("logged_in", False)
        player.unlocked_commands = session.get("unlocked_commands", [])
        player.accessed_files = session.get("accessed_files", [])
        player.solved_puzzles = session.get("solved_puzzles", [])
        player.collected_items = session.get("collected_items", [])
        player.flags = session.get("flags", [])
        player.language = session.get("language", "FR")
        player.installed_packages = session.get("installed_packages", [])
        player.total_commands = (player.total_commands or 0) + 1
        
        save_player_progress(db, player)
        return True
    except:
        return False

