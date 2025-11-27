from typing import Dict, Any, Optional
from sqlalchemy.orm import Session
from commands.base_command import BaseCommand
from commands.help_command import HelpCommand
from commands.status_command import StatusCommand
from commands.login_command import LoginCommand
from commands.scan_command import ScanCommand
from commands.access_command import AccessCommand
from commands.decode_command import DecodeCommand
from commands.activate_command import ActivateCommand
from commands.network_command import NetworkCommand
from commands.analyze_command import AnalyzeCommand
from commands.bypass_command import BypassCommand
from commands.connect_command import ConnectCommand
from commands.restore_command import RestoreCommand
from commands.solve_command import SolveCommand
from commands.man_command import ManCommand
from commands.ssh_command import SshCommand
from commands.exploit_command import ExploitCommand
from commands.create_user_command import CreateUserCommand
from commands.pkg_command import PkgCommand
from commands.exit_command import ExitCommand
from commands.ls_command import LsCommand
from commands.talk_command import TalkCommand, AriaCommand
from commands.cd_command import CdCommand
from commands.pwd_command import PwdCommand
from commands.alias_command import AliasCommand
from commands.edit_command import EditCommand
from commands.admin_command import (
    AdminStatsCommand, AdminOnlineCommand, 
    AdminListCommand, AdminViewCommand, AdminExitCommand
)
from config import DEV_MODE
from adventures.adventure_data import get_adventure_data
from adventures.adventure_loader import get_chapter
from services.aria_service import is_aria_choice_command, handle_aria_choice

COMMAND_MAP = {
    "HELP": HelpCommand,
    "STATUS": StatusCommand,
    "LOGIN": LoginCommand,
    "SCAN": ScanCommand,
    "ACCESS": AccessCommand,
    "CAT": AccessCommand,
    "DECODE": DecodeCommand,
    "ACTIVATE": ActivateCommand,
    "NETWORK": NetworkCommand,
    "ANALYZE": AnalyzeCommand,
    "BYPASS": BypassCommand,
    "CONNECT": ConnectCommand,
    "RESTORE": RestoreCommand,
    "SOLVE": SolveCommand,
    "MAN": ManCommand,
    "SSH": SshCommand,
    "EXPLOIT": ExploitCommand,
    "CREATE_USER": CreateUserCommand,
    "PKG": PkgCommand,
    "EXIT": ExitCommand,
    "LS": LsCommand,
    "TALK": TalkCommand,
    "ARIA": AriaCommand,
    "CD": CdCommand,
    "PWD": PwdCommand,
    "ALIAS": AliasCommand,
    "EDIT": EditCommand,
}

ADMIN_COMMAND_MAP = {
    "STATS": AdminStatsCommand,
    "ONLINE": AdminOnlineCommand,
    "LIST": AdminListCommand,
    "VIEW": AdminViewCommand,
    "EXIT": AdminExitCommand,
    "HELP": None,
}

