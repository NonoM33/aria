from fastapi import APIRouter, Depends, Header
from pydantic import BaseModel
from typing import Optional, Dict, Any
from sqlalchemy.orm import Session
from commands.command_handler import handle_command
from services.session_service import get_session, normalize_language
from services.progress_service import save_session_to_db
from services.event_service import create_global_event
from adventures.adventure_data import get_adventure_data
from adventures.global_state import GlobalState
from man_pages import MAN_PAGES
from api.dependencies import get_database, get_current_user
from config import DEFAULT_LANGUAGE

router = APIRouter()
global_state = GlobalState()

class CommandRequest(BaseModel):
    command: str
    session_id: str
    language: Optional[str] = DEFAULT_LANGUAGE
    username: Optional[str] = None

@router.post("/api/command")
async def handle_command_route(
    request: CommandRequest,
    authorization: Optional[str] = Header(None),
    db: Session = Depends(get_database)
):
    command_parts = request.command.strip().split(" ", 1)
    command = command_parts[0].upper() if request.command.strip() else ""
    args = command_parts[1] if len(command_parts) > 1 else ""
    
    lang = normalize_language(request.language)
    
    token = None
    if authorization and authorization.startswith("Bearer "):
        token = authorization[7:]
    
    session = get_session(request.session_id, lang, db, request.username, token)
    session["language"] = lang
    
    adventure_data = get_adventure_data(lang)
    data = adventure_data.get(lang, {})
    
    if not command or command == "":
        system_messages = data.get("system_messages", {})
        welcome_msg = system_messages.get("welcome", "")
        if not welcome_msg:
            if lang == "EN":
                welcome_msg = "SYSTEM_VOID v2.0 initialized.\nType HELP to start."
            else:
                welcome_msg = "SYSTEM_VOID v2.0 initialisé.\nTapez HELP pour commencer."
        
        if session.get("username"):
            if lang == "FR":
                welcome_msg += f"\n\nBienvenue de retour, {session['username']}!"
            else:
                welcome_msg += f"\n\nWelcome back, {session['username']}!"
        
        return {"response": welcome_msg, "status": "info"}
    
    player = None
    if session.get("player_id") and db:
        try:
            from auth.player_service import get_player_by_id
            player = get_player_by_id(db, session["player_id"])
        except:
            pass
    
    try:
        result = handle_command(command, args, session, db, lang, token)
        
        if result.get("token"):
            session["ssh_token"] = result.get("token")
        
        if db and (player or session.get("player_id")):
            try:
                save_session_to_db(db, session, player)
            except Exception as e:
                pass
        
        return result
    except Exception as e:
        import traceback
        error_msg = str(e)
        if lang == "FR":
            return {
                "response": f"Erreur lors de l'exécution de la commande: {error_msg}",
                "status": "error"
            }
        else:
            return {
                "response": f"Error executing command: {error_msg}",
                "status": "error"
            }

@router.get("/api/man/{command}")
async def get_man_page(command: str, language: str = DEFAULT_LANGUAGE):
    lang = normalize_language(language)
    command_upper = command.upper()
    man_pages = MAN_PAGES.get(lang, MAN_PAGES["FR"])
    
    if command_upper in man_pages:
        return {
            "command": command_upper,
            "content": man_pages[command_upper],
            "language": lang
        }
    else:
        if lang == "FR":
            return {
                "command": command_upper,
                "content": f"MAN(1)                    Manuel SYSTEM_VOID                   MAN(1)\n\nAucune page de manuel trouvée pour '{command_upper}'.\n\nUtilisez MAN HELP pour voir les commandes disponibles.",
                "language": lang
            }
        else:
            return {
                "command": command_upper,
                "content": f"MAN(1)                    SYSTEM_VOID Manual                   MAN(1)\n\nNo manual page found for '{command_upper}'.\n\nUse MAN HELP to see available commands.",
                "language": lang
            }

@router.get("/api/unlocked-commands")
async def get_unlocked_commands(session_id: str, language: str = DEFAULT_LANGUAGE):
    lang = normalize_language(language)
    session = get_session(session_id, lang)
    return {"commands": session.get("unlocked_commands", [])}

@router.get("/api/files")
async def get_available_files(session_id: str, language: str = DEFAULT_LANGUAGE):
    lang = normalize_language(language)
    session = get_session(session_id, lang)
    chapter_id = session.get("chapter", "chapter_1")
    
    adventure_data = get_adventure_data(lang)
    data = adventure_data.get(lang, {})
    chapter = data.get("chapters", {}).get(chapter_id, {})
    
    files = list(chapter.get("files", {}).keys())
    return {"files": files}

@router.get("/api/packages")
async def get_installed_packages(
    session_id: str,
    language: str = DEFAULT_LANGUAGE,
    authorization: Optional[str] = Header(None),
    db: Session = Depends(get_database)
):
    lang = normalize_language(language)
    
    token = None
    if authorization and authorization.startswith("Bearer "):
        token = authorization[7:]
    
    username = None
    session = get_session(session_id, lang, db, username, token)
    
    installed_packages = session.get("installed_packages", [])
    return {"packages": installed_packages}

@router.get("/api/global-status")
async def get_global_status(session_id: Optional[str] = None):
    global_state_data = global_state.get_state()
    
    from services.session_service import sessions
    if session_id and session_id in sessions:
        session = sessions[session_id]
        integrity = 34 + (session.get("level", 0) * 15)
        if session.get("level", 0) >= 5:
            integrity = 100
        return {
            "system_integrity": integrity,
            "global_integrity": global_state_data["global_integrity"],
            "active_users": global_state_data["players_online"],
            "total_players": global_state_data["total_players"],
            "security_level": "CRITICAL" if session.get("level", 0) < 3 else "BREACHED",
            "access_level": session.get("level", 0),
            "chapter": session.get("chapter", "chapter_1"),
            "world_state": global_state_data["world_state"],
            "chapters_unlocked": global_state_data["chapters_unlocked"],
            "last_update": global_state_data["last_update"]
        }
    return {
        "system_integrity": 34,
        "global_integrity": global_state_data["global_integrity"],
        "active_users": global_state_data["players_online"],
        "total_players": global_state_data["total_players"],
        "security_level": "CRITICAL",
        "world_state": global_state_data["world_state"],
        "last_update": global_state_data["last_update"]
    }

@router.get("/api/global-events")
async def get_global_events(limit: int = 10, db: Session = Depends(get_database)):
    if not db:
        return {"events": []}
    
    try:
        from database import GlobalEvent
        events = db.query(GlobalEvent).order_by(GlobalEvent.created_at.desc()).limit(limit).all()
        return {
            "events": [
                {
                    "type": event.event_type,
                    "data": event.event_data,
                    "triggered_by": event.triggered_by,
                    "impact_level": event.impact_level,
                    "created_at": event.created_at.isoformat() if event.created_at else None
                }
                for event in events
            ]
        }
    except:
        return {"events": []}

@router.get("/")
async def root():
    return {"message": "SYSTEM_VOID API"}

