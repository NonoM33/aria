from typing import Optional
from fastapi import Header, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from auth.session import extract_token_from_header, verify_jwt_token
from auth.player_service import get_player_by_id

def get_database() -> Session:
    try:
        db = next(get_db())
        return db
    except:
        return None

def get_current_user(authorization: Optional[str] = Header(None)) -> Optional[dict]:
    if not authorization:
        return None
    
    token = extract_token_from_header(authorization)
    if not token:
        return None
    
    payload = verify_jwt_token(token)
    if not payload:
        return None
    
    return payload

