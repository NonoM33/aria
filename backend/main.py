from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Dict, Optional, Any
import base64
import os
from adventures.adventure_data import get_adventure_data
from adventures.global_state import GlobalState
from man_pages import MAN_PAGES

# Imports optionnels pour la base de données
DB_AVAILABLE = False
try:
    import sqlalchemy
    from database import init_db, get_db, Player, GlobalEvent, PlayerEvent
    from auth import create_player, authenticate_player, get_player_by_username, save_player_progress, get_player_by_id, player_to_session_dict
    DB_AVAILABLE = True
except (ImportError, Exception):
    DB_AVAILABLE = False
    def init_db():
        pass
    def get_db():
        yield None
    def player_to_session_dict(player):
        return {}

DEV_MODE = os.getenv("DEV_MODE", "false").lower() == "true"
global_state = GlobalState()

# Initialiser la base de données au démarrage (si disponible)
if DB_AVAILABLE:
    try:
        init_db()
    except:
        DB_AVAILABLE = False

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

def get_session(session_id: str, language: str = "FR", db: Any = None, username: str = None) -> Dict:
    # Normaliser la langue : par défaut FR, valider FR ou EN
    lang_upper = "FR"  # Par défaut FR
    if language:
        lang_upper = language.upper().strip()
        if lang_upper not in ["FR", "EN"]:
            lang_upper = "FR"
    
    # Si on a un username, charger depuis la DB
    if username and db and DB_AVAILABLE:
        try:
            from auth import get_player_by_username
            player = get_player_by_username(db, username)
            if player:
                session_dict = player_to_session_dict(player)
                session_dict["language"] = lang_upper  # S'assurer que la langue est bien définie
                return session_dict
        except:
            pass
    
    # Sinon, utiliser les sessions temporaires
    is_new_session = session_id not in sessions
    
    if is_new_session:
        sessions[session_id] = {
            "level": 0,
            "chapter": "chapter_1",
            "logged_in": False,
            "unlocked_commands": ["HELP", "STATUS", "LOGIN"],
            "accessed_files": [],
            "solved_puzzles": [],
            "collected_items": [],
            "flags": [],
            "language": lang_upper,
            "username": None,
            "player_id": None
        }
        global_state.add_player()
    
    # Toujours mettre à jour la langue dans la session
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
    username: Optional[str] = None

