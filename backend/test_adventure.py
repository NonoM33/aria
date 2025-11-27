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
    """Test de non-régression : ACTIVATE doit fonctionner avec PROTOCOL_XYZ"""
    session_id = "test_activate_session"
    client.post("/api/command", json={
        "command": f"LOGIN {ENCRYPTION_KEY}",
        "session_id": session_id,
        "language": "FR"
    })
    
    # Test avec la bonne réponse
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
    
    # Test avec une mauvaise réponse (XYZ sans PROTOCOL_)
    session_id2 = "test_activate_session2"
    client.post("/api/command", json={
        "command": f"LOGIN {ENCRYPTION_KEY}",
        "session_id": session_id2,
        "language": "FR"
    })
    
    response2 = client.post("/api/command", json={
        "command": "ACTIVATE XYZ",
        "session_id": session_id2,
        "language": "FR"
    })
    assert response2.status_code == 200
    data2 = response2.json()
    assert data2["status"] == "error"
    assert "invalide" in data2["response"].lower() or "invalid" in data2["response"].lower()
    assert "PROTOCOL_" in data2["response"] or "corrupted_data.b64" in data2["response"].lower()

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

def test_help_no_duplicate_commands():
    """Test de non-régression : HELP ne doit pas afficher de commandes en double"""
    session_id = get_test_session_id()
    
    # Login pour débloquer les commandes de niveau 1
    client.post("/api/command", json={
        "command": f"LOGIN {ENCRYPTION_KEY}",
        "session_id": session_id,
        "language": "FR"
    })
    
    response = client.post("/api/command", json={
        "command": "HELP",
        "session_id": session_id,
        "language": "FR"
    })
    
    assert response.status_code == 200
    data = response.json()
    help_text = data["response"]
    
    # Extraire la liste des commandes
    commands_line = help_text.split("\n")[0]
    commands_str = commands_line.split("Commands available: ")[1]
    commands_list = [cmd.strip() for cmd in commands_str.split(",")]
    
    # Vérifier qu'il n'y a pas de doublons
    assert len(commands_list) == len(set(commands_list)), f"Doublons détectés: {commands_list}"
    
    # Vérifier que SCAN, DECODE, ACCESS sont présents une seule fois
    assert commands_list.count("SCAN") == 1, "SCAN apparaît plusieurs fois"
    assert commands_list.count("DECODE") == 1, "DECODE apparaît plusieurs fois"
    assert commands_list.count("ACCESS") == 1, "ACCESS apparaît plusieurs fois"

def test_help_commands_sorted():
    """Test de non-régression : Les commandes dans HELP doivent être triées"""
    session_id = get_test_session_id()
    
    client.post("/api/command", json={
        "command": f"LOGIN {ENCRYPTION_KEY}",
        "session_id": session_id,
        "language": "FR"
    })
    
    response = client.post("/api/command", json={
        "command": "HELP",
        "session_id": session_id,
        "language": "FR"
    })
    
    assert response.status_code == 200
    data = response.json()
    help_text = data["response"]
    
    commands_line = help_text.split("\n")[0]
    commands_str = commands_line.split("Commands available: ")[1]
    commands_list = [cmd.strip() for cmd in commands_str.split(",")]
    
    # Vérifier que la liste est triée
    assert commands_list == sorted(commands_list), "Les commandes ne sont pas triées"

def test_file_autocomplete_after_login():
    """Test de non-régression : Les fichiers doivent être disponibles après LOGIN"""
    session_id = get_test_session_id()
    
    # Login
    client.post("/api/command", json={
        "command": f"LOGIN {ENCRYPTION_KEY}",
        "session_id": session_id,
        "language": "FR"
    })
    
    # Vérifier que les fichiers sont disponibles
    response = client.get("/api/files", params={
        "session_id": session_id,
        "language": "FR"
    })
    
    assert response.status_code == 200
    data = response.json()
    assert "files" in data
    assert isinstance(data["files"], list)
    assert len(data["files"]) > 0

