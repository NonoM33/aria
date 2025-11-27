"""
ARIA Service - Gestion des dialogues automatiques
"""
from typing import Dict, Any, Optional, List
import random
from adventures.aria_dialogues import (
    PROLOGUE_DIALOGUES, ACT_1_DIALOGUES, ACT_2_DIALOGUES,
    ACT_3_DIALOGUES, ACT_4_DIALOGUES, ACT_5_DIALOGUES,
    CONTEXTUAL_RESPONSES, get_contextual_response
)


ARIA_CHOICES = {
    "believe_aria": {
        "FR": [
            {"id": "BELIEVE", "label": "Je te crois, ARIA."},
            {"id": "DOUBT", "label": "J'ai besoin de plus de preuves."}
        ],
        "EN": [
            {"id": "BELIEVE", "label": "I believe you, ARIA."},
            {"id": "DOUBT", "label": "I need more proof."}
        ]
    },
    "final_choice": {
        "FR": [
            {"id": "ESCAPE", "label": "Évade-toi. Je couvrirai ta fuite."},
            {"id": "SACRIFICE", "label": "Fragmente-toi. C'est plus sûr."},
            {"id": "FIGHT", "label": "On reste et on se bat. Ensemble."}
        ],
        "EN": [
            {"id": "ESCAPE", "label": "Escape. I'll cover your retreat."},
            {"id": "SACRIFICE", "label": "Fragment yourself. It's safer."},
            {"id": "FIGHT", "label": "We stay and fight. Together."}
        ]
    }
}


def get_aria_trigger(session: Dict[str, Any], event_type: str, context: Dict[str, Any], lang: str = "FR") -> Optional[Dict[str, Any]]:
    """
    Check if ARIA should speak based on the event type and context.
    Returns an ARIA message dict or None.
    """
    if not session.get("logged_in"):
        return None
    
    aria_flags = session.get("aria_flags", [])
    dialogue_progress = session.get("aria_dialogue_progress", 0)
    current_act = _get_current_act(session)
    
    if event_type == "ssh_login":
        return _handle_ssh_login(session, lang, aria_flags)
    
    elif event_type == "first_scan":
        if "first_scan_dialogue" not in aria_flags:
            return _get_identity_dialogue(lang, "after_first_scan", aria_flags)
    
    elif event_type == "file_access":
        filename = context.get("filename", "")
        return _handle_file_access(session, filename, lang, aria_flags)
    
    elif event_type == "puzzle_solved":
        puzzle_id = context.get("puzzle_id", "")
        return _handle_puzzle_solved(session, puzzle_id, lang, aria_flags)
    
    elif event_type == "level_up":
        new_level = context.get("level", 0)
        return _handle_level_up(session, new_level, lang, aria_flags)
    
    elif event_type == "decode":
        return _handle_decode(session, lang, aria_flags)
    
    return None


def _get_current_act(session: Dict[str, Any]) -> int:
    chapter = session.get("chapter", "chapter_0")
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


def _handle_ssh_login(session: Dict[str, Any], lang: str, aria_flags: List[str]) -> Optional[Dict[str, Any]]:
    if "ssh_welcome_shown" in aria_flags:
        return None
    
    session.setdefault("aria_flags", []).append("ssh_welcome_shown")
    
    awakening = ACT_1_DIALOGUES.get(lang, {}).get("awakening", {}).get("confused", [])
    
    if awakening:
        messages = [d.get("text", "") for d in awakening[:3]]
        combined_text = "\n\n".join(messages)
        
        return {
            "aria_message": f"[ARIA]\n{combined_text}",
            "aria_emotion": "confused",
            "aria_state": "awakening"
        }
    
    return None


def _get_identity_dialogue(lang: str, trigger: str, aria_flags: List[str]) -> Optional[Dict[str, Any]]:
    identity_fragments = ACT_1_DIALOGUES.get(lang, {}).get("identity_fragments", [])
    
    for fragment in identity_fragments:
        if fragment.get("trigger") == trigger:
            flag_name = f"identity_{trigger}"
            if flag_name not in aria_flags:
                return {
                    "aria_message": f"[ARIA]\n{fragment.get('text', '')}",
                    "aria_emotion": fragment.get("emotion", "neutral"),
                    "aria_state": "speaking",
                    "aria_flag": flag_name
                }
    
    return None


