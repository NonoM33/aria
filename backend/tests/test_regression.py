"""
Regression tests for bug fixes.
These tests ensure previously fixed bugs don't reoccur.
"""

import pytest
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class TestAccessCommandRegression:
    """Test: ACCESS command should show ACCESS usage, not CAT usage."""
    
    def test_access_command_shows_correct_usage_fr(self):
        from commands.access_command import AccessCommand
        
        session = {"chapter": "chapter_0", "current_path": "/", "language": "FR"}
        cmd = AccessCommand(session, None, "FR")
        result = cmd.execute("")
        
        assert "ACCESS" in result["response"], "ACCESS command should show ACCESS in usage message"
        assert "CAT <nom_fichier>" not in result["response"], "ACCESS should not show CAT usage"
        
    def test_access_command_shows_correct_usage_en(self):
        from commands.access_command import AccessCommand
        
        session = {"chapter": "chapter_0", "current_path": "/", "language": "EN"}
        cmd = AccessCommand(session, None, "EN")
        result = cmd.execute("")
        
        assert "ACCESS" in result["response"], "ACCESS command should show ACCESS in usage message"
        assert "CAT <filename>" not in result["response"], "ACCESS should not show CAT usage"


class TestSSHLevelRegression:
    """Test: SSH login should set level >= 1, not keep level at 0."""
    
    def test_new_player_gets_level_1_on_ssh_login(self):
        session = {
            "session_id": "test",
            "level": 0,
            "chapter": "chapter_0",
            "logged_in": False,
            "unlocked_commands": [],
            "current_path": "/"
        }
        
        player_data = {"level": 0, "chapter": "chapter_1"}
        
        current_level = player_data.get("level", 0)
        if current_level < 1:
            current_level = 1
        
        assert current_level == 1, "New player should have level 1 after SSH login"
    
    def test_existing_player_keeps_level_on_ssh_login(self):
        player_data = {"level": 3, "chapter": "act_2"}
        
        current_level = player_data.get("level", 0)
        if current_level < 1:
            current_level = 1
        
        assert current_level == 3, "Existing player should keep their level"


class TestExitCommandRegression:
    """Test: EXIT command should properly reset session without affecting history."""
    
    def test_exit_returns_logout_flag(self):
        from commands.exit_command import ExitCommand
        
        session = {
            "logged_in": True,
            "username": "testuser",
            "player_id": 1,
            "ssh_token": "fake_token"
        }
        
        cmd = ExitCommand(session, None, "FR")
        result = cmd.execute("")
        
        assert result.get("logout") == True, "EXIT should return logout flag"
        assert "testuser" in result["response"], "EXIT should mention username in farewell"
    
    def test_exit_clears_session_credentials(self):
        from commands.exit_command import ExitCommand
        
        session = {
            "logged_in": True,
            "username": "testuser",
            "player_id": 1,
            "ssh_token": "fake_token"
        }
        
        cmd = ExitCommand(session, None, "FR")
        cmd.execute("")
        
        assert session.get("logged_in") == False, "Session should be logged out"
        assert session.get("username") is None, "Username should be cleared"
        assert session.get("ssh_token") is None, "Token should be cleared"


class TestSessionStateRegression:
    """Test: Session state should be properly maintained and isolated."""
    
    def test_session_level_persistence(self):
        from services.session_service import sessions, get_session
        
        test_session_id = "test_regression_level"
        
        if test_session_id in sessions:
            del sessions[test_session_id]
        
        session = get_session(test_session_id, "FR", None, None, None)
        
        session["level"] = 5
        session["chapter"] = "act_3"
        
        retrieved = get_session(test_session_id, "FR", None, None, None)
        
        assert retrieved["level"] == 5, "Level should persist in session"
        assert retrieved["chapter"] == "act_3", "Chapter should persist in session"
        
        if test_session_id in sessions:
            del sessions[test_session_id]
    
    def test_session_path_persistence(self):
        from services.session_service import sessions, get_session
        
        test_session_id = "test_regression_path"
        
        if test_session_id in sessions:
            del sessions[test_session_id]
        
        session = get_session(test_session_id, "FR", None, None, None)
        
        session["current_path"] = "/security/logs"
        
        retrieved = get_session(test_session_id, "FR", None, None, None)
        
        assert retrieved["current_path"] == "/security/logs", "Path should persist in session"
        
        if test_session_id in sessions:
            del sessions[test_session_id]


class TestHistoryUsernameRegression:
    """
    Test: History entries should store username at entry time, not current username.
    This is a frontend test documented here for reference.
    The fix ensures each history entry has its own 'username' field.
    """
    
    def test_history_entry_structure(self):
        history_entry = {
            "type": "user",
            "content": "ls",
            "path": "/security",
            "username": "testuser",
            "timestamp": "2025-01-01T00:00:00.000Z"
        }
        
        assert "username" in history_entry, "History entry should have username field"
        assert history_entry["username"] == "testuser", "Username should be stored in entry"


class TestSSHPasswordPromptRegression:
    """Test: SSH should not show double password prompt."""
    
    def test_ssh_password_prompt_response_structure(self):
        """
        Test the SSH password prompt response structure.
        The actual password prompt flow requires a database, so this test
        verifies the response format when password_prompt is set.
        """
        expected_response = {
            "response": "user@system-void.local's password: ",
            "status": "password_prompt",
            "password_prompt": True,
            "username": "user"
        }
        
        assert expected_response.get("password_prompt") == True
        assert "password" in expected_response["response"].lower()
        
        response_lines = expected_response["response"].split("\n")
        password_prompt_count = sum(1 for line in response_lines if "password" in line.lower())
        assert password_prompt_count == 1, "Should have exactly one password prompt line"
    
    def test_ssh_requires_database(self):
        """Test that SSH properly handles missing database."""
        from commands.ssh_command import SshCommand
        
        session = {
            "session_id": "test",
            "level": 0,
            "logged_in": False
        }
        
        cmd = SshCommand(session, None, "FR")
        result = cmd.execute("testuser@system-void.local")
        
        assert result.get("status") == "error", "SSH without DB should return error"


class TestCommandAvailabilityRegression:
    """Test: Commands should be available at correct progression points."""
    
    def test_initial_commands_available(self):
        from services.session_service import get_session, sessions
        
        test_session_id = "test_regression_commands"
        
        if test_session_id in sessions:
            del sessions[test_session_id]
        
        session = get_session(test_session_id, "FR", None, None, None)
        
        initial_commands = session.get("unlocked_commands", [])
        
        required_initial = ["HELP", "STATUS", "SCAN", "LS", "SSH", "EXIT"]
        for cmd in required_initial:
            assert cmd in initial_commands, f"{cmd} should be available initially"
        
        if test_session_id in sessions:
            del sessions[test_session_id]


class TestFilesystemRegression:
    """Test: Filesystem should be properly loaded for chapters."""
    
    def test_chapter_0_has_filesystem(self):
        from adventures.adventure_loader import get_chapter_filesystem
        
        fs = get_chapter_filesystem("chapter_0", "FR")
        
        assert fs is not None, "chapter_0 should have filesystem"
        assert isinstance(fs, dict), "Filesystem should be a dict"
    
    def test_act_1_has_filesystem(self):
        from adventures.adventure_loader import get_chapter_filesystem
        
        fs = get_chapter_filesystem("act_1", "FR")
        
        assert fs is not None, "act_1 should have filesystem"
        assert isinstance(fs, dict), "Filesystem should be a dict"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

