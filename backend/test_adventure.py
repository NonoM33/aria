import pytest
from fastapi.testclient import TestClient
from main import app, get_session, ENCRYPTION_KEY
from adventures.adventure_data import get_adventure_data

client = TestClient(app)

def get_test_session_id():
    return "test_session_123"

def test_welcome_message_fr():
    response = client.post("/api/command", json={
        "command": "",
        "session_id": get_test_session_id(),
        "language": "FR"
    })
    assert response.status_code == 200
    data = response.json()
    assert "initialisé" in data["response"].lower() or "system_void" in data["response"].lower()

def test_welcome_message_en():
    response = client.post("/api/command", json={
        "command": "",
        "session_id": "test_session_en",
        "language": "EN"
    })
    assert response.status_code == 200
    data = response.json()
    assert "initialized" in data["response"].lower() or "system_void" in data["response"].lower()

def test_help_command():
    response = client.post("/api/command", json={
        "command": "HELP",
        "session_id": get_test_session_id(),
        "language": "FR"
    })
    assert response.status_code == 200
    data = response.json()
    assert "HELP" in data["response"]
    assert "STATUS" in data["response"]
    assert "LOGIN" in data["response"]

def test_status_initial():
    response = client.post("/api/command", json={
        "command": "STATUS",
        "session_id": get_test_session_id(),
        "language": "FR"
    })
    assert response.status_code == 200
    data = response.json()
    assert "34%" in data["response"] or "34" in data["response"]
    assert "CRITIQUE" in data["response"] or "CRITICAL" in data["response"]

def test_login_without_key():
    response = client.post("/api/command", json={
        "command": "LOGIN",
        "session_id": get_test_session_id(),
        "language": "FR"
    })
    assert response.status_code == 200
    data = response.json()
    assert "clé" in data["response"].lower() or "key" in data["response"].lower()

def test_login_with_wrong_key():
    response = client.post("/api/command", json={
        "command": "LOGIN WRONGKEY",
        "session_id": get_test_session_id(),
        "language": "FR"
    })
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "error"
    assert "invalide" in data["response"].lower() or "invalid" in data["response"].lower()

def test_login_with_correct_key():
    response = client.post("/api/command", json={
        "command": f"LOGIN {ENCRYPTION_KEY}",
        "session_id": get_test_session_id(),
        "language": "FR"
    })
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    assert "niveau 1" in data["response"].lower() or "level 1" in data["response"].lower()
    assert "SCAN" in data["response"] or "scan" in data["response"].lower()

def test_scan_after_login():
    session_id = "test_scan_session"
    client.post("/api/command", json={
        "command": f"LOGIN {ENCRYPTION_KEY}",
        "session_id": session_id,
        "language": "FR"
    })
    
    response = client.post("/api/command", json={
        "command": "SCAN",
        "session_id": session_id,
        "language": "FR"
    })
    assert response.status_code == 200
    data = response.json()
    assert "corrupted_data.b64" in data["response"] or "fichiers" in data["response"].lower()

def test_access_file():
    session_id = "test_access_session"
    client.post("/api/command", json={
        "command": f"LOGIN {ENCRYPTION_KEY}",
        "session_id": session_id,
        "language": "FR"
    })
    
    response = client.post("/api/command", json={
        "command": "ACCESS protocol_xyz.txt",
        "session_id": session_id,
        "language": "FR"
    })
    assert response.status_code == 200
    data = response.json()
    assert "PROTOCOL" in data["response"] or "protocole" in data["response"].lower()

def test_decode_base64():
    session_id = "test_decode_session"
    client.post("/api/command", json={
        "command": f"LOGIN {ENCRYPTION_KEY}",
        "session_id": session_id,
        "language": "FR"
    })
    
    test_b64 = "SGVsbG8gV29ybGQ="
    response = client.post("/api/command", json={
        "command": f"DECODE {test_b64}",
        "session_id": session_id,
        "language": "FR"
    })
    assert response.status_code == 200
    data = response.json()
    assert "Hello World" in data["response"] or "décodé" in data["response"].lower()

