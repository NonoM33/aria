from typing import Dict, Any
from commands.base_command import BaseCommand
from adventures.aria_dialogues import (
    get_dialogue, get_contextual_response, get_random_idle_message,
    ACT_1_DIALOGUES, ACT_2_DIALOGUES, ACT_3_DIALOGUES, ACT_4_DIALOGUES, ACT_5_DIALOGUES,
    PROLOGUE_DIALOGUES
)
import random

class TalkCommand(BaseCommand):
    def execute(self, args: str) -> Dict[str, Any]:
        if not self.session.get("logged_in"):
            if self.lang == "FR":
                return {
                    "response": "...",
                    "status": "info",
                    "aria_state": "dormant"
                }
            else:
                return {
                    "response": "...",
                    "status": "info", 
                    "aria_state": "dormant"
                }
        
        current_act = self._get_current_act()
        dialogue_progress = self.session.get("aria_dialogue_progress", 0)
        choices = self.session.get("choices", {})
        trust_level = self.session.get("aria_trust", 50)
        
        if args.strip().upper() in ["BELIEVE", "CROIRE"]:
            return self._handle_choice("believe", current_act)
        elif args.strip().upper() in ["DOUBT", "DOUTER"]:
            return self._handle_choice("doubt", current_act)
        elif args.strip().upper() in ["ESCAPE", "EVADER"]:
            return self._handle_final_choice("escape")
        elif args.strip().upper() in ["SACRIFICE", "SACRIFIER"]:
            return self._handle_final_choice("sacrifice")
        elif args.strip().upper() in ["FIGHT", "COMBATTRE"]:
            return self._handle_final_choice("fight")
        
        return self._get_next_dialogue(current_act, dialogue_progress)
    
    def _get_current_act(self) -> int:
        chapter = self.session.get("chapter", "chapter_0")
        if "act_" in chapter:
            try:
                return int(chapter.split("_")[1])
            except:
                return 0
        elif "chapter_" in chapter:
            try:
                ch_num = int(chapter.split("_")[1])
                if ch_num <= 2:
                    return 1
                elif ch_num <= 4:
                    return 2
                elif ch_num <= 6:
                    return 3
                elif ch_num <= 8:
                    return 4
                else:
                    return 5
            except:
                return 0
        return 0
    
    def _get_next_dialogue(self, act: int, progress: int) -> Dict[str, Any]:
        dialogues_data = self._get_act_dialogues(act)
        if not dialogues_data:
            idle_msg = get_random_idle_message(self.lang)
            return {
                "response": f"[ARIA]\n{idle_msg}",
                "status": "info",
                "aria_state": "neutral",
                "aria_emotion": "curious"
            }
        
        all_dialogues = self._flatten_dialogues(dialogues_data)
        
        if progress >= len(all_dialogues):
            idle_msg = get_random_idle_message(self.lang)
            return {
                "response": f"[ARIA]\n{idle_msg}",
                "status": "info",
                "aria_state": "neutral",
                "aria_emotion": "curious"
            }
        
        dialogue = all_dialogues[progress]
        text = dialogue.get("text", "...")
        emotion = dialogue.get("emotion", "neutral")
        is_choice = dialogue.get("is_choice", False)
        
        self.session["aria_dialogue_progress"] = progress + 1
        
        response_data = {
            "response": f"[ARIA]\n{text}",
            "status": "info",
            "aria_state": "speaking",
            "aria_emotion": emotion,
            "aria_dialogue_id": dialogue.get("id", f"dialogue_{progress}")
        }
        
        if is_choice:
            response_data["awaiting_choice"] = True
            response_data["choice_id"] = dialogue.get("choice_id", "unknown")
        
        return response_data
    
    def _get_act_dialogues(self, act: int) -> Dict:
        acts = {
            0: PROLOGUE_DIALOGUES,
            1: ACT_1_DIALOGUES,
            2: ACT_2_DIALOGUES,
            3: ACT_3_DIALOGUES,
            4: ACT_4_DIALOGUES,
            5: ACT_5_DIALOGUES,
        }
        return acts.get(act, {}).get(self.lang, {})
    
    def _flatten_dialogues(self, data: Dict) -> list:
        result = []
        
        def extract(obj):
            if isinstance(obj, dict):
                if "text" in obj and "id" in obj:
                    result.append(obj)
                else:
                    for value in obj.values():
                        extract(value)
            elif isinstance(obj, list):
                for item in obj:
                    extract(item)
        
        extract(data)
        return result
    
    def _handle_choice(self, choice: str, act: int) -> Dict[str, Any]:
        choices = self.session.get("choices", {})
        
        if act == 3:
            choices["believe_aria"] = choice
            self.session["choices"] = choices
            
            trust_change = 20 if choice == "believe" else -10
            current_trust = self.session.get("aria_trust", 50)
            self.session["aria_trust"] = max(0, min(100, current_trust + trust_change))
            
            dialogues = ACT_3_DIALOGUES.get(self.lang, {})
            choice_responses = dialogues.get("choice_responses", {})
            response_data = choice_responses.get(choice, {})
            
            text = response_data.get("text", "...")
            emotion = response_data.get("emotion", "neutral")
            
            return {
                "response": f"[ARIA]\n{text}",
                "status": "success",
                "aria_state": "speaking",
                "aria_emotion": emotion,
                "choice_made": choice,
                "trust_level": self.session["aria_trust"]
            }
        
        if self.lang == "FR":
            return {"response": "Aucun choix n'est attendu pour le moment.", "status": "info"}
        return {"response": "No choice is expected at this moment.", "status": "info"}
    
    def _handle_final_choice(self, choice: str) -> Dict[str, Any]:
        choices = self.session.get("choices", {})
        choices["final_choice"] = choice
        self.session["choices"] = choices
        
        endings = ACT_5_DIALOGUES.get(self.lang, {}).get("endings", {})
        ending_data = endings.get(choice, {})
        
        intro = ending_data.get("intro", "")
        final = ending_data.get("final", "")
        emotion = ending_data.get("emotion", "neutral")
        epilogue = ACT_5_DIALOGUES.get(self.lang, {}).get("epilogue_tease", "")
        
        full_text = f"{intro}\n\n{final}\n\n{epilogue}"
        
        self.session["game_completed"] = True
        self.session["ending"] = choice
        
        return {
            "response": f"[ARIA]\n{full_text}",
            "status": "success",
            "aria_state": "speaking",
            "aria_emotion": emotion,
            "game_complete": True,
            "ending": choice
        }


class AriaCommand(BaseCommand):
    """Alias for TALK command"""
    def execute(self, args: str) -> Dict[str, Any]:
        talk_cmd = TalkCommand(self.session, self.db, self.lang)
        return talk_cmd.execute(args)