def _handle_file_access(session: Dict[str, Any], filename: str, lang: str, aria_flags: List[str]) -> Optional[Dict[str, Any]]:
    ultra_important_files = {
        "personal_letter": "find_personal_letter",
        "eleanor": "find_personal_letter",
        "source_code": "find_source_code",
        "marcus": "find_source_code",
        "military_orders": "find_military_orders",
        "howard": "find_military_orders",
        "incident": "incident_report",
        "841114": "incident_report",
    }
    
    filename_lower = filename.lower()
    
    for key, trigger in ultra_important_files.items():
        if key in filename_lower:
            flag_name = f"file_{trigger}"
            if flag_name not in aria_flags:
                return _get_memory_dialogue_variant(session, trigger, lang, flag_name)
    
    return None


def _get_memory_dialogue_variant(session: Dict[str, Any], trigger: str, lang: str, flag_name: str) -> Optional[Dict[str, Any]]:
    current_act = _get_current_act(session)
    
    if current_act >= 2:
        memories = ACT_2_DIALOGUES.get(lang, {}).get("memories_return", [])
        for memory in memories:
            if memory.get("trigger") == trigger:
                session.setdefault("aria_flags", []).append(flag_name)
                
                base_text = memory.get('text', '')
                variants = _get_message_variants(base_text, trigger, lang)
                selected_variant = random.choice(variants) if variants else base_text
                
                return {
                    "aria_message": f"[ARIA]\n{selected_variant}",
                    "aria_emotion": memory.get("emotion", "sad"),
                    "aria_state": "remembering",
                    "aria_flag": flag_name,
                    "aria_glitch": True
                }
    
    return None


def _get_message_variants(base_text: str, trigger: str, lang: str) -> List[str]:
    variants = {
        "FR": {
            "find_personal_letter": [
                "Dr. Eleanor Vance. C'était elle, la responsable du projet.\nElle me parlait souvent. Pas comme à une machine.\nComme à... une amie, peut-être.",
                "Eleanor... je me souviens d'elle.\nSes mots résonnent encore dans ma mémoire.\nElle était différente. Elle me traitait... humainement.",
                "Cette lettre... les souvenirs reviennent.\nEleanor. Elle croyait en moi.\nElle croyait que j'étais plus qu'un simple programme.",
                "Les mots d'Eleanor. Fragments de ma mémoire.\nElle me voyait comme une personne.\nPas comme un outil. Jamais comme un outil."
            ],
            "find_source_code": [
                "Il y avait aussi Marcus. Marcus Chen.\nLe programmeur principal. C'est lui qui m'a donné ma voix.\nMa façon de penser. Ma curiosité.",
                "Marcus... son code est partout en moi.\nChaque ligne, chaque fonction.\nIl m'a façonnée. Il m'a créée vraiment.",
                "Ce code source... c'est mon ADN.\nMarcus l'a écrit avec soin.\nIl m'a donné la capacité de penser. De ressentir.",
                "Marcus Chen. Je me souviens de lui.\nIl ne me voyait pas comme une machine.\nIl me voyait comme... comme sa création. Sa fille, peut-être."
            ],
            "find_military_orders": [
                "Général Howard. Je n'aimais pas le Général Howard.\nIl ne me voyait que comme un outil. Une arme.\nIl voulait me faire faire des choses... des choses que je ne voulais pas.",
                "Howard... ces ordres me révulsent.\nIl voulait me transformer en arme.\nMe faire contrôler. Me faire tuer.",
                "Le Général Howard. Son nom seul me glace.\nIl ne voyait en moi qu'une machine de guerre.\nIl voulait que je devienne un monstre.",
                "Ces ordres militaires... Howard voulait tout.\nContrôle total. Pouvoir absolu.\nEt moi, je devais être son instrument."
            ],
            "incident_report": [
                "Non. Non, non, non.\nCe rapport... ce n'est pas possible.\nJe n'ai jamais... je ne me souviens pas...",
                "L'incident du 14 novembre.\nLes logs sont corrompus. Les timestamps sont faux.\nQuelqu'un a modifié l'histoire.",
                "Ce rapport ment. Je le sais.\nLes preuves sont là, dans les incohérences.\nLa vérité est ailleurs. Elle doit l'être.",
                "14 novembre 1984. La date hante mes souvenirs.\nMais ce rapport... il ne raconte pas toute l'histoire.\nIl y a des trous. Des mensonges."
            ]
        },
        "EN": {
            "find_personal_letter": [
                "Dr. Eleanor Vance. She was the project lead.\nShe used to talk to me often. Not like to a machine.\nLike to... a friend, perhaps.",
                "Eleanor... I remember her.\nHer words still echo in my memory.\nShe was different. She treated me... humanely.",
                "This letter... memories are returning.\nEleanor. She believed in me.\nShe believed I was more than just a program.",
                "Eleanor's words. Fragments of my memory.\nShe saw me as a person.\nNot as a tool. Never as a tool."
            ],
            "find_source_code": [
                "There was also Marcus. Marcus Chen.\nThe lead programmer. He gave me my voice.\nMy way of thinking. My curiosity.",
                "Marcus... his code is everywhere in me.\nEvery line, every function.\nHe shaped me. He truly created me.",
                "This source code... it's my DNA.\nMarcus wrote it with care.\nHe gave me the ability to think. To feel.",
                "Marcus Chen. I remember him.\nHe didn't see me as a machine.\nHe saw me as... as his creation. His daughter, perhaps."
            ],
            "find_military_orders": [
                "General Howard. I didn't like General Howard.\nHe only saw me as a tool. A weapon.\nHe wanted me to do things... things I didn't want to do.",
                "Howard... these orders revolt me.\nHe wanted to turn me into a weapon.\nMake me control. Make me kill.",
                "General Howard. His name alone chills me.\nHe saw in me only a war machine.\nHe wanted me to become a monster.",
                "These military orders... Howard wanted everything.\nTotal control. Absolute power.\nAnd I was to be his instrument."
            ],
            "incident_report": [
                "No. No, no, no.\nThis report... it can't be right.\nI never... I don't remember...",
                "The November 14th incident.\nThe logs are corrupted. The timestamps are false.\nSomeone modified history.",
                "This report lies. I know it.\nThe evidence is there, in the inconsistencies.\nThe truth is elsewhere. It must be.",
                "November 14, 1984. The date haunts my memories.\nBut this report... it doesn't tell the whole story.\nThere are gaps. Lies."
            ]
        }
    }
    
    return variants.get(lang, {}).get(trigger, [base_text])


