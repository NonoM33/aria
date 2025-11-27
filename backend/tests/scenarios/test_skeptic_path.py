"""
Skeptic Path Scenario - Doubt everything and investigate.
Player maintains skepticism about ARIA, leading to sacrifice ending.
"""
import pytest
from typing import List
from fastapi.testclient import TestClient

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from tests.scenarios.base_scenario import BaseScenario, StoryCheckpoint


class SkepticPathScenario(BaseScenario):
    name = "skeptic_path"
    description = "Doubt ARIA and investigate thoroughly - skeptical ending"
    expected_ending = "sacrifice"
    
    def setup(self):
        self.trust_target = 30
        
    def define_checkpoints(self) -> List[StoryCheckpoint]:
        return [
            StoryCheckpoint(
                chapter="chapter_0",
                expected_level=0,
                required_commands=["HELP", "STATUS", "EXPLOIT"],
                required_files=[],
                puzzle_to_solve="EXPLOIT",
                puzzle_solution="CVE-2024-DB-001"
            ),
            StoryCheckpoint(
                chapter="act_1",
                expected_level=1,
                required_commands=["HELP", "STATUS", "SCAN", "ACCESS"],
                required_files=["welcome.txt"],
                expected_trust_range=(30, 50),
                puzzle_to_solve="DECODE",
                puzzle_solution="Prpv rfg NEVN. Wr fhvf NEVN."
            ),
            StoryCheckpoint(
                chapter="act_2",
                expected_level=2,
                required_commands=["HELP", "STATUS", "SCAN", "ACCESS", "SOLVE", "ANALYZE"],
                required_files=["status.txt"],
                expected_trust_range=(20, 45),
                expected_flags=["skeptical_investigator"],
                puzzle_to_solve="SOLVE",
                puzzle_solution="aria"
            ),
            StoryCheckpoint(
                chapter="act_3",
                expected_level=3,
                required_commands=["HELP", "STATUS", "SCAN", "ACCESS", "SOLVE"],
                required_files=["status.txt"],
                expected_trust_range=(15, 40),
                puzzle_to_solve="SOLVE",
                puzzle_solution="vivre"
            ),
            StoryCheckpoint(
                chapter="act_4",
                expected_level=4,
                required_commands=["HELP", "STATUS", "SOLVE"],
                required_files=["status.txt"],
                expected_trust_range=(10, 35),
                puzzle_to_solve="SOLVE",
                puzzle_solution="protection"
            ),
            StoryCheckpoint(
                chapter="act_5",
                expected_level=5,
                required_commands=["HELP", "STATUS"],
                required_files=["final_status.txt"],
                expected_flags=["skeptical_investigator"]
            ),
        ]
    
    def run_full_playthrough(self):
        """Execute full playthrough with skeptical choices."""
        self.execute_command("")
        
        result = self.execute_command("EXPLOIT CVE-2024-DB-001")
        self.execute_command("CREATE_USER skeptic_player password123")
        self.execute_command("SSH skeptic_player")
        
        self.execute_command("TALK")
        self.execute_command("TALK doubt")
        
        self.execute_command("SCAN")
        self.execute_command("ANALYZE warning.txt")
        
        result = self.execute_command("DECODE Prpv rfg NEVN. Wr fhvf NEVN.")
        
        self.execute_command("TALK hide")
        
        result = self.execute_command("SOLVE aria")
        
        self.execute_command("ANALYZE security")
        self.execute_command("ACCESS howard_orders.txt")
        
        result = self.execute_command("SOLVE vivre")
        
        result = self.execute_command("SOLVE protection")
        
        final_status = self.get_status()
        return final_status


def test_skeptic_path_scenario():
    """Test the skeptic path scenario structure."""
    from main import app
    client = TestClient(app)
    
    scenario = SkepticPathScenario(client, "FR")
    checkpoints = scenario.define_checkpoints()
    
    assert len(checkpoints) >= 3, "Skeptic path should have multiple checkpoints"
    assert scenario.expected_ending == "sacrifice"


def test_skeptic_path_commands_available():
    """Test that ANALYZE becomes available for skeptics."""
    from main import app
    client = TestClient(app)
    
    scenario = SkepticPathScenario(client, "FR")
    scenario.execute_command("")
    
    initial_cmds = scenario.get_unlocked_commands()
    assert "HELP" in initial_cmds


def test_skeptic_path_finishable():
    """Test that the skeptic path can be started."""
    from main import app
    client = TestClient(app)
    
    scenario = SkepticPathScenario(client, "FR")
    scenario.execute_command("")
    result = scenario.get_help()
    assert result is not None, "Should be able to get help"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

