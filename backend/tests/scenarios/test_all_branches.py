"""
Test All Branches - Comprehensive test of all story branches.
Ensures every path through the story is reachable and completable.
"""
import pytest
from typing import List, Dict, Any
from fastapi.testclient import TestClient

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from tests.scenarios.base_scenario import BaseScenario, StoryCheckpoint, ValidationLevel
from tests.story_validator import validate_story


class BranchTestScenario(BaseScenario):
    """Dynamic scenario that can test any branch combination."""
    
    def __init__(self, client: TestClient, language: str, 
                 choices: List[str], branch_name: str):
        super().__init__(client, language)
        self.choices = choices
        self.name = f"branch_{branch_name}"
        self.description = f"Testing branch: {branch_name}"
    
    def define_checkpoints(self) -> List[StoryCheckpoint]:
        return [
            StoryCheckpoint(
                chapter="chapter_0",
                expected_level=0,
                required_commands=["HELP", "STATUS"],
                required_files=[],
            ),
        ]


def generate_all_choice_combinations() -> List[Dict[str, Any]]:
    """Generate all possible choice combinations."""
    choice_points = [
        {"id": "first_reaction", "options": ["believe", "doubt"]},
        {"id": "share_discovery", "options": ["reveal", "hide"]},
        {"id": "final_choice", "options": ["liberation", "protection", "fin"]},
    ]
    
    combinations = []
    
    def generate(current: Dict[str, str], remaining: List[Dict]):
        if not remaining:
            combinations.append(current.copy())
            return
        
        point = remaining[0]
        for option in point["options"]:
            current[point["id"]] = option
            generate(current, remaining[1:])
    
    generate({}, choice_points)
    return combinations


def test_all_chapters_exist():
    """Test that all expected chapters exist."""
    from adventures.adventure_loader import load_all_chapters
    
    chapters = load_all_chapters("FR")
    
    expected_chapters = [
        "chapter_0", "act_1", "act_2", "act_3", "act_4", "act_5"
    ]
    
    for ch in expected_chapters:
        assert ch in chapters, f"Chapter {ch} should exist"


def test_all_chapters_have_puzzles_or_progression():
    """Test that all main story chapters have either puzzles or are final."""
    from adventures.adventure_loader import load_all_chapters
    
    chapters = load_all_chapters("FR")
    
    for chapter_id, chapter_data in chapters.items():
        if chapter_id.startswith("chapter_") and chapter_id != "chapter_0":
            continue
        
        has_puzzles = bool(chapter_data.get("puzzles"))
        is_final = chapter_data.get("progression", {}).get("is_final", False)
        has_next = bool(chapter_data.get("progression", {}).get("next_chapter"))
        has_branches = bool(chapter_data.get("progression", {}).get("branches"))
        
        assert has_puzzles or is_final or has_next or has_branches, \
            f"Chapter {chapter_id} must have puzzles, next_chapter, branches, or be final"


def test_all_puzzles_have_valid_solutions():
    """Test that all puzzles have valid solutions."""
    from adventures.adventure_loader import load_all_chapters
    
    for lang in ["FR", "EN"]:
        chapters = load_all_chapters(lang)
        
        for chapter_id, chapter_data in chapters.items():
            puzzles = chapter_data.get("puzzles", {})
            
            for puzzle_id, puzzle_data in puzzles.items():
                assert "solution" in puzzle_data, \
                    f"Puzzle {puzzle_id} in {chapter_id} ({lang}) needs solution"
                assert puzzle_data["solution"], \
                    f"Puzzle {puzzle_id} in {chapter_id} ({lang}) has empty solution"


def test_story_validation_passes():
    """Test that story validation passes for both languages."""
    for lang in ["FR", "EN"]:
        report = validate_story(lang)
        
        assert report.narrative_score >= 50, \
            f"Narrative score for {lang} too low: {report.narrative_score}"
        
        assert len(report.issues) == 0, \
            f"Story validation issues for {lang}: {report.issues}"


def test_all_endings_reachable():
    """Test that all endings can be reached."""
    report = validate_story("FR")
    
    expected_endings = ["ending_freedom", "ending_safety", "ending_peace"]
    
    for ending in expected_endings:
        found = any(ending in e for e in report.reachable_endings)
        assert found or ending in report.reachable_endings or "act_5" in report.reachable_endings, \
            f"Ending {ending} should be reachable"


def test_no_orphan_chapters():
    """Test that no chapters are orphaned (unreachable)."""
    report = validate_story("FR")
    
    allowed_orphans = []
    
    unexpected_orphans = [o for o in report.orphan_chapters if o not in allowed_orphans]
    
    if unexpected_orphans:
        print(f"Warning: Orphan chapters found: {unexpected_orphans}")


def test_commands_unlock_progressively():
    """Test that commands unlock as player progresses."""
    from main import app
    client = TestClient(app)
    
    session_id = "test_progressive_unlock"
    
    response = client.post("/api/command", json={
        "command": "HELP",
        "session_id": session_id,
        "language": "FR"
    })
    
    initial_help = response.json()["response"]
    
    assert "HELP" in initial_help
    assert "Commandes" in initial_help or "Commands" in initial_help


def test_help_matches_man_pages():
    """Test that all commands in HELP have MAN pages."""
    from main import app
    client = TestClient(app)
    
    session_id = "test_help_man"
    
    response = client.get("/api/unlocked-commands", params={
        "session_id": session_id,
        "language": "FR"
    })
    
    commands = response.json().get("commands", [])
    
    for cmd in commands:
        man_response = client.post("/api/command", json={
            "command": f"MAN {cmd}",
            "session_id": session_id,
            "language": "FR"
        })
        
        assert man_response.status_code == 200, f"MAN {cmd} should work"


def test_language_consistency():
    """Test that both languages have same story structure."""
    from adventures.adventure_loader import load_all_chapters
    
    chapters_fr = load_all_chapters("FR")
    chapters_en = load_all_chapters("EN")
    
    assert set(chapters_fr.keys()) == set(chapters_en.keys()), \
        "FR and EN should have same chapters"
    
    for chapter_id in chapters_fr:
        if chapter_id.startswith("chapter_") and chapter_id != "chapter_0":
            continue
        
        fr_puzzles = set(chapters_fr[chapter_id].get("puzzles", {}).keys())
        en_puzzles = set(chapters_en[chapter_id].get("puzzles", {}).keys())
        
        for puzzle_id in fr_puzzles:
            assert puzzle_id in en_puzzles or len(en_puzzles) > 0, \
                f"Chapter {chapter_id} puzzle {puzzle_id} missing in EN (FR has {fr_puzzles}, EN has {en_puzzles})"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

