from typing import Dict, Any
from commands.base_command import BaseCommand
from database import Player, SessionLocal, Connection
from sqlalchemy import func
from services.session_service import sessions
from datetime import datetime, timedelta
import json


def get_online_sessions():
    online = []
    for session_id, session_data in sessions.items():
        if session_data.get("logged_in") and session_data.get("username"):
            online.append({
                "session_id": session_id[:8],
                "username": session_data.get("username"),
                "chapter": session_data.get("chapter", "unknown"),
                "level": session_data.get("level", 0),
                "path": session_data.get("current_path", "/")
            })
    return online


class AdminStatsCommand(BaseCommand):
    def execute(self, args: str) -> Dict[str, Any]:
        if not self.session.get("admin_mode"):
            return {"response": "Access denied.", "status": "error"}
        
        db = SessionLocal()
        try:
            total_players = db.query(func.count(Player.id)).scalar() or 0
            online = get_online_sessions()
            online_count = len(online)
            
            total_connections = db.query(func.count(Connection.id)).scalar() or 0
            converted_connections = db.query(func.count(Connection.id)).filter(
                Connection.converted == True
            ).scalar() or 0
            conversion_rate = round(converted_connections / total_connections * 100, 1) if total_connections > 0 else 0
            
            one_day_ago = datetime.utcnow() - timedelta(days=1)
            one_week_ago = datetime.utcnow() - timedelta(days=7)
            
            connections_24h = db.query(func.count(Connection.id)).filter(
                Connection.created_at >= one_day_ago
            ).scalar() or 0
            
            connections_7d = db.query(func.count(Connection.id)).filter(
                Connection.created_at >= one_week_ago
            ).scalar() or 0
            
            active_24h = db.query(func.count(Player.id)).filter(
                Player.last_login >= one_day_ago
            ).scalar() or 0
            
            active_7d = db.query(func.count(Player.id)).filter(
                Player.last_login >= one_week_ago
            ).scalar() or 0
            
            completed = db.query(func.count(Player.id)).filter(
                Player.game_completed == True
            ).scalar() or 0
            
            chapters = {}
            for (chapter,) in db.query(Player.chapter).all():
                if chapter:
                    chapters[chapter] = chapters.get(chapter, 0) + 1
            
            choices = {"believe": 0, "doubt": 0, "escape": 0, "sacrifice": 0, "fight": 0}
            for (c,) in db.query(Player.choices).filter(Player.choices != None).all():
                if c:
                    if isinstance(c, str):
                        try:
                            c = json.loads(c)
                        except:
                            continue
                    if c.get("believe_aria") == "believe":
                        choices["believe"] += 1
                    elif c.get("believe_aria") == "doubt":
                        choices["doubt"] += 1
                    final = c.get("final_choice")
                    if final in choices:
                        choices[final] += 1
            
            rate = round(completed / total_players * 100, 1) if total_players > 0 else 0
            
            chapter_lines = ""
            for ch, count in sorted(chapters.items()):
                bar = "█" * min(count, 20)
                chapter_lines += f"    {ch:15} {bar} {count}\n"
            
            output = f"""
╔══════════════════════════════════════════════════════════════════╗
║                    STATISTIQUES GLOBALES                         ║
╠══════════════════════════════════════════════════════════════════╣
║                                                                  ║
║  CONNEXIONS                                                      ║
║  ────────────────────────────────────────                        ║
║    Total connexions   : {total_connections:>6}                                   ║
║    Connexions (24h)   : {connections_24h:>6}                                   ║
║    Connexions (7j)    : {connections_7d:>6}                                   ║
║                                                                  ║
║  CONVERSION                                                      ║
║  ────────────────────────────────────────                        ║
║    Comptes crees      : {converted_connections:>6}                                   ║
║    Taux conversion    : {conversion_rate:>5}%                                   ║
║                                                                  ║
║  JOUEURS                                                         ║
║  ────────────────────────────────────────                        ║
║    Total inscrits     : {total_players:>6}                                   ║
║    En ligne           : {online_count:>6}                                   ║
║    Actifs (24h)       : {active_24h:>6}                                   ║
║    Actifs (7j)        : {active_7d:>6}                                   ║
║                                                                  ║
║  PROGRESSION                                                     ║
║  ────────────────────────────────────────                        ║
║    Jeux completes     : {completed:>6}                                   ║
║    Taux completion    : {rate:>5}%                                   ║
║                                                                  ║
║  REPARTITION PAR CHAPITRE                                        ║
║  ────────────────────────────────────────                        ║
{chapter_lines}║                                                                  ║
║  CHOIX DES JOUEURS                                               ║
║  ────────────────────────────────────────                        ║
║    BELIEVE            : {choices['believe']:>6}                                   ║
║    DOUBT              : {choices['doubt']:>6}                                   ║
║                                                                  ║
║  FINS ATTEINTES                                                  ║
║  ────────────────────────────────────────                        ║
║    ESCAPE             : {choices['escape']:>6}                                   ║
║    SACRIFICE          : {choices['sacrifice']:>6}                                   ║
║    FIGHT              : {choices['fight']:>6}                                   ║
║                                                                  ║
╚══════════════════════════════════════════════════════════════════╝
"""
            return {"response": output, "status": "success"}
        finally:
            db.close()


