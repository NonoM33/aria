from typing import Dict, Any
from commands.base_command import BaseCommand


class AliasCommand(BaseCommand):
    def execute(self, args: str) -> Dict[str, Any]:
        if not args or args.strip() == "":
            return self._list_aliases()
        
        args = args.strip()
        parts = args.split(" ", 1)
        subcommand = parts[0].upper()
        
        if subcommand in ["LIST", "LS", "SHOW"]:
            return self._list_aliases()
        elif subcommand in ["CREATE", "ADD", "SET"]:
            if len(parts) < 2:
                if self.lang == "FR":
                    return {"response": "Usage: ALIAS CREATE <alias>=<commande>\nExemple: ALIAS CREATE l=ls", "status": "error"}
                else:
                    return {"response": "Usage: ALIAS CREATE <alias>=<command>\nExample: ALIAS CREATE l=ls", "status": "error"}
            return self._create_alias(parts[1])
        elif subcommand in ["REMOVE", "DELETE", "DEL", "RM"]:
            if len(parts) < 2:
                if self.lang == "FR":
                    return {"response": "Usage: ALIAS REMOVE <alias>", "status": "error"}
                else:
                    return {"response": "Usage: ALIAS REMOVE <alias>", "status": "error"}
            return self._remove_alias(parts[1])
        else:
            if "=" in args:
                return self._create_alias(args)
            else:
                if self.lang == "FR":
                    return {"response": "Usage: ALIAS [LIST|CREATE <alias>=<commande>|REMOVE <alias>]", "status": "error"}
                else:
                    return {"response": "Usage: ALIAS [LIST|CREATE <alias>=<command>|REMOVE <alias>]", "status": "error"}
    
    def _list_aliases(self) -> Dict[str, Any]:
        aliases = self.session.get("aliases", {})
        
        if not aliases:
            if self.lang == "FR":
                return {"response": "Aucun alias défini.\n\nUtilisez: ALIAS <alias>=<commande> pour créer un alias.\nExemple: ALIAS l=ls", "status": "info"}
            else:
                return {"response": "No aliases defined.\n\nUse: ALIAS <alias>=<command> to create an alias.\nExample: ALIAS l=ls", "status": "info"}
        
        lines = []
        if self.lang == "FR":
            lines.append("Alias définis:")
        else:
            lines.append("Defined aliases:")
        
        lines.append("")
        for alias, command in sorted(aliases.items()):
            lines.append(f"  {alias:<15} -> {command}")
        
        return {"response": "\n".join(lines), "status": "success"}
    
    def _create_alias(self, alias_def: str) -> Dict[str, Any]:
        if "=" not in alias_def:
            if self.lang == "FR":
                return {"response": "Format invalide. Utilisez: <alias>=<commande>\nExemple: ALIAS l=ls", "status": "error"}
            else:
                return {"response": "Invalid format. Use: <alias>=<command>\nExample: ALIAS l=ls", "status": "error"}
        
        parts = alias_def.split("=", 1)
        alias = parts[0].strip().upper()
        command = parts[1].strip()
        
        if not alias:
            if self.lang == "FR":
                return {"response": "Le nom de l'alias ne peut pas être vide.", "status": "error"}
            else:
                return {"response": "Alias name cannot be empty.", "status": "error"}
        
        if not command:
            if self.lang == "FR":
                return {"response": "La commande ne peut pas être vide.", "status": "error"}
            else:
                return {"response": "Command cannot be empty.", "status": "error"}
        
        if alias in ["ALIAS", "HELP", "EXIT"]:
            if self.lang == "FR":
                return {"response": f"Impossible de créer un alias pour '{alias}'. Cette commande est réservée.", "status": "error"}
            else:
                return {"response": f"Cannot create alias for '{alias}'. This command is reserved.", "status": "error"}
        
        aliases = self.session.setdefault("aliases", {})
        aliases[alias] = command
        
        if self.lang == "FR":
            return {"response": f"Alias '{alias}' créé: {alias} -> {command}", "status": "success"}
        else:
            return {"response": f"Alias '{alias}' created: {alias} -> {command}", "status": "success"}
    
    def _remove_alias(self, alias: str) -> Dict[str, Any]:
        alias = alias.strip().upper()
        aliases = self.session.get("aliases", {})
        
        if alias not in aliases:
            if self.lang == "FR":
                return {"response": f"Alias '{alias}' introuvable.", "status": "error"}
            else:
                return {"response": f"Alias '{alias}' not found.", "status": "error"}
        
        del aliases[alias]
        
        if self.lang == "FR":
            return {"response": f"Alias '{alias}' supprimé.", "status": "success"}
        else:
            return {"response": f"Alias '{alias}' removed.", "status": "success"}

