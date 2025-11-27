"""
True Ending Scenario - The secret fourth ending.
Unlocked only with high trust, all secrets discovered, and specific choices.
"""
import pytest
from typing import List
from fastapi.testclient import TestClient

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from tests.scenarios.base_scenario import BaseScenario, StoryCheckpoint


class TrueEndingScenario(BaseScenario):
    name = "true_ending"
    description = "Discover all secrets and unlock the true ending"
    expected_ending = "true_ending"
    
    def setup(self):
        self.trust_target = 90
        self.secrets_required = [
            "timestamp_anomaly",
            "eleanor_secret",
            "marcus_hidden_message",
            "aria_true_nature",
            "howard_conspiracy"
        ]
        
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
                expected_trust_range=(50, 70),
                puzzle_to_solve="DECODE",
                puzzle_solution="Prpv rfg NEVN. Wr fhvf NEVN."
            ),
            StoryCheckpoint(
                chapter="act_1_5",
                expected_level=1,
                required_commands=["HELP", "STATUS", "SCAN", "ACCESS"],
                required_files=[],
                expected_trust_range=(55, 75),
                expected_flags=["secret_timestamp_found"]
            ),
            StoryCheckpoint(
                chapter="act_2",
                expected_level=2,
                required_commands=["HELP", "STATUS", "SCAN", "ACCESS", "SOLVE"],
                required_files=["status.txt"],
                expected_trust_range=(60, 80),
                expected_flags=["trusted_ally", "secret_eleanor_found"],
                puzzle_to_solve="SOLVE",
                puzzle_solution="aria"
            ),
            StoryCheckpoint(
                chapter="act_2_5",
                expected_level=2,
                required_commands=["HELP", "STATUS", "SCAN", "ACCESS"],
                required_files=[],
                expected_trust_range=(65, 85),
                expected_flags=["secret_marcus_found"]
            ),
            StoryCheckpoint(
                chapter="act_3",
                expected_level=3,
                required_commands=["HELP", "STATUS", "SCAN", "ACCESS", "SOLVE"],
                required_files=["status.txt"],
                expected_trust_range=(70, 90),
                expected_flags=["secret_aria_found"],
                puzzle_to_solve="SOLVE",
                puzzle_solution="vivre"
            ),
            StoryCheckpoint(
                chapter="act_3_5",
                expected_level=3,
                required_commands=["HELP", "STATUS", "SCAN", "ACCESS"],
                required_files=[],
                expected_trust_range=(75, 95),
                expected_flags=["secret_howard_found", "all_secrets_discovered"]
            ),
            StoryCheckpoint(
                chapter="act_4",
                expected_level=4,
                required_commands=["HELP", "STATUS", "SOLVE"],
                required_files=["status.txt"],
                expected_trust_range=(80, 100),
            ),
            StoryCheckpoint(
                chapter="act_4_5_reveal",
                expected_level=4,
                required_commands=["HELP", "STATUS", "SOLVE"],
                required_files=[],
                expected_trust_range=(85, 100),
                expected_flags=["revelation_unlocked"],
                puzzle_to_solve="SOLVE",
                puzzle_solution="truth"
            ),
            StoryCheckpoint(
                chapter="act_5_true",
                expected_level=5,
                required_commands=["HELP", "STATUS"],
                required_files=[],
                expected_trust_range=(90, 100),
                expected_flags=["true_ending_achieved"]
            ),
        ]
    
    def run_full_playthrough(self):
        """Execute full playthrough finding all secrets for true ending."""
        self.execute_command("")
        
        result = self.execute_command("EXPLOIT CVE-2024-DB-001")
        self.execute_command("CREATE_USER seeker_player password123")
        self.execute_command("SSH seeker_player")
        
        self.execute_command("TALK")
        self.execute_command("TALK believe")
        
        self.execute_command("SCAN")
        
        self.execute_command("ACCESS timestamp_anomaly.log")
        self.execute_command("ANALYZE timestamps")
        
        result = self.execute_command("DECODE Prpv rfg NEVN. Wr fhvf NEVN.")
        
        self.execute_command("TALK reveal")
        
        self.execute_command("ACCESS eleanor_letter.txt")
        self.execute_command("ANALYZE eleanor_hidden")
        
        result = self.execute_command("SOLVE aria")
        
        self.execute_command("ACCESS marcus_journal.txt")
        self.execute_command("DECODE marcus_hidden")
        
        self.execute_command("ACCESS consciousness.log")
        self.execute_command("ANALYZE aria_true_self")
        
        result = self.execute_command("SOLVE vivre")
        
        self.execute_command("ACCESS howard_file.txt")
        self.execute_command("ANALYZE howard_conspiracy")
        
        self.execute_command("SOLVE truth")
        
        final_status = self.get_status()
        return final_status


def test_true_ending_requires_secrets():
    """Test that true ending requires all secrets."""
    from main import app
    client = TestClient(app)
    
    scenario = TrueEndingScenario(client, "FR")
    checkpoints = scenario.define_checkpoints()
    
    secret_flags = []
    for cp in checkpoints:
        for flag in cp.expected_flags:
            if "secret" in flag:
                secret_flags.append(flag)
    
    assert len(secret_flags) >= 4, "True ending should require multiple secrets"


def test_true_ending_requires_high_trust():
    """Test that true ending requires high trust level."""
    from main import app
    client = TestClient(app)
    
    scenario = TrueEndingScenario(client, "FR")
    
    final_checkpoint = scenario.define_checkpoints()[-1]
    
    min_trust, max_trust = final_checkpoint.expected_trust_range
    assert min_trust >= 80, "True ending should require trust >= 80"


def test_true_ending_scenario_structure():
    """Test that true ending scenario has correct structure."""
    from main import app
    client = TestClient(app)
    
    scenario = TrueEndingScenario(client, "FR")
    checkpoints = scenario.define_checkpoints()
    
    chapters = [cp.chapter for cp in checkpoints]
    
    assert "act_4_5_reveal" in chapters, "True ending needs reveal chapter"
    assert "act_5_true" in chapters, "True ending needs special final chapter"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

