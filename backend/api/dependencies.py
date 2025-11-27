from typing import Optional, Generator
from fastapi import Header, HTTPException, Depends
from sqlalchemy.orm import Session
from database import get_db as _get_db
from auth.session import extract_token_from_header, verify_jwt_token
from auth.player_service import get_player_by_id

def get_database() -> Generator[Session, None, None]:
    db = next(_get_db())
    try:
        yield db
    finally:
        db.close()

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

