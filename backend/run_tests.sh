#!/bin/bash

echo "🧪 Configuration de l'environnement de test..."

# Détecter si on utilise python3 ou python
if command -v python3 &> /dev/null; then
    PYTHON_CMD="python3"
else
    PYTHON_CMD="python"
fi

# Créer le venv s'il n'existe pas
if [ ! -d "venv" ]; then
    echo "📦 Création de l'environnement virtuel..."
    $PYTHON_CMD -m venv venv
fi

# Activer le venv
echo "📦 Activation de l'environnement virtuel..."
source venv/bin/activate

# Installer les dépendances
echo "📥 Installation des dépendances..."
pip install -r requirements.txt

echo ""
echo "🚀 Lancement des tests..."
pytest test_adventure.py -v

echo ""
echo "✅ Tests terminés!"