@app.post("/api/command")
async def handle_command(request: CommandRequest):
    db = None
    if DB_AVAILABLE:
        try:
            db = next(get_db())
        except:
            db = None
    command_parts = request.command.strip().split(" ", 1)
    command = command_parts[0].upper() if request.command.strip() else ""
    args = command_parts[1] if len(command_parts) > 1 else ""
    
    # Normaliser la langue : par défaut FR
    requested_lang = "FR"  # Par défaut FR
    if request.language:
        requested_lang = request.language.upper().strip()
        if requested_lang not in ["FR", "EN"]:
            requested_lang = "FR"
    
    # Charger depuis la DB si username fourni
    session = get_session(request.session_id, requested_lang, db, request.username)
    session["language"] = requested_lang
    lang = requested_lang
    
    adventure_data = get_adventure_data(lang)
    if lang not in adventure_data:
        lang = "FR"
    data = adventure_data.get(lang, {})
    chapter_id = session.get("chapter", "chapter_1")
    chapter = data["chapters"].get(chapter_id, {})
    
    # Si on a un player_id, charger le joueur depuis la DB
    player = None
    if session.get("player_id") and db and DB_AVAILABLE:
        try:
            player = get_player_by_id(db, session["player_id"])
        except:
            pass
    
    if not command or command == "":
        system_messages = data.get("system_messages", {})
        welcome_msg = system_messages.get("welcome", "")
        if not welcome_msg:
            if lang == "EN":
                welcome_msg = "SYSTEM_VOID v2.0 initialized.\nType HELP to start."
            else:
                welcome_msg = "SYSTEM_VOID v2.0 initialisé.\nTapez HELP pour commencer."
        
        # Si le joueur est connecté, ajouter un message personnalisé
        if session.get("username"):
            if lang == "FR":
                welcome_msg += f"\n\nBienvenue de retour, {session['username']}!"
            else:
                welcome_msg += f"\n\nWelcome back, {session['username']}!"
        
        return {"response": welcome_msg, "status": "info"}
    
    # Si on a un player_id, charger le joueur depuis la DB
    player = None
    if session.get("player_id") and db and DB_AVAILABLE:
        try:
            player = get_player_by_id(db, session["player_id"])
        except:
            pass
    
    # Sauvegarder la progression à la fin de chaque commande si on a un joueur
    def finalize_response(response_data):
        """Helper pour sauvegarder et retourner la réponse"""
        if DB_AVAILABLE and (player or session.get("player_id")):
            try:
                save_session_to_db(db, session, player)
            except:
                pass  # Ignorer les erreurs de sauvegarde
        return response_data
    
    def save_session_to_db(db: Any, session: Dict, player: Any = None):
        """Sauvegarde la session dans la base de données"""
        if not DB_AVAILABLE or not db:
            return
        
        # Si on a un player_id, charger le joueur
        if not player and session.get("player_id"):
            try:
                player = get_player_by_id(db, session["player_id"])
            except:
                pass
        
        if player:
            # Mettre à jour la progression
            player.level = session.get("level", 0)
            player.chapter = session.get("chapter", "chapter_1")
            player.logged_in = session.get("logged_in", False)
            player.unlocked_commands = session.get("unlocked_commands", [])
            player.accessed_files = session.get("accessed_files", [])
            player.solved_puzzles = session.get("solved_puzzles", [])
            player.collected_items = session.get("collected_items", [])
            player.flags = session.get("flags", [])
            player.language = session.get("language", "FR")
            player.total_commands = (player.total_commands or 0) + 1
            
            try:
                save_player_progress(db, player)
            except:
                pass
    
    def create_global_event(db: Any, event_type: str, event_data: dict, triggered_by: str = None, impact_level: int = 1):
        """Crée un événement global qui impacte tous les joueurs"""
        if not DB_AVAILABLE or not db:
            return
        
        try:
            event = GlobalEvent(
                event_type=event_type,
                event_data=event_data,
                triggered_by=triggered_by,
                impact_level=impact_level
            )
            db.add(event)
            db.commit()
            
            # Mettre à jour le global_state
            global_state._add_event(event_type, event_data)
        except:
            pass
    
    if command == "HELP":
        # Construire la liste des commandes disponibles sans duplication
        all_commands = set(session["unlocked_commands"])
        
        if session["level"] >= 1:
            all_commands.update(["SCAN", "DECODE", "ACCESS"])
        if session["level"] >= 2:
            all_commands.update(["ACTIVATE", "NETWORK", "ANALYZE", "BYPASS"])
        if session["level"] >= 3:
            all_commands.update(["CONNECT", "RESTORE", "SOLVE"])
        if session["level"] >= 6:
            all_commands.update(["NVIM", "MAN"])
        if DEV_MODE:
            all_commands.add("DEV")
        
        # Trier pour un affichage cohérent
        sorted_commands = sorted(all_commands)
        available = ", ".join(sorted_commands)
        
        help_msg = f"Commands available: {available}"
        if lang == "FR":
            help_msg += "\n\nTapez STATUS pour voir l'état du système."
            help_msg += f"\n[GLOBAL] Intégrité mondiale: {global_state._state['global_integrity']}%"
        else:
            help_msg += "\n\nType STATUS to see system status."
            help_msg += f"\n[GLOBAL] World integrity: {global_state._state['global_integrity']}%"
        return finalize_response({"response": help_msg, "status": "success"})
    
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
            
            global_state.update_integrity(global_state._state["global_integrity"] + 1)
            global_state.unlock_chapter("chapter_2")
            
            chapter_2_data = data["chapters"].get("chapter_2", {})
            intro = chapter_2_data.get("intro", "")
            
            global_integrity = global_state._state["global_integrity"]
            if lang == "FR":
                intro += f"\n\nNouvelles commandes: SCAN, DECODE, ACCESS\n\n[GLOBAL] Intégrité mondiale: {global_integrity}% ({global_state._state['players_online']} joueurs actifs)"
            else:
                intro += f"\n\nNew commands: SCAN, DECODE, ACCESS\n\n[GLOBAL] World integrity: {global_integrity}% ({global_state._state['players_online']} active players)"
            
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
                return {"response": "Usage: DECODE <texte_base64> ou DECODE <nom_fichier>\nExemple: DECODE VGhpcyBpcyBhIHRlc3Q=\nExemple: DECODE corrupted_data.b64", "status": "info"}
            else:
                return {"response": "Usage: DECODE <base64_text> or DECODE <filename>\nExample: DECODE VGhpcyBpcyBhIHRlc3Q=\nExample: DECODE corrupted_data.b64", "status": "info"}
        
        # Vérifier si c'est un nom de fichier
        files = chapter.get("files", {})
        filename = args.lower().strip()
        
        if filename in files:
            # C'est un nom de fichier, décoder son contenu
            file_content = files[filename]
            try:
                decoded = base64.b64decode(file_content).decode('utf-8')
                if lang == "FR":
                    return {"response": f"Fichier {filename} décodé:\n\n{decoded}", "status": "success"}
                else:
                    return {"response": f"File {filename} decoded:\n\n{decoded}", "status": "success"}
            except:
                if lang == "FR":
                    return {"response": f"Le fichier {filename} ne contient pas de Base64 valide.", "status": "error"}
                else:
                    return {"response": f"File {filename} does not contain valid Base64.", "status": "error"}
        else:
            # C'est du Base64 direct
            try:
                decoded = base64.b64decode(args).decode('utf-8')
                if lang == "FR":
                    return {"response": f"Décodé: {decoded}", "status": "success"}
                else:
                    return {"response": f"Decoded: {decoded}", "status": "success"}
            except:
                if lang == "FR":
                    return {"response": "Échec du décodage. Format invalide ou fichier introuvable.", "status": "error"}
                else:
                    return {"response": "Decoding failed. Invalid format or file not found.", "status": "error"}
    
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
            
            # Sauvegarder la progression
            save_session_to_db(db, session, player)
            
            new_chapter = data["chapters"].get("chapter_3", {})
            intro = new_chapter.get("intro", "")
            
            if lang == "FR":
                intro += "\n\nNiveau 2 débloqué! Nouvelles commandes: NETWORK, ANALYZE, BYPASS"
            else:
                intro += "\n\nLevel 2 unlocked! New commands: NETWORK, ANALYZE, BYPASS"
            
            return finalize_response({"response": intro, "status": "success"})
        else:
            if lang == "FR":
                return {"response": "Protocole invalide.\n\nIndice: Le nom du protocole se trouve dans le fichier corrupted_data.b64 décodé.\nIl commence par PROTOCOL_ et se termine par _XYZ.", "status": "error"}
            else:
                return {"response": "Invalid protocol.\n\nHint: The protocol name is in the decoded corrupted_data.b64 file.\nIt starts with PROTOCOL_ and ends with _XYZ.", "status": "error"}
    
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
            
            # Sauvegarder la progression
            save_session_to_db(db, session, player)
            
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
            
            # Sauvegarder la progression
            save_session_to_db(db, session, player)
            
            # Créer un événement global
            if session.get("username"):
                create_global_event(
                    db, 
                    "SYSTEM_RESTORED", 
                    {"level": 5, "restored_by": session.get("username")},
                    triggered_by=session.get("username"),
                    impact_level=8
                )
            
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
            session["chapter"] = "chapter_6"
            session["flags"].append("adventure_complete")
            if "NVIM" not in session["unlocked_commands"]:
                session["unlocked_commands"].extend(["NVIM", "MAN"])
            
            if lang == "FR":
                return {"response": """FÉLICITATIONS!
================

Vous avez complété la première partie de SYSTEM_VOID!
L'intégrité du système est restaurée à 50%.
Nouvelles commandes débloquées: NVIM, MAN

Chapitre 6: L'Exploration
Utilisez NVIM pour explorer le système de fichiers.

Tapez MAN NVIM pour apprendre à utiliser le gestionnaire de fichiers.""", "status": "success"}
            else:
                return {"response": """CONGRATULATIONS!
==================

You have completed the first part of SYSTEM_VOID!
System integrity restored to 50%.
New commands unlocked: NVIM, MAN

Chapter 6: The Exploration
Use NVIM to explore the file system.

Type MAN NVIM to learn how to use the file manager.""", "status": "success"}
        else:
            if lang == "FR":
                return {"response": "Réponse incorrecte. Réessayez.", "status": "error"}
            else:
                return {"response": "Incorrect answer. Try again.", "status": "error"}
    
    elif command == "MAN":
        if not args:
            if lang == "FR":
                return {"response": "Usage: MAN <commande>\nExemple: MAN HELP", "status": "info"}
            else:
                return {"response": "Usage: MAN <command>\nExample: MAN HELP", "status": "info"}
        
        command_name = args.upper().strip()
        man_pages = MAN_PAGES.get(lang, MAN_PAGES["FR"])
        
        if command_name in man_pages:
            return {"response": man_pages[command_name], "status": "success"}
        else:
            if lang == "FR":
                return {"response": f"Aucune page de manuel trouvée pour '{command_name}'.\n\nUtilisez MAN HELP pour voir les commandes disponibles.", "status": "error"}
            else:
                return {"response": f"No manual page found for '{command_name}'.\n\nUse MAN HELP to see available commands.", "status": "error"}
    
    elif command == "DEV" and DEV_MODE:
        if not args:
            if lang == "FR":
                return {"response": """MODE DÉVELOPPEMENT
==================

Commandes disponibles:
- DEV JUMP <chapter_id> : Aller à un chapitre
- DEV LEVEL <niveau> : Définir le niveau
- DEV GLOBAL : Voir l'état global
- DEV RESET : Réinitialiser la session
- DEV LIST : Lister tous les chapitres

Exemple: DEV JUMP chapter_6""", "status": "info"}
            else:
                return {"response": """DEVELOPMENT MODE
==================

Available commands:
- DEV JUMP <chapter_id> : Jump to a chapter
- DEV LEVEL <level> : Set level
- DEV GLOBAL : View global state
- DEV RESET : Reset session
- DEV LIST : List all chapters

Example: DEV JUMP chapter_6""", "status": "info"}
        
        dev_parts = args.split(" ", 1)
        dev_command = dev_parts[0].upper()
        dev_args = dev_parts[1] if len(dev_parts) > 1 else ""
        
        if dev_command == "JUMP":
            if not dev_args:
                return {"response": "Usage: DEV JUMP <chapter_id>\nExemple: DEV JUMP chapter_6", "status": "error"}
            chapter_id = dev_args.lower().strip()
            from adventures.adventure_loader import get_chapter
            chapter_data = get_chapter(chapter_id, lang)
            if chapter_data:
                session["chapter"] = chapter_id
                session["level"] = int(chapter_id.split("_")[1]) if "_" in chapter_id else 0
                if lang == "FR":
                    return {"response": f"Chapitre changé: {chapter_id}\n\n{chapter_data.get('intro', '')}", "status": "success"}
                else:
                    return {"response": f"Chapter changed: {chapter_id}\n\n{chapter_data.get('intro', '')}", "status": "success"}
            else:
                return {"response": f"Chapitre '{chapter_id}' introuvable.", "status": "error"}
        
        elif dev_command == "LEVEL":
            if not dev_args:
                return {"response": "Usage: DEV LEVEL <niveau>", "status": "error"}
            try:
                level = int(dev_args)
                session["level"] = level
                return {"response": f"Niveau défini à {level}", "status": "success"}
            except:
                return {"response": "Niveau invalide", "status": "error"}
        
        elif dev_command == "GLOBAL":
            state = global_state.get_state()
            return {"response": f"""ÉTAT GLOBAL
============

Intégrité globale: {state['global_integrity']}%
Joueurs totaux: {state['total_players']}
Joueurs en ligne: {state['players_online']}
Chapitres débloqués: {', '.join(state['chapters_unlocked']) if state['chapters_unlocked'] else 'Aucun'}
État du monde: {state['world_state']}
Dernière mise à jour: {state['last_update']}""", "status": "success"}
        
        elif dev_command == "RESET":
            session_id = request.session_id
            if session_id in sessions:
                del sessions[session_id]
            return {"response": "Session réinitialisée", "status": "success"}
        
        elif dev_command == "LIST":
            from adventures.adventure_loader import load_all_chapters
            all_chapters = load_all_chapters(lang)
            chapter_list = "\n".join([f"- {cid}: {ch.get('title', 'N/A')}" for cid, ch in all_chapters.items()])
            return {"response": f"CHAPITRES DISPONIBLES:\n\n{chapter_list}", "status": "success"}
        
        else:
            return {"response": f"Commande DEV inconnue: {dev_command}", "status": "error"}
    
    else:
        if lang == "FR":
            return {"response": "Commande inconnue. Accès refusé.\n\nTapez HELP pour voir les commandes disponibles.", "status": "error"}
        else:
            return {"response": "Unknown command. Access Denied.\n\nType HELP to see available commands.", "status": "error"}

