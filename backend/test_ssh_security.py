import pytest
from sqlalchemy.orm import Session
from database import init_db, get_db, Player, SessionLocal
from auth.ssh_auth import ssh_connect
from auth.player_service import create_player, get_player_by_username
from auth.session import create_jwt_token, verify_jwt_token

@pytest.fixture
def db_session():
    init_db()
    db = SessionLocal()
    yield db
    db.rollback()
    db.close()

@pytest.fixture
def test_user(db_session):
    username = "testuser_ssh"
    password = "testpass123"
    try:
        existing = get_player_by_username(db_session, username)
        if existing:
            db_session.delete(existing)
            db_session.commit()
        player = create_player(db_session, username, password)
        db_session.commit()
        return {"username": username, "password": password, "player": player}
    except ValueError as e:
        if "already exists" in str(e):
            existing = get_player_by_username(db_session, username)
            return {"username": username, "password": password, "player": existing}
        raise

def test_ssh_connect_with_valid_password(db_session, test_user):
    result = ssh_connect(db_session, test_user["username"], test_user["password"], None)
    assert result["success"] is True
    assert result["username"] == test_user["username"]
    assert "token" in result
    assert "player_id" in result

def test_ssh_connect_with_invalid_password(db_session, test_user):
    result = ssh_connect(db_session, test_user["username"], "wrongpassword", None)
    assert result["success"] is False
    assert "Invalid credentials" in result["message"]

def test_ssh_connect_without_password_or_token(db_session, test_user):
    result = ssh_connect(db_session, test_user["username"], None, None)
    assert result["success"] is False
    assert "Password required" in result["message"]

def test_ssh_connect_with_valid_token(db_session, test_user):
    token = create_jwt_token(test_user["username"], test_user["player"].id)
    result = ssh_connect(db_session, test_user["username"], None, token)
    assert result["success"] is True
    assert result["username"] == test_user["username"]
    assert "token" in result
    assert result["token"] != token

def test_ssh_connect_with_invalid_token(db_session, test_user):
    result = ssh_connect(db_session, test_user["username"], None, "invalid_token")
    assert result["success"] is False
    assert "Password required" in result["message"]

def test_ssh_connect_with_token_wrong_username(db_session, test_user):
    token = create_jwt_token(test_user["username"], test_user["player"].id)
    result = ssh_connect(db_session, "wronguser", None, token)
    assert result["success"] is False
    assert "Password required" in result["message"]

def test_ssh_connect_security_no_password_bypass(db_session, test_user):
    result = ssh_connect(db_session, test_user["username"], None, None)
    assert result["success"] is False
    assert "Password required" in result["message"]

def test_ssh_connect_token_takes_precedence_over_password(db_session, test_user):
    token = create_jwt_token(test_user["username"], test_user["player"].id)
    result = ssh_connect(db_session, test_user["username"], "wrongpassword", token)
    assert result["success"] is True
    assert result["username"] == test_user["username"]

if __name__ == "__main__":
    pytest.main([__file__, "-v"])

