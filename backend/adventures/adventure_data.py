from .adventure_loader import load_all_chapters

def get_adventure_data(language: str = "FR"):
    chapters = load_all_chapters(language)
    
    system_messages = {
        "FR": {
            "welcome": "SYSTEM_VOID v2.0 - Système de base de données compromis\n\nVous devez exploiter une vulnérabilité pour créer un accès SSH.\nTapez SCAN pour commencer.",
            "level_up": "Niveau {level} débloqué!",
            "file_accessed": "Fichier {filename} ouvert.",
            "puzzle_solved": "Énigme résolue!",
            "chapter_complete": "Chapitre '{title}' terminé!"
        },
        "EN": {
            "welcome": "SYSTEM_VOID v2.0 - Compromised Database System\n\nYou must exploit a vulnerability to create SSH access.\nType SCAN to start.",
            "level_up": "Level {level} unlocked!",
            "file_accessed": "File {filename} opened.",
            "puzzle_solved": "Riddle solved!",
            "chapter_complete": "Chapter '{title}' completed!"
        }
    }
    
    return {
        language: {
            "chapters": chapters,
            "system_messages": system_messages.get(language, system_messages["FR"])
        }
    }