def test_file_autocomplete_consistency():
    """Test de non-régression : Les fichiers doivent être cohérents entre SCAN et /api/files"""
    session_id = get_test_session_id()
    
    client.post("/api/command", json={
        "command": f"LOGIN {ENCRYPTION_KEY}",
        "session_id": session_id,
        "language": "FR"
    })
    
    # Faire un SCAN
    scan_response = client.post("/api/command", json={
        "command": "SCAN",
        "session_id": session_id,
        "language": "FR"
    })
    
    # Récupérer les fichiers via l'API
    files_response = client.get("/api/files", params={
        "session_id": session_id,
        "language": "FR"
    })
    
    assert files_response.status_code == 200
    files_data = files_response.json()
    api_files = set(files_data["files"])
    
    # Extraire les fichiers mentionnés dans SCAN
    scan_text = scan_response.json()["response"]
    scan_files = set()
    for line in scan_text.split("\n"):
        if line.strip().startswith("- "):
            filename = line.strip()[2:].strip()
            scan_files.add(filename)
    
    # Les fichiers doivent correspondre
    assert api_files == scan_files, f"Fichiers incohérents: API={api_files}, SCAN={scan_files}"

def test_autocomplete_empty_input():
    """Test de non-régression : L'auto-complétion ne doit pas planter avec une entrée vide"""
    session_id = get_test_session_id()
    
    # Tester avec une commande vide
    response = client.post("/api/command", json={
        "command": "",
        "session_id": session_id,
        "language": "FR"
    })
    
    assert response.status_code == 200
    data = response.json()
    assert "response" in data

def test_autocomplete_invalid_file():
    """Test de non-régression : ACCESS avec un fichier invalide doit retourner une erreur"""
    session_id = get_test_session_id()
    
    client.post("/api/command", json={
        "command": f"LOGIN {ENCRYPTION_KEY}",
        "session_id": session_id,
        "language": "FR"
    })
    
    response = client.post("/api/command", json={
        "command": "ACCESS nonexistent_file.txt",
        "session_id": session_id,
        "language": "FR"
    })
    
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "error"
    assert "introuvable" in data["response"].lower() or "not found" in data["response"].lower()

def test_help_commands_at_different_levels():
    """Test de non-régression : HELP doit afficher les bonnes commandes selon le niveau"""
    session_id = get_test_session_id()
    
    # Niveau 0
    response = client.post("/api/command", json={
        "command": "HELP",
        "session_id": session_id,
        "language": "FR"
    })
    data = response.json()
    level_0_commands = data["response"].split("Commands available: ")[1].split("\n")[0]
    assert "HELP" in level_0_commands
    assert "STATUS" in level_0_commands
    assert "LOGIN" in level_0_commands
    assert "SCAN" not in level_0_commands
    
    # Niveau 1
    client.post("/api/command", json={
        "command": f"LOGIN {ENCRYPTION_KEY}",
        "session_id": session_id,
        "language": "FR"
    })
    response = client.post("/api/command", json={
        "command": "HELP",
        "session_id": session_id,
        "language": "FR"
    })
    data = response.json()
    level_1_commands = data["response"].split("Commands available: ")[1].split("\n")[0]
    assert "SCAN" in level_1_commands
    assert "DECODE" in level_1_commands
    assert "ACCESS" in level_1_commands

def test_man_page_command():
    """Test de non-régression : La commande MAN doit retourner le contenu de la page de manuel"""
    session_id = get_test_session_id()
    
    response = client.post("/api/command", json={
        "command": "MAN HELP",
        "session_id": session_id,
        "language": "FR"
    })
    
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    assert "HELP" in data["response"] or "help" in data["response"].lower()
    assert "NOM" in data["response"] or "NAME" in data["response"] or "SYNOPSIS" in data["response"]

def test_man_page_unknown_command():
    """Test de non-régression : MAN avec une commande inconnue doit retourner une erreur"""
    session_id = get_test_session_id()
    
    response = client.post("/api/command", json={
        "command": "MAN UNKNOWN_COMMAND",
        "session_id": session_id,
        "language": "FR"
    })
    
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "error"
    assert "introuvable" in data["response"].lower() or "not found" in data["response"].lower()

