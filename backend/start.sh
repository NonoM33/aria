#!/bin/bash

echo "🚀 Démarrage de SYSTEM_VOID Backend..."

if [ ! -d "venv" ]; then
    echo "📦 Création de l'environnement virtuel..."
    python3 -m venv venv
fi

echo "📦 Activation de l'environnement virtuel..."
source venv/bin/activate

echo "📥 Installation des dépendances..."
pip install -q -r requirements.txt

echo ""
echo "✅ Backend prêt !"
echo ""
echo "🌐 Démarrage du serveur sur http://localhost:8000"
echo "   Appuyez sur Ctrl+C pour arrêter"
echo ""

if [ "$DEV_MODE" = "true" ]; then
    echo "🔧 Mode DEV activé"
    uvicorn main:app --reload --port 8000
else
    uvicorn main:app --reload --port 8000
fi

