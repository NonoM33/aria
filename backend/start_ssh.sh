#!/bin/bash

# Generate SSH host key if it doesn't exist
if [ ! -f ssh_host_key ]; then
    echo "Génération de la clé SSH du serveur..."
    ssh-keygen -t rsa -f ssh_host_key -N '' -q
    echo "Clé générée: ssh_host_key"
fi

# Start SSH server
cd "$(dirname "$0")"
source venv/bin/activate
python ssh_server.py --host 0.0.0.0 --port 2222