def handle_command(
    command: str,
    args: str,
    session: Dict[str, Any],
    db: Optional[Session],
    lang: str,
    token: Optional[str] = None,
    alias_depth: int = 0
) -> Dict[str, Any]:
    if alias_depth > 10:
        if lang == "FR":
            return {"response": "Erreur: Boucle infinie détectée dans les alias.", "status": "error"}
        else:
            return {"response": "Error: Infinite loop detected in aliases.", "status": "error"}
    
    command_upper = command.upper()
    
    aliases = session.get("aliases", {})
    if command_upper in aliases:
        alias_command = aliases[command_upper]
        if args:
            full_command = f"{alias_command} {args}"
        else:
            full_command = alias_command
        
        parts = full_command.split(" ", 1)
        new_command = parts[0].strip()
        new_args = parts[1].strip() if len(parts) > 1 else ""
        
        return handle_command(new_command, new_args, session, db, lang, token, alias_depth + 1)
    
    if session.get("ssh_pending_username") and command_upper == "":
        if "SSH" in COMMAND_MAP:
            cmd_class = COMMAND_MAP["SSH"]
            cmd_instance = cmd_class(session, db, lang)
            if token and hasattr(cmd_instance, 'token'):
                cmd_instance.token = token
            elif session.get("ssh_token") and hasattr(cmd_instance, 'token'):
                cmd_instance.token = session.get("ssh_token")
            if hasattr(cmd_instance, 'execute_password'):
                return cmd_instance.execute_password(args)
    
    if session.get("admin_mode"):
        if command_upper == "HELP":
            help_text = """
╔══════════════════════════════════════════════════════════════════╗
║                    AIDE - MODE ADMINISTRATEUR                    ║
╠══════════════════════════════════════════════════════════════════╣
║                                                                  ║
║  Commandes disponibles:                                          ║
║                                                                  ║
║    STATS        Affiche les statistiques globales                ║
║    ONLINE       Liste les joueurs en ligne                       ║
║    LIST         Liste tous les joueurs (20 derniers)             ║
║    VIEW <user>  Affiche les details d'un joueur                  ║
║    EXIT         Quitte le mode administrateur                    ║
║    HELP         Affiche cette aide                               ║
║                                                                  ║
╚══════════════════════════════════════════════════════════════════╝
"""
            return {"response": help_text, "status": "success"}
        
        if command_upper in ADMIN_COMMAND_MAP:
            cmd_class = ADMIN_COMMAND_MAP[command_upper]
            if cmd_class:
                cmd_instance = cmd_class(session, db, lang)
                return cmd_instance.execute(args)
        
        if lang == "FR":
            return {"response": f"Commande admin inconnue: {command}\nTapez HELP pour voir les commandes disponibles.", "status": "error"}
        else:
            return {"response": f"Unknown admin command: {command}\nType HELP to see available commands.", "status": "error"}
    
    if is_aria_choice_command(command_upper):
        result = handle_aria_choice(session, command_upper, lang)
        if result:
            return {"response": "", "status": "success", **result}
    
    if command_upper in COMMAND_MAP:
        cmd_class = COMMAND_MAP[command_upper]
        cmd_instance = cmd_class(session, db, lang)
        if token and hasattr(cmd_instance, 'token'):
            cmd_instance.token = token
        elif session.get("ssh_token") and hasattr(cmd_instance, 'token'):
            cmd_instance.token = session.get("ssh_token")
        return cmd_instance.execute(args)
    
    if command_upper == "DEV" and DEV_MODE:
        return handle_dev_command(args, session, lang)
    
    if lang == "FR":
        return {"response": "Commande inconnue. Accès refusé.\n\nTapez HELP pour voir les commandes disponibles.", "status": "error"}
    else:
        return {"response": "Unknown command. Access Denied.\n\nType HELP to see available commands.", "status": "error"}

def handle_dev_command(args: str, session: Dict[str, Any], lang: str) -> Dict[str, Any]:
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
        from adventures.global_state import GlobalState
        global_state = GlobalState()
        state = global_state.get_state()
        return {"response": f"""ÉTAT GLOBAL
============

Intégrité globale: {state['global_integrity']}%
Joueurs totaux: {state['total_players']}
Joueurs en ligne: {state['players_online']}
Chapitres débloqués: {', '.join(state['chapters_unlocked']) if state['chapters_unlocked'] else 'Aucun'}
État du monde: {state['world_state']}
Dernière mise à jour: {state['last_update']}""", "status": "success"}
    
    elif dev_command == "LIST":
        from adventures.adventure_loader import load_all_chapters
        all_chapters = load_all_chapters(lang)
        chapter_list = "\n".join([f"- {cid}: {ch.get('title', 'N/A')}" for cid, ch in all_chapters.items()])
        return {"response": f"CHAPITRES DISPONIBLES:\n\n{chapter_list}", "status": "success"}
    
    else:
        return {"response": f"Commande DEV inconnue: {dev_command}", "status": "error"}

