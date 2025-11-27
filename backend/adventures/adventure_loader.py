import os
import importlib.util
from typing import Dict, Any, Optional, List, Tuple


def get_branched_chapter_id(base_chapter_id: str, session_state: Dict[str, Any]) -> str:
    """
    Determine which chapter variant to load based on session state.
    Supports branching based on trust, choices, and narrative flags.
    """
    trust = session_state.get("aria_trust", 50)
    choices = session_state.get("choices", {})
    flags = session_state.get("narrative_flags", [])
    
    branch_rules = {
        "act_2": {
            "conditions": [
                {"trust_min": 60, "flags_any": ["trusted_ally"], "target": "act_2_trust"},
                {"trust_max": 40, "flags_any": ["skeptical_investigator"], "target": "act_2_doubt"},
            ]
        },
        "act_3": {
            "conditions": [
                {"trust_min": 70, "flags_all": ["trusted_ally", "honest_player"], "target": "act_3_light"},
                {"trust_max": 30, "flags_any": ["secretive_player"], "target": "act_3_dark"},
            ]
        },
    }
    
    if base_chapter_id in branch_rules:
        for condition in branch_rules[base_chapter_id]["conditions"]:
            if _check_branch_condition(condition, trust, choices, flags):
                return condition["target"]
    
    return base_chapter_id


def _check_branch_condition(condition: Dict, trust: int, choices: Dict, flags: List[str]) -> bool:
    """Check if a branching condition is met."""
    if "trust_min" in condition and trust < condition["trust_min"]:
        return False
    if "trust_max" in condition and trust > condition["trust_max"]:
        return False
    
    if "flags_all" in condition:
        if not all(f in flags for f in condition["flags_all"]):
            return False
    
    if "flags_any" in condition:
        if not any(f in flags for f in condition["flags_any"]):
            return False
    
    if "choices" in condition:
        for choice_id, required_value in condition["choices"].items():
            if choices.get(choice_id) != required_value:
                return False
    
    return True


def get_next_chapter(current_chapter_id: str, session_state: Dict[str, Any], 
                     language: str = "FR") -> Optional[str]:
    """
    Determine the next chapter based on current chapter and session state.
    Supports branching narratives.
    """
    chapter_data = get_chapter(current_chapter_id, language)
    if not chapter_data:
        return None
    
    progression = chapter_data.get("progression", {})
    
    if progression.get("is_final"):
        return None
    
    branches = chapter_data.get("branches", {})
    if branches:
        trust = session_state.get("aria_trust", 50)
        
        if "trust_high" in branches and trust >= 70:
            return branches["trust_high"]
        elif "trust_low" in branches and trust <= 30:
            return branches["trust_low"]
        elif "trust_medium" in branches:
            return branches["trust_medium"]
    
    for choice_id, choice_value in session_state.get("choices", {}).items():
        branch_key = f"choice_{choice_id}_{choice_value}"
        if branch_key in branches:
            return branches[branch_key]
    
    return progression.get("next_chapter")


def check_chapter_requirements(chapter_id: str, session_state: Dict[str, Any],
                               language: str = "FR") -> Tuple[bool, Optional[str]]:
    """
    Check if player meets requirements to enter a chapter.
    Returns (can_enter, reason_if_not).
    """
    chapter_data = get_chapter(chapter_id, language)
    if not chapter_data:
        return False, "Chapter not found"
    
    requirements = chapter_data.get("requirements", {})
    
    if "min_trust" in requirements:
        if session_state.get("aria_trust", 50) < requirements["min_trust"]:
            return False, f"Requires trust level {requirements['min_trust']}"
    
    if "max_trust" in requirements:
        if session_state.get("aria_trust", 50) > requirements["max_trust"]:
            return False, f"Requires trust level below {requirements['max_trust']}"
    
    if "required_flags" in requirements:
        flags = session_state.get("narrative_flags", [])
        missing = [f for f in requirements["required_flags"] if f not in flags]
        if missing:
            return False, f"Missing requirements: {', '.join(missing)}"
    
    if "required_secrets" in requirements:
        secrets = session_state.get("discovered_secrets", [])
        missing = [s for s in requirements["required_secrets"] if s not in secrets]
        if missing:
            return False, f"Secrets not yet discovered"
    
    if "required_choices" in requirements:
        choices = session_state.get("choices", {})
        for choice_id, required_value in requirements["required_choices"].items():
            if choices.get(choice_id) != required_value:
                return False, f"Different path taken"
    
    return True, None


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

