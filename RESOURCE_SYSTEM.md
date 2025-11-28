# Système de Ressources et Terminaux Split

## 🎮 Nouvelles Fonctionnalités

### 1. Terminaux Split (CTRL+T)

Ouvre plusieurs terminaux en parallèle pour une expérience multitâche.

**Raccourcis clavier :**

- `CTRL+T` : Ouvrir un nouveau terminal split
- `CTRL+W` : Fermer le dernier terminal split

**Utilisation :**

- Chaque terminal split est indépendant
- Tu peux avoir plusieurs terminaux ouverts simultanément
- Le terminal actif est mis en évidence (bordure cyan)

### 2. Gestion des Ressources

Le système consomme et gère des ressources pendant le jeu :

**Ressources disponibles :**

- **CPU** : Consommé par les commandes (SCAN, DECODE, ACCESS)
- **Mémoire** : Utilisée pour les opérations complexes
- **Énergie** : Se régénère lentement, se consomme avec les actions
- **Bande passante** : Pour les scans réseau
- **Stockage** : Espace de stockage disponible

**Commandes :**

- `MONITOR` : Affiche l'état de toutes les ressources en temps réel
- `RESOURCE` : Gère les ressources et quêtes
  - `RESOURCE QUESTS` : Affiche les quêtes quotidiennes
  - `RESOURCE ACHIEVEMENTS` : Affiche les achievements débloqués
  - `RESOURCE RESTORE <type>` : Restaure une ressource (coûte 10 crédits)
- `UPGRADE` : Améliore les ressources (coûte des crédits)

### 3. Système de Quêtes Quotidiennes

**Quêtes disponibles :**

- Explorer 10 fichiers
- Résoudre 3 puzzles
- Scanner 5 systèmes
- Décoder 3 fichiers

**Récompenses :**

- Crédits
- Restauration de ressources
- Achievements

### 4. Système d'Achievements

**Achievements disponibles :**

- 🏆 **Explorateur** : Accéder à 10 fichiers
- 🏆 **Archiviste** : Accéder à 100 fichiers
- 🏆 **Résolveur** : Résoudre 5 puzzles
- 🏆 **Maître Hacker** : Atteindre le niveau 5

### 5. Système de Crédits

**Obtention de crédits :**

- Résoudre des puzzles : +50 crédits
- Compléter des quêtes quotidiennes
- Débloquer des achievements

**Utilisation des crédits :**

- Restaurer des ressources : 10 crédits
- Améliorer des ressources : Niveau × 100 crédits

## 🎯 Mécaniques Addictives

### Progression Continue

- Les ressources se régénèrent lentement
- Les quêtes se réinitialisent chaque jour
- Les achievements offrent des récompenses permanentes

### Feedback Immédiat

- Barres de progression visuelles
- Notifications d'achievements
- Récompenses instantanées

### Objectifs à Court Terme

- Quêtes quotidiennes renouvelables
- Progression visible des ressources
- Système d'amélioration incrémental

## 📊 Intégration dans le Jeu

Les ressources sont automatiquement consommées lors de :

- `ACCESS` : -0.5 CPU, -0.3 Énergie
- `SCAN` : -1.0 CPU, -0.5 Énergie, -0.3 Bande passante
- `DECODE` : -2.0 CPU, -1.5 Mémoire, -1.0 Énergie
- `SOLVE` : -3.0 CPU, -2.0 Mémoire, -1.5 Énergie (+50 crédits)

Les quêtes se mettent à jour automatiquement lors de ces actions.

## 🚀 Pour Commencer

1. Tape `MONITOR` pour voir tes ressources
2. Tape `RESOURCE QUESTS` pour voir tes quêtes quotidiennes
3. Tape `RESOURCE ACHIEVEMENTS` pour voir tes achievements
4. Utilise `CTRL+T` pour ouvrir un terminal split
5. Complète des quêtes pour gagner des crédits
6. Améliore tes ressources avec `UPGRADE`

Bon hacking ! 🎮
