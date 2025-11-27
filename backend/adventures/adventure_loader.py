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

def load_act_file(act_id: str, language: str = "FR") -> Dict[str, Any]:
    base_path = os.path.dirname(__file__)
    chapters_path = os.path.join(base_path, "chapters")
    
    act_file = os.path.join(chapters_path, f"{act_id}.py")
    
    if not os.path.exists(act_file):
        return None
    
    spec = importlib.util.spec_from_file_location(act_id, act_file)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    
    if hasattr(module, f"CHAPTER_{language}"):
        return getattr(module, f"CHAPTER_{language}")
    elif hasattr(module, "CHAPTER_FR"):
        return getattr(module, "CHAPTER_FR")
    
    act_number = act_id.replace("act_", "")
    getter_name = f"get_act_{act_number}_data"
    
    if hasattr(module, getter_name):
        return getattr(module, getter_name)(language)
    
    data_name = f"ACT_{act_number}_DATA"
    if hasattr(module, data_name):
        data = getattr(module, data_name)
        return data.get(language, data.get("FR", data.get("EN", {})))
    
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
    if chapter_id.startswith("act_"):
        return load_act_file(chapter_id, language)
    return load_chapter_file(chapter_id, language)

def get_act(act_id: str, language: str = "FR") -> Dict[str, Any]:
    return load_act_file(act_id, language)

def get_act_files(act_id: str, language: str = "FR") -> Dict[str, Any]:
    act_data = get_act(act_id, language)
    if act_data:
        return act_data.get("files", {})
    return {}

def get_act_puzzles(act_id: str, language: str = "FR") -> Dict[str, Any]:
    act_data = get_act(act_id, language)
    if act_data:
        return act_data.get("puzzles", {})
    return {}

def get_act_progression(act_id: str, language: str = "FR") -> Dict[str, Any]:
    act_data = get_act(act_id, language)
    if act_data:
        return act_data.get("progression", {})
    return {}

def get_chapter_filesystem(chapter_id: str, language: str = "FR") -> Dict[str, Any]:
    chapter_data = get_chapter(chapter_id, language)
    if chapter_data:
        return chapter_data.get("filesystem", {})
    return {}

def get_chapter_intro(chapter_id: str, language: str = "FR") -> str:
    chapter_data = get_chapter(chapter_id, language)
    if chapter_data:
        return chapter_data.get("intro", "")
    return ""

def get_chapter_puzzles(chapter_id: str, language: str = "FR") -> Dict[str, Any]:
    chapter_data = get_chapter(chapter_id, language)
    if chapter_data:
        return chapter_data.get("puzzles", {})
    return {}

