import os
import importlib.util
from typing import Dict, Any

def load_chapter_file(chapter_id: str, language: str = "FR") -> Dict[str, Any]:
    base_path = os.path.dirname(__file__)
    chapters_path = os.path.join(base_path, "chapters")
    
    chapter_file = os.path.join(chapters_path, f"{chapter_id}.py")
    
    if not os.path.exists(chapter_file):
        return None
    
    spec = importlib.util.spec_from_file_location(chapter_id, chapter_file)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    
    if hasattr(module, f"CHAPTER_{language}"):
        return getattr(module, f"CHAPTER_{language}")
    elif hasattr(module, "CHAPTER_FR"):
        return getattr(module, "CHAPTER_FR")
    else:
        return None

def load_all_chapters(language: str = "FR") -> Dict[str, Any]:
    chapters = {}
    base_path = os.path.dirname(__file__)
    chapters_path = os.path.join(base_path, "chapters")
    
    if not os.path.exists(chapters_path):
        return chapters
    
    for filename in sorted(os.listdir(chapters_path)):
        if filename.endswith(".py") and filename != "__init__.py":
            chapter_id = filename[:-3]
            chapter_data = load_chapter_file(chapter_id, language)
            if chapter_data:
                chapters[chapter_id] = chapter_data
    
    return chapters

def get_chapter(chapter_id: str, language: str = "FR") -> Dict[str, Any]:
    return load_chapter_file(chapter_id, language)

