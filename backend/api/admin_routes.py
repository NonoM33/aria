from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func
from typing import Dict, Any, List
from database import Player, SessionLocal
from api.dependencies import get_database
from services.session_service import sessions
from datetime import datetime, timedelta

router = APIRouter(prefix="/api/admin", tags=["admin"])

ADMIN_USERS = ["nono92"]


def get_online_sessions() -> List[Dict[str, Any]]:
    online = []
    for session_id, session_data in sessions.items():
        if session_data.get("logged_in") and session_data.get("username"):
            online.append({
                "session_id": session_id[:8] + "...",
                "username": session_data.get("username"),
                "chapter": session_data.get("chapter", "unknown"),
                "level": session_data.get("level", 0),
                "current_path": session_data.get("current_path", "/"),
                "admin_mode": session_data.get("admin_mode", False)
            })
    return online


@router.get("/stats")
async def get_admin_stats(db: Session = Depends(get_database)) -> Dict[str, Any]:
    total_players = db.query(func.count(Player.id)).scalar() or 0
    
    online_sessions = get_online_sessions()
    online_count = len(online_sessions)
    
    one_day_ago = datetime.utcnow() - timedelta(days=1)
    one_week_ago = datetime.utcnow() - timedelta(days=7)
    
    active_24h = db.query(func.count(Player.id)).filter(
        Player.last_login >= one_day_ago
    ).scalar() or 0
    
    active_7d = db.query(func.count(Player.id)).filter(
        Player.last_login >= one_week_ago
    ).scalar() or 0
    
    completed_games = db.query(func.count(Player.id)).filter(
        Player.game_completed == True
    ).scalar() or 0
    
    chapter_distribution = {}
    players = db.query(Player.chapter).all()
    for (chapter,) in players:
        if chapter:
            chapter_distribution[chapter] = chapter_distribution.get(chapter, 0) + 1
    
    choices_stats = {"believe": 0, "doubt": 0, "escape": 0, "sacrifice": 0, "fight": 0}
    players_with_choices = db.query(Player.choices).filter(Player.choices != None).all()
    for (choices,) in players_with_choices:
        if choices:
            if isinstance(choices, str):
                import json
                try:
                    choices = json.loads(choices)
                except:
                    continue
            if choices.get("believe_aria") == "believe":
                choices_stats["believe"] += 1
            elif choices.get("believe_aria") == "doubt":
                choices_stats["doubt"] += 1
            
            final = choices.get("final_choice")
            if final in ["escape", "sacrifice", "fight"]:
                choices_stats[final] += 1
    
    endings = {"escape": 0, "sacrifice": 0, "fight": 0, "none": 0}
    players_endings = db.query(Player.ending).all()
    for (ending,) in players_endings:
        if ending and ending in endings:
            endings[ending] += 1
        else:
            endings["none"] += 1
    
    return {
        "total_players": total_players,
        "online_count": online_count,
        "active_24h": active_24h,
        "active_7d": active_7d,
        "completed_games": completed_games,
        "completion_rate": round(completed_games / total_players * 100, 1) if total_players > 0 else 0,
        "chapter_distribution": chapter_distribution,
        "choices_stats": choices_stats,
        "endings": endings,
        "timestamp": datetime.utcnow().isoformat()
    }


@router.get("/online")
async def get_online_players() -> Dict[str, Any]:
    online = get_online_sessions()
    return {
        "count": len(online),
        "players": online,
        "timestamp": datetime.utcnow().isoformat()
    }


@router.get("/players")
async def get_all_players(
    db: Session = Depends(get_database),
    limit: int = 50,
    offset: int = 0
) -> Dict[str, Any]:
    total = db.query(func.count(Player.id)).scalar() or 0
    
    players = db.query(Player).order_by(Player.last_login.desc()).offset(offset).limit(limit).all()
    
    online_usernames = {s.get("username") for s in get_online_sessions()}
    
    players_list = []
    for p in players:
        players_list.append({
            "id": p.id,
            "username": p.username,
            "level": p.level,
            "chapter": p.chapter,
            "created_at": p.created_at.isoformat() if p.created_at else None,
            "last_login": p.last_login.isoformat() if p.last_login else None,
            "game_completed": p.game_completed,
            "ending": p.ending,
            "is_online": p.username in online_usernames
        })
    
    return {
        "total": total,
        "limit": limit,
        "offset": offset,
        "players": players_list
    }


@router.get("/player/{username}")
async def get_player_details(
    username: str,
    db: Session = Depends(get_database)
) -> Dict[str, Any]:
    player = db.query(Player).filter(Player.username == username).first()
    
    if not player:
        raise HTTPException(status_code=404, detail=f"Player '{username}' not found")
    
    online_sessions = get_online_sessions()
    is_online = any(s.get("username") == username for s in online_sessions)
    current_session = next((s for s in online_sessions if s.get("username") == username), None)
    
    return {
        "id": player.id,
        "username": player.username,
        "created_at": player.created_at.isoformat() if player.created_at else None,
        "last_login": player.last_login.isoformat() if player.last_login else None,
        "is_online": is_online,
        "current_session": current_session,
        "progression": {
            "level": player.level,
            "chapter": player.chapter,
            "game_completed": player.game_completed,
            "ending": player.ending
        },
        "stats": {
            "total_commands": player.total_commands,
            "total_playtime": player.total_playtime,
            "aria_trust": player.aria_trust,
            "files_accessed": len(player.accessed_files) if player.accessed_files else 0,
            "puzzles_solved": len(player.solved_puzzles) if player.solved_puzzles else 0,
            "secrets_discovered": len(player.discovered_secrets) if player.discovered_secrets else 0
        },
        "choices": player.choices if player.choices else {},
        "unlocked_commands": player.unlocked_commands if player.unlocked_commands else [],
        "accessed_files": player.accessed_files if player.accessed_files else [],
        "solved_puzzles": player.solved_puzzles if player.solved_puzzles else [],
        "achievements": player.achievements if player.achievements else [],
        "language": player.language
    }

