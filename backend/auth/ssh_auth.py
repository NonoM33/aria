from typing import Optional, Dict, Any
from sqlalchemy.orm import Session
from auth.player_service import get_player_by_username, create_player
from auth.session import create_jwt_token, verify_jwt_token
from config import DEFAULT_LANGUAGE

def hack_database_and_create_user(db: Session, username: str, password: str) -> Dict[str, Any]:
    try:
        player = create_player(db, username, password)
        token = create_jwt_token(player.username, player.id)
        return {
            "success": True,
            "username": player.username,
            "token": token,
            "message": f"User {username} created successfully via database exploit"
        }
    except ValueError as e:
        if "already exists" in str(e):
            player = get_player_by_username(db, username)
            if player:
                token = create_jwt_token(player.username, player.id)
                return {
                    "success": True,
                    "username": player.username,
                    "token": token,
                    "message": f"User {username} already exists, token generated"
                }
        return {
            "success": False,
            "message": str(e)
        }
    except Exception as e:
        return {
            "success": False,
            "message": f"Database exploit failed: {str(e)}"
        }

def ssh_connect(db: Session, username: str, password: Optional[str] = None, token: Optional[str] = None) -> Dict[str, Any]:
    if token:
        payload = verify_jwt_token(token)
        if payload and payload.get("username") == username:
            player = get_player_by_username(db, username)
            if player:
                new_token = create_jwt_token(player.username, player.id)
                return {
                    "success": True,
                    "username": player.username,
                    "token": new_token,
                    "player_id": player.id
                }
    
    if password:
        try:
            from auth.player_service import authenticate_player
            player = authenticate_player(db, username, password)
            token = create_jwt_token(player.username, player.id)
            return {
                "success": True,
                "username": player.username,
                "token": token,
                "player_id": player.id
            }
        except ValueError:
            pass
    
    return {
        "success": False,
        "message": "SSH connection failed: Invalid credentials or token"
    }

def validate_ssh_token(token: str) -> Optional[Dict[str, Any]]:
    return verify_jwt_token(token)