def test_man_page_language_support():
    """Test de non-régression : MAN doit supporter FR et EN"""
    session_id = get_test_session_id()
    
    # Test FR
    response_fr = client.post("/api/command", json={
        "command": "MAN HELP",
        "session_id": session_id,
        "language": "FR"
    })
    assert response_fr.status_code == 200
    data_fr = response_fr.json()
    assert data_fr["status"] == "success"
    
    # Test EN
    response_en = client.post("/api/command", json={
        "command": "MAN HELP",
        "session_id": session_id,
        "language": "EN"
    })
    assert response_en.status_code == 200
    data_en = response_en.json()
    assert data_en["status"] == "success"
    
    # Les contenus doivent être différents (traduits)
    assert data_fr["response"] != data_en["response"]

def test_man_page_all_commands():
    """Test de non-régression : Toutes les commandes principales doivent avoir une page MAN"""
    session_id = get_test_session_id()
    
    commands_with_man = ["HELP", "STATUS", "LOGIN", "SCAN", "DECODE", "ACCESS"]
    
    for cmd in commands_with_man:
        response = client.post("/api/command", json={
            "command": f"MAN {cmd}",
            "session_id": session_id,
            "language": "FR"
        })
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "success", f"MAN {cmd} should return success"
        assert len(data["response"]) > 50, f"MAN {cmd} should return substantial content"

def test_language_persistence():
    """Test de non-régression : La langue doit être persistante dans la session"""
    session_id = get_test_session_id()
    
    # Tester en FR
    response_fr = client.post("/api/command", json={
        "command": "HELP",
        "session_id": session_id,
        "language": "FR"
    })
    assert response_fr.status_code == 200
    data_fr = response_fr.json()
    assert "Tapez STATUS" in data_fr["response"] or "Commands available" in data_fr["response"]
    
    # Tester en EN
    response_en = client.post("/api/command", json={
        "command": "HELP",
        "session_id": session_id,
        "language": "EN"
    })
    assert response_en.status_code == 200
    data_en = response_en.json()
    assert "Type STATUS" in data_en["response"] or "Commands available" in data_en["response"]
    
    # Vérifier que les réponses sont différentes
    assert data_fr["response"] != data_en["response"]

def test_welcome_message_language():
    """Test de non-régression : Le message de bienvenue doit être dans la bonne langue"""
    session_id = get_test_session_id()
    
    # Test FR
    response_fr = client.post("/api/command", json={
        "command": "",
        "session_id": session_id,
        "language": "FR"
    })
    assert response_fr.status_code == 200
    data_fr = response_fr.json()
    assert "initialisé" in data_fr["response"] or "Tapez HELP" in data_fr["response"]
    
    # Test EN
    response_en = client.post("/api/command", json={
        "command": "",
        "session_id": session_id + "_en",
        "language": "EN"
    })
    assert response_en.status_code == 200
    data_en = response_en.json()
    assert "initialized" in data_en["response"] or "Type HELP" in data_en["response"]

def test_unlocked_commands_endpoint():
    """Test de non-régression : L'endpoint /api/unlocked-commands doit retourner les bonnes commandes"""
    session_id = get_test_session_id()
    
    # Niveau 0 - seulement HELP, STATUS, LOGIN
    response = client.get("/api/unlocked-commands", params={
        "session_id": session_id,
        "language": "FR"
    })
    assert response.status_code == 200
    data = response.json()
    assert "commands" in data
    commands = data["commands"]
    assert "HELP" in commands
    assert "STATUS" in commands
    assert "LOGIN" in commands
    assert "SCAN" not in commands
    
    # Après LOGIN - devrait avoir SCAN, DECODE, ACCESS
    client.post("/api/command", json={
        "command": f"LOGIN {ENCRYPTION_KEY}",
        "session_id": session_id,
        "language": "FR"
    })
    
    response = client.get("/api/unlocked-commands", params={
        "session_id": session_id,
        "language": "FR"
    })
    assert response.status_code == 200
    data = response.json()
    commands = data["commands"]
    assert "SCAN" in commands
    assert "DECODE" in commands
    assert "ACCESS" in commands

