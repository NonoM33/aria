from typing import Dict, Optional, Any
from sqlalchemy.orm import Session as DBSession
from config import DEFAULT_LANGUAGE, SUPPORTED_LANGUAGES
from auth.player_service import get_player_by_username, get_player_by_id, player_to_session_dict
from adventures.global_state import GlobalState

global_state = GlobalState()
sessions: Dict[str, Dict] = {}


def track_connection(session_id: str, db: Optional[DBSession] = None):
    if db:
        try:
            from database import Connection
            existing = db.query(Connection).filter(Connection.session_id == session_id).first()
            if not existing:
                connection = Connection(session_id=session_id)
                db.add(connection)
                db.commit()
        except Exception:
            pass


def mark_connection_converted(session_id: str, player_id: int, db: Optional[DBSession] = None):
    if db:
        try:
            from database import Connection
            connection = db.query(Connection).filter(Connection.session_id == session_id).first()
            if connection:
                connection.converted = True
                connection.player_id = player_id
                db.commit()
        except Exception:
            pass

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
    db: Optional[DBSession] = None,
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
                existing_path = existing_session.get("current_path")
                existing_aliases = existing_session.get("aliases")
                existing_voidrc = existing_session.get("voidrc")
                existing_admin_mode = existing_session.get("admin_mode")
                existing_admin_pending = existing_session.get("admin_pending")
                session_dict = player_to_session_dict(player)
                session_dict["language"] = lang
                if ssh_pending_username:
                    session_dict["ssh_pending_username"] = ssh_pending_username
                if existing_path:
                    session_dict["current_path"] = existing_path
                if existing_aliases:
                    session_dict["aliases"] = existing_aliases
                if existing_voidrc:
                    session_dict["voidrc"] = existing_voidrc
                if existing_admin_mode:
                    session_dict["admin_mode"] = existing_admin_mode
                if existing_admin_pending:
                    session_dict["admin_pending"] = existing_admin_pending
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
                    existing_path = existing_session.get("current_path")
                    existing_aliases = existing_session.get("aliases")
                    existing_voidrc = existing_session.get("voidrc")
                    existing_admin_mode = existing_session.get("admin_mode")
                    existing_admin_pending = existing_session.get("admin_pending")
                    session_dict = player_to_session_dict(player)
                    session_dict["language"] = lang
                    if ssh_pending_username:
                        session_dict["ssh_pending_username"] = ssh_pending_username
                    if existing_path:
                        session_dict["current_path"] = existing_path
                    if existing_aliases:
                        session_dict["aliases"] = existing_aliases
                    if existing_voidrc:
                        session_dict["voidrc"] = existing_voidrc
                    if existing_admin_mode:
                        session_dict["admin_mode"] = existing_admin_mode
                    if existing_admin_pending:
                        session_dict["admin_pending"] = existing_admin_pending
                    sessions[session_id] = session_dict
                    return session_dict
        except:
            pass
    
    is_new_session = session_id not in sessions
    
    if is_new_session:
        sessions[session_id] = {
            "session_id": session_id,
            "level": 0,
            "chapter": "chapter_0",
            "logged_in": False,
            "unlocked_commands": ["HELP", "STATUS", "SCAN", "LS", "SSH", "EXIT", "EDIT", "MONITOR", "RESOURCE"],
            "accessed_files": [],
            "solved_puzzles": [],
            "collected_items": [],
            "flags": [],
            "language": lang,
            "username": None,
            "player_id": None,
            "installed_packages": [],
            "choices": {},
            "aria_trust": 50,
            "puzzle_attempts": {},
            "narrative_flags": [],
            "discovered_secrets": [],
            "aria_dialogue_progress": 0,
            "ending": None,
            "game_completed": False,
            "current_path": "/",
            "aliases": {},
            "voidrc": "",
            "credits": 100
        }
        global_state.add_player()
        track_connection(session_id, db)
    
    sessions[session_id]["language"] = lang
    return sessions[session_id]

def update_session_language(session_id: str, language: str):
    if session_id in sessions:
        sessions[session_id]["language"] = normalize_language(language)

