from typing import Dict, Any
from commands.base_command import BaseCommand
from auth.ssh_auth import ssh_connect
from auth.player_service import get_player_by_id, player_to_session_dict
import re


def parse_voidrc_aliases(content: str) -> Dict[str, str]:
    aliases = {}
    if not content:
        return aliases
    
    for line in content.split("\n"):
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        
        alias_match = re.match(r'^alias\s+([a-zA-Z0-9_-]+)\s*=\s*(.+)$', line, re.IGNORECASE)
        if alias_match:
            alias_name = alias_match.group(1).upper()
            alias_command = alias_match.group(2).strip()
            
            if alias_command.startswith('"') and alias_command.endswith('"'):
                alias_command = alias_command[1:-1]
            elif alias_command.startswith("'") and alias_command.endswith("'"):
                alias_command = alias_command[1:-1]
            
            if alias_name not in ["ALIAS", "HELP", "EXIT", "EDIT"]:
                aliases[alias_name] = alias_command
    
    return aliases


class SshCommand(BaseCommand):
    def execute(self, args: str) -> Dict[str, Any]:
        if not args:
            if self.lang == "FR":
                return {"response": "Usage: ssh <username>@system-void.local\nExemple: ssh hacker@system-void.local\n\nLe mot de passe vous sera demandé après.", "status": "info"}
            else:
                return {"response": "Usage: ssh <username>@system-void.local\nExample: ssh hacker@system-void.local\n\nPassword will be prompted after.", "status": "info"}
        
        parts = args.split("@")
        if len(parts) != 2 or parts[1].strip() not in ["system-void.local", "localhost"]:
            if self.lang == "FR":
                return {"response": "Format invalide. Utilisez: ssh <username>@system-void.local", "status": "error"}
            else:
                return {"response": "Invalid format. Use: ssh <username>@system-void.local", "status": "error"}
        
        username = parts[0].strip()
        
        if not username:
            if self.lang == "FR":
                return {"response": "Nom d'utilisateur requis.", "status": "error"}
            else:
                return {"response": "Username required.", "status": "error"}
        
        if not self.db:
            if self.lang == "FR":
                return {"response": "Base de données non disponible.", "status": "error"}
            else:
                return {"response": "Database not available.", "status": "error"}
        
        token = None
        if hasattr(self, 'token') and self.token:
            token = self.token
        elif self.session.get("ssh_token"):
            token = self.session.get("ssh_token")
        
        if token:
            try:
                result = ssh_connect(self.db, username, None, token)
                if result.get("success"):
                    new_token = result.get("token")
                    self.update_session({
                        "username": result["username"],
                        "player_id": result.get("player_id"),
                        "logged_in": True,
                        "ssh_token": new_token,
                        "chapter": "act_1",
                        "level": 1,
                        "current_path": "/"
                    })
                    self.add_unlocked_command("SCAN")
                    self.add_unlocked_command("DECODE")
                    self.add_unlocked_command("ACCESS")
                    
                    if self.lang == "FR":
                        return {
                            "response": f"Connexion SSH etablie avec {username}@system-void.local\n\nBienvenue, {username}!\n\nAcces niveau 1 obtenu.\nNouvelles commandes: SCAN, DECODE, ACCESS\n\nTapez LS pour explorer.",
                            "status": "success",
                            "token": new_token,
                            "username": result["username"]
                        }
                    else:
                        return {
                            "response": f"SSH connection established with {username}@system-void.local\n\nWelcome, {username}!\n\nLevel 1 access granted.\nNew commands: SCAN, DECODE, ACCESS\n\nType LS to explore.",
                            "status": "success",
                            "token": new_token,
                            "username": result["username"]
                        }
            except Exception:
                pass
        
        self.session["ssh_pending_username"] = username
        
        if self.lang == "FR":
            return {
                "response": f"{username}@system-void.local's password: ",
                "status": "password_prompt",
                "password_prompt": True,
                "username": username
            }
        else:
            return {
                "response": f"{username}@system-void.local's password: ",
                "status": "password_prompt",
                "password_prompt": True,
                "username": username
            }
    
    def execute_password(self, password: str) -> Dict[str, Any]:
        username = self.session.get("ssh_pending_username")
        if not username:
            if self.lang == "FR":
                return {"response": "Aucune connexion SSH en attente.", "status": "error"}
            else:
                return {"response": "No pending SSH connection.", "status": "error"}
        
        if not self.db:
            if self.lang == "FR":
                return {"response": "Base de données non disponible.", "status": "error"}
            else:
                return {"response": "Database not available.", "status": "error"}
        
        try:
            result = ssh_connect(self.db, username, password, None)
            
            if result.get("success"):
                new_token = result.get("token")
                self.update_session({
                    "username": result["username"],
                    "player_id": result.get("player_id"),
                    "logged_in": True,
                    "ssh_token": new_token,
                    "chapter": "act_1",
                    "level": 1,
                    "current_path": "/"
                })
                self.add_unlocked_command("SCAN")
                self.add_unlocked_command("DECODE")
                self.add_unlocked_command("ACCESS")
                if "ssh_pending_username" in self.session:
                    del self.session["ssh_pending_username"]
                
                if self.lang == "FR":
                    return {
                        "response": f"\nConnexion SSH etablie avec {username}@system-void.local\n\nBienvenue, {username}!\n\nAcces niveau 1 obtenu.\nNouvelles commandes: SCAN, DECODE, ACCESS\n\nTapez LS pour explorer.",
                        "status": "success",
                        "token": new_token,
                        "username": result["username"]
                    }
                else:
                    return {
                        "response": f"\nSSH connection established with {username}@system-void.local\n\nWelcome, {username}!\n\nLevel 1 access granted.\nNew commands: SCAN, DECODE, ACCESS\n\nType LS to explore.",
                        "status": "success",
                        "token": new_token,
                        "username": result["username"]
                    }
            else:
                if "ssh_pending_username" in self.session:
                    del self.session["ssh_pending_username"]
                if self.lang == "FR":
                    return {"response": f"\nÉchec de la connexion SSH: {result.get('message', 'Identifiants invalides')}", "status": "error"}
                else:
                    return {"response": f"\nSSH connection failed: {result.get('message', 'Invalid credentials')}", "status": "error"}
        except Exception as e:
            if "ssh_pending_username" in self.session:
                del self.session["ssh_pending_username"]
            if self.lang == "FR":
                return {"response": f"\nErreur lors de la connexion SSH: {str(e)}", "status": "error"}
            else:
                return {"response": f"\nSSH connection error: {str(e)}", "status": "error"}

