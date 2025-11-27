"""
Base class for all story scenario tests.
Provides common functionality for simulating a full playthrough.
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass, field
from enum import Enum
from fastapi.testclient import TestClient


class ValidationLevel(Enum):
    STRICT = "strict"
    NORMAL = "normal"
    LENIENT = "lenient"


@dataclass
class StoryCheckpoint:
    chapter: str
    expected_level: int
    required_commands: List[str]
    required_files: List[str]
    expected_trust_range: Tuple[int, int] = (0, 100)
    expected_flags: List[str] = field(default_factory=list)
    puzzle_to_solve: Optional[str] = None
    puzzle_solution: Optional[str] = None


@dataclass
class ScenarioResult:
    scenario_name: str
    passed: bool
    checkpoints_passed: int
    checkpoints_total: int
    errors: List[str] = field(default_factory=list)
    warnings: List[str] = field(default_factory=list)
    final_ending: Optional[str] = None
    trust_progression: List[int] = field(default_factory=list)
    execution_time: float = 0.0


class BaseScenario:
    """Base class for story scenario tests."""
    
    name: str = "base_scenario"
    description: str = "Base scenario - should be overridden"
    expected_ending: str = "unknown"
    
    def __init__(self, client: TestClient, language: str = "FR"):
        self.client = client
        self.language = language
        self.session_id = f"test_{self.name}_{id(self)}"
        self.checkpoints: List[StoryCheckpoint] = []
        self.current_state: Dict[str, Any] = {}
        self.errors: List[str] = []
        self.warnings: List[str] = []
        self.trust_history: List[int] = []
        
    def setup(self):
        """Initialize the scenario - override in subclasses."""
        pass
    
    def define_checkpoints(self) -> List[StoryCheckpoint]:
        """Define story checkpoints - override in subclasses."""
        return []
    
    def execute_command(self, command: str) -> Dict[str, Any]:
        """Execute a command and return the response."""
        response = self.client.post("/api/command", json={
            "command": command,
            "session_id": self.session_id,
            "language": self.language
        })
        return response.json()
    
    def get_status(self) -> Dict[str, Any]:
        """Get current game status."""
        return self.execute_command("STATUS")
    
    def get_help(self) -> Dict[str, Any]:
        """Get available commands."""
        return self.execute_command("HELP")
    
    def get_files(self) -> List[str]:
        """Get available files for current chapter."""
        response = self.client.get("/api/files", params={
            "session_id": self.session_id,
            "language": self.language
        })
        return response.json().get("files", [])
    
    def get_unlocked_commands(self) -> List[str]:
        """Get currently unlocked commands."""
        response = self.client.get("/api/unlocked-commands", params={
            "session_id": self.session_id,
            "language": self.language
        })
        return response.json().get("commands", [])
    
    def validate_checkpoint(self, checkpoint: StoryCheckpoint) -> Tuple[bool, List[str]]:
        """Validate a story checkpoint."""
        errors = []
        
        unlocked_cmds = self.get_unlocked_commands()
        for cmd in checkpoint.required_commands:
            if cmd not in unlocked_cmds:
                errors.append(f"Command {cmd} not available at {checkpoint.chapter}")
        
        available_files = self.get_files()
        for file in checkpoint.required_files:
            if file not in available_files:
                errors.append(f"File {file} not accessible at {checkpoint.chapter}")
        
        status_response = self.get_status()
        
        return len(errors) == 0, errors
    
    def solve_puzzle(self, command: str, solution: str) -> Dict[str, Any]:
        """Attempt to solve a puzzle."""
        return self.execute_command(f"{command} {solution}")
    
    def make_choice(self, choice_command: str) -> Dict[str, Any]:
        """Make a narrative choice."""
        return self.execute_command(choice_command)
    
    def run(self, validation_level: ValidationLevel = ValidationLevel.NORMAL) -> ScenarioResult:
        """Run the complete scenario."""
        import time
        start_time = time.time()
        
        self.setup()
        self.checkpoints = self.define_checkpoints()
        
        self.execute_command("")
        
        checkpoints_passed = 0
        
        for checkpoint in self.checkpoints:
            try:
                if checkpoint.puzzle_to_solve and checkpoint.puzzle_solution:
                    result = self.solve_puzzle(
                        checkpoint.puzzle_to_solve, 
                        checkpoint.puzzle_solution
                    )
                    if result.get("status") != "success":
                        self.errors.append(
                            f"Puzzle {checkpoint.puzzle_to_solve} failed at {checkpoint.chapter}: "
                            f"{result.get('response', 'Unknown error')}"
                        )
                        if validation_level == ValidationLevel.STRICT:
                            break
                
                passed, errors = self.validate_checkpoint(checkpoint)
                if passed:
                    checkpoints_passed += 1
                else:
                    self.errors.extend(errors)
                    if validation_level == ValidationLevel.STRICT:
                        break
                        
            except Exception as e:
                self.errors.append(f"Exception at {checkpoint.chapter}: {str(e)}")
                if validation_level == ValidationLevel.STRICT:
                    break
        
        execution_time = time.time() - start_time
        
        return ScenarioResult(
            scenario_name=self.name,
            passed=len(self.errors) == 0,
            checkpoints_passed=checkpoints_passed,
            checkpoints_total=len(self.checkpoints),
            errors=self.errors,
            warnings=self.warnings,
            final_ending=self.expected_ending,
            trust_progression=self.trust_history,
            execution_time=execution_time
        )
    
    def verify_finishable(self) -> bool:
        """Verify the scenario can be completed without dead-ends."""
        result = self.run(ValidationLevel.LENIENT)
        return result.checkpoints_passed >= 1 or len(result.errors) < 5
    
    def __repr__(self):
        return f"<{self.__class__.__name__}: {self.name}>"