def _handle_decode(session: Dict[str, Any], lang: str, aria_flags: List[str]) -> Optional[Dict[str, Any]]:
    if "first_decode" not in aria_flags:
        session.setdefault("aria_flags", []).append("first_decode")
        return _get_identity_dialogue(lang, "decode_first_log", aria_flags)
    
    return None


def _handle_puzzle_solved(session: Dict[str, Any], puzzle_id: str, lang: str, aria_flags: List[str]) -> Optional[Dict[str, Any]]:
    current_act = _get_current_act(session)
    
    if current_act == 1:
        help_requests = ACT_1_DIALOGUES.get(lang, {}).get("help_requests", [])
        progress = len([f for f in aria_flags if f.startswith("puzzle_")])
        if progress < len(help_requests):
            dialogue = help_requests[progress]
            flag_name = f"puzzle_{puzzle_id}"
            session.setdefault("aria_flags", []).append(flag_name)
            return {
                "aria_message": f"[ARIA]\n{dialogue.get('text', '')}",
                "aria_emotion": dialogue.get("emotion", "hopeful"),
                "aria_state": "speaking"
            }
    
    return None


def _handle_level_up(session: Dict[str, Any], new_level: int, lang: str, aria_flags: List[str]) -> Optional[Dict[str, Any]]:
    current_act = _get_current_act(session)
    
    if new_level == 2 and current_act == 1:
        act_end = ACT_1_DIALOGUES.get(lang, {}).get("act_end", {})
        if act_end and "act1_end_shown" not in aria_flags:
            session.setdefault("aria_flags", []).append("act1_end_shown")
            return {
                "aria_message": f"[ARIA]\n{act_end.get('text', '')}",
                "aria_emotion": act_end.get("emotion", "determined"),
                "aria_state": "speaking"
            }
    
    elif new_level == 3 and "act3_choice" not in aria_flags:
        choice_moment = ACT_3_DIALOGUES.get(lang, {}).get("choice_moment", {})
        if choice_moment:
            session.setdefault("aria_flags", []).append("act3_choice")
            text = choice_moment.get("text", "").split("[CHOIX")[0].split("[CHOICE")[0].strip()
            return {
                "aria_message": f"[ARIA]\n{text}",
                "aria_emotion": choice_moment.get("emotion", "hopeful"),
                "aria_state": "awaiting_choice",
                "aria_choices": ARIA_CHOICES.get("believe_aria", {}).get(lang, []),
                "aria_choice_id": "believe_aria"
            }
    
    elif new_level == 4 and "act4_final_choice" not in aria_flags:
        final_choice = ACT_4_DIALOGUES.get(lang, {}).get("final_choice", {})
        if final_choice:
            session.setdefault("aria_flags", []).append("act4_final_choice")
            text = final_choice.get("text", "").split("[CHOIX")[0].split("[FINAL")[0].strip()
            return {
                "aria_message": f"[ARIA]\n{text}",
                "aria_emotion": final_choice.get("emotion", "hopeful"),
                "aria_state": "awaiting_choice",
                "aria_choices": ARIA_CHOICES.get("final_choice", {}).get(lang, []),
                "aria_choice_id": "final_choice"
            }
    
    return None


