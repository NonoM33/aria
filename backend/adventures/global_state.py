from typing import Dict, List, Any
from datetime import datetime
import json

class GlobalState:
    _instance = None
    _state = {
        "global_integrity": 0,
        "total_players": 0,
        "players_online": 0,
        "chapters_unlocked": [],
        "global_events": [],
        "collective_progress": {},
        "world_state": "INITIAL",
        "last_update": None
    }
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(GlobalState, cls).__new__(cls)
        return cls._instance
    
    def get_state(self) -> Dict[str, Any]:
        self._state["last_update"] = datetime.now().isoformat()
        return self._state.copy()
    
    def update_integrity(self, value: int):
        self._state["global_integrity"] = max(0, min(100, value))
        self._add_event("INTEGRITY_UPDATE", {"value": self._state["global_integrity"]})
    
    def add_player(self):
        self._state["total_players"] += 1
        self._state["players_online"] += 1
        self._add_event("PLAYER_JOINED", {"total": self._state["total_players"]})
    
    def remove_player(self):
        self._state["players_online"] = max(0, self._state["players_online"] - 1)
    
    def unlock_chapter(self, chapter_id: str):
        if chapter_id not in self._state["chapters_unlocked"]:
            self._state["chapters_unlocked"].append(chapter_id)
            self._add_event("CHAPTER_UNLOCKED", {"chapter": chapter_id})
    
    def update_collective_progress(self, key: str, value: Any):
        self._state["collective_progress"][key] = value
        self._add_event("PROGRESS_UPDATE", {"key": key, "value": value})
    
    def set_world_state(self, state: str):
        self._state["world_state"] = state
        self._add_event("WORLD_STATE_CHANGE", {"state": state})
    
    def _add_event(self, event_type: str, data: Dict):
        event = {
            "type": event_type,
            "data": data,
            "timestamp": datetime.now().isoformat()
        }
        self._state["global_events"].append(event)
        if len(self._state["global_events"]) > 100:
            self._state["global_events"] = self._state["global_events"][-100:]
    
    def get_recent_events(self, limit: int = 10) -> List[Dict]:
        return self._state["global_events"][-limit:]
    
    def reset(self):
        self._state = {
            "global_integrity": 0,
            "total_players": 0,
            "players_online": 0,
            "chapters_unlocked": [],
            "global_events": [],
            "collective_progress": {},
            "world_state": "INITIAL",
            "last_update": None
        }

