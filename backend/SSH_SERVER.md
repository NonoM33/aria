# Serveur SSH SYSTEM_VOID

## Installation

1. Installer les dépendances :

```bash
cd backend
source venv/bin/activate
pip install asyncssh
```

2. Générer la clé SSH du serveur (une seule fois) :

```bash
ssh-keygen -t rsa -f ssh_host_key -N ''
```

## Démarrage

### Option 1 : Script automatique

```bash
./start_ssh.sh
```

### Option 2 : Manuel

```bash
source venv/bin/activate
python ssh_server.py --host 0.0.0.0 --port 2222
```

## Connexion

### Depuis le même ordinateur :

```bash
ssh <username>@localhost -p 2222
```

### Depuis un autre ordinateur :

```bash
ssh <username>@<ip_serveur> -p 2222
```

**Important** : Vous devez d'abord créer un compte dans le jeu (via l'interface web ou la commande CREATE_USER).

## Utilisation

Une fois connecté en SSH, vous pouvez utiliser toutes les commandes du jeu :

- `HELP` - Liste des commandes
- `LS` - Lister les fichiers
- `ACCESS <fichier>` - Lire un fichier
- `SCAN` - Scanner le système
- `STATUS` - État du système
- `EXIT` - Se déconnecter

## Avantages

✅ **Vraie connexion SSH** - Utilisez votre terminal préféré  
✅ **Expérience immersive** - Comme un vrai hack  
✅ **Multi-joueurs** - Plusieurs connexions simultanées  
✅ **Synchronisé** - Même base de données que l'interface web

## Sécurité

⚠️ **Note** : Ce serveur SSH est conçu pour le jeu uniquement.  
Ne l'exposez pas sur Internet sans protection (firewall, VPN, etc.).

## Dépannage

**Erreur "Connection refused"** :

- Vérifiez que le serveur est démarré
- Vérifiez le port (2222 par défaut)
- Vérifiez le firewall

**Erreur "Permission denied"** :

- Vérifiez vos identifiants
- Créez un compte via l'interface web d'abord

**Erreur "Host key verification failed"** :

- Supprimez l'ancienne clé : `ssh-keygen -R [localhost]:2222`