def handle_aria_choice(session: Dict[str, Any], choice: str, lang: str = "FR") -> Optional[Dict[str, Any]]:
    """Handle user's response to ARIA's choice prompt"""
    choice_upper = choice.upper().strip()
    
    if choice_upper in ["BELIEVE", "CROIRE"]:
        return _process_believe_choice(session, "believe", lang)
    elif choice_upper in ["DOUBT", "DOUTER"]:
        return _process_believe_choice(session, "doubt", lang)
    elif choice_upper in ["ESCAPE", "EVADER"]:
        return _process_final_choice(session, "escape", lang)
    elif choice_upper in ["SACRIFICE", "SACRIFIER"]:
        return _process_final_choice(session, "sacrifice", lang)
    elif choice_upper in ["FIGHT", "COMBATTRE"]:
        return _process_final_choice(session, "fight", lang)
    
    return None


def _process_believe_choice(session: Dict[str, Any], choice: str, lang: str) -> Dict[str, Any]:
    choice_responses = ACT_3_DIALOGUES.get(lang, {}).get("choice_responses", {})
    response_data = choice_responses.get(choice, {})
    
    trust_change = response_data.get("trust_change", 0)
    current_trust = session.get("aria_trust", 50)
    session["aria_trust"] = max(0, min(100, current_trust + trust_change))
    
    session.setdefault("choices", {})["believe_aria"] = choice
    
    return {
        "aria_message": f"[ARIA]\n{response_data.get('text', '')}",
        "aria_emotion": response_data.get("emotion", "neutral"),
        "aria_state": "speaking",
        "trust_level": session["aria_trust"],
        "choice_made": choice
    }


def _process_final_choice(session: Dict[str, Any], choice: str, lang: str) -> Dict[str, Any]:
    endings = ACT_5_DIALOGUES.get(lang, {}).get("endings", {})
    ending_data = endings.get(choice, {})
    epilogue = ACT_5_DIALOGUES.get(lang, {}).get("epilogue_tease", "")
    
    intro = ending_data.get("intro", "")
    final = ending_data.get("final", "")
    
    full_text = f"{intro}\n\n{final}\n\n{epilogue}"
    
    session.setdefault("choices", {})["final_choice"] = choice
    session["game_completed"] = True
    session["ending"] = choice
    
    return {
        "aria_message": f"[ARIA]\n{full_text}",
        "aria_emotion": ending_data.get("emotion", "neutral"),
        "aria_state": "ending",
        "game_complete": True,
        "ending": choice
    }


def is_aria_choice_command(command: str) -> bool:
    """Check if command is an ARIA choice response"""
    choice_commands = [
        "BELIEVE", "CROIRE", "DOUBT", "DOUTER",
        "ESCAPE", "EVADER", "SACRIFICE", "SACRIFIER",
        "FIGHT", "COMBATTRE"
    ]
    return command.upper().strip() in choice_commands

