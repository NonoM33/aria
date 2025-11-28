"""
SSH Server for SYSTEM_VOID
Allows real SSH connections to play the game via terminal
Supports both game commands and real terminal commands
"""
import asyncio
import asyncssh
import sys
import os
import subprocess
import shlex
from typing import Optional
from sqlalchemy.orm import Session

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from database import SessionLocal
from auth.player_service import authenticate_player, get_player_by_username
from commands.command_handler import handle_command, COMMAND_MAP
from services.session_service import get_session
from config import DEFAULT_LANGUAGE
from adventures.adventure_loader import get_chapter_filesystem


class SystemVoidSSHServerSession(asyncssh.SSHServerSession):
    def __init__(self, username: str, db: Session):
        self.username = username
        self.db = db
        self.session_id = f"ssh_{username}_{id(self)}"
        self.lang = DEFAULT_LANGUAGE
        self.session = None
        self.connected = True
        self.current_line = ""
        
    def connection_made(self, chan):
        self._chan = chan
        
    def shell_requested(self):
        return True
        
    def session_started(self):
        self.session = get_session(self.session_id, self.lang, self.db, self.username, None)
        
        welcome_msg = f"""╔════════════════════════════════════════════════════════════════════╗
║                    SYSTEM_VOID v2.0                                ║
╠════════════════════════════════════════════════════════════════════╣
║                                                                    ║
║  Bienvenue, {self.username}                                        ║
║                                                                    ║
║  Connexion SSH établie. Tapez HELP pour commencer.                 ║
║                                                                    ║
╚════════════════════════════════════════════════════════════════════╝

"""
        self._chan.write(welcome_msg)
        current_path = self.session.get("current_path", "/")
        self._chan.write(f"{self.username}@system-void:{current_path}$ ")
        
    def _is_game_command(self, command: str) -> bool:
        """Check if command is a game command"""
        game_commands = [
            "HELP", "STATUS", "LOGIN", "SCAN", "ACCESS", "CAT", "DECODE",
            "ACTIVATE", "NETWORK", "ANALYZE", "BYPASS", "CONNECT", "RESTORE",
            "SOLVE", "MAN", "SSH", "EXPLOIT", "CREATE_USER", "PKG", "EXIT",
            "LS", "TALK", "ARIA", "CD", "PWD", "ALIAS", "EDIT", "CLEAR"
        ]
        return command.upper() in game_commands
    
    def _get_autocomplete_suggestions(self, line: str) -> list:
        """Get autocomplete suggestions for the current line"""
        if not self.session:
            self.session = get_session(self.session_id, self.lang, self.db, self.username, None)
        
        parts = line.split()
        if not parts:
            return []
        
        command = parts[0]  # Keep original case for matching
        command_upper = command.upper()
        arg = parts[1] if len(parts) > 1 else ""
        
        # Command autocomplete
        if len(parts) == 1:
            all_commands = list(COMMAND_MAP.keys())
            all_commands.extend(["ls", "cat", "pwd", "whoami", "date", "echo", "clear", "history", "env", "uname"])
            suggestions = [cmd for cmd in all_commands if cmd.lower().startswith(command.lower())]
            return suggestions
        
        # File/directory autocomplete for game commands
        if command_upper in ["ACCESS", "CAT", "CD", "LS"] or command.lower() in ["cat", "cd", "ls"]:
            chapter_id = self.session.get("chapter", "chapter_0")
            filesystem = get_chapter_filesystem(chapter_id, self.lang) or {}
            current_path = self.session.get("current_path", "/")
            
            if arg.startswith("/"):
                target_path = arg
            else:
                if current_path == "/":
                    target_path = "/" + arg
                else:
                    target_path = current_path + "/" + arg
            
            target_path = target_path.replace("//", "/")
            dir_path = "/".join(target_path.split("/")[:-1]) or "/"
            prefix = target_path.split("/")[-1] if "/" in target_path else target_path
            
            # Get directory contents
            parts_path = dir_path.strip("/").split("/")
            current = filesystem
            for part in parts_path:
                if part and isinstance(current, dict) and part in current:
                    current = current[part]
                elif not part:
                    current = filesystem
                else:
                    return []
            
            if not isinstance(current, dict):
                return []
            
            suggestions = []
            for name in current.keys():
                if name.lower().startswith(prefix.lower()):
                    if isinstance(current[name], dict):
                        suggestions.append(name + "/")
                    else:
                        suggestions.append(name)
            
            return suggestions
        
        return []
    
    def _execute_system_command(self, command_line: str) -> str:
        """Execute a real system command in a safe environment"""
        try:
            parts = shlex.split(command_line)
            if not parts:
                return ""
            
            cmd = parts[0]
            args = parts[1:] if len(parts) > 1 else []
            
            # Whitelist of safe commands
            safe_commands = {
                "ls": ["ls", "-la"],
                "cat": ["cat"],
                "pwd": ["pwd"],
                "whoami": ["whoami"],
                "date": ["date"],
                "echo": ["echo"],
                "clear": ["clear"],
                "history": ["history"],
                "env": ["env"],
                "uname": ["uname", "-a"],
            }
            
            if cmd in safe_commands:
                safe_cmd = safe_commands[cmd]
                if args:
                    safe_cmd.extend(args)
                
                result = subprocess.run(
                    safe_cmd,
                    capture_output=True,
                    text=True,
                    timeout=5,
                    cwd=os.path.expanduser("~")
                )
                
                if result.returncode == 0:
                    return result.stdout
                else:
                    return result.stderr or f"Command failed with exit code {result.returncode}"
            else:
                return f"Command '{cmd}' not available in restricted environment.\nUse game commands (HELP to see list)."
                
        except subprocess.TimeoutExpired:
            return "Command timed out."
        except Exception as e:
            return f"Error executing command: {str(e)}"
    
    def data_received(self, data, datatype):
        if not self.connected:
            return
            
        try:
            if isinstance(data, bytes):
                command_line = data.decode('utf-8', errors='ignore').strip()
            else:
                command_line = str(data).strip()
            
            if not command_line:
                current_path = self.session.get("current_path", "/") if self.session else "/"
                self._chan.write(f"\r\n{self.username}@system-void:{current_path}$ ")
                return
            
            if command_line.upper() in ["EXIT", "QUIT"]:
                self.connected = False
                self._chan.write("\r\nDéconnexion réussie. Au revoir!\r\n")
                self._chan.exit(0)
                return
            
            # Process command
            self._process_command(command_line)
            
        except Exception as e:
            import traceback
            error_msg = str(e)
            self._chan.write(f"\r\nErreur: {error_msg}\r\n")
            current_path = self.session.get("current_path", "/") if self.session else "/"
            self._chan.write(f"{self.username}@system-void:{current_path}$ ")
    
    def _process_command(self, command_line: str):
        """Process a complete command line"""
        try:
            parts = command_line.split(" ", 1)
            command = parts[0] if parts else ""
            args = parts[1] if len(parts) > 1 else ""
            command_upper = command.upper()
            
            if not self.session:
                self.session = get_session(self.session_id, self.lang, self.db, self.username, None)
            
            # Check if it's a game command or system command
            if self._is_game_command(command_upper):
                # Game command - always use uppercase
                result = handle_command(command_upper, args, self.session, self.db, self.lang, None)
                response = result.get("response", "")
                if response:
                    self._chan.write(f"\r\n{response}\r\n")
            else:
                # Try system command (case-sensitive for system commands)
                system_output = self._execute_system_command(command_line)
                if system_output:
                    self._chan.write(f"\r\n{system_output}\r\n")
            
            current_path = self.session.get("current_path", "/")
            self._chan.write(f"{self.username}@system-void:{current_path}$ ")
            
        except Exception as e:
            import traceback
            error_msg = str(e)
            self._chan.write(f"\r\nErreur: {error_msg}\r\n")
            current_path = self.session.get("current_path", "/") if self.session else "/"
            self._chan.write(f"{self.username}@system-void:{current_path}$ ")