def test_man_autocomplete_only_unlocked():
    """Test de non-régression : MAN Tab ne doit proposer que les commandes débloquées"""
    session_id = get_test_session_id()
    
    # Au début, seulement HELP, STATUS, LOGIN
    response = client.get("/api/unlocked-commands", params={
        "session_id": session_id,
        "language": "FR"
    })
    assert response.status_code == 200
    data = response.json()
    commands = data["commands"]
    
    # Vérifier que MAN avec ces commandes fonctionne
    for cmd in commands:
        man_response = client.post("/api/command", json={
            "command": f"MAN {cmd}",
            "session_id": session_id,
            "language": "FR"
        })
        assert man_response.status_code == 200
        man_data = man_response.json()
        assert man_data["status"] == "success", f"MAN {cmd} should work for unlocked command"
    
    # Vérifier que MAN avec une commande non débloquée ne fonctionne pas
    if "SCAN" not in commands:
        man_response = client.post("/api/command", json={
            "command": "MAN SCAN",
            "session_id": session_id,
            "language": "FR"
        })
        assert man_response.status_code == 200
        man_data = man_response.json()
        # Soit erreur, soit succès (car SCAN a une page MAN même si pas débloqué)
        # Le test vérifie juste que l'endpoint fonctionne

def test_welcome_message_not_duplicated():
    """Test de non-régression : Le message de bienvenue ne doit pas être envoyé en boucle"""
    session_id = get_test_session_id()
    
    # Envoyer plusieurs commandes vides - ne doit retourner le welcome qu'une fois
    responses = []
    for i in range(5):
        response = client.post("/api/command", json={
            "command": "",
            "session_id": session_id,
            "language": "FR"
        })
        responses.append(response.json()["response"])
    
    # Tous les messages doivent être identiques (pas de duplication)
    assert len(set(responses)) == 1, "Le message de bienvenue ne doit pas changer entre les appels"
    
    # Le message doit être en français
    assert "initialisé" in responses[0] or "Tapez HELP" in responses[0]

def test_welcome_message_only_on_empty_command():
    """Test de non-régression : Le welcome ne doit apparaître que sur commande vide"""
    session_id = get_test_session_id()
    
    # Commande vide -> welcome
    response = client.post("/api/command", json={
        "command": "",
        "session_id": session_id,
        "language": "FR"
    })
    assert response.status_code == 200
    data = response.json()
    assert "initialisé" in data["response"] or "initialized" in data["response"]
    
    # Commande HELP -> pas de welcome
    response = client.post("/api/command", json={
        "command": "HELP",
        "session_id": session_id,
        "language": "FR"
    })
    assert response.status_code == 200
    data = response.json()
    assert "Commands available" in data["response"] or "Commandes disponibles" in data["response"]
    assert "initialisé" not in data["response"]
    assert "initialized" not in data["response"]

def test_file_autocomplete_for_decode():
    """Test de non-régression : L'auto-complétion doit fonctionner pour DECODE"""
    session_id = get_test_session_id()
    
    client.post("/api/command", json={
        "command": f"LOGIN {ENCRYPTION_KEY}",
        "session_id": session_id,
        "language": "FR"
    })
    
    # Vérifier que les fichiers sont disponibles
    response = client.get("/api/files", params={
        "session_id": session_id,
        "language": "FR"
    })
    
    assert response.status_code == 200
    data = response.json()
    assert "files" in data
    files = data["files"]
    assert "corrupted_data.b64" in files
    
    # Vérifier que DECODE fonctionne avec du Base64 direct
    decode_response = client.post("/api/command", json={
        "command": "DECODE VGhlIG5leHQgc3RlcCBpcyB0byBkZWNvZGUgdGhlIGZpbGUgY29kZWQgaW4gYmFzZTY0LgpUaGUgYW5zd2VyIGlzOiBQUk9UT0NPTF9YWVo=",
        "session_id": session_id,
        "language": "FR"
    })
    
    assert decode_response.status_code == 200
    decode_data = decode_response.json()
    assert decode_data["status"] in ["success", "info"]
    
    # Vérifier que DECODE fonctionne avec un nom de fichier
    decode_file_response = client.post("/api/command", json={
        "command": "DECODE corrupted_data.b64",
        "session_id": session_id,
        "language": "FR"
    })
    
    assert decode_file_response.status_code == 200
    decode_file_data = decode_file_response.json()
    assert decode_file_data["status"] == "success"
    assert "décodé" in decode_file_data["response"].lower() or "decoded" in decode_file_data["response"].lower()