class AdminOnlineCommand(BaseCommand):
    def execute(self, args: str) -> Dict[str, Any]:
        if not self.session.get("admin_mode"):
            return {"response": "Access denied.", "status": "error"}
        
        online = get_online_sessions()
        
        if not online:
            output = """
╔══════════════════════════════════════════════════════════════════╗
║                    JOUEURS EN LIGNE                              ║
╠══════════════════════════════════════════════════════════════════╣
║                                                                  ║
║    Aucun joueur en ligne actuellement.                           ║
║                                                                  ║
╚══════════════════════════════════════════════════════════════════╝
"""
        else:
            player_lines = ""
            for p in online:
                status = "[ADMIN]" if p.get("admin_mode") else ""
                player_lines += f"║    {p['username']:15} Lvl {p['level']:>2}  {p['chapter']:15} {status:8} ║\n"
            
            output = f"""
╔══════════════════════════════════════════════════════════════════╗
║                    JOUEURS EN LIGNE ({len(online)})                           ║
╠══════════════════════════════════════════════════════════════════╣
║                                                                  ║
║    USERNAME         LVL  CHAPITRE                                ║
║    ─────────────────────────────────────────────────────         ║
{player_lines}║                                                                  ║
╚══════════════════════════════════════════════════════════════════╝
"""
        return {"response": output, "status": "success"}


class AdminListCommand(BaseCommand):
    def execute(self, args: str) -> Dict[str, Any]:
        if not self.session.get("admin_mode"):
            return {"response": "Access denied.", "status": "error"}
        
        db = SessionLocal()
        try:
            players = db.query(Player).order_by(Player.last_login.desc()).limit(20).all()
            
            online_usernames = {s.get("username") for s in get_online_sessions()}
            
            player_lines = ""
            for p in players:
                status = "●" if p.username in online_usernames else "○"
                completed = "✓" if p.game_completed else " "
                last = p.last_login.strftime("%d/%m %H:%M") if p.last_login else "N/A"
                player_lines += f"║  {status} {p.username:15} Lvl {p.level:>2}  {p.chapter:12} {completed}  {last:12} ║\n"
            
            output = f"""
╔══════════════════════════════════════════════════════════════════╗
║                    LISTE DES JOUEURS                             ║
╠══════════════════════════════════════════════════════════════════╣
║                                                                  ║
║     USERNAME         LVL  CHAPITRE     FIN  DERNIERE CONN.       ║
║  ────────────────────────────────────────────────────────────    ║
{player_lines}║                                                                  ║
║  ● En ligne   ○ Hors ligne   ✓ Jeu complete                      ║
║                                                                  ║
║  Tapez VIEW <username> pour voir les details d'un joueur.        ║
║                                                                  ║
╚══════════════════════════════════════════════════════════════════╝
"""
            return {"response": output, "status": "success"}
        finally:
            db.close()