@app.get("/api/man/{command}")
async def get_man_page(command: str, language: str = "FR"):
    lang = language.upper().strip() if language else "FR"
    if lang not in ["FR", "EN"]:
        lang = "FR"
    
    command_upper = command.upper()
    man_pages = MAN_PAGES.get(lang, MAN_PAGES["FR"])
    
    if command_upper in man_pages:
        return {
            "command": command_upper,
            "content": man_pages[command_upper],
            "language": lang
        }
    else:
        if lang == "FR":
            return {
                "command": command_upper,
                "content": f"MAN(1)                    Manuel SYSTEM_VOID                   MAN(1)\n\nAucune page de manuel trouvée pour '{command_upper}'.\n\nUtilisez MAN HELP pour voir les commandes disponibles.",
                "language": lang
            }
        else:
            return {
                "command": command_upper,
                "content": f"MAN(1)                    SYSTEM_VOID Manual                   MAN(1)\n\nNo manual page found for '{command_upper}'.\n\nUse MAN HELP to see available commands.",
                "language": lang
            }

@app.get("/api/unlocked-commands")
async def get_unlocked_commands(session_id: str, language: str = "FR"):
    requested_lang = (language or "FR").upper().strip()
    if requested_lang not in ["FR", "EN"]:
        requested_lang = "FR"
    
    session = get_session(session_id, requested_lang)
    return {"commands": session.get("unlocked_commands", [])}

