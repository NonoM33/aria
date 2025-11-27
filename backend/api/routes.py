from fastapi import APIRouter, Depends, Header, WebSocket, WebSocketDisconnect
from pydantic import BaseModel
from typing import Optional, Dict, Any
from sqlalchemy.orm import Session
from commands.command_handler import handle_command
from services.session_service import get_session, normalize_language
from services.progress_service import save_session_to_db
from services.event_service import create_global_event
from adventures.adventure_data import get_adventure_data
from adventures.adventure_loader import get_chapter_filesystem, get_chapter_intro
from adventures.global_state import GlobalState
from man_pages import MAN_PAGES
from api.dependencies import get_database, get_current_user
from api.websocket_manager import manager
from config import DEFAULT_LANGUAGE
import json
import uuid

router = APIRouter()
global_state = GlobalState()

def get_directory_contents(filesystem: dict, path: str) -> dict:
    if path == "/":
        return filesystem
    parts = path.strip("/").split("/")
    current = filesystem
    for part in parts:
        if isinstance(current, dict) and part in current:
            current = current[part]
        else:
            return {}
    if isinstance(current, dict):
        return current
    return {}

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
        if session.get("logged_in") and session.get("username"):
            if lang == "FR":
                welcome_msg = f"SYSTEM_VOID v2.0\n\nBienvenue de retour, {session['username']}!\nVous êtes connecté. Votre progression est sauvegardée.\n\nTapez HELP pour voir les commandes disponibles."
            else:
                welcome_msg = f"SYSTEM_VOID v2.0\n\nWelcome back, {session['username']}!\nYou are connected. Your progress is saved.\n\nType HELP to see available commands."
        else:
            system_messages = data.get("system_messages", {})
            welcome_msg = system_messages.get("welcome", "")
            if not welcome_msg:
                if lang == "EN":
                    welcome_msg = "SYSTEM_VOID v2.0 initialized.\nType HELP to start."
                else:
                    welcome_msg = "SYSTEM_VOID v2.0 initialisé.\nTapez HELP pour commencer."
        
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
                db.commit()
            except Exception as e:
                db.rollback()
            finally:
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
    chapter_id = session.get("chapter", "chapter_0")
    
    filesystem = get_chapter_filesystem(chapter_id, lang)
    
    def get_all_files(fs, prefix=""):
        files = []
        for name, value in fs.items():
            path = f"{prefix}/{name}" if prefix else name
            if isinstance(value, dict):
                files.extend(get_all_files(value, path))
            else:
                files.append(path)
        return files
    
    files = get_all_files(filesystem)
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

