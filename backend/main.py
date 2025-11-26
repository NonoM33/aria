from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Dict, Optional
import base64
from adventure_data import ADVENTURE_DATA

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

sessions: Dict[str, Dict] = {}

ENCRYPTION_KEY = "VOID2024"

def get_session(session_id: str, language: str = "FR") -> Dict:
    lang_upper = language.upper().strip() if language else "FR"
    if lang_upper not in ["FR", "EN"]:
        lang_upper = "FR"
    
    if session_id not in sessions:
        sessions[session_id] = {
            "level": 0,
            "chapter": "chapter_1",
            "logged_in": False,
            "unlocked_commands": ["HELP", "STATUS", "LOGIN"],
            "accessed_files": [],
            "solved_puzzles": [],
            "collected_items": [],
            "flags": [],
            "language": lang_upper
        }
    
    sessions[session_id]["language"] = lang_upper
    return sessions[session_id]

def get_text(session: Dict, key: str, default: str = "") -> str:
    lang = session.get("language", "FR")
    data = ADVENTURE_DATA.get(lang, ADVENTURE_DATA["FR"])
    
    if key.startswith("chapter_"):
        chapter_id = session.get("chapter", "chapter_1")
        chapter = data["chapters"].get(chapter_id, {})
        if key == "intro":
            return chapter.get("intro", default)
        elif key.startswith("file_"):
            filename = key.replace("file_", "")
            files = chapter.get("files", {})
            return files.get(filename, default)
        elif key.startswith("puzzle_"):
            puzzle_id = key.replace("puzzle_", "")
            puzzles = chapter.get("puzzles", {})
            puzzle = puzzles.get(puzzle_id, {})
            return puzzle.get("question", puzzle.get("hint", default))
    
    messages = data.get("system_messages", {})
    return messages.get(key, default)

class CommandRequest(BaseModel):
    command: str
    session_id: str
    language: Optional[str] = "FR"