def test_decode_corrupted_data():
    session_id = "test_decode_corrupted"
    client.post("/api/command", json={
        "command": f"LOGIN {ENCRYPTION_KEY}",
        "session_id": session_id,
        "language": "FR"
    })
    
    corrupted_b64 = "VGhlIG5leHQgc3RlcCBpcyB0byBkZWNvZGUgdGhlIGZpbGUgY29kZWQgaW4gYmFzZTY0LgpUaGUgYW5zd2VyIGlzOiBQUk9UT0NPTF9YWVo="
    response = client.post("/api/command", json={
        "command": f"DECODE {corrupted_b64}",
        "session_id": session_id,
        "language": "FR"
    })
    assert response.status_code == 200
    data = response.json()
    assert "PROTOCOL_XYZ" in data["response"]

def test_activate_protocol():
    session_id = "test_activate_session"
    client.post("/api/command", json={
        "command": f"LOGIN {ENCRYPTION_KEY}",
        "session_id": session_id,
        "language": "FR"
    })
    
    response = client.post("/api/command", json={
        "command": "ACTIVATE PROTOCOL_XYZ",
        "session_id": session_id,
        "language": "FR"
    })
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    assert "niveau 2" in data["response"].lower() or "level 2" in data["response"].lower()
    assert "NETWORK" in data["response"] or "network" in data["response"].lower()

def test_network_command():
    session_id = "test_network_session"
    client.post("/api/command", json={
        "command": f"LOGIN {ENCRYPTION_KEY}",
        "session_id": session_id,
        "language": "FR"
    })
    client.post("/api/command", json={
        "command": "ACTIVATE PROTOCOL_XYZ",
        "session_id": session_id,
        "language": "FR"
    })
    
    response = client.post("/api/command", json={
        "command": "NETWORK",
        "session_id": session_id,
        "language": "FR"
    })
    assert response.status_code == 200
    data = response.json()
    assert "SERVER_GAMMA" in data["response"] or "server" in data["response"].lower()

def test_analyze_security():
    session_id = "test_analyze_session"
    client.post("/api/command", json={
        "command": f"LOGIN {ENCRYPTION_KEY}",
        "session_id": session_id,
        "language": "FR"
    })
    client.post("/api/command", json={
        "command": "ACTIVATE PROTOCOL_XYZ",
        "session_id": session_id,
        "language": "FR"
    })
    
    response = client.post("/api/command", json={
        "command": "ANALYZE security",
        "session_id": session_id,
        "language": "FR"
    })
    assert response.status_code == 200
    data = response.json()
    assert "BYPASS" in data["response"] or "bypass" in data["response"].lower()

def test_bypass_magic_square():
    session_id = "test_bypass_session"
    client.post("/api/command", json={
        "command": f"LOGIN {ENCRYPTION_KEY}",
        "session_id": session_id,
        "language": "FR"
    })
    client.post("/api/command", json={
        "command": "ACTIVATE PROTOCOL_XYZ",
        "session_id": session_id,
        "language": "FR"
    })
    
    response = client.post("/api/command", json={
        "command": "BYPASS 5",
        "session_id": session_id,
        "language": "FR"
    })
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    assert "correct" in data["response"].lower() or "niveau 3" in data["response"].lower()

def test_connect_server_gamma():
    session_id = "test_connect_session"
    client.post("/api/command", json={
        "command": f"LOGIN {ENCRYPTION_KEY}",
        "session_id": session_id,
        "language": "FR"
    })
    client.post("/api/command", json={
        "command": "ACTIVATE PROTOCOL_XYZ",
        "session_id": session_id,
        "language": "FR"
    })
    client.post("/api/command", json={
        "command": "BYPASS 5",
        "session_id": session_id,
        "language": "FR"
    })
    
    response = client.post("/api/command", json={
        "command": "CONNECT SERVER_GAMMA DIOV",
        "session_id": session_id,
        "language": "FR"
    })
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    assert "GAMMA" in data["response"] or "connecté" in data["response"].lower()

