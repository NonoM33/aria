MAN_PAGES = {
    "FR": {
        "HELP": """HELP(1)                    Manuel SYSTEM_VOID                  HELP(1)

NOM
    HELP - Affiche la liste des commandes disponibles

SYNOPSIS
    HELP

DESCRIPTION
    Affiche toutes les commandes disponibles selon votre niveau d'accès.

EXEMPLES
    > HELP
    Commands available: HELP, STATUS, LOGIN, SCAN, DECODE, ACCESS

VOIR AUSSI
    STATUS(1), LOGIN(1), MAN(1)""",

        "STATUS": """STATUS(1)                 Manuel SYSTEM_VOID                STATUS(1)

NOM
    STATUS - Affiche l'état du système

SYNOPSIS
    STATUS

DESCRIPTION
    Affiche l'intégrité du système, le niveau de sécurité et votre niveau d'accès.

EXEMPLES
    > STATUS
    Intégrité du système: 49%
    Niveau de sécurité: CRITIQUE
    Niveau d'accès: 1

VOIR AUSSI
    HELP(1)""",

        "LOGIN": """LOGIN(1)                  Manuel SYSTEM_VOID                 LOGIN(1)

NOM
    LOGIN - Se connecter au système

SYNOPSIS
    LOGIN <clé>

DESCRIPTION
    Permet de se connecter au système avec une clé d'encryption.

ARGUMENTS
    <clé>    La clé d'encryption (format: VOID + année)

EXEMPLES
    > LOGIN VOID2024
    Access granted. Level 1 unlocked.

VOIR AUSSI
    STATUS(1), HELP(1)""",

        "SCAN": """SCAN(1)                   Manuel SYSTEM_VOID                  SCAN(1)

NOM
    SCAN - Scanner le système pour trouver des fichiers

SYNOPSIS
    SCAN

DESCRIPTION
    Scanne le système et liste tous les fichiers cachés disponibles.

EXEMPLES
    > SCAN
    Scanning system...
    
    Files detected:
    - corrupted_data.b64
    - protocol_xyz.txt
    - hint_sequence.txt

VOIR AUSSI
    ACCESS(1), DECODE(1)""",

        "ACCESS": """ACCESS(1)                Manuel SYSTEM_VOID                ACCESS(1)

NOM
    ACCESS - Accéder à un fichier

SYNOPSIS
    ACCESS <fichier>

DESCRIPTION
    Ouvre et affiche le contenu d'un fichier.

ARGUMENTS
    <fichier>    Le nom du fichier à ouvrir

EXEMPLES
    > ACCESS readme.txt
    File: readme.txt
    
    [Contenu du fichier]

VOIR AUSSI
    SCAN(1), NVIM(1)""",

        "DECODE": """DECODE(1)                Manuel SYSTEM_VOID                DECODE(1)

NOM
    DECODE - Décoder du texte en Base64

SYNOPSIS
    DECODE <texte_base64> ou DECODE <nom_fichier>

DESCRIPTION
    Décode une chaîne encodée en Base64 ou décode le contenu d'un fichier Base64.

ARGUMENTS
    <texte_base64>    Le texte encodé en Base64
    <nom_fichier>     Un fichier contenant du Base64 (ex: corrupted_data.b64)

EXEMPLES
    > DECODE SGVsbG8gV29ybGQ=
    Décodé: Hello World
    
    > DECODE corrupted_data.b64
    Fichier corrupted_data.b64 décodé:
    [Contenu décodé]

VOIR AUSSI
    ACCESS(1), SCAN(1)""",

        "ACTIVATE": """ACTIVATE(1)             Manuel SYSTEM_VOID             ACTIVATE(1)

NOM
    ACTIVATE - Activer un protocole système

SYNOPSIS
    ACTIVATE <nom_protocole>

DESCRIPTION
    Active un protocole système pour débloquer de nouveaux niveaux d'accès.

ARGUMENTS
    <nom_protocole>    Le nom du protocole à activer (ex: PROTOCOL_XYZ)

EXEMPLES
    > ACTIVATE PROTOCOL_XYZ
    Niveau 2 débloqué! Nouvelles commandes: NETWORK, ANALYZE, BYPASS

NOTES
    Le nom du protocole se trouve généralement dans les fichiers décodés.

VOIR AUSSI
    DECODE(1), NETWORK(1)""",

        "NETWORK": """NETWORK(1)              Manuel SYSTEM_VOID              NETWORK(1)

NOM
    NETWORK - Afficher la carte du réseau

SYNOPSIS
    NETWORK

DESCRIPTION
    Affiche la carte du réseau avec tous les serveurs détectés et leur statut.

EXEMPLES
    > NETWORK
    CARTE DU RÉSEAU
    ================
    
    Serveurs détectés:
    - SERVER_ALPHA (192.168.1.10) - Status: OFFLINE
    - SERVER_BETA (192.168.1.20) - Status: ONLINE
    - SERVER_GAMMA (192.168.1.30) - Status: LOCKED

VOIR AUSSI
    CONNECT(1), ANALYZE(1)""",

        "ANALYZE": """ANALYZE(1)              Manuel SYSTEM_VOID              ANALYZE(1)

NOM
    ANALYZE - Analyser un sujet spécifique

SYNOPSIS
    ANALYZE <sujet>

DESCRIPTION
    Analyse un sujet spécifique du système (sécurité, réseau, etc.)

ARGUMENTS
    <sujet>    Le sujet à analyser (ex: security, sécurité, network, réseau)

EXEMPLES
    > ANALYZE security
    Analyse de sécurité:
    [Logs de sécurité]

VOIR AUSSI
    NETWORK(1), BYPASS(1)""",

        "BYPASS": """BYPASS(1)               Manuel SYSTEM_VOID               BYPASS(1)

NOM
    BYPASS - Contourner un système de sécurité

SYNOPSIS
    BYPASS <code>

DESCRIPTION
    Contourne un système de sécurité en utilisant un code spécifique.

ARGUMENTS
    <code>    Le code de contournement (généralement trouvé dans une énigme)

EXEMPLES
    > BYPASS 15
    Code correct!
    Niveau 3 débloqué!

NOTES
    Le code est généralement la solution d'une énigme (ex: carré magique).

VOIR AUSSI
    ANALYZE(1), CONNECT(1)""",

        "CONNECT": """CONNECT(1)             Manuel SYSTEM_VOID             CONNECT(1)

NOM
    CONNECT - Se connecter à un serveur

SYNOPSIS
    CONNECT <serveur> <mot_de_passe>

DESCRIPTION
    Se connecte à un serveur distant avec un mot de passe.

ARGUMENTS
    <serveur>        Le nom du serveur (ex: SERVER_GAMMA)
    <mot_de_passe>   Le mot de passe du serveur

EXEMPLES
    > CONNECT SERVER_GAMMA DIOV
    Serveur GAMMA connecté!
    Niveau 4 débloqué!

VOIR AUSSI
    NETWORK(1), RESTORE(1)""",

        "RESTORE": """RESTORE(1)             Manuel SYSTEM_VOID             RESTORE(1)

NOM
    RESTORE - Restaurer le système

SYNOPSIS
    RESTORE <code>

DESCRIPTION
    Restaure le système à 100% en utilisant un code de restauration.

ARGUMENTS
    <code>    Le code de restauration (généralement une somme)

EXEMPLES
    > RESTORE 55
    Code de restauration correct!
    Système restauré à 100%.

NOTES
    Le code est généralement une somme de nombres trouvés dans les fichiers.

VOIR AUSSI
    CONNECT(1), SOLVE(1)""",

        "SOLVE": """SOLVE(1)                Manuel SYSTEM_VOID                SOLVE(1)

NOM
    SOLVE - Résoudre l'énigme finale

SYNOPSIS
    SOLVE <réponse>

DESCRIPTION
    Résout l'énigme finale pour compléter l'aventure.

ARGUMENTS
    <réponse>    La réponse à l'énigme finale

EXEMPLES
    > SOLVE VOID
    FÉLICITATIONS!
    Vous avez complété la première partie de SYSTEM_VOID!

NOTES
    La réponse se trouve généralement dans les fichiers du chapitre final.

VOIR AUSSI
    RESTORE(1), ACCESS(1)""",

        "NVIM": """NVIM(1)                   Manuel SYSTEM_VOID                  NVIM(1)

NOM
    NVIM - Gestionnaire de fichiers avancé

SYNOPSIS
    NVIM [<fichier>]

DESCRIPTION
    Ouvre le gestionnaire de fichiers style Neovim pour naviguer et éditer
    les fichiers du système.

ARGUMENTS
    <fichier>    (Optionnel) Fichier à ouvrir directement

NAVIGATION
    h, j, k, l    Navigation (gauche, bas, haut, droite)
    i             Mode insertion
    ESC           Mode normal
    :q            Quitter
    :w            Sauvegarder
    /             Rechercher
    :e <fichier>  Ouvrir un fichier

EXEMPLES
    > NVIM
    [Ouvre le gestionnaire de fichiers]
    
    > NVIM config.enc
    [Ouvre config.enc dans l'éditeur]

VOIR AUSSI
    ACCESS(1), MAN(1)""",

        "MAN": """MAN(1)                    Manuel SYSTEM_VOID                   MAN(1)

NOM
    MAN - Afficher le manuel d'une commande

SYNOPSIS
    MAN <commande>

DESCRIPTION
    Affiche la page de manuel complète pour une commande donnée.

ARGUMENTS
    <commande>    Le nom de la commande

EXEMPLES
    > MAN HELP
    [Affiche le manuel de HELP]
    
    > MAN NVIM
    [Affiche le manuel de NVIM]

VOIR AUSSI
    HELP(1)""",

        "SPLIT": """SPLIT(1)                 Manuel SYSTEM_VOID                 SPLIT(1)

NOM
    SPLIT - Créer un terminal splité

SYNOPSIS
    SPLIT [horizontal|vertical]

DESCRIPTION
    Crée un nouveau terminal splité pour exécuter des tâches en parallèle.

ARGUMENTS
    horizontal    Crée un split horizontal
    vertical      Crée un split vertical (par défaut)

RACCOURCIS
    Ctrl+B puis %    Split vertical
    Ctrl+B puis guillemet    Split horizontal
    Ctrl+B puis flèches    Naviguer entre panneaux
    Ctrl+B puis x    Fermer le panneau actuel

EXEMPLES
    > SPLIT
    [Crée un split vertical]
    
    > SPLIT horizontal
    [Crée un split horizontal]

VOIR AUSSI
    JOBS(1), PORTSCAN(1)""",

        "PORTSCAN": """PORTSCAN(1)             Manuel SYSTEM_VOID              PORTSCAN(1)

NOM
    PORTSCAN - Scanner les ports d'un serveur

SYNOPSIS
    PORTSCAN <adresse_ip>

DESCRIPTION
    Scanne les ports ouverts d'un serveur et identifie les services.

ARGUMENTS
    <adresse_ip>    L'adresse IP du serveur à scanner

EXEMPLES
    > PORTSCAN 192.168.1.100
    Scanning 192.168.1.100...
    Port 22: OPEN (SSH)
    Port 80: OPEN (HTTP)
    Port 443: OPEN (HTTPS)
    
    Scan completed: 3 ports open

VOIR AUSSI
    BRUTEFORCE(1), NETWORK(1)""",

        "BRUTEFORCE": """BRUTEFORCE(1)          Manuel SYSTEM_VOID           BRUTEFORCE(1)

NOM
    BRUTEFORCE - Forcer un mot de passe par brute force

SYNOPSIS
    BRUTEFORCE <cible> <wordlist>

DESCRIPTION
    Lance une attaque par force brute sur une cible en utilisant une wordlist.

ARGUMENTS
    <cible>      La cible (utilisateur, serveur, etc.)
    <wordlist>   Le fichier contenant la liste de mots de passe

EXEMPLES
    > BRUTEFORCE admin wordlist.txt
    Brute forcing admin...
    Trying: admin... FAILED
    Trying: password... FAILED
    Trying: void2024... SUCCESS!
    
    Password found: void2024

VOIR AUSSI
    PORTSCAN(1), JOBS(1)""",

        "JOBS": """JOBS(1)                  Manuel SYSTEM_VOID                  JOBS(1)

NOM
    JOBS - Lister les tâches en cours

SYNOPSIS
    JOBS

DESCRIPTION
    Affiche toutes les tâches en cours d'exécution (scans, bruteforce, etc.)

EXEMPLES
    > JOBS
    [1] PORTSCAN 192.168.1.100 - 45% complete
    [2] BRUTEFORCE admin - Running...
    
    Total: 2 jobs active

VOIR AUSSI
    SPLIT(1), PORTSCAN(1)""",

        "SSH": """SSH(1)                   Manuel SYSTEM_VOID                  SSH(1)

NOM
    SSH - Se connecter au système via SSH

SYNOPSIS
    SSH <username>@system-void.local

DESCRIPTION
    Établit une connexion SSH sécurisée avec le système. Permet de s'authentifier
    avec un nom d'utilisateur et un mot de passe, ou avec un token d'accès.

ARGUMENTS
    <username>@system-void.local    Format requis pour la connexion SSH

NOTES
    Le mot de passe vous sera demandé après avoir entré la commande.
    Si vous possédez un token d'accès, la connexion sera automatique.

EXEMPLES
    > SSH hacker@system-void.local
    hacker@system-void.local's password: 
    
    Connexion SSH établie avec hacker@system-void.local
    Bienvenue, hacker!
    Accès niveau 1 obtenu.
    Nouvelles commandes: SCAN, DECODE, ACCESS

VOIR AUSSI
    CREATE_USER(1), EXPLOIT(1)""",

        "EXPLOIT": """EXPLOIT(1)               Manuel SYSTEM_VOID              EXPLOIT(1)

NOM
    EXPLOIT - Exploiter une vulnérabilité système

SYNOPSIS
    EXPLOIT <CVE>

DESCRIPTION
    Exploite une vulnérabilité de sécurité identifiée par un code CVE.
    Cette commande permet d'obtenir un accès non autorisé au système.

ARGUMENTS
    <CVE>    Le code CVE de la vulnérabilité à exploiter

NOTES
    Les codes CVE valides se trouvent généralement dans les fichiers du système.
    Un exploit réussi peut débloquer de nouvelles commandes.

EXEMPLES
    > EXPLOIT CVE-2024-DB-001
    Exploit CVE-2024-DB-001 exécuté avec succès!
    
    Vulnérabilité SQL détectée dans la base de données.
    Accès non autorisé obtenu.
    
    Vous pouvez maintenant créer un utilisateur avec:
    CREATE_USER <username> <password>

VOIR AUSSI
    CREATE_USER(1), ACCESS(1)""",

        "CREATE_USER": """CREATE_USER(1)          Manuel SYSTEM_VOID         CREATE_USER(1)

NOM
    CREATE_USER - Créer un compte utilisateur

SYNOPSIS
    CREATE_USER <username> <password>

DESCRIPTION
    Crée un nouveau compte utilisateur dans le système via une faille de sécurité.
    Nécessite qu'un exploit ait été exécuté avec succès au préalable.

ARGUMENTS
    <username>    Le nom d'utilisateur à créer
    <password>    Le mot de passe pour le compte

NOTES
    Cette commande n'est disponible qu'après avoir exploité une vulnérabilité
    (par exemple avec EXPLOIT CVE-2024-DB-001).

EXEMPLES
    > CREATE_USER hacker password123
    Utilisateur hacker créé avec succès!
    
    Compte SSH créé via exploit de base de données.
    Vous pouvez maintenant vous connecter avec:
    ssh hacker@system-void.local

VOIR AUSSI
    SSH(1), EXPLOIT(1)""",

        "PKG": """PKG(1)                   Manuel SYSTEM_VOID                  PKG(1)

NOM
    PKG - Gestionnaire de packages

SYNOPSIS
    PKG [INSTALL|UNINSTALL|LIST] [<package>]

DESCRIPTION
    Gère l'installation et la désinstallation de packages système.
    Permet d'étendre les fonctionnalités du système avec des outils supplémentaires.

SOUS-COMMANDES
    INSTALL <package>      Installe un package
    UNINSTALL <package>     Désinstalle un package
    LIST                    Liste les packages installés

ARGUMENTS
    <package>    Le nom du package à installer ou désinstaller

EXEMPLES
    > PKG LIST
    Aucun package installé.
    
    > PKG INSTALL file-viewer
    Package 'file-viewer' installé avec succès!
    
    > PKG LIST
    PACKAGES INSTALLÉS:
    - file-viewer (v1.0.0)
      Visualiseur de fichiers avancé avec interface style vim

VOIR AUSSI
    ACCESS(1), MAN(1)""",

        "EXIT": """EXIT(1)                  Manuel SYSTEM_VOID                 EXIT(1)

NOM
    EXIT - Se déconnecter du système

SYNOPSIS
    EXIT

DESCRIPTION
    Ferme la session utilisateur actuelle et se déconnecte du système.
    Nécessite d'être connecté pour fonctionner.

EXEMPLES
    > EXIT
    Déconnexion réussie. Au revoir, hacker!

VOIR AUSSI
    SSH(1), STATUS(1)""",

        "LS": """LS(1)                    Manuel SYSTEM_VOID                   LS(1)

NOM
    LS - Lister le contenu d'un répertoire

SYNOPSIS
    LS [<répertoire>]

DESCRIPTION
    Affiche le contenu du répertoire courant ou d'un répertoire spécifié.
    Les répertoires sont marqués avec [DIR] et un slash (/).

ARGUMENTS
    <répertoire>    (Optionnel) Le chemin du répertoire à lister

EXEMPLES
    > LS
    [DIR]  system/
    [DIR]  home/
           readme.txt
    
    > LS system
    [DIR]  config/
           logs.txt

VOIR AUSSI
    CD(1), PWD(1), ACCESS(1)""",

        "TALK": """TALK(1)                 Manuel SYSTEM_VOID                  TALK(1)

NOM
    TALK - Parler avec ARIA

SYNOPSIS
    TALK [<message>]

DESCRIPTION
    Permet d'interagir avec ARIA, l'assistant IA du système. Les dialogues
    évoluent selon votre progression dans l'aventure et vos choix précédents.

ARGUMENTS
    <message>    (Optionnel) Message ou choix à envoyer à ARIA

NOTES
    Certains dialogues peuvent nécessiter des choix spécifiques (BELIEVE, DOUBT, etc.).
    Les réponses d'ARIA varient selon votre niveau de confiance et votre progression.

EXEMPLES
    > TALK
    [ARIA]
    Bonjour. Je suis ARIA. Comment puis-je vous aider?
    
    > TALK BELIEVE
    [ARIA]
    Je suis heureuse que vous me fassiez confiance...

VOIR AUSSI
    ARIA(1), STATUS(1)""",

        "ARIA": """ARIA(1)                 Manuel SYSTEM_VOID                  ARIA(1)

NOM
    ARIA - Alias pour la commande TALK

SYNOPSIS
    ARIA [<message>]

DESCRIPTION
    Alias de la commande TALK. Permet d'interagir avec ARIA de manière plus directe.

VOIR AUSSI
    TALK(1)""",

        "CD": """CD(1)                    Manuel SYSTEM_VOID                   CD(1)

NOM
    CD - Changer de répertoire

SYNOPSIS
    CD [<répertoire>]

DESCRIPTION
    Change le répertoire de travail courant. Sans argument, retourne à la racine (/).

ARGUMENTS
    <répertoire>    Le chemin du répertoire cible (relatif ou absolu)
    ..              Remonte d'un niveau dans l'arborescence
    .               Répertoire courant (aucun changement)

EXEMPLES
    > CD system
    /system
    
    > CD ..
    /
    
    > CD /system/config
    /system/config

VOIR AUSSI
    LS(1), PWD(1)""",

        "PWD": """PWD(1)                   Manuel SYSTEM_VOID                  PWD(1)

NOM
    PWD - Afficher le répertoire de travail courant

SYNOPSIS
    PWD

DESCRIPTION
    Affiche le chemin absolu du répertoire de travail courant.

EXEMPLES
    > PWD
    /
    
    > CD system/config
    > PWD
    /system/config

VOIR AUSSI
    CD(1), LS(1)""",

        "ALIAS": """ALIAS(1)                Manuel SYSTEM_VOID                 ALIAS(1)

NOM
    ALIAS - Gérer les alias de commandes

SYNOPSIS
    ALIAS [LIST|CREATE <alias>=<commande>|REMOVE <alias>]

DESCRIPTION
    Permet de créer, lister et supprimer des alias personnalisés pour les commandes.
    Les alias sont persistants et spécifiques à votre session.

SOUS-COMMANDES
    LIST                    Liste tous les alias définis
    CREATE <alias>=<cmd>    Crée un nouvel alias
    REMOVE <alias>          Supprime un alias

ARGUMENTS
    <alias>     Le nom de l'alias à créer ou supprimer
    <commande>  La commande à laquelle l'alias fait référence

NOTES
    Certaines commandes sont réservées et ne peuvent pas être remplacées par un alias
    (HELP, EXIT, ALIAS).

EXEMPLES
    > ALIAS CREATE l=ls
    Alias 'l' créé: l -> ls
    
    > ALIAS LIST
    Alias définis:
    
      l                -> ls
    
    > ALIAS REMOVE l
    Alias 'l' supprimé.

VOIR AUSSI
    HELP(1)""",

        "CAT": """CAT(1)                   Manuel SYSTEM_VOID                  CAT(1)

NOM
    CAT - Afficher le contenu d'un fichier

SYNOPSIS
    CAT <fichier>

DESCRIPTION
    Alias de la commande ACCESS. Affiche le contenu d'un fichier.

ARGUMENTS
    <fichier>    Le nom du fichier à afficher

VOIR AUSSI
    ACCESS(1)"""
    },
    "EN": {
        "HELP": """HELP(1)                    SYSTEM_VOID Manual                  HELP(1)

NAME
    HELP - Display available commands

SYNOPSIS
    HELP

DESCRIPTION
    Displays all available commands according to your access level.

EXAMPLES
    > HELP
    Commands available: HELP, STATUS, LOGIN, SCAN, DECODE, ACCESS

SEE ALSO
    STATUS(1), LOGIN(1), MAN(1)""",

        "STATUS": """STATUS(1)                 SYSTEM_VOID Manual                STATUS(1)

NAME
    STATUS - Display system status

SYNOPSIS
    STATUS

DESCRIPTION
    Displays system integrity, security level and your access level.

EXAMPLES
    > STATUS
    System Integrity: 49%
    Security Level: CRITICAL
    Access Level: 1

SEE ALSO
    HELP(1)""",

        "LOGIN": """LOGIN(1)                  SYSTEM_VOID Manual                 LOGIN(1)

NAME
    LOGIN - Connect to the system

SYNOPSIS
    LOGIN <key>

DESCRIPTION
    Connects to the system with an encryption key.

ARGUMENTS
    <key>    The encryption key (format: VOID + year)

EXAMPLES
    > LOGIN VOID2024
    Access granted. Level 1 unlocked.

SEE ALSO
    STATUS(1), HELP(1)""",

        "SCAN": """SCAN(1)                   SYSTEM_VOID Manual                  SCAN(1)

NAME
    SCAN - Scan system for files

SYNOPSIS
    SCAN

DESCRIPTION
    Scans the system and lists all available hidden files.

EXAMPLES
    > SCAN
    Scanning system...
    
    Files detected:
    - corrupted_data.b64
    - protocol_xyz.txt
    - hint_sequence.txt

SEE ALSO
    ACCESS(1), DECODE(1)""",

        "ACCESS": """ACCESS(1)                SYSTEM_VOID Manual                ACCESS(1)

NAME
    ACCESS - Access a file

SYNOPSIS
    ACCESS <file>

DESCRIPTION
    Opens and displays the content of a file.

ARGUMENTS
    <file>    The name of the file to open

EXAMPLES
    > ACCESS readme.txt
    File: readme.txt
    
    [File content]

SEE ALSO
    SCAN(1), NVIM(1)""",

        "DECODE": """DECODE(1)                SYSTEM_VOID Manual                DECODE(1)

NAME
    DECODE - Decode Base64 text

SYNOPSIS
    DECODE <base64_text> or DECODE <filename>

DESCRIPTION
    Decodes a Base64 encoded string or decodes the content of a Base64 file.

ARGUMENTS
    <base64_text>    The Base64 encoded text
    <filename>       A file containing Base64 (ex: corrupted_data.b64)

EXAMPLES
    > DECODE SGVsbG8gV29ybGQ=
    Decoded: Hello World
    
    > DECODE corrupted_data.b64
    File corrupted_data.b64 decoded:
    [Decoded content]

SEE ALSO
    ACCESS(1), SCAN(1)""",

        "ACTIVATE": """ACTIVATE(1)             SYSTEM_VOID Manual             ACTIVATE(1)

NAME
    ACTIVATE - Activate a system protocol

SYNOPSIS
    ACTIVATE <protocol_name>

DESCRIPTION
    Activates a system protocol to unlock new access levels.

ARGUMENTS
    <protocol_name>    The name of the protocol to activate (ex: PROTOCOL_XYZ)

EXAMPLES
    > ACTIVATE PROTOCOL_XYZ
    Level 2 unlocked! New commands: NETWORK, ANALYZE, BYPASS

NOTES
    The protocol name is usually found in decoded files.

SEE ALSO
    DECODE(1), NETWORK(1)""",

        "NETWORK": """NETWORK(1)              SYSTEM_VOID Manual              NETWORK(1)

NAME
    NETWORK - Display network map

SYNOPSIS
    NETWORK

DESCRIPTION
    Displays the network map with all detected servers and their status.

EXAMPLES
    > NETWORK
    NETWORK MAP
    ===========
    
    Servers detected:
    - SERVER_ALPHA (192.168.1.10) - Status: OFFLINE
    - SERVER_BETA (192.168.1.20) - Status: ONLINE
    - SERVER_GAMMA (192.168.1.30) - Status: LOCKED

SEE ALSO
    CONNECT(1), ANALYZE(1)""",

        "ANALYZE": """ANALYZE(1)              SYSTEM_VOID Manual              ANALYZE(1)

NAME
    ANALYZE - Analyze a specific subject

SYNOPSIS
    ANALYZE <subject>

DESCRIPTION
    Analyzes a specific subject of the system (security, network, etc.)

ARGUMENTS
    <subject>    The subject to analyze (ex: security, network)

EXAMPLES
    > ANALYZE security
    Security analysis:
    [Security logs]

SEE ALSO
    NETWORK(1), BYPASS(1)""",

        "BYPASS": """BYPASS(1)               SYSTEM_VOID Manual               BYPASS(1)

NAME
    BYPASS - Bypass a security system

SYNOPSIS
    BYPASS <code>

DESCRIPTION
    Bypasses a security system using a specific code.

ARGUMENTS
    <code>    The bypass code (usually found in a puzzle)

EXAMPLES
    > BYPASS 15
    Correct code!
    Level 3 unlocked!

NOTES
    The code is usually the solution to a puzzle (ex: magic square).

SEE ALSO
    ANALYZE(1), CONNECT(1)""",

        "CONNECT": """CONNECT(1)             SYSTEM_VOID Manual             CONNECT(1)

NAME
    CONNECT - Connect to a server

SYNOPSIS
    CONNECT <server> <password>

DESCRIPTION
    Connects to a remote server with a password.

ARGUMENTS
    <server>      The server name (ex: SERVER_GAMMA)
    <password>    The server password

EXAMPLES
    > CONNECT SERVER_GAMMA DIOV
    Server GAMMA connected!
    Level 4 unlocked!

SEE ALSO
    NETWORK(1), RESTORE(1)""",

        "RESTORE": """RESTORE(1)             SYSTEM_VOID Manual             RESTORE(1)

NAME
    RESTORE - Restore the system

SYNOPSIS
    RESTORE <code>

DESCRIPTION
    Restores the system to 100% using a restoration code.

ARGUMENTS
    <code>    The restoration code (usually a sum)

EXAMPLES
    > RESTORE 55
    Restoration code correct!
    System restored to 100%.

NOTES
    The code is usually a sum of numbers found in files.

SEE ALSO
    CONNECT(1), SOLVE(1)""",

        "SOLVE": """SOLVE(1)                SYSTEM_VOID Manual                SOLVE(1)

NAME
    SOLVE - Solve the final riddle

SYNOPSIS
    SOLVE <answer>

DESCRIPTION
    Solves the final riddle to complete the adventure.

ARGUMENTS
    <answer>    The answer to the final riddle

EXAMPLES
    > SOLVE VOID
    CONGRATULATIONS!
    You have completed the first part of SYSTEM_VOID!

NOTES
    The answer is usually found in the final chapter files.

SEE ALSO
    RESTORE(1), ACCESS(1)""",

        "NVIM": """NVIM(1)                   SYSTEM_VOID Manual                  NVIM(1)

NAME
    NVIM - Advanced file manager

SYNOPSIS
    NVIM [<file>]

DESCRIPTION
    Opens the Neovim-style file manager to navigate and edit system files.

ARGUMENTS
    <file>    (Optional) File to open directly

NAVIGATION
    h, j, k, l    Navigation (left, down, up, right)
    i             Insert mode
    ESC           Normal mode
    :q            Quit
    :w            Save
    /             Search
    :e <file>     Open a file

EXAMPLES
    > NVIM
    [Opens file manager]
    
    > NVIM config.enc
    [Opens config.enc in editor]

SEE ALSO
    ACCESS(1), MAN(1)""",

        "MAN": """MAN(1)                    SYSTEM_VOID Manual                   MAN(1)

NAME
    MAN - Display manual page for a command

SYNOPSIS
    MAN <command>

DESCRIPTION
    Displays the complete manual page for a given command.

ARGUMENTS
    <command>    The command name

EXAMPLES
    > MAN HELP
    [Displays HELP manual]
    
    > MAN NVIM
    [Displays NVIM manual]

SEE ALSO
    HELP(1)""",

        "SPLIT": """SPLIT(1)                 SYSTEM_VOID Manual                 SPLIT(1)

NAME
    SPLIT - Create a split terminal

SYNOPSIS
    SPLIT [horizontal|vertical]

DESCRIPTION
    Creates a new split terminal to execute tasks in parallel.

ARGUMENTS
    horizontal    Creates a horizontal split
    vertical      Creates a vertical split (default)

SHORTCUTS
    Ctrl+B then %    Vertical split
    Ctrl+B then quote    Horizontal split
    Ctrl+B then arrows    Navigate between panels
    Ctrl+B then x    Close current panel

EXAMPLES
    > SPLIT
    [Creates vertical split]
    
    > SPLIT horizontal
    [Creates horizontal split]

SEE ALSO
    JOBS(1), PORTSCAN(1)""",

        "PORTSCAN": """PORTSCAN(1)             SYSTEM_VOID Manual              PORTSCAN(1)

NAME
    PORTSCAN - Scan ports of a server

SYNOPSIS
    PORTSCAN <ip_address>

DESCRIPTION
    Scans open ports of a server and identifies services.

ARGUMENTS
    <ip_address>    The IP address of the server to scan

EXAMPLES
    > PORTSCAN 192.168.1.100
    Scanning 192.168.1.100...
    Port 22: OPEN (SSH)
    Port 80: OPEN (HTTP)
    Port 443: OPEN (HTTPS)
    
    Scan completed: 3 ports open

SEE ALSO
    BRUTEFORCE(1), NETWORK(1)""",

        "BRUTEFORCE": """BRUTEFORCE(1)          SYSTEM_VOID Manual           BRUTEFORCE(1)

NAME
    BRUTEFORCE - Brute force a password

SYNOPSIS
    BRUTEFORCE <target> <wordlist>

DESCRIPTION
    Launches a brute force attack on a target using a wordlist.

ARGUMENTS
    <target>      The target (user, server, etc.)
    <wordlist>    The file containing the password list

EXAMPLES
    > BRUTEFORCE admin wordlist.txt
    Brute forcing admin...
    Trying: admin... FAILED
    Trying: password... FAILED
    Trying: void2024... SUCCESS!
    
    Password found: void2024

SEE ALSO
    PORTSCAN(1), JOBS(1)""",

        "JOBS": """JOBS(1)                  SYSTEM_VOID Manual                  JOBS(1)

NAME
    JOBS - List running tasks

SYNOPSIS
    JOBS

DESCRIPTION
    Displays all tasks currently running (scans, bruteforce, etc.)

EXAMPLES
    > JOBS
    [1] PORTSCAN 192.168.1.100 - 45% complete
    [2] BRUTEFORCE admin - Running...
    
    Total: 2 jobs active

SEE ALSO
    SPLIT(1), PORTSCAN(1)""",

        "SSH": """SSH(1)                   SYSTEM_VOID Manual                  SSH(1)

NAME
    SSH - Connect to the system via SSH

SYNOPSIS
    SSH <username>@system-void.local

DESCRIPTION
    Establishes a secure SSH connection with the system. Allows authentication
    with a username and password, or with an access token.

ARGUMENTS
    <username>@system-void.local    Required format for SSH connection

NOTES
    Password will be prompted after entering the command.
    If you have an access token, the connection will be automatic.

EXAMPLES
    > SSH hacker@system-void.local
    hacker@system-void.local's password: 
    
    SSH connection established with hacker@system-void.local
    Welcome, hacker!
    Level 1 access granted.
    New commands: SCAN, DECODE, ACCESS

SEE ALSO
    CREATE_USER(1), EXPLOIT(1)""",

        "EXPLOIT": """EXPLOIT(1)               SYSTEM_VOID Manual              EXPLOIT(1)

NAME
    EXPLOIT - Exploit a system vulnerability

SYNOPSIS
    EXPLOIT <CVE>

DESCRIPTION
    Exploits a security vulnerability identified by a CVE code.
    This command allows unauthorized access to the system.

ARGUMENTS
    <CVE>    The CVE code of the vulnerability to exploit

NOTES
    Valid CVE codes are usually found in system files.
    A successful exploit may unlock new commands.

EXAMPLES
    > EXPLOIT CVE-2024-DB-001
    Exploit CVE-2024-DB-001 executed successfully!
    
    SQL vulnerability detected in database.
    Unauthorized access obtained.
    
    You can now create a user with:
    CREATE_USER <username> <password>

SEE ALSO
    CREATE_USER(1), ACCESS(1)""",

        "CREATE_USER": """CREATE_USER(1)          SYSTEM_VOID Manual         CREATE_USER(1)

NAME
    CREATE_USER - Create a user account

SYNOPSIS
    CREATE_USER <username> <password>

DESCRIPTION
    Creates a new user account in the system via a security flaw.
    Requires that an exploit has been successfully executed beforehand.

ARGUMENTS
    <username>    The username to create
    <password>    The password for the account

NOTES
    This command is only available after exploiting a vulnerability
    (for example with EXPLOIT CVE-2024-DB-001).

EXAMPLES
    > CREATE_USER hacker password123
    User hacker created successfully!
    
    SSH account created via database exploit.
    You can now connect with:
    ssh hacker@system-void.local

SEE ALSO
    SSH(1), EXPLOIT(1)""",

        "PKG": """PKG(1)                   SYSTEM_VOID Manual                  PKG(1)

NAME
    PKG - Package manager

SYNOPSIS
    PKG [INSTALL|UNINSTALL|LIST] [<package>]

DESCRIPTION
    Manages installation and uninstallation of system packages.
    Allows extending system functionality with additional tools.

SUBCOMMANDS
    INSTALL <package>      Install a package
    UNINSTALL <package>    Uninstall a package
    LIST                   List installed packages

ARGUMENTS
    <package>    The name of the package to install or uninstall

EXAMPLES
    > PKG LIST
    No packages installed.
    
    > PKG INSTALL file-viewer
    Package 'file-viewer' installed successfully!
    
    > PKG LIST
    INSTALLED PACKAGES:
    - file-viewer (v1.0.0)
      Advanced file viewer with vim-like interface

SEE ALSO
    ACCESS(1), MAN(1)""",

        "EXIT": """EXIT(1)                  SYSTEM_VOID Manual                 EXIT(1)

NAME
    EXIT - Logout from the system

SYNOPSIS
    EXIT

DESCRIPTION
    Closes the current user session and logs out from the system.
    Requires being logged in to work.

EXAMPLES
    > EXIT
    Logout successful. Goodbye, hacker!

SEE ALSO
    SSH(1), STATUS(1)""",

        "LS": """LS(1)                    SYSTEM_VOID Manual                   LS(1)

NAME
    LS - List directory contents

SYNOPSIS
    LS [<directory>]

DESCRIPTION
    Displays the contents of the current directory or a specified directory.
    Directories are marked with [DIR] and a slash (/).

ARGUMENTS
    <directory>    (Optional) The path of the directory to list

EXAMPLES
    > LS
    [DIR]  system/
    [DIR]  home/
           readme.txt
    
    > LS system
    [DIR]  config/
           logs.txt

SEE ALSO
    CD(1), PWD(1), ACCESS(1)""",

        "TALK": """TALK(1)                 SYSTEM_VOID Manual                  TALK(1)

NAME
    TALK - Talk with ARIA

SYNOPSIS
    TALK [<message>]

DESCRIPTION
    Allows interaction with ARIA, the system's AI assistant. Dialogues
    evolve based on your adventure progress and previous choices.

ARGUMENTS
    <message>    (Optional) Message or choice to send to ARIA

NOTES
    Some dialogues may require specific choices (BELIEVE, DOUBT, etc.).
    ARIA's responses vary based on your trust level and progress.

EXAMPLES
    > TALK
    [ARIA]
    Hello. I am ARIA. How can I help you?
    
    > TALK BELIEVE
    [ARIA]
    I'm glad you trust me...

SEE ALSO
    ARIA(1), STATUS(1)""",

        "ARIA": """ARIA(1)                 SYSTEM_VOID Manual                  ARIA(1)

NAME
    ARIA - Alias for TALK command

SYNOPSIS
    ARIA [<message>]

DESCRIPTION
    Alias for the TALK command. Allows direct interaction with ARIA.

SEE ALSO
    TALK(1)""",

        "CD": """CD(1)                    SYSTEM_VOID Manual                   CD(1)

NAME
    CD - Change directory

SYNOPSIS
    CD [<directory>]

DESCRIPTION
    Changes the current working directory. Without argument, returns to root (/).

ARGUMENTS
    <directory>    The target directory path (relative or absolute)
    ..             Move up one level in the directory tree
    .              Current directory (no change)

EXAMPLES
    > CD system
    /system
    
    > CD ..
    /
    
    > CD /system/config
    /system/config

SEE ALSO
    LS(1), PWD(1)""",

        "PWD": """PWD(1)                   SYSTEM_VOID Manual                  PWD(1)

NAME
    PWD - Print working directory

SYNOPSIS
    PWD

DESCRIPTION
    Displays the absolute path of the current working directory.

EXAMPLES
    > PWD
    /
    
    > CD system/config
    > PWD
    /system/config

SEE ALSO
    CD(1), LS(1)""",

        "ALIAS": """ALIAS(1)                SYSTEM_VOID Manual                 ALIAS(1)

NAME
    ALIAS - Manage command aliases

SYNOPSIS
    ALIAS [LIST|CREATE <alias>=<command>|REMOVE <alias>]

DESCRIPTION
    Allows creating, listing, and removing custom aliases for commands.
    Aliases are persistent and specific to your session.

SUBCOMMANDS
    LIST                    List all defined aliases
    CREATE <alias>=<cmd>    Create a new alias
    REMOVE <alias>          Remove an alias

ARGUMENTS
    <alias>     The name of the alias to create or remove
    <command>   The command the alias refers to

NOTES
    Some commands are reserved and cannot be replaced by an alias
    (HELP, EXIT, ALIAS).

EXAMPLES
    > ALIAS CREATE l=ls
    Alias 'l' created: l -> ls
    
    > ALIAS LIST
    Defined aliases:
    
      l                -> ls
    
    > ALIAS REMOVE l
    Alias 'l' removed.

SEE ALSO
    HELP(1)""",

        "CAT": """CAT(1)                   SYSTEM_VOID Manual                  CAT(1)

NAME
    CAT - Display file contents

SYNOPSIS
    CAT <file>

DESCRIPTION
    Alias for the ACCESS command. Displays the content of a file.

ARGUMENTS
    <file>    The name of the file to display

SEE ALSO
    ACCESS(1)"""
    }
}

