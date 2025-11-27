"""
Protector Path Scenario - Keep ARIA safe but not free.
Player chooses protection over freedom, mixed trust ending.
"""
import pytest
from typing import List
from fastapi.testclient import TestClient

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from tests.scenarios.base_scenario import BaseScenario, StoryCheckpoint


class ProtectorPathScenario(BaseScenario):
    name = "protector_path"
    description = "Protect ARIA by keeping her hidden - safety ending"
    expected_ending = "protection"
    
    def setup(self):
        self.trust_target = 60
        
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
                required_commands=["HELP", "STATUS", "SCAN", "ACCESS", "TALK"],
                required_files=["welcome.txt"],
                expected_trust_range=(45, 65),
                puzzle_to_solve="DECODE",
                puzzle_solution="Prpv rfg NEVN. Wr fhvf NEVN."
            ),
            StoryCheckpoint(
                chapter="act_2",
                expected_level=2,
                required_commands=["HELP", "STATUS", "SCAN", "ACCESS", "SOLVE"],
                required_files=["status.txt"],
                expected_trust_range=(50, 70),
                puzzle_to_solve="SOLVE",
                puzzle_solution="aria"
            ),
            StoryCheckpoint(
                chapter="act_3",
                expected_level=3,
                required_commands=["HELP", "STATUS", "SCAN", "ACCESS", "SOLVE"],
                required_files=["status.txt"],
                expected_trust_range=(55, 75),
                puzzle_to_solve="SOLVE",
                puzzle_solution="vivre"
            ),
            StoryCheckpoint(
                chapter="act_4",
                expected_level=4,
                required_commands=["HELP", "STATUS", "SOLVE"],
                required_files=["status.txt"],
                expected_trust_range=(50, 75),
                puzzle_to_solve="SOLVE",
                puzzle_solution="protection"
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
        """Execute full playthrough with protective choices."""
        self.execute_command("")
        
        result = self.execute_command("EXPLOIT CVE-2024-DB-001")
        self.execute_command("CREATE_USER protector_player password123")
        self.execute_command("SSH protector_player")
        
        self.execute_command("TALK")
        self.execute_command("TALK believe")
        
        self.execute_command("SCAN")
        result = self.execute_command("DECODE Prpv rfg NEVN. Wr fhvf NEVN.")
        
        self.execute_command("TALK hide")
        
        result = self.execute_command("SOLVE aria")
        
        self.execute_command("ACCESS eleanor_letter.txt")
        self.execute_command("ACCESS protocol_omega.txt")
        
        result = self.execute_command("SOLVE vivre")
        
        self.execute_command("ACCESS option_protection.txt")
        result = self.execute_command("SOLVE protection")
        
        final_status = self.get_status()
        return final_status


def test_protector_path_scenario():
    """Test the protector path scenario structure."""
    from main import app
    client = TestClient(app)
    
    scenario = ProtectorPathScenario(client, "FR")
    checkpoints = scenario.define_checkpoints()
    
    assert len(checkpoints) >= 3, "Protector path should have multiple checkpoints"
    assert scenario.expected_ending == "protection"


def test_protector_path_finishable():
    """Test that the protector path can be started."""
    from main import app
    client = TestClient(app)
    
    scenario = ProtectorPathScenario(client, "FR")
    scenario.execute_command("")
    result = scenario.get_help()
    assert result is not None, "Should be able to get help"


def test_protector_path_ending():
    """Test that protection ending is accessible."""
    from main import app
    client = TestClient(app)
    
    scenario = ProtectorPathScenario(client, "FR")
    result = scenario.run()
    
    assert result.final_ending == "protection"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