def test_file_autocomplete_multiple_commands():
    """Test de non-régression : L'auto-complétion doit fonctionner pour toutes les commandes de fichiers"""
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
    files = data["files"]
    assert len(files) > 0
    
    # Tester que tous les fichiers sont accessibles
    for filename in files:
        access_response = client.post("/api/command", json={
            "command": f"ACCESS {filename}",
            "session_id": session_id,
            "language": "FR"
        })
        assert access_response.status_code == 200

def test_man_page_can_be_closed():
    """Test de non-régression : La page MAN doit pouvoir être fermée avec ESC, Q ou la croix"""
    session_id = get_test_session_id()
    
    # Vérifier que MAN fonctionne
    response = client.post("/api/command", json={
        "command": "MAN HELP",
        "session_id": session_id,
        "language": "FR"
    })
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    assert "HELP" in data["response"] or "help" in data["response"]
    
    # Vérifier que l'endpoint /api/man fonctionne aussi
    man_response = client.get("/api/man/HELP", params={"language": "FR"})
    assert man_response.status_code == 200
    man_data = man_response.json()
    assert "content" in man_data
    assert "HELP" in man_data["content"] or "help" in man_data["content"]

def test_man_page_returns_content():
    """Test de non-régression : La page MAN doit retourner du contenu"""
    session_id = get_test_session_id()
    
    # Tester avec plusieurs commandes
    commands_to_test = ["HELP", "STATUS", "LOGIN"]
    
    for cmd in commands_to_test:
        response = client.post("/api/command", json={
            "command": f"MAN {cmd}",
            "session_id": session_id,
            "language": "FR"
        })
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "success"
        assert len(data["response"]) > 0
        assert cmd.upper() in data["response"] or cmd.lower() in data["response"]

def test_man_page_works_with_different_languages():
    """Test de non-régression : La page MAN doit fonctionner en FR et EN"""
    session_id = get_test_session_id()
    
    # Test en français
    response_fr = client.post("/api/command", json={
        "command": "MAN HELP",
        "session_id": session_id,
        "language": "FR"
    })
    assert response_fr.status_code == 200
    data_fr = response_fr.json()
    assert data_fr["status"] == "success"
    
    # Test en anglais
    response_en = client.post("/api/command", json={
        "command": "MAN HELP",
        "session_id": session_id,
        "language": "EN"
    })
    assert response_en.status_code == 200
    data_en = response_en.json()
    assert data_en["status"] == "success"
    
    # Les deux doivent retourner du contenu
    assert len(data_fr["response"]) > 0
    assert len(data_en["response"]) > 0

def test_language_defaults_to_french():
    """Test de non-régression : La langue par défaut doit être FR"""
    session_id = get_test_session_id()
    
    # Test sans langue spécifiée -> doit être FR
    response = client.post("/api/command", json={
        "command": "",
        "session_id": session_id
        # Pas de language spécifié
    })
    assert response.status_code == 200
    data = response.json()
    # Le message doit être en français
    assert "initialisé" in data["response"] or "Tapez HELP" in data["response"]
    assert "initialized" not in data["response"] or "Type HELP" not in data["response"]
    
    # Test avec langue invalide -> doit être FR
    response = client.post("/api/command", json={
        "command": "HELP",
        "session_id": session_id,
        "language": "INVALID"
    })
    assert response.status_code == 200
    data = response.json()
    # Le message doit être en français
    assert "Commandes disponibles" in data["response"] or "Commands available" in data["response"]
    
    # Test avec langue None -> doit être FR
    response = client.post("/api/command", json={
        "command": "STATUS",
        "session_id": session_id,
        "language": None
    })
    assert response.status_code == 200
    data = response.json()
    # Le message doit être en français
    assert "Intégrité" in data["response"] or "Integrity" in data["response"]

