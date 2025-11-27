from sqlalchemy import create_engine, Column, Integer, String, Boolean, JSON, DateTime, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from datetime import datetime
import json
import os

Base = declarative_base()

class Player(Base):
    __tablename__ = "players"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    password_hash = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    last_login = Column(DateTime, default=datetime.utcnow)
    
    level = Column(Integer, default=0)
    chapter = Column(String, default="chapter_1")
    logged_in = Column(Boolean, default=False)
    unlocked_commands = Column(JSON, default=list)
    accessed_files = Column(JSON, default=list)
    solved_puzzles = Column(JSON, default=list)
    collected_items = Column(JSON, default=list)
    flags = Column(JSON, default=list)
    language = Column(String, default="FR")
    installed_packages = Column(JSON, default=list)
    
    choices = Column(JSON, default=dict)
    aria_trust = Column(Integer, default=50)
    puzzle_attempts = Column(JSON, default=dict)
    narrative_flags = Column(JSON, default=list)
    discovered_secrets = Column(JSON, default=list)
    aria_dialogue_progress = Column(Integer, default=0)
    ending = Column(String, nullable=True)
    game_completed = Column(Boolean, default=False)
    aliases = Column(JSON, default=dict)
    
    total_commands = Column(Integer, default=0)
    total_playtime = Column(Integer, default=0)
    achievements = Column(JSON, default=list)

class GlobalEvent(Base):
    __tablename__ = "global_events"
    
    id = Column(Integer, primary_key=True, index=True)
    event_type = Column(String, nullable=False)
    event_data = Column(JSON, default=dict)
    triggered_by = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    impact_level = Column(Integer, default=1)

class PlayerEvent(Base):
    __tablename__ = "player_events"
    
    id = Column(Integer, primary_key=True, index=True)
    player_id = Column(Integer, nullable=False)
    event_type = Column(String, nullable=False)
    event_data = Column(JSON, default=dict)
    created_at = Column(DateTime, default=datetime.utcnow)

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./system_void.db")

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False} if "sqlite" in DATABASE_URL else {},
    pool_size=10,
    max_overflow=20,
    pool_pre_ping=True,
    pool_recycle=3600
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    Base.metadata.create_all(bind=engine)
    _migrate_installed_packages()

def _migrate_installed_packages():
    try:
        import sqlite3
        db_path = DATABASE_URL.replace("sqlite:///", "")
        if os.path.exists(db_path):
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            
            new_columns = [
                ("installed_packages", "TEXT DEFAULT '[]'"),
                ("choices", "TEXT DEFAULT '{}'"),
                ("aria_trust", "INTEGER DEFAULT 50"),
                ("puzzle_attempts", "TEXT DEFAULT '{}'"),
                ("narrative_flags", "TEXT DEFAULT '[]'"),
                ("discovered_secrets", "TEXT DEFAULT '[]'"),
                ("aria_dialogue_progress", "INTEGER DEFAULT 0"),
                ("ending", "TEXT"),
                ("game_completed", "BOOLEAN DEFAULT 0"),
                ("aliases", "TEXT DEFAULT '{}'"),
            ]
            
            for col_name, col_def in new_columns:
                try:
                    cursor.execute(f"SELECT {col_name} FROM players LIMIT 1")
                except sqlite3.OperationalError:
                    cursor.execute(f"ALTER TABLE players ADD COLUMN {col_name} {col_def}")
                    conn.commit()
            
            conn.close()
    except Exception:
        pass

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