@app.post("/api/command")
async def handle_command(request: CommandRequest):
    command_parts = request.command.strip().split(" ", 1)
    command = command_parts[0].upper() if request.command.strip() else ""
    args = command_parts[1] if len(command_parts) > 1 else ""
    
    requested_lang = (request.language or "FR").upper().strip()
    if requested_lang not in ["FR", "EN"]:
        requested_lang = "FR"
    
    session = get_session(request.session_id, requested_lang)
    session["language"] = requested_lang
    lang = requested_lang
    
    data = ADVENTURE_DATA.get(lang, ADVENTURE_DATA["FR"])
    chapter_id = session.get("chapter", "chapter_1")
    chapter = data["chapters"].get(chapter_id, {})
    
    if not command or command == "":
        system_messages = data.get("system_messages", {})
        welcome_msg = system_messages.get("welcome", "")
        if not welcome_msg:
            if lang == "EN":
                welcome_msg = "SYSTEM_VOID v2.0 initialized.\nType HELP to start."
            else:
                welcome_msg = "SYSTEM_VOID v2.0 initialisé.\nTapez HELP pour commencer."
        return {"response": welcome_msg, "status": "info"}
    
    if command == "HELP":
        available = ", ".join(session["unlocked_commands"])
        if session["level"] >= 1:
            available += ", SCAN, DECODE, ACCESS"
        if session["level"] >= 2:
            available += ", ACTIVATE, NETWORK, ANALYZE, BYPASS"
        if session["level"] >= 3:
            available += ", CONNECT, RESTORE, SOLVE"
        
        help_msg = f"Commands available: {available}"
        if lang == "FR":
            help_msg += "\n\nTapez STATUS pour voir l'état du système."
        else:
            help_msg += "\n\nType STATUS to see system status."
        return {"response": help_msg, "status": "success"}
    
    elif command == "STATUS":
        integrity = 34 + (session["level"] * 15)
        if session["level"] >= 5:
            integrity = 100
        
        if session["level"] == 0:
            if lang == "FR":
                status_msg = f"Intégrité du système: {integrity}%\nNiveau de sécurité: CRITIQUE\n\nMessage système: Le vide attend... 2024"
            else:
                status_msg = f"System Integrity: {integrity}%\nSecurity Level: CRITICAL\n\nSystem Message: The void awaits... 2024"
        else:
            if lang == "FR":
                status_msg = f"Intégrité du système: {integrity}%\nNiveau de sécurité: {'CRITIQUE' if session['level'] < 3 else 'BRÈCHE'}\nNiveau d'accès: {session['level']}\nChapitre: {chapter.get('title', 'N/A')}"
            else:
                status_msg = f"System Integrity: {integrity}%\nSecurity Level: {'CRITICAL' if session['level'] < 3 else 'BREACHED'}\nAccess Level: {session['level']}\nChapter: {chapter.get('title', 'N/A')}"
        
        return {"response": status_msg, "status": "success"}
    
    elif command == "LOGIN":
        if not args:
            if lang == "FR":
                return {"response": "Entrez la clé d'encryption...\nFormat: LOGIN <clé>", "status": "info"}
            else:
                return {"response": "Enter encryption key...\nFormat: LOGIN <key>", "status": "info"}
        
        if args.upper() == ENCRYPTION_KEY:
            session["logged_in"] = True
            session["level"] = 1
            session["chapter"] = "chapter_2"
            if "SCAN" not in session["unlocked_commands"]:
                session["unlocked_commands"].extend(["SCAN", "DECODE", "ACCESS"])
            
            chapter_2_data = data["chapters"].get("chapter_2", {})
            intro = chapter_2_data.get("intro", "")
            
            if lang == "FR":
                intro += "\n\nNouvelles commandes: SCAN, DECODE, ACCESS"
            else:
                intro += "\n\nNew commands: SCAN, DECODE, ACCESS"
            
            return {"response": intro, "status": "success"}
        else:
            if lang == "FR":
                return {"response": "Clé d'encryption invalide. Accès refusé.", "status": "error"}
            else:
                return {"response": "Invalid encryption key. Access denied.", "status": "error"}
    
    elif command == "SCAN" and session["level"] >= 1:
        files = chapter.get("files", {})
        file_list = "\n".join([f"- {name}" for name in files.keys()])
        
        if lang == "FR":
            response = f"Scan du système en cours...\n\nFichiers détectés:\n{file_list}\n\nUtilisez: ACCESS <nom_fichier> pour lire"
        else:
            response = f"Scanning system...\n\nFiles detected:\n{file_list}\n\nUse: ACCESS <filename> to read"
        
        return {"response": response, "status": "success"}
    
    elif command == "ACCESS" and session["level"] >= 1:
        if not args:
            if lang == "FR":
                return {"response": "Usage: ACCESS <nom_fichier>\nExemple: ACCESS mission.txt", "status": "info"}
            else:
                return {"response": "Usage: ACCESS <filename>\nExample: ACCESS mission.txt", "status": "info"}
        
        filename = args.lower().strip()
        files = chapter.get("files", {})
        
        if filename in files:
            if filename not in session["accessed_files"]:
                session["accessed_files"].append(filename)
            
            content = files[filename]
            
            if filename == "corrupted_data.b64":
                if lang == "FR":
                    content += "\n\n[Indice: Utilisez DECODE pour décoder ce fichier]"
                else:
                    content += "\n\n[Hint: Use DECODE to decode this file]"
            
            return {"response": f"Fichier: {filename}\n\n{content}", "status": "success"}
        else:
            if lang == "FR":
                return {"response": f"Fichier '{filename}' introuvable ou accès refusé.", "status": "error"}
            else:
                return {"response": f"File '{filename}' not found or access denied.", "status": "error"}
    
    elif command == "DECODE" and session["level"] >= 1:
        if not args:
            if lang == "FR":
                return {"response": "Usage: DECODE <texte_base64>\nExemple: DECODE VGhpcyBpcyBhIHRlc3Q=", "status": "info"}
            else:
                return {"response": "Usage: DECODE <base64_text>\nExample: DECODE VGhpcyBpcyBhIHRlc3Q=", "status": "info"}
        
        try:
            decoded = base64.b64decode(args).decode('utf-8')
            if lang == "FR":
                return {"response": f"Décodé: {decoded}", "status": "success"}
            else:
                return {"response": f"Decoded: {decoded}", "status": "success"}
        except:
            if lang == "FR":
                return {"response": "Échec du décodage. Format invalide.", "status": "error"}
            else:
                return {"response": "Decoding failed. Invalid format.", "status": "error"}
    
    elif command == "ACTIVATE" and session["level"] >= 1:
        if not args:
            if lang == "FR":
                return {"response": "Usage: ACTIVATE <nom_protocole>", "status": "info"}
            else:
                return {"response": "Usage: ACTIVATE <protocol_name>", "status": "info"}
        
        if args.upper() == "PROTOCOL_XYZ":
            session["logged_in"] = True
            session["level"] = 2
            session["chapter"] = "chapter_3"
            if "NETWORK" not in session["unlocked_commands"]:
                session["unlocked_commands"].extend(["ACTIVATE", "NETWORK", "ANALYZE", "BYPASS"])
            
            new_chapter = data["chapters"].get("chapter_3", {})
            intro = new_chapter.get("intro", "")
            
            if lang == "FR":
                intro += "\n\nNiveau 2 débloqué! Nouvelles commandes: NETWORK, ANALYZE, BYPASS"
            else:
                intro += "\n\nLevel 2 unlocked! New commands: NETWORK, ANALYZE, BYPASS"
            
            return {"response": intro, "status": "success"}
        else:
            if lang == "FR":
                return {"response": "Protocole invalide.", "status": "error"}
            else:
                return {"response": "Invalid protocol.", "status": "error"}
    
    elif command == "NETWORK" and session["level"] >= 2:
        if lang == "FR":
            response = """CARTE DU RÉSEAU
================

Serveurs détectés:
- SERVER_ALPHA (192.168.1.10) - Status: OFFLINE
- SERVER_BETA (192.168.1.20) - Status: ONLINE
- SERVER_GAMMA (192.168.1.30) - Status: LOCKED

Pour déverrouiller SERVER_GAMMA:
1. Trouvez le mot de passe dans les logs
2. Utilisez: CONNECT SERVER_GAMMA <password>

Le mot de passe est l'inverse de "VOID"."""
        else:
            response = """NETWORK MAP
===========

Detected servers:
- SERVER_ALPHA (192.168.1.10) - Status: OFFLINE
- SERVER_BETA (192.168.1.20) - Status: ONLINE
- SERVER_GAMMA (192.168.1.30) - Status: LOCKED

To unlock SERVER_GAMMA:
1. Find password in logs
2. Use: CONNECT SERVER_GAMMA <password>

Password is the reverse of "VOID"."""
        return {"response": response, "status": "success"}
    
    elif command == "ANALYZE" and session["level"] >= 2:
        if not args:
            if lang == "FR":
                return {"response": "Usage: ANALYZE <sujet>\nExemples: ANALYZE security, ANALYZE network", "status": "info"}
            else:
                return {"response": "Usage: ANALYZE <subject>\nExamples: ANALYZE security, ANALYZE network", "status": "info"}
        
        subject = args.lower().strip()
        if subject == "security" or subject == "sécurité":
            chapter_3 = data["chapters"].get("chapter_3", {})
            files = chapter_3.get("files", {})
            security_log = files.get("security_log.txt", "")
            if lang == "FR":
                return {"response": f"Analyse de sécurité:\n\n{security_log}", "status": "success"}
            else:
                return {"response": f"Security analysis:\n\n{security_log}", "status": "success"}
        elif subject == "network" or subject == "réseau":
            if lang == "FR":
                return {"response": "Utilisez la commande NETWORK pour voir la carte du réseau.", "status": "info"}
            else:
                return {"response": "Use NETWORK command to see network map.", "status": "info"}
        else:
            if lang == "FR":
                return {"response": f"Analyse de '{subject}' non disponible.", "status": "error"}
            else:
                return {"response": f"Analysis of '{subject}' not available.", "status": "error"}
    
    elif command == "BYPASS" and session["level"] >= 2:
        if not args:
            if lang == "FR":
                return {"response": "Usage: BYPASS <code>\nLe code est la réponse à l'énigme du carré magique.", "status": "info"}
            else:
                return {"response": "Usage: BYPASS <code>\nThe code is the answer to the magic square riddle.", "status": "info"}
        
        puzzles = chapter.get("puzzles", {})
        puzzle = puzzles.get("magic_square", {})
        
        if args.strip() == puzzle.get("solution", ""):
            session["logged_in"] = True
            session["level"] = 3
            session["chapter"] = "chapter_4"
            if "CONNECT" not in session["unlocked_commands"]:
                session["unlocked_commands"].extend(["CONNECT"])
            if "magic_square" not in session["solved_puzzles"]:
                session["solved_puzzles"].append("magic_square")
            
            new_chapter = data["chapters"].get("chapter_4", {})
            intro = new_chapter.get("intro", "")
            
            if lang == "FR":
                return {"response": f"Code correct!\n\n{intro}", "status": "success"}
            else:
                return {"response": f"Correct code!\n\n{intro}", "status": "success"}
        else:
            if lang == "FR":
                return {"response": "Code incorrect. Réessayez.", "status": "error"}
            else:
                return {"response": "Incorrect code. Try again.", "status": "error"}
    
    elif command == "CONNECT" and session["level"] >= 3:
        if not args:
            if lang == "FR":
                return {"response": "Usage: CONNECT SERVER_GAMMA <mot_de_passe>", "status": "info"}
            else:
                return {"response": "Usage: CONNECT SERVER_GAMMA <password>", "status": "info"}
        
        parts = args.split(" ", 1)
        if len(parts) < 2:
            if lang == "FR":
                return {"response": "Format: CONNECT <serveur> <mot_de_passe>", "status": "error"}
            else:
                return {"response": "Format: CONNECT <server> <password>", "status": "error"}
        
        server = parts[0].upper()
        password = parts[1].upper()
        
        if server == "SERVER_GAMMA" and password == "DIOV":
            session["logged_in"] = True
            session["level"] = 4
            session["chapter"] = "chapter_5"
            if "RESTORE" not in session["unlocked_commands"]:
                session["unlocked_commands"].extend(["RESTORE", "SOLVE"])
            
            new_chapter = data["chapters"].get("chapter_5", {})
            intro = new_chapter.get("intro", "")
            
            if lang == "FR":
                return {"response": f"Serveur GAMMA connecté!\n\n{intro}", "status": "success"}
            else:
                return {"response": f"Server GAMMA connected!\n\n{intro}", "status": "success"}
        else:
            if lang == "FR":
                return {"response": "Connexion échouée. Serveur ou mot de passe incorrect.", "status": "error"}
            else:
                return {"response": "Connection failed. Server or password incorrect.", "status": "error"}
    
    elif command == "RESTORE" and session["level"] >= 4:
        if not args:
            if lang == "FR":
                return {"response": "Usage: RESTORE <code>\nLe code est: 34 + 15 + 5 + 1", "status": "info"}
            else:
                return {"response": "Usage: RESTORE <code>\nThe code is: 34 + 15 + 5 + 1", "status": "info"}
        
        if args.strip() == "55":
            session["level"] = 5
            session["flags"].append("system_restored")
            
            if lang == "FR":
                return {"response": "Code de restauration correct!\n\nSystème restauré à 100%.\n\nÉtape finale: résolvez l'énigme finale avec SOLVE.", "status": "success"}
            else:
                return {"response": "Restoration code correct!\n\nSystem restored to 100%.\n\nFinal step: solve the final riddle with SOLVE.", "status": "success"}
        else:
            if lang == "FR":
                return {"response": "Code incorrect. Réessayez.", "status": "error"}
            else:
                return {"response": "Incorrect code. Try again.", "status": "error"}
    
    elif command == "SOLVE" and session["level"] >= 4:
        if not args:
            if lang == "FR":
                return {"response": "Usage: SOLVE <réponse>\nRésolvez l'énigme finale du fichier final_riddle.txt", "status": "info"}
            else:
                return {"response": "Usage: SOLVE <answer>\nSolve the final riddle from final_riddle.txt file", "status": "info"}
        
        puzzles = chapter.get("puzzles", {})
        puzzle = puzzles.get("final_riddle", {})
        
        if args.upper().strip() == puzzle.get("solution", "").upper():
            session["level"] = 6
            session["flags"].append("adventure_complete")
            
            if lang == "FR":
                return {"response": """FÉLICITATIONS!
================

Vous avez complété SYSTEM_VOID!
L'intégrité du système est restaurée à 100%.
Tous les fichiers ont été récupérés.
La mission est un succès.

Temps estimé: 1 heure
Votre temps: Variable

Merci d'avoir joué!""", "status": "success"}
            else:
                return {"response": """CONGRATULATIONS!
==================

You have completed SYSTEM_VOID!
System integrity restored to 100%.
All files have been recovered.
Mission successful.

Estimated time: 1 hour
Your time: Variable

Thank you for playing!""", "status": "success"}
        else:
            if lang == "FR":
                return {"response": "Réponse incorrecte. Réessayez.", "status": "error"}
            else:
                return {"response": "Incorrect answer. Try again.", "status": "error"}
    
    else:
        if lang == "FR":
            return {"response": "Commande inconnue. Accès refusé.\n\nTapez HELP pour voir les commandes disponibles.", "status": "error"}
        else:
            return {"response": "Unknown command. Access Denied.\n\nType HELP to see available commands.", "status": "error"}

@app.get("/api/global-status")
async def get_global_status(session_id: str = None):
    if session_id and session_id in sessions:
        session = sessions[session_id]
        integrity = 34 + (session["level"] * 15)
        if session["level"] >= 5:
            integrity = 100
        return {
            "system_integrity": integrity,
            "active_users": 127,
            "security_level": "CRITICAL" if session["level"] < 3 else "BREACHED",
            "access_level": session["level"],
            "chapter": session.get("chapter", "chapter_1"),
            "last_update": "2024-01-15T10:23:45Z"
        }
    return {
        "system_integrity": 34,
        "active_users": 127,
        "security_level": "CRITICAL",
        "last_update": "2024-01-15T10:23:45Z"
    }

@app.get("/")
async def root():
    return {"message": "SYSTEM_VOID API"}