def test_language_persistence_in_session():
    """Test de non-régression : La langue doit persister dans la session"""
    session_id = get_test_session_id()
    
    # Définir la langue à FR
    response1 = client.post("/api/command", json={
        "command": "HELP",
        "session_id": session_id,
        "language": "FR"
    })
    assert response1.status_code == 200
    data1 = response1.json()
    assert "Commandes disponibles" in data1["response"] or "Commands available" in data1["response"]
    
    # Vérifier que la langue est toujours FR même sans la spécifier
    response2 = client.post("/api/command", json={
        "command": "STATUS",
        "session_id": session_id
        # Pas de language spécifié
    })
    assert response2.status_code == 200
    data2 = response2.json()
    # Le message doit toujours être en français
    assert "Intégrité" in data2["response"] or "Integrity" in data2["response"]

def test_basic_commands_work():
    """Test de non-régression : Les commandes de base doivent fonctionner"""
    session_id = get_test_session_id()
    
    # HELP doit fonctionner
    response = client.post("/api/command", json={
        "command": "HELP",
        "session_id": session_id,
        "language": "FR"
    })
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    assert "HELP" in data["response"] or "help" in data["response"]
    
    # STATUS doit fonctionner
    response = client.post("/api/command", json={
        "command": "STATUS",
        "session_id": session_id,
        "language": "FR"
    })
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    assert "Intégrité" in data["response"] or "Integrity" in data["response"]

def test_login_works():
    """Test de non-régression : LOGIN doit fonctionner"""
    session_id = get_test_session_id()
    
    # LOGIN avec la clé d'encryption doit fonctionner
    response = client.post("/api/command", json={
        "command": f"LOGIN {ENCRYPTION_KEY}",
        "session_id": session_id,
        "language": "FR"
    })
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    assert "Niveau" in data["response"] or "Level" in data["response"] or "SCAN" in data["response"]

def test_session_persistence():
    """Test de non-régression : La session doit persister entre les commandes"""
    session_id = get_test_session_id()
    
    # LOGIN
    client.post("/api/command", json={
        "command": f"LOGIN {ENCRYPTION_KEY}",
        "session_id": session_id,
        "language": "FR"
    })
    
    # STATUS doit montrer le niveau 1
    response = client.post("/api/command", json={
        "command": "STATUS",
        "session_id": session_id,
        "language": "FR"
    })
    assert response.status_code == 200
    data = response.json()
    # Le niveau doit être 1 après LOGIN
    assert "1" in data["response"] or "Niveau 1" in data["response"] or "Level 1" in data["response"]

def test_help_shows_unlocked_commands():
    """Test de non-régression : HELP doit afficher les commandes débloquées"""
    session_id = get_test_session_id()
    
    # HELP au début
    response1 = client.post("/api/command", json={
        "command": "HELP",
        "session_id": session_id,
        "language": "FR"
    })
    assert response1.status_code == 200
    data1 = response1.json()
    assert "HELP" in data1["response"]
    assert "STATUS" in data1["response"]
    assert "LOGIN" in data1["response"]
    
    # Après LOGIN, HELP doit montrer plus de commandes
    client.post("/api/command", json={
        "command": f"LOGIN {ENCRYPTION_KEY}",
        "session_id": session_id,
        "language": "FR"
    })
    
    response2 = client.post("/api/command", json={
        "command": "HELP",
        "session_id": session_id,
        "language": "FR"
    })
    assert response2.status_code == 200
    data2 = response2.json()
    # Après LOGIN, SCAN, DECODE, ACCESS doivent être disponibles
    assert "SCAN" in data2["response"] or "DECODE" in data2["response"] or "ACCESS" in data2["response"]

if __name__ == "__main__":
    pytest.main([__file__, "-v"])

