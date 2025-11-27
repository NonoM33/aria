from typing import Dict, Any, Optional
from sqlalchemy.orm import Session
from database import GlobalEvent
from adventures.global_state import GlobalState

global_state = GlobalState()

def create_global_event(
    db: Optional[Session],
    event_type: str,
    event_data: Dict[str, Any],
    triggered_by: Optional[str] = None,
    impact_level: int = 1
) -> bool:
    if not db:
        return False
    
    try:
        event = GlobalEvent(
            event_type=event_type,
            event_data=event_data,
            triggered_by=triggered_by,
            impact_level=impact_level
        )
        db.add(event)
        db.commit()
        
        global_state._add_event(event_type, event_data)
        return True
    except:
        return False

