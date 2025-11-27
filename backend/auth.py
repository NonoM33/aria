import hashlib
import secrets
from datetime import datetime
from sqlalchemy.orm import Session
from database import Player, get_db

def hash_password(password: str) -> str:
    """Hash un mot de passe avec SHA256 + salt"""
    salt = secrets.token_hex(16)
    password_hash = hashlib.sha256((password + salt).encode()).hexdigest()
    return f"{salt}:{password_hash}"

def verify_password(password: str, stored_hash: str) -> bool:
    """Vérifie un mot de passe"""
    try:
        salt, password_hash = stored_hash.split(":")
        computed_hash = hashlib.sha256((password + salt).encode()).hexdigest()
        return computed_hash == password_hash
    except:
        return False

def create_player(db: Session, username: str, password: str) -> Player:
    """Crée un nouveau joueur"""
    # Vérifier si le joueur existe déjà
    existing = db.query(Player).filter(Player.username == username).first()
    if existing:
        raise ValueError("Username already exists")
    
    # Créer le joueur
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
    """Authentifie un joueur"""
    player = db.query(Player).filter(Player.username == username).first()
    if not player:
        raise ValueError("Invalid credentials")
    
    if not verify_password(password, player.password_hash):
        raise ValueError("Invalid credentials")
    
    player.last_login = datetime.utcnow()
    db.commit()
    return player

def get_player_by_username(db: Session, username: str) -> Player:
    """Récupère un joueur par son username"""
    return db.query(Player).filter(Player.username == username).first()

def get_player_by_id(db: Session, player_id: int) -> Player:
    """Récupère un joueur par son ID"""
    return db.query(Player).filter(Player.id == player_id).first()

def save_player_progress(db: Session, player: Player):
    """Sauvegarde la progression d'un joueur"""
    db.commit()
    db.refresh(player)

