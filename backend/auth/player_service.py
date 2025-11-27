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
        language="FR",
        installed_packages=[]
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
    try:
        installed_packages = player.installed_packages or []
    except (AttributeError, KeyError):
        installed_packages = []
    
    try:
        choices = player.choices or {}
    except (AttributeError, KeyError):
        choices = {}
    
    try:
        aria_trust = player.aria_trust if player.aria_trust is not None else 50
    except (AttributeError, KeyError):
        aria_trust = 50
    
    try:
        puzzle_attempts = player.puzzle_attempts or {}
    except (AttributeError, KeyError):
        puzzle_attempts = {}
    
    try:
        narrative_flags = player.narrative_flags or []
    except (AttributeError, KeyError):
        narrative_flags = []
    
    try:
        discovered_secrets = player.discovered_secrets or []
    except (AttributeError, KeyError):
        discovered_secrets = []
    
    try:
        aria_dialogue_progress = player.aria_dialogue_progress or 0
    except (AttributeError, KeyError):
        aria_dialogue_progress = 0
    
    try:
        ending = player.ending
    except (AttributeError, KeyError):
        ending = None
    
    try:
        game_completed = player.game_completed or False
    except (AttributeError, KeyError):
        game_completed = False
    
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
        "player_id": player.id,
        "installed_packages": installed_packages,
        "choices": choices,
        "aria_trust": aria_trust,
        "puzzle_attempts": puzzle_attempts,
        "narrative_flags": narrative_flags,
        "discovered_secrets": discovered_secrets,
        "aria_dialogue_progress": aria_dialogue_progress,
        "ending": ending,
        "game_completed": game_completed,
        "aliases": aliases
    }

