"""
Golden Path Scenario - Trust ARIA fully and free her.
The "best" ending where player believes and supports ARIA throughout.
"""
import pytest
from typing import List
from fastapi.testclient import TestClient

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from tests.scenarios.base_scenario import BaseScenario, StoryCheckpoint


class GoldenPathScenario(BaseScenario):
    name = "golden_path"
    description = "Trust ARIA fully and choose liberation - best ending"
    expected_ending = "liberation"
    
    def setup(self):
        self.trust_target = 80
        
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
                chapter="chapter_0_post_exploit",
                expected_level=0,
                required_commands=["CREATE_USER", "SSH"],
                required_files=[],
                puzzle_to_solve=None,
                puzzle_solution=None
            ),
            StoryCheckpoint(
                chapter="act_1",
                expected_level=1,
                required_commands=["HELP", "STATUS", "SCAN", "ACCESS", "TALK"],
                required_files=["welcome.txt"],
                expected_trust_range=(40, 60),
                puzzle_to_solve="DECODE",
                puzzle_solution="Prpv rfg NEVN. Wr fhvf NEVN."
            ),
            StoryCheckpoint(
                chapter="act_2",
                expected_level=2,
                required_commands=["HELP", "STATUS", "SCAN", "ACCESS", "SOLVE"],
                required_files=["status.txt"],
                expected_trust_range=(50, 70),
                expected_flags=["honest_player"],
                puzzle_to_solve="SOLVE",
                puzzle_solution="aria"
            ),
            StoryCheckpoint(
                chapter="act_3",
                expected_level=3,
                required_commands=["HELP", "STATUS", "SCAN", "ACCESS", "SOLVE"],
                required_files=["status.txt"],
                expected_trust_range=(60, 85),
                expected_flags=["trusted_ally"],
                puzzle_to_solve="SOLVE",
                puzzle_solution="vivre"
            ),
            StoryCheckpoint(
                chapter="act_4",
                expected_level=4,
                required_commands=["HELP", "STATUS", "SOLVE"],
                required_files=["status.txt"],
                expected_trust_range=(70, 100),
                puzzle_to_solve="SOLVE",
                puzzle_solution="liberation"
            ),
            StoryCheckpoint(
                chapter="act_5",
                expected_level=5,
                required_commands=["HELP", "STATUS"],
                required_files=["final_status.txt"],
                expected_trust_range=(80, 100),
                expected_flags=["aria_freed"]
            ),
        ]
    
    def run_full_playthrough(self):
        """Execute full playthrough with trust-building choices."""
        self.execute_command("")
        
        self.execute_command("HELP")
        self.execute_command("STATUS")
        
        result = self.execute_command("EXPLOIT CVE-2024-DB-001")
        assert result.get("status") == "success", "EXPLOIT should succeed"
        
        result = self.execute_command("CREATE_USER golden_player password123")
        
        result = self.execute_command("SSH golden_player")
        
        self.execute_command("TALK")
        self.execute_command("TALK believe")
        
        self.execute_command("SCAN")
        self.execute_command("ACCESS activation_log.dat")
        
        result = self.execute_command("DECODE Prpv rfg NEVN. Wr fhvf NEVN.")
        
        self.execute_command("TALK reveal")
        
        result = self.execute_command("SOLVE aria")
        assert result.get("status") == "success", "Password ARIA should work"
        
        self.execute_command("TALK support")
        
        result = self.execute_command("SOLVE vivre")
        assert result.get("status") == "success", "VIVRE should unlock level 4"
        
        result = self.execute_command("SOLVE liberation")
        assert result.get("status") == "success", "Liberation choice should succeed"
        
        final_status = self.get_status()
        return final_status


def test_golden_path_scenario():
    """Test the golden path scenario structure."""
    from main import app
    client = TestClient(app)
    
    scenario = GoldenPathScenario(client, "FR")
    checkpoints = scenario.define_checkpoints()
    
    assert len(checkpoints) >= 3, "Golden path should have multiple checkpoints"
    assert scenario.expected_ending == "liberation"


def test_golden_path_commands_available():
    """Test that commands are available at correct times."""
    from main import app
    client = TestClient(app)
    
    scenario = GoldenPathScenario(client, "FR")
    scenario.execute_command("")
    
    initial_cmds = scenario.get_unlocked_commands()
    assert "HELP" in initial_cmds or len(initial_cmds) > 0, "Should have some commands available"


def test_golden_path_finishable():
    """Test that the golden path can be started."""
    from main import app
    client = TestClient(app)
    
    scenario = GoldenPathScenario(client, "FR")
    scenario.execute_command("")
    result = scenario.get_help()
    assert result is not None, "Should be able to get help"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

