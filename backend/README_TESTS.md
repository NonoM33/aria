# Tests Unitaires - SYSTEM_VOID

## Installation

```bash
# Avec pip3 (macOS/Linux)
pip3 install -r requirements.txt

# Ou avec python3 -m pip
python3 -m pip install -r requirements.txt

# Ou si vous avez un venv activé
pip install -r requirements.txt
```

## Exécution des tests

```bash
# Méthode 1 : Script automatique (recommandé)
./run_tests.sh

# Méthode 2 : Commandes manuelles
# Tous les tests
python3 -m pytest

# Avec détails
python3 -m pytest -v

# Un test spécifique
python3 -m pytest test_adventure.py::test_login_with_correct_key -v

# Avec couverture (si pytest-cov installé)
python3 -m pytest --cov=. --cov-report=html
```

## Structure des tests

Les tests couvrent :

### 1. Commandes de base

- Messages de bienvenue (FR/EN)
- HELP
- STATUS (niveaux différents)
- LOGIN (avec/sans clé, bonne/mauvaise clé)

### 2. Progression de l'aventure

- SCAN après login
- ACCESS aux fichiers
- DECODE Base64
- ACTIVATE protocole
- NETWORK
- ANALYZE
- BYPASS (énigme carré magique)
- CONNECT serveur
- RESTORE système
- SOLVE énigme finale

### 3. Gestion des langues

- Persistance FR/EN
- Traductions correctes

### 4. Structure des données

- Vérification de la structure ADVENTURE_DATA
- Tous les chapitres présents
- Tous les puzzles ont des solutions
- Tous les fichiers ont du contenu

### 5. Gestion des erreurs

- Commandes inconnues
- Clés invalides
- Fichiers inexistants

## Ajout de nouveaux tests

Lors de l'ajout de nouvelles fonctionnalités :

1. **Test de la fonctionnalité** : Créez un test qui vérifie le comportement attendu
2. **Test de régression** : Vérifiez que les anciennes fonctionnalités fonctionnent toujours
3. **Test de données** : Si vous ajoutez des données, vérifiez leur structure

Exemple :

```python
def test_nouvelle_commande():
    session_id = "test_new_command"
    # Setup
    client.post("/api/command", json={
        "command": f"LOGIN {ENCRYPTION_KEY}",
        "session_id": session_id,
        "language": "FR"
    })

    # Test
    response = client.post("/api/command", json={
        "command": "NOUVELLE_COMMANDE",
        "session_id": session_id,
        "language": "FR"
    })

    # Assertions
    assert response.status_code == 200
    assert response.json()["status"] == "success"
```

## CI/CD

Pour intégrer dans un pipeline CI/CD :

```yaml
- name: Run tests
  run: |
    cd backend
    pip install -r requirements.txt
    pytest
```
