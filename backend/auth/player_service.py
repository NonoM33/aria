from datetime import datetime
from typing import Dict, Any, Optional
from sqlalchemy.orm import Session
from database import Player
from auth.password import hash_password, verify_password

def create_player(db: Session, username: str, password: str) -> Player:
    existing = db.query(Player).filter(Player.username == username).first()
    if existing:
        raise ValueError("Username already exists")
    
    player = Player(
        username=username,
        password_hash=hash_password(password),
        created_at=datetime.utcnow(),
        last_login=datetime.utcnow(),
        level=0,
        chapter="chapter_1",
        logged_in=False,
        unlocked_commands=["HELP", "STATUS", "LOGIN"],
        accessed_files=[],
        solved_puzzles=[],
        collected_items=[],
        flags=[],
        language="FR"
    )
    
    db.add(player)
    db.commit()
    db.refresh(player)
    return player

def authenticate_player(db: Session, username: str, password: str) -> Player:
    player = db.query(Player).filter(Player.username == username).first()
    if not player:
        raise ValueError("Invalid credentials")
    
    if not verify_password(password, player.password_hash):
        raise ValueError("Invalid credentials")
    
    player.last_login = datetime.utcnow()
    db.commit()
    return player

def get_player_by_username(db: Session, username: str) -> Optional[Player]:
    return db.query(Player).filter(Player.username == username).first()

def get_player_by_id(db: Session, player_id: int) -> Optional[Player]:
    return db.query(Player).filter(Player.id == player_id).first()

def save_player_progress(db: Session, player: Player):
    db.commit()
    db.refresh(player)

def player_to_session_dict(player: Player) -> Dict[str, Any]:
    return {
        "level": player.level,
        "chapter": player.chapter,
        "logged_in": player.logged_in,
        "unlocked_commands": player.unlocked_commands or [],
        "accessed_files": player.accessed_files or [],
        "solved_puzzles": player.solved_puzzles or [],
        "collected_items": player.collected_items or [],
        "flags": player.flags or [],
        "language": player.language or "FR",
        "username": player.username,
        "player_id": player.id
    }

