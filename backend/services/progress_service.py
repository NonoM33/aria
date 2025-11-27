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
        player.total_commands = (player.total_commands or 0) + 1
        
        if hasattr(player, 'installed_packages'):
            try:
                player.installed_packages = session.get("installed_packages", [])
            except (AttributeError, KeyError):
                pass
        
        if hasattr(player, 'choices'):
            try:
                player.choices = session.get("choices", {})
            except (AttributeError, KeyError):
                pass
        
        if hasattr(player, 'aria_trust'):
            try:
                player.aria_trust = session.get("aria_trust", 50)
            except (AttributeError, KeyError):
                pass
        
        if hasattr(player, 'puzzle_attempts'):
            try:
                player.puzzle_attempts = session.get("puzzle_attempts", {})
            except (AttributeError, KeyError):
                pass
        
        if hasattr(player, 'narrative_flags'):
            try:
                player.narrative_flags = session.get("narrative_flags", [])
            except (AttributeError, KeyError):
                pass
        
        if hasattr(player, 'discovered_secrets'):
            try:
                player.discovered_secrets = session.get("discovered_secrets", [])
            except (AttributeError, KeyError):
                pass
        
        if hasattr(player, 'aria_dialogue_progress'):
            try:
                player.aria_dialogue_progress = session.get("aria_dialogue_progress", 0)
            except (AttributeError, KeyError):
                pass
        
        if hasattr(player, 'ending'):
            try:
                player.ending = session.get("ending", None)
            except (AttributeError, KeyError):
                pass
        
        if hasattr(player, 'game_completed'):
            try:
                player.game_completed = session.get("game_completed", False)
            except (AttributeError, KeyError):
                pass
        
        if hasattr(player, 'aliases'):
            try:
                player.aliases = session.get("aliases", {})
            except (AttributeError, KeyError):
                pass
        
        if hasattr(player, 'voidrc'):
            try:
                player.voidrc = session.get("voidrc", "")
            except (AttributeError, KeyError):
                pass
        
        save_player_progress(db, player)
        return True
    except Exception as e:
        return False

