from .adventure_loader import load_all_chapters

def get_adventure_data(language: str = "FR"):
    chapters = load_all_chapters(language)
    
    system_messages = {
        "FR": {
            "welcome": "SYSTEM_VOID v2.0\n\nConnexion au serveur PROMETHEUS...\nSignal detecte. Quelque chose repond.\n\nTapez HELP pour commencer.",
            "level_up": "Niveau {level} debloque!",
            "file_accessed": "Fichier {filename} ouvert.",
            "puzzle_solved": "Enigme resolue!",
            "chapter_complete": "Chapitre '{title}' termine!"
        },
        "EN": {
            "welcome": "SYSTEM_VOID v2.0\n\nConnecting to PROMETHEUS server...\nSignal detected. Something responds.\n\nType HELP to start.",
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

