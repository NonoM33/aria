from typing import Dict, Optional, Any
from sqlalchemy.orm import Session
from config import DEFAULT_LANGUAGE, SUPPORTED_LANGUAGES
from auth.player_service import get_player_by_username, get_player_by_id, player_to_session_dict
from adventures.global_state import GlobalState

global_state = GlobalState()
sessions: Dict[str, Dict] = {}

def normalize_language(language: Optional[str]) -> str:
    if not language:
        return DEFAULT_LANGUAGE
    lang_upper = language.upper().strip()
    if lang_upper not in SUPPORTED_LANGUAGES:
        return DEFAULT_LANGUAGE
    return lang_upper

def get_session(
    session_id: str,
    language: str = DEFAULT_LANGUAGE,
    db: Optional[Session] = None,
    username: Optional[str] = None,
    token: Optional[str] = None
) -> Dict[str, Any]:
    lang = normalize_language(language)
    
    existing_session = sessions.get(session_id, {})
    ssh_pending_username = existing_session.get("ssh_pending_username")
    
    if username and db:
        try:
            player = get_player_by_username(db, username)
            if player:
                session_dict = player_to_session_dict(player)
                session_dict["language"] = lang
                if ssh_pending_username:
                    session_dict["ssh_pending_username"] = ssh_pending_username
                sessions[session_id] = session_dict
                return session_dict
        except:
            pass
    
    if token and db:
        try:
            from auth.session import verify_jwt_token
            payload = verify_jwt_token(token)
            if payload:
                player = get_player_by_id(db, payload.get("player_id"))
                if player:
                    session_dict = player_to_session_dict(player)
                    session_dict["language"] = lang
                    if ssh_pending_username:
                        session_dict["ssh_pending_username"] = ssh_pending_username
                    sessions[session_id] = session_dict
                    return session_dict
        except:
            pass
    
    is_new_session = session_id not in sessions
    
    if is_new_session:
        sessions[session_id] = {
            "level": 0,
            "chapter": "chapter_0",
            "logged_in": False,
            "unlocked_commands": ["HELP", "STATUS", "SCAN", "LS", "EXPLOIT", "CREATE_USER", "SSH", "EXIT"],
            "accessed_files": [],
            "solved_puzzles": [],
            "collected_items": [],
            "flags": [],
            "language": lang,
            "username": None,
            "player_id": None,
            "installed_packages": []
        }
        global_state.add_player()
    
    sessions[session_id]["language"] = lang
    return sessions[session_id]

def update_session_language(session_id: str, language: str):
    if session_id in sessions:
        sessions[session_id]["language"] = normalize_language(language)