def test_restore_code():
    session_id = "test_restore_session"
    client.post("/api/command", json={
        "command": f"LOGIN {ENCRYPTION_KEY}",
        "session_id": session_id,
        "language": "FR"
    })
    client.post("/api/command", json={
        "command": "ACTIVATE PROTOCOL_XYZ",
        "session_id": session_id,
        "language": "FR"
    })
    client.post("/api/command", json={
        "command": "BYPASS 5",
        "session_id": session_id,
        "language": "FR"
    })
    client.post("/api/command", json={
        "command": "CONNECT SERVER_GAMMA DIOV",
        "session_id": session_id,
        "language": "FR"
    })
    
    response = client.post("/api/command", json={
        "command": "RESTORE 55",
        "session_id": session_id,
        "language": "FR"
    })
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    assert "100%" in data["response"] or "restor" in data["response"].lower()

def test_solve_final_riddle():
    session_id = "test_solve_session"
    client.post("/api/command", json={
        "command": f"LOGIN {ENCRYPTION_KEY}",
        "session_id": session_id,
        "language": "FR"
    })
    client.post("/api/command", json={
        "command": "ACTIVATE PROTOCOL_XYZ",
        "session_id": session_id,
        "language": "FR"
    })
    client.post("/api/command", json={
        "command": "BYPASS 5",
        "session_id": session_id,
        "language": "FR"
    })
    client.post("/api/command", json={
        "command": "CONNECT SERVER_GAMMA DIOV",
        "session_id": session_id,
        "language": "FR"
    })
    client.post("/api/command", json={
        "command": "RESTORE 55",
        "session_id": session_id,
        "language": "FR"
    })
    
    response = client.post("/api/command", json={
        "command": "SOLVE E",
        "session_id": session_id,
        "language": "FR"
    })
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    assert "complété" in data["response"].lower() or "completed" in data["response"].lower()

def test_language_persistence():
    session_id = "test_lang_session"
    response1 = client.post("/api/command", json={
        "command": "HELP",
        "session_id": session_id,
        "language": "FR"
    })
    assert "Tapez" in response1.json()["response"] or "tapez" in response1.json()["response"].lower()
    
    response2 = client.post("/api/command", json={
        "command": "HELP",
        "session_id": session_id,
        "language": "EN"
    })
    assert "Type" in response2.json()["response"] or "type" in response2.json()["response"].lower()

def test_session_progression():
    session_id = "test_progression_session"
    
    response1 = client.post("/api/command", json={
        "command": "STATUS",
        "session_id": session_id,
        "language": "FR"
    })
    assert "34" in response1.json()["response"]
    
    client.post("/api/command", json={
        "command": f"LOGIN {ENCRYPTION_KEY}",
        "session_id": session_id,
        "language": "FR"
    })
    
    response2 = client.post("/api/command", json={
        "command": "STATUS",
        "session_id": session_id,
        "language": "FR"
    })
    assert "49" in response2.json()["response"] or "niveau 1" in response2.json()["response"].lower()

def test_unknown_command():
    response = client.post("/api/command", json={
        "command": "UNKNOWN_COMMAND",
        "session_id": get_test_session_id(),
        "language": "FR"
    })
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "error"
    assert "inconnue" in data["response"].lower() or "unknown" in data["response"].lower()

def test_chapter_files_availability():
    session_id = "test_files_session"
    client.post("/api/command", json={
        "command": f"LOGIN {ENCRYPTION_KEY}",
        "session_id": session_id,
        "language": "FR"
    })
    
    response = client.post("/api/command", json={
        "command": "SCAN",
        "session_id": session_id,
        "language": "FR"
    })
    data = response.json()
    files_mentioned = ["corrupted_data.b64", "protocol_xyz.txt", "hint_sequence.txt"]
    assert any(f in data["response"] for f in files_mentioned)

