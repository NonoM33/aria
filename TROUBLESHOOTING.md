# Troubleshooting - SYSTEM_VOID

## Erreur "Network Error"

Si vous voyez "ERROR: Network Error" dans le terminal, cela signifie que le frontend ne peut pas se connecter au backend.

### Solution 1 : Vérifier que le backend est démarré

```bash
cd backend
source venv/bin/activate  # Si vous avez un venv
uvicorn main:app --reload --port 8000
```

Vous devriez voir :

```
INFO:     Uvicorn running on http://127.0.0.1:8000
```

### Solution 2 : Vérifier le port

Le backend doit tourner sur le port 8000. Si le port est occupé :

```bash
# Voir ce qui utilise le port 8000
lsof -ti:8000

# Ou utiliser un autre port et mettre à jour vite.config.js
uvicorn main:app --reload --port 8001
```

### Solution 3 : Vérifier les imports

Si le backend ne démarre pas à cause d'erreurs d'import :

```bash
cd backend
python3 -c "from adventures.adventure_data import get_adventure_data; print('OK')"
```

Si erreur, réinstallez les dépendances :

```bash
pip install -r requirements.txt
```

### Solution 4 : Vérifier CORS

Le backend doit autoriser les requêtes depuis `http://localhost:5173`.

Vérifiez dans `main.py` :

```python
allow_origins=["http://localhost:5173", "http://localhost:3000"],
```

## Erreurs d'import après refactorisation

Si vous avez des erreurs d'import :

1. Vérifiez que tous les fichiers sont bien créés dans `adventures/`
2. Redémarrez le backend
3. Vérifiez les logs du backend pour voir l'erreur exacte

## Le mode DEV ne fonctionne pas

Assurez-vous d'avoir activé le mode dev :

```bash
export DEV_MODE=true
uvicorn main:app --reload
```

Puis dans le terminal du jeu, tapez `DEV` pour voir les commandes disponibles.

## Les chapitres ne se chargent pas

Vérifiez que les fichiers sont bien dans `adventures/chapters/` :

```bash
ls backend/adventures/chapters/
```

Vous devriez voir `chapter_1.py` à `chapter_10.py`.

## Test rapide

Pour tester si tout fonctionne :

```bash
# Terminal 1 - Backend
cd backend
uvicorn main:app --reload

# Terminal 2 - Frontend
cd frontend
npm run dev

# Dans le navigateur, tapez dans le terminal :
> HELP
```

Si vous voyez toujours "Network Error", vérifiez :

- Le backend est bien démarré
- Le port 8000 est libre
- Aucune erreur dans les logs du backend
