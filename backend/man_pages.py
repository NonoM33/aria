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
    SPLIT(1), PORTSCAN(1)"""
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
    SPLIT(1), PORTSCAN(1)"""
    }
}