def test_adventure_data_structure():
    for lang in ["FR", "EN"]:
        adventure_data = get_adventure_data(lang)
        data = adventure_data.get(lang, {})
        assert "chapters" in data
        assert "system_messages" in data
        assert "chapter_1" in data["chapters"]
        assert "chapter_2" in data["chapters"]
        assert "chapter_3" in data["chapters"]
        assert "chapter_4" in data["chapters"]
        assert "chapter_5" in data["chapters"]

def test_all_puzzles_have_solutions():
    for lang in ["FR", "EN"]:
        adventure_data = get_adventure_data(lang)
        data = adventure_data.get(lang, {})
        chapters = data["chapters"]
        for chapter_id, chapter_data in chapters.items():
            if "puzzles" in chapter_data:
                for puzzle_id, puzzle_data in chapter_data["puzzles"].items():
                    assert "solution" in puzzle_data, f"Puzzle {puzzle_id} in {chapter_id} missing solution"
                    assert puzzle_data["solution"], f"Puzzle {puzzle_id} in {chapter_id} has empty solution"

def test_all_files_have_content():
    for lang in ["FR", "EN"]:
        adventure_data = get_adventure_data(lang)
        data = adventure_data.get(lang, {})
        chapters = data["chapters"]
        for chapter_id, chapter_data in chapters.items():
            if "files" in chapter_data:
                for filename, content in chapter_data["files"].items():
                    assert content, f"File {filename} in {chapter_id} is empty"
                    assert isinstance(content, str), f"File {filename} in {chapter_id} is not a string"

def test_get_available_files_endpoint():
    session_id = get_test_session_id()
    
    client.post("/api/command", json={
        "command": f"LOGIN {ENCRYPTION_KEY}",
        "session_id": session_id,
        "language": "FR"
    })
    
    response = client.get("/api/files", params={
        "session_id": session_id,
        "language": "FR"
    })
    
    assert response.status_code == 200
    data = response.json()
    assert "files" in data
    assert isinstance(data["files"], list)
    assert len(data["files"]) > 0
    assert "corrupted_data.b64" in data["files"]
    assert "protocol_xyz.txt" in data["files"]

def test_file_autocomplete_after_scan():
    session_id = get_test_session_id()
    
    client.post("/api/command", json={
        "command": f"LOGIN {ENCRYPTION_KEY}",
        "session_id": session_id,
        "language": "FR"
    })
    
    client.post("/api/command", json={
        "command": "SCAN",
        "session_id": session_id,
        "language": "FR"
    })
    
    response = client.get("/api/files", params={
        "session_id": session_id,
        "language": "FR"
    })
    
    assert response.status_code == 200
    data = response.json()
    files = data["files"]
    
    assert len(files) >= 3
    assert all(isinstance(f, str) for f in files)

def test_file_autocomplete_different_chapters():
    session_id = get_test_session_id()
    
    client.post("/api/command", json={
        "command": f"LOGIN {ENCRYPTION_KEY}",
        "session_id": session_id,
        "language": "FR"
    })
    
    chapter_2_files = client.get("/api/files", params={
        "session_id": session_id,
        "language": "FR"
    }).json()["files"]
    
    assert "corrupted_data.b64" in chapter_2_files
    
    client.post("/api/command", json={
        "command": "ACTIVATE PROTOCOL_XYZ",
        "session_id": session_id,
        "language": "FR"
    })
    
    chapter_3_files = client.get("/api/files", params={
        "session_id": session_id,
        "language": "FR"
    }).json()["files"]
    
    assert "matrix.txt" in chapter_3_files or len(chapter_3_files) > 0

def test_file_autocomplete_language_support():
    session_id = get_test_session_id()
    
    client.post("/api/command", json={
        "command": f"LOGIN {ENCRYPTION_KEY}",
        "session_id": session_id,
        "language": "EN"
    })
    
    response = client.get("/api/files", params={
        "session_id": session_id,
        "language": "EN"
    })
    
    assert response.status_code == 200
    data = response.json()
    assert "files" in data
    assert len(data["files"]) > 0

if __name__ == "__main__":
    pytest.main([__file__, "-v"])