@app.get("/api/files")
async def get_available_files(session_id: str, language: str = "FR"):
    requested_lang = (language or "FR").upper().strip()
    if requested_lang not in ["FR", "EN"]:
        requested_lang = "FR"
    
    session = get_session(session_id, requested_lang)
    chapter_id = session.get("chapter", "chapter_1")
    
    adventure_data = get_adventure_data(requested_lang)
    data = adventure_data.get(requested_lang, {})
    chapter = data["chapters"].get(chapter_id, {})
    
    files = list(chapter.get("files", {}).keys())
    return {"files": files}

@app.get("/api/global-status")
async def get_global_status(session_id: str = None):
    global_state_data = global_state.get_state()
    
    if session_id and session_id in sessions:
        session = sessions[session_id]
        integrity = 34 + (session["level"] * 15)
        if session["level"] >= 5:
            integrity = 100
        return {
            "system_integrity": integrity,
            "global_integrity": global_state_data["global_integrity"],
            "active_users": global_state_data["players_online"],
            "total_players": global_state_data["total_players"],
            "security_level": "CRITICAL" if session["level"] < 3 else "BREACHED",
            "access_level": session["level"],
            "chapter": session.get("chapter", "chapter_1"),
            "world_state": global_state_data["world_state"],
            "chapters_unlocked": global_state_data["chapters_unlocked"],
            "last_update": global_state_data["last_update"]
        }
    return {
        "system_integrity": 34,
        "global_integrity": global_state_data["global_integrity"],
        "active_users": global_state_data["players_online"],
        "total_players": global_state_data["total_players"],
        "security_level": "CRITICAL",
        "world_state": global_state_data["world_state"],
        "last_update": global_state_data["last_update"]
    }

@app.get("/api/global-events")
async def get_global_events(limit: int = 10):
    """Récupère les événements globaux récents"""
    if not DB_AVAILABLE:
        return {"events": []}
    
    try:
        db = next(get_db())
        events = db.query(GlobalEvent).order_by(GlobalEvent.created_at.desc()).limit(limit).all()
        return {
            "events": [
                {
                    "type": event.event_type,
                    "data": event.event_data,
                    "triggered_by": event.triggered_by,
                    "impact_level": event.impact_level,
                    "created_at": event.created_at.isoformat() if event.created_at else None
                }
                for event in events
            ]
        }
    except:
        return {"events": []}

@app.get("/")
async def root():
    return {"message": "SYSTEM_VOID API"}
