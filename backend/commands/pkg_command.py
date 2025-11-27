from typing import Dict, Any
from commands.base_command import BaseCommand

AVAILABLE_PACKAGES = {
    "file-viewer": {
        "name": "file-viewer",
        "description_fr": "Visualiseur de fichiers avancé avec interface style vim",
        "description_en": "Advanced file viewer with vim-like interface",
        "version": "1.0.0"
    }
}

class PkgCommand(BaseCommand):
    def execute(self, args: str) -> Dict[str, Any]:
        if not self.session.get("logged_in") or not self.session.get("player_id"):
            if self.lang == "FR":
                return {"response": "Acces refuse. Authentification requise.\n\nTrouvez un moyen d'obtenir un acces au systeme...", "status": "error"}
            else:
                return {"response": "Access denied. Authentication required.\n\nFind a way to gain access to the system...", "status": "error"}
        
        if not args:
            if self.lang == "FR":
                return {"response": """GESTIONNAIRE DE PACKAGES
======================

Commandes disponibles:
- PKG INSTALL <package> : Installer un package
- PKG UNINSTALL <package> : Désinstaller un package
- PKG LIST : Lister les packages installés

Packages disponibles:
- file-viewer : Visualiseur de fichiers avancé avec interface style vim

Visitez /wiki pour plus d'informations.""", "status": "info"}
            else:
                return {"response": """PACKAGE MANAGER
================

Available commands:
- PKG INSTALL <package> : Install a package
- PKG UNINSTALL <package> : Uninstall a package
- PKG LIST : List installed packages

Available packages:
- file-viewer : Advanced file viewer with vim-like interface

Visit /wiki for more information.""", "status": "info"}
        
        parts = args.split(" ", 1)
        subcommand = parts[0].upper() if parts else ""
        package_name = parts[1].strip() if len(parts) > 1 else ""
        
        if subcommand == "INSTALL":
            return self._install_package(package_name)
        elif subcommand == "UNINSTALL":
            return self._uninstall_package(package_name)
        elif subcommand == "LIST":
            return self._list_packages()
        else:
            if self.lang == "FR":
                return {"response": f"Commande inconnue: {subcommand}\n\nUtilisez PKG INSTALL, PKG UNINSTALL ou PKG LIST.", "status": "error"}
            else:
                return {"response": f"Unknown command: {subcommand}\n\nUse PKG INSTALL, PKG UNINSTALL or PKG LIST.", "status": "error"}
    
    def _install_package(self, package_name: str) -> Dict[str, Any]:
        if not package_name:
            if self.lang == "FR":
                return {"response": "Usage: PKG INSTALL <package>\nExemple: PKG INSTALL file-viewer", "status": "error"}
            else:
                return {"response": "Usage: PKG INSTALL <package>\nExample: PKG INSTALL file-viewer", "status": "error"}
        
        package_name = package_name.lower().strip()
        
        if package_name not in AVAILABLE_PACKAGES:
            if self.lang == "FR":
                return {"response": f"Package '{package_name}' introuvable.\n\nPackages disponibles: {', '.join(AVAILABLE_PACKAGES.keys())}", "status": "error"}
            else:
                return {"response": f"Package '{package_name}' not found.\n\nAvailable packages: {', '.join(AVAILABLE_PACKAGES.keys())}", "status": "error"}
        
        installed_packages = self.session.get("installed_packages", [])
        
        if package_name in installed_packages:
            if self.lang == "FR":
                return {"response": f"Le package '{package_name}' est déjà installé.", "status": "info"}
            else:
                return {"response": f"Package '{package_name}' is already installed.", "status": "info"}
        
        installed_packages.append(package_name)
        self.update_session({"installed_packages": installed_packages})
        
        package_info = AVAILABLE_PACKAGES[package_name]
        if self.lang == "FR":
            return {
                "response": f"""Package '{package_name}' installé avec succès!

{package_info['description_fr']}
Version: {package_info['version']}

Le package est maintenant actif.""",
                "status": "success"
            }
        else:
            return {
                "response": f"""Package '{package_name}' installed successfully!

{package_info['description_en']}
Version: {package_info['version']}

The package is now active.""",
                "status": "success"
            }
    
    def _uninstall_package(self, package_name: str) -> Dict[str, Any]:
        if not package_name:
            if self.lang == "FR":
                return {"response": "Usage: PKG UNINSTALL <package>\nExemple: PKG UNINSTALL file-viewer", "status": "error"}
            else:
                return {"response": "Usage: PKG UNINSTALL <package>\nExample: PKG UNINSTALL file-viewer", "status": "error"}
        
        package_name = package_name.lower().strip()
        installed_packages = self.session.get("installed_packages", [])
        
        if package_name not in installed_packages:
            if self.lang == "FR":
                return {"response": f"Le package '{package_name}' n'est pas installé.", "status": "error"}
            else:
                return {"response": f"Package '{package_name}' is not installed.", "status": "error"}
        
        installed_packages.remove(package_name)
        self.update_session({"installed_packages": installed_packages})
        
        if self.lang == "FR":
            return {"response": f"Package '{package_name}' désinstallé avec succès.", "status": "success"}
        else:
            return {"response": f"Package '{package_name}' uninstalled successfully.", "status": "success"}
    
    def _list_packages(self) -> Dict[str, Any]:
        installed_packages = self.session.get("installed_packages", [])
        
        if not installed_packages:
            if self.lang == "FR":
                return {"response": "Aucun package installé.\n\nUtilisez PKG INSTALL <package> pour installer un package.", "status": "info"}
            else:
                return {"response": "No packages installed.\n\nUse PKG INSTALL <package> to install a package.", "status": "info"}
        
        if self.lang == "FR":
            response = "PACKAGES INSTALLÉS:\n==================\n\n"
        else:
            response = "INSTALLED PACKAGES:\n==================\n\n"
        
        for pkg_name in installed_packages:
            if pkg_name in AVAILABLE_PACKAGES:
                pkg_info = AVAILABLE_PACKAGES[pkg_name]
                if self.lang == "FR":
                    response += f"- {pkg_name} (v{pkg_info['version']})\n  {pkg_info['description_fr']}\n\n"
                else:
                    response += f"- {pkg_name} (v{pkg_info['version']})\n  {pkg_info['description_en']}\n\n"
            else:
                response += f"- {pkg_name}\n\n"
        
        return {"response": response.strip(), "status": "success"}