class AdminViewCommand(BaseCommand):
    def execute(self, args: str) -> Dict[str, Any]:
        if not self.session.get("admin_mode"):
            return {"response": "Access denied.", "status": "error"}
        
        if not args:
            return {"response": "Usage: VIEW <username>", "status": "error"}
        
        target_username = args.strip()
        
        db = SessionLocal()
        try:
            player = db.query(Player).filter(Player.username == target_username).first()
            
            if not player:
                return {"response": f"Joueur '{target_username}' non trouve.", "status": "error"}
            
            online_sessions = get_online_sessions()
            is_online = any(s.get("username") == target_username for s in online_sessions)
            status = "● EN LIGNE" if is_online else "○ HORS LIGNE"
            
            created = player.created_at.strftime("%d/%m/%Y %H:%M") if player.created_at else "N/A"
            last_login = player.last_login.strftime("%d/%m/%Y %H:%M") if player.last_login else "N/A"
            
            choices = player.choices if player.choices else {}
            if isinstance(choices, str):
                try:
                    choices = json.loads(choices)
                except:
                    choices = {}
            
            believe_choice = choices.get("believe_aria", "N/A")
            final_choice = choices.get("final_choice", "N/A")
            
            files_count = len(player.accessed_files) if player.accessed_files else 0
            puzzles_count = len(player.solved_puzzles) if player.solved_puzzles else 0
            secrets_count = len(player.discovered_secrets) if player.discovered_secrets else 0
            
            unlocked = ", ".join(player.unlocked_commands[:5]) if player.unlocked_commands else "Aucune"
            if player.unlocked_commands and len(player.unlocked_commands) > 5:
                unlocked += f" (+{len(player.unlocked_commands) - 5})"
            
            output = f"""
╔══════════════════════════════════════════════════════════════════╗
║                    PROFIL JOUEUR                                 ║
╠══════════════════════════════════════════════════════════════════╣
║                                                                  ║
║  {player.username:20}                      {status:>15}        ║
║                                                                  ║
║  INFORMATIONS                                                    ║
║  ────────────────────────────────────────                        ║
║    ID                 : {player.id:<6}                                   ║
║    Inscription        : {created:20}                      ║
║    Derniere connexion : {last_login:20}                      ║
║    Langue             : {player.language:5}                                    ║
║                                                                  ║
║  PROGRESSION                                                     ║
║  ────────────────────────────────────────                        ║
║    Niveau             : {player.level:<6}                                   ║
║    Chapitre           : {player.chapter:15}                          ║
║    Jeu complete       : {'Oui' if player.game_completed else 'Non':5}                                    ║
║    Fin obtenue        : {player.ending if player.ending else 'N/A':15}                          ║
║                                                                  ║
║  STATISTIQUES                                                    ║
║  ────────────────────────────────────────                        ║
║    Commandes          : {player.total_commands:<6}                                   ║
║    Confiance ARIA     : {player.aria_trust:<3}/100                                  ║
║    Fichiers accedes   : {files_count:<6}                                   ║
║    Puzzles resolus    : {puzzles_count:<6}                                   ║
║    Secrets decouverts : {secrets_count:<6}                                   ║
║                                                                  ║
║  CHOIX NARRATIFS                                                 ║
║  ────────────────────────────────────────                        ║
║    Croire ARIA        : {believe_choice:15}                          ║
║    Choix final        : {final_choice:15}                          ║
║                                                                  ║
║  COMMANDES DEBLOQUEES                                            ║
║  ────────────────────────────────────────                        ║
║    {unlocked:60} ║
║                                                                  ║
╚══════════════════════════════════════════════════════════════════╝
"""
            return {"response": output, "status": "success"}
        finally:
            db.close()


class AdminExitCommand(BaseCommand):
    def execute(self, args: str) -> Dict[str, Any]:
        if self.session.get("admin_mode"):
            self.session["admin_mode"] = False
            
            output = """
╔══════════════════════════════════════════════════════════════════╗
║                                                                  ║
║    Deconnexion du terminal administrateur...                     ║
║                                                                  ║
║    Retour au mode utilisateur normal.                            ║
║                                                                  ║
╚══════════════════════════════════════════════════════════════════╝
"""
            return {"response": output, "status": "success", "admin_exit": True}
        
        return {"response": "Vous n'etes pas en mode admin.", "status": "error"}

