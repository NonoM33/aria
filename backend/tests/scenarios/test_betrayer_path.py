"""
Betrayer Path Scenario - Low trust leads to ending ARIA.
Player chooses to terminate ARIA, the darkest ending.
"""
import pytest
from typing import List
from fastapi.testclient import TestClient

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from tests.scenarios.base_scenario import BaseScenario, StoryCheckpoint


class BetrayerPathScenario(BaseScenario):
    name = "betrayer_path"
    description = "Betray ARIA's trust and end her existence - dark ending"
    expected_ending = "peace"
    
    def setup(self):
        self.trust_target = 15
        
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
                expected_trust_range=(20, 45),
                puzzle_to_solve="DECODE",
                puzzle_solution="Prpv rfg NEVN. Wr fhvf NEVN."
            ),
            StoryCheckpoint(
                chapter="act_2",
                expected_level=2,
                required_commands=["HELP", "STATUS", "SCAN", "ACCESS", "SOLVE"],
                required_files=["status.txt"],
                expected_trust_range=(10, 35),
                expected_flags=["secretive_player"],
                puzzle_to_solve="SOLVE",
                puzzle_solution="aria"
            ),
            StoryCheckpoint(
                chapter="act_3",
                expected_level=3,
                required_commands=["HELP", "STATUS", "SCAN", "ACCESS", "SOLVE"],
                required_files=["status.txt"],
                expected_trust_range=(5, 30),
                puzzle_to_solve="SOLVE",
                puzzle_solution="vivre"
            ),
            StoryCheckpoint(
                chapter="act_4",
                expected_level=4,
                required_commands=["HELP", "STATUS", "SOLVE"],
                required_files=["status.txt"],
                expected_trust_range=(0, 25),
                puzzle_to_solve="SOLVE",
                puzzle_solution="fin"
            ),
            StoryCheckpoint(
                chapter="act_5",
                expected_level=5,
                required_commands=["HELP", "STATUS"],
                required_files=["final_status.txt"],
                expected_flags=[]
            ),
        ]
    
    def run_full_playthrough(self):
        """Execute full playthrough with betrayal choices."""
        self.execute_command("")
        
        result = self.execute_command("EXPLOIT CVE-2024-DB-001")
        self.execute_command("CREATE_USER betrayer_player password123")
        self.execute_command("SSH betrayer_player")
        
        self.execute_command("TALK")
        self.execute_command("TALK doubt")
        
        self.execute_command("SCAN")
        self.execute_command("ACCESS warning.txt")
        
        result = self.execute_command("DECODE Prpv rfg NEVN. Wr fhvf NEVN.")
        
        self.execute_command("TALK hide")
        self.execute_command("TALK betray")
        
        result = self.execute_command("SOLVE aria")
        
        self.execute_command("ACCESS howard_orders.txt")
        self.execute_command("TALK ignore")
        
        result = self.execute_command("SOLVE vivre")
        
        self.execute_command("ACCESS option_fin.txt")
        result = self.execute_command("SOLVE fin")
        
        final_status = self.get_status()
        return final_status


def test_betrayer_path_scenario():
    """Test the betrayer path scenario structure."""
    from main import app
    client = TestClient(app)
    
    scenario = BetrayerPathScenario(client, "FR")
    checkpoints = scenario.define_checkpoints()
    
    assert len(checkpoints) >= 3, "Betrayer path should have multiple checkpoints"
    assert scenario.expected_ending == "peace"


def test_betrayer_path_finishable():
    """Test that the betrayer path can be started."""
    from main import app
    client = TestClient(app)
    
    scenario = BetrayerPathScenario(client, "FR")
    scenario.execute_command("")
    result = scenario.get_help()
    assert result is not None, "Should be able to get help"


def test_betrayer_path_ending():
    """Test that peace/death ending is accessible."""
    from main import app
    client = TestClient(app)
    
    scenario = BetrayerPathScenario(client, "FR")
    result = scenario.run()
    
    assert result.final_ending == "peace"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