@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket, session_id: Optional[str] = None):
    connection_id = str(uuid.uuid4())
    
    if not session_id:
        await websocket.close(code=1008, reason="Session ID required")
        return
    
    await manager.connect(websocket, connection_id, session_id)
    
    from database import SessionLocal
    db = SessionLocal()
    lang = DEFAULT_LANGUAGE
    token = None
    username = None
    
    try:
        session = get_session(session_id, lang, db, username, token)
        
        await manager.send_personal_message({
            "type": "connected",
            "message": "WebSocket connection established"
        }, connection_id)
        
        await send_session_updates(connection_id, session_id, session, lang, db)
        
        while True:
            data = await websocket.receive_json()
            message_type = data.get("type")
            
            if message_type == "command":
                command = data.get("command", "")
                password = data.get("password")
                language = data.get("language", DEFAULT_LANGUAGE)
                auth_token = data.get("token")
                
                lang = normalize_language(language)
                token = auth_token
                
                if auth_token:
                    from auth.session import verify_jwt_token
                    payload = verify_jwt_token(auth_token)
                    if payload:
                        username = payload.get("username")
                
                session = get_session(session_id, lang, db, username, token)
                session["language"] = lang
                
                if password and session.get("ssh_pending_username"):
                    result = handle_command("", password, session, db, lang, token)
                    
                    if result.get("token"):
                        session["ssh_token"] = result.get("token")
                        await manager.send_personal_message({
                            "type": "token_update",
                            "token": result.get("token")
                        }, connection_id)
                    
                    if result.get("username"):
                        await manager.send_personal_message({
                            "type": "username_update",
                            "username": result.get("username")
                        }, connection_id)
                    
                    if db:
                        try:
                            from auth.player_service import get_player_by_id
                            player = None
                            if session.get("player_id"):
                                player = get_player_by_id(db, session["player_id"])
                            if player or session.get("player_id"):
                                from services.progress_service import save_session_to_db
                                save_session_to_db(db, session, player)
                                db.commit()
                        except Exception as e:
                            db.rollback()
                    
                    await manager.send_personal_message({
                        "type": "command_response",
                        "response": result.get("response", ""),
                        "status": result.get("status", "info")
                    }, connection_id)
                    
                    await send_session_updates(connection_id, session_id, session, lang, db)
                    continue
                
                command_parts = command.strip().split(" ", 1) if command.strip() else ["", ""]
                cmd = command_parts[0].upper() if command_parts[0] else ""
                args = command_parts[1] if len(command_parts) > 1 else ""
                
                adventure_data = get_adventure_data(lang)
                data_resp = adventure_data.get(lang, {})
                
                if not cmd or cmd == "":
                    if session.get("logged_in") and session.get("username"):
                        if lang == "FR":
                            welcome_msg = f"SYSTEM_VOID v2.0\n\nBienvenue de retour, {session['username']}!\nVous êtes connecté. Votre progression est sauvegardée.\n\nTapez HELP pour voir les commandes disponibles."
                        else:
                            welcome_msg = f"SYSTEM_VOID v2.0\n\nWelcome back, {session['username']}!\nYou are connected. Your progress is saved.\n\nType HELP to see available commands."
                    else:
                        system_messages = data_resp.get("system_messages", {})
                        welcome_msg = system_messages.get("welcome", "")
                        if not welcome_msg:
                            if lang == "EN":
                                welcome_msg = "SYSTEM_VOID v2.0 initialized.\nType HELP to start."
                            else:
                                welcome_msg = "SYSTEM_VOID v2.0 initialisé.\nTapez HELP pour commencer."
                    
                    await manager.send_personal_message({
                        "type": "command_response",
                        "response": welcome_msg,
                        "status": "info"
                    }, connection_id)
                    continue
                
                player = None
                if session.get("player_id") and db:
                    try:
                        from auth.player_service import get_player_by_id
                        player = get_player_by_id(db, session["player_id"])
                    except:
                        pass
                
                try:
                    result = handle_command(cmd, args, session, db, lang, token)
                    
                    if result.get("token"):
                        session["ssh_token"] = result.get("token")
                        await manager.send_personal_message({
                            "type": "token_update",
                            "token": result.get("token")
                        }, connection_id)
                    
                    if result.get("username"):
                        await manager.send_personal_message({
                            "type": "username_update",
                            "username": result.get("username")
                        }, connection_id)
                    
                    if result.get("logout"):
                        await manager.send_personal_message({
                            "type": "logout",
                            "username": None
                        }, connection_id)
                    
                    if db and (player or session.get("player_id")):
                        try:
                            save_session_to_db(db, session, player)
                            db.commit()
                        except Exception as e:
                            db.rollback()
                    
                    response_message = {
                        "type": "command_response",
                        "response": result.get("response", ""),
                        "status": result.get("status", "info"),
                        "current_path": session.get("current_path", "/")
                    }
                    if result.get("password_prompt"):
                        response_message["password_prompt"] = True
                        response_message["username"] = result.get("username")
                    if result.get("logout"):
                        response_message["logout"] = True
                    if result.get("username") is not None and not result.get("password_prompt"):
                        response_message["username"] = result.get("username")
                    if result.get("token"):
                        response_message["token"] = result.get("token")
                    
                    await manager.send_personal_message(response_message, connection_id)
                    
                    await send_session_updates(connection_id, session_id, session, lang, db)
                    
                except Exception as e:
                    error_msg = str(e)
                    if lang == "FR":
                        await manager.send_personal_message({
                            "type": "command_response",
                            "response": f"Erreur lors de l'exécution de la commande: {error_msg}",
                            "status": "error"
                        }, connection_id)
                    else:
                        await manager.send_personal_message({
                            "type": "command_response",
                            "response": f"Error executing command: {error_msg}",
                            "status": "error"
                        }, connection_id)
            
            elif message_type == "subscribe":
                subscriptions = data.get("subscriptions", [])
                await manager.send_personal_message({
                    "type": "subscribed",
                    "subscriptions": subscriptions
                }, connection_id)
                
                if "global_events" in subscriptions:
                    await send_global_state_update(connection_id)
                if "files" in subscriptions:
                    await send_files_update(connection_id, session_id, lang, db)
                if "commands" in subscriptions:
                    await send_commands_update(connection_id, session_id, lang, db)
                if "packages" in subscriptions:
                    await send_packages_update(connection_id, session_id, lang, db)
            
            elif message_type == "ping":
                await manager.send_personal_message({
                    "type": "pong"
                }, connection_id)
    
    except WebSocketDisconnect:
        manager.disconnect(connection_id, session_id)
    except Exception as e:
        try:
            manager.disconnect(connection_id, session_id)
        except:
            pass
    finally:
        try:
            db.close()
        except:
            pass

async def send_session_updates(connection_id: str, session_id: str, session: Dict[str, Any], lang: str, db: Session):
    chapter_id = session.get("chapter", "chapter_0")
    filesystem = get_chapter_filesystem(chapter_id, lang)
    current_path = session.get("current_path", "/")
    
    await manager.send_personal_message({
        "type": "filesystem_update",
        "filesystem": filesystem,
        "current_path": current_path,
        "chapter": chapter_id,
        "level": session.get("level", 0)
    }, connection_id)
    
    await manager.send_personal_message({
        "type": "commands_update",
        "commands": session.get("unlocked_commands", [])
    }, connection_id)
    
    await manager.send_personal_message({
        "type": "packages_update",
        "packages": session.get("installed_packages", [])
    }, connection_id)

async def send_global_state_update(connection_id: str):
    global_state_data = global_state.get_state()
    await manager.send_personal_message({
        "type": "global_state_update",
        "state": global_state_data
    }, connection_id)

async def send_files_update(connection_id: str, session_id: str, lang: str, db: Session):
    session = get_session(session_id, lang, db, None, None)
    chapter_id = session.get("chapter", "chapter_0")
    filesystem = get_chapter_filesystem(chapter_id, lang)
    current_path = session.get("current_path", "/")
    
    await manager.send_personal_message({
        "type": "filesystem_update",
        "filesystem": filesystem,
        "current_path": current_path,
        "chapter": chapter_id
    }, connection_id)

async def send_commands_update(connection_id: str, session_id: str, lang: str, db: Session):
    session = get_session(session_id, lang, db, None, None)
    await manager.send_personal_message({
        "type": "commands_update",
        "commands": session.get("unlocked_commands", [])
    }, connection_id)

async def send_packages_update(connection_id: str, session_id: str, lang: str, db: Session):
    session = get_session(session_id, lang, db, None, None)
    await manager.send_personal_message({
        "type": "packages_update",
        "packages": session.get("installed_packages", [])
    }, connection_id)

@router.get("/")
async def root():
    return {"message": "SYSTEM_VOID API"}

