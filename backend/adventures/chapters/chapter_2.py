CHAPTER_FR = {
    "title": "Le Décodage",
    "intro": "Accès niveau 1 obtenu.\n\nNouvelles commandes disponibles: SCAN, DECODE, ACCESS\n\nVous devez maintenant scanner le système pour trouver les fichiers corrompus.",
    "files": {
        "corrupted_data.b64": "VGhlIG5leHQgc3RlcCBpcyB0byBkZWNvZGUgdGhlIGZpbGUgY29kZWQgaW4gYmFzZTY0LgpUaGUgYW5zd2VyIGlzOiBQUk9UT0NPTF9YWVo=",
        "protocol_xyz.txt": """PROTOCOL XYZ
==============

Ce protocole permet d'accéder au niveau 2.

Pour activer le protocole, vous devez:
1. Décoder le fichier corrupted_data.b64
2. Utiliser la commande: ACTIVATE <protocol_name>

Le nom du protocole est dans le fichier décodé.""",
        "hint_sequence.txt": """SÉQUENCE D'ACTIVATION
=====================

Les fichiers doivent être lus dans un ordre spécifique:
1. corrupted_data.b64 -> Décoder avec DECODE
2. protocol_xyz.txt -> Lire le contenu
3. Utiliser ACTIVATE avec le nom du protocole trouvé

Indice: Le protocole commence par PROTOCOL_""",
    }
}

CHAPTER_EN = {
    "title": "The Decoding",
    "intro": "Level 1 access obtained.\n\nNew commands available: SCAN, DECODE, ACCESS\n\nYou must now scan the system to find corrupted files.",
    "files": {
        "corrupted_data.b64": "VGhlIG5leHQgc3RlcCBpcyB0byBkZWNvZGUgdGhlIGZpbGUgY29kZWQgaW4gYmFzZTY0LgpUaGUgYW5zd2VyIGlzOiBQUk9UT0NPTF9YWVo=",
        "protocol_xyz.txt": """PROTOCOL XYZ
==============

This protocol allows access to level 2.

To activate the protocol, you must:
1. Decode the corrupted_data.b64 file
2. Use command: ACTIVATE <protocol_name>

The protocol name is in the decoded file.""",
        "hint_sequence.txt": """ACTIVATION SEQUENCE
====================

Files must be read in a specific order:
1. corrupted_data.b64 -> Decode with DECODE
2. protocol_xyz.txt -> Read content
3. Use ACTIVATE with found protocol name

Hint: Protocol starts with PROTOCOL_""",
    }
}