class SystemVoidSSHServer(asyncssh.SSHServer):
    def __init__(self):
        self.db = SessionLocal()
        self._username = None
        
    def connection_made(self, conn):
        self._conn = conn
        
    def connection_lost(self, exc):
        if exc:
            print(f"SSH connection error: {exc}")
        if hasattr(self, 'db'):
            try:
                self.db.close()
            except:
                pass
    
    def password_auth_supported(self):
        return True
    
    def validate_password(self, username: str, password: str) -> bool:
        try:
            player = authenticate_player(self.db, username, password)
            if player:
                self._username = username
                return True
        except:
            pass
        return False
    
    def session_requested(self):
        username = self._username or self._conn.get_extra_info('username', 'guest')
        return SystemVoidSSHServerSession(username, self.db)


async def start_ssh_server(host: str = '0.0.0.0', port: int = 2222):
    """Start the SSH server"""
    try:
        server = await asyncssh.create_server(
            SystemVoidSSHServer,
            host,
            port,
            server_host_keys=['ssh_host_key'],
            process_factory=None
        )
        
        print(f"╔════════════════════════════════════════════════════════════════════╗")
        print(f"║                    SYSTEM_VOID SSH SERVER                          ║")
        print(f"╠════════════════════════════════════════════════════════════════════╣")
        print(f"║                                                                    ║")
        print(f"║  Serveur SSH démarré sur {host}:{port}                            ║")
        print(f"║                                                                    ║")
        print(f"║  Connectez-vous avec:                                             ║")
        print(f"║    ssh <username>@localhost -p {port}                             ║")
        print(f"║                                                                    ║")
        print(f"║  Ou depuis un autre ordinateur:                                    ║")
        print(f"║    ssh <username>@<ip_serveur> -p {port}                           ║")
        print(f"║                                                                    ║")
        print(f"╚════════════════════════════════════════════════════════════════════╝")
        print()
        
        await server.wait_closed()
    except Exception as e:
        print(f"Erreur lors du démarrage du serveur SSH: {e}")
        print("Assurez-vous d'avoir généré une clé SSH avec:")
        print("  ssh-keygen -t rsa -f ssh_host_key -N ''")


if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description='SYSTEM_VOID SSH Server')
    parser.add_argument('--host', default='0.0.0.0', help='Host to bind to (default: 0.0.0.0)')
    parser.add_argument('--port', type=int, default=2222, help='Port to listen on (default: 2222)')
    
    args = parser.parse_args()
    
    try:
        asyncio.run(start_ssh_server(args.host, args.port))
    except KeyboardInterrupt:
        print("\nArrêt du serveur SSH...")
    except Exception as e:
        print(f"Erreur: {e}")

