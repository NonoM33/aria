# Guide d'Aventure SYSTEM_VOID

## Introduction

SYSTEM_VOID est un ARG (Alternate Reality Game) dans lequel vous incarnez un hacker éthique infiltré dans un système corrompu. Votre mission : restaurer l'intégrité du système avant qu'il ne s'effondre.

**Temps estimé** : 1-2 heures  
**Difficulté** : Progressive (facile au début, plus complexe ensuite)

---

## Chapitre 1 : L'Infiltration

### Objectif

Trouver la clé d'encryption et vous connecter au système.

### Commandes disponibles

- `HELP` - Liste des commandes
- `STATUS` - État du système
- `LOGIN <clé>` - Se connecter

### Indices

1. Tapez `STATUS` pour voir l'état du système
2. Le message système contient un indice : "Le vide attend... 2024"
3. La clé est de la forme : VOID + année

### Solution

```
> STATUS
[Voir le message avec l'indice]

> LOGIN VOID2024
[Accès accordé]
```

---

## Chapitre 2 : Le Décodage

### Objectif

Scanner le système, décoder les fichiers corrompus et activer le protocole.

### Nouvelles commandes

- `SCAN` - Scanner le système
- `DECODE <base64>` - Décoder du Base64
- `ACCESS <fichier>` - Lire un fichier

### Étapes

1. `SCAN` pour voir les fichiers disponibles
2. `ACCESS hint_sequence.txt` pour connaître l'ordre
3. `ACCESS corrupted_data.b64` pour voir le fichier encodé
4. `DECODE <contenu_base64>` pour décoder (copiez le contenu du fichier)
5. Le résultat contient "PROTOCOL_XYZ"
6. `ACCESS protocol_xyz.txt` pour lire les instructions
7. `ACTIVATE PROTOCOL_XYZ` pour activer le protocole

### Solution

```
> SCAN
> ACCESS corrupted_data.b64
> DECODE VGhlIG5leHQgc3RlcCBpcyB0byBkZWNvZGUgdGhlIGZpbGUgY29kZWQgaW4gYmFzZTY0LgpUaGUgYW5zd2VyIGlzOiBQUk9UT0NPTF9YWVo=
> ACTIVATE PROTOCOL_XYZ
```

---

## Chapitre 3 : L'Activation

### Objectif

Résoudre l'énigme du carré magique pour accéder au niveau 3.

### Nouvelles commandes

- `NETWORK` - Voir la carte du réseau
- `ANALYZE <sujet>` - Analyser la sécurité
- `BYPASS <code>` - Contourner la sécurité

### Étapes

1. `ACCESS matrix.txt` pour voir l'énigme
2. `ACCESS security_log.txt` pour les instructions
3. Résoudre : Dans un carré magique 3x3 (somme = 15), quel est le nombre au centre ?
4. `BYPASS 5` (la réponse est 5)

### Solution

```
> ACCESS matrix.txt
> ACCESS security_log.txt
> BYPASS 5
```

---

## Chapitre 4 : Le Réseau

### Objectif

Se connecter au serveur GAMMA.

### Nouvelles commandes

- `CONNECT <serveur> <password>` - Se connecter à un serveur

### Étapes

1. `NETWORK` pour voir les serveurs
2. `ACCESS network_map.txt` pour les détails
3. `ACCESS server_logs.txt` pour trouver le mot de passe
4. Le mot de passe est l'inverse de "VOID" = "DIOV"
5. `CONNECT SERVER_GAMMA DIOV`

### Solution

```
> NETWORK
> ACCESS network_map.txt
> ACCESS server_logs.txt
> CONNECT SERVER_GAMMA DIOV
```

---

## Chapitre 5 : Le Noyau

### Objectif

Restaurer le système et résoudre l'énigme finale.

### Nouvelles commandes

- `RESTORE <code>` - Restaurer le système
- `SOLVE <réponse>` - Résoudre l'énigme

### Étapes

1. `ACCESS core_access.txt` pour les instructions
2. Calculer : 34 + 15 + 5 + 1 = 55
3. `RESTORE 55`
4. `ACCESS final_riddle.txt` pour l'énigme finale
5. L'énigme : "Je suis le début de la fin, la fin de l'éternité..."
6. La réponse est la première lettre de chaque mot-clé = "E"
7. `SOLVE E`

### Solution

```
> ACCESS core_access.txt
> RESTORE 55
> ACCESS final_riddle.txt
> SOLVE E
```

---

## Chapitre 6 : L'Exploration (NOUVEAU)

### Objectif

Découvrir le gestionnaire de fichiers et explorer le système.

### Nouvelles commandes

- `NVIM [<fichier>]` - Ouvrir le gestionnaire de fichiers
- `MAN <commande>` - Afficher le manuel d'une commande

### Étapes

1. `MAN NVIM` pour apprendre à utiliser le gestionnaire
2. `NVIM` pour ouvrir le gestionnaire de fichiers
3. `ACCESS file_structure.txt` pour voir la structure
4. Explorer les fichiers avec NVIM

### Navigation NVIM

- `h, j, k, l` : Navigation
- `i` : Mode insertion
- `ESC` : Mode normal
- `:q` : Quitter
- `:w` : Sauvegarder
- `/` : Rechercher

---

## Chapitres 7-10 (À venir)

Les chapitres suivants introduiront :

- **Chapitre 7** : Scan de ports et bruteforce
- **Chapitre 8** : Terminaux splités et multi-tâche
- **Chapitre 9** : Exploits et chiffrement
- **Chapitre 10** : Finale avec toutes les mécaniques

---

## Commandes de référence rapide

### Niveau 0

- `HELP` - Aide
- `STATUS` - État du système
- `LOGIN <clé>` - Connexion

### Niveau 1+

- `SCAN` - Scanner
- `DECODE <base64>` - Décoder
- `ACCESS <fichier>` - Lire un fichier

### Niveau 2+

- `ACTIVATE <protocole>` - Activer
- `NETWORK` - Réseau
- `ANALYZE <sujet>` - Analyser
- `BYPASS <code>` - Contourner

### Niveau 3+

- `CONNECT <serveur> <password>` - Se connecter

### Niveau 4+

- `RESTORE <code>` - Restaurer
- `SOLVE <réponse>` - Résoudre

### Niveau 6+

- `NVIM [<fichier>]` - Gestionnaire de fichiers
- `MAN <commande>` - Manuel

---

## Astuces

1. **Utilisez MAN** : `MAN <commande>` pour voir l'aide complète
2. **Historique** : Flèches haut/bas pour naviguer dans l'historique
3. **Auto-complétion** : Tab pour compléter les commandes
4. **Langue** : Bouton FR/EN en haut à droite pour changer la langue

---

## Troubleshooting

### Le système répond en anglais alors que j'ai sélectionné FR

- Rechargez la page (F5)
- Ou supprimez la session : `localStorage.removeItem('session_id')` dans la console

### Je suis bloqué

- Utilisez `HELP` pour voir les commandes disponibles
- Utilisez `STATUS` pour voir votre niveau
- Utilisez `MAN <commande>` pour l'aide détaillée

### La commande n'existe pas

- Vérifiez votre niveau avec `STATUS`
- Certaines commandes nécessitent un niveau spécifique
- Utilisez `HELP` pour voir les commandes débloquées

---

Bon hacking ! 🚀
