from typing import Dict, Any
from commands.base_command import BaseCommand
import re


DEFAULT_VOIDRC = """# ~/.voidrc - SYSTEM_VOID Configuration File
# 
# Aliases:
#   alias <name>=<command>
#   Example: alias l=ls
#
# Lines starting with # are comments

"""


class EditCommand(BaseCommand):
    def execute(self, args: str) -> Dict[str, Any]:
        if not self.session.get("logged_in"):
            if self.lang == "FR":
                return {"response": "Acces refuse. Authentification requise.", "status": "error"}
            else:
                return {"response": "Access denied. Authentication required.", "status": "error"}
        
        if not args or args.strip() == "":
            if self.lang == "FR":
                return {"response": "Usage: EDIT <fichier>\n\nFichiers editables:\n  .voidrc    Configuration et alias", "status": "info"}
            else:
                return {"response": "Usage: EDIT <file>\n\nEditable files:\n  .voidrc    Configuration and aliases", "status": "info"}
        
        parts = args.strip().split(" ", 1)
        filename = parts[0].lower()
        content_arg = parts[1] if len(parts) > 1 else None
        
        if filename in [".voidrc", "voidrc", "~/.voidrc"]:
            return self._handle_voidrc(content_arg)
        else:
            if self.lang == "FR":
                return {"response": f"Fichier '{filename}' non editable.\n\nFichiers editables: .voidrc", "status": "error"}
            else:
                return {"response": f"File '{filename}' is not editable.\n\nEditable files: .voidrc", "status": "error"}
    
    def _handle_voidrc(self, content_arg: str) -> Dict[str, Any]:
        current_content = self.session.get("voidrc", "")
        
        if not current_content:
            current_content = DEFAULT_VOIDRC
            self.session["voidrc"] = current_content
        
        if not content_arg:
            return {
                "response": current_content,
                "status": "success",
                "file_content": current_content,
                "filename": ".voidrc",
                "editable": True,
                "open_editor": True
            }
        
        subcommand = content_arg.split(" ", 1)[0].upper()
        
        if subcommand == "SAVE":
            new_content = content_arg[5:].strip() if len(content_arg) > 5 else ""
            return self._save_voidrc(new_content)
        elif subcommand == "ADD":
            line_to_add = content_arg[4:].strip() if len(content_arg) > 4 else ""
            if line_to_add:
                new_content = current_content.rstrip() + "\n" + line_to_add + "\n"
                return self._save_voidrc(new_content)
            else:
                if self.lang == "FR":
                    return {"response": "Usage: EDIT .voidrc ADD <ligne>", "status": "error"}
                else:
                    return {"response": "Usage: EDIT .voidrc ADD <line>", "status": "error"}
        elif subcommand == "CLEAR":
            return self._save_voidrc(DEFAULT_VOIDRC)
        elif subcommand == "RELOAD":
            return self._reload_aliases()
        else:
            if self.lang == "FR":
                return {"response": f"""Usage: EDIT .voidrc [SAVE|ADD|CLEAR|RELOAD]

Commandes:
  EDIT .voidrc              Afficher le contenu
  EDIT .voidrc ADD <ligne>  Ajouter une ligne
  EDIT .voidrc CLEAR        Reinitialiser le fichier
  EDIT .voidrc RELOAD       Recharger les alias

Exemple:
  EDIT .voidrc ADD alias l=ls""", "status": "info"}
            else:
                return {"response": f"""Usage: EDIT .voidrc [SAVE|ADD|CLEAR|RELOAD]

Commands:
  EDIT .voidrc              Display content
  EDIT .voidrc ADD <line>   Add a line
  EDIT .voidrc CLEAR        Reset file
  EDIT .voidrc RELOAD       Reload aliases

Example:
  EDIT .voidrc ADD alias l=ls""", "status": "info"}
    
    def _save_voidrc(self, content: str) -> Dict[str, Any]:
        self.session["voidrc"] = content
        
        aliases = self._parse_aliases(content)
        self.session["aliases"] = aliases
        
        if self.lang == "FR":
            alias_count = len(aliases)
            return {
                "response": f"Fichier .voidrc sauvegarde.\n{alias_count} alias charge(s).",
                "status": "success",
                "aliases_loaded": alias_count
            }
        else:
            alias_count = len(aliases)
            return {
                "response": f"File .voidrc saved.\n{alias_count} alias(es) loaded.",
                "status": "success",
                "aliases_loaded": alias_count
            }
    
    def _reload_aliases(self) -> Dict[str, Any]:
        content = self.session.get("voidrc", "")
        aliases = self._parse_aliases(content)
        self.session["aliases"] = aliases
        
        if self.lang == "FR":
            if aliases:
                alias_list = "\n".join([f"  {k} -> {v}" for k, v in aliases.items()])
                return {"response": f"Alias recharges:\n{alias_list}", "status": "success"}
            else:
                return {"response": "Aucun alias trouve dans .voidrc", "status": "info"}
        else:
            if aliases:
                alias_list = "\n".join([f"  {k} -> {v}" for k, v in aliases.items()])
                return {"response": f"Aliases reloaded:\n{alias_list}", "status": "success"}
            else:
                return {"response": "No aliases found in .voidrc", "status": "info"}
    
    def _parse_aliases(self, content: str) -> Dict[str, str]:
        aliases = {}
        
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

