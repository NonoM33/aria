"""
Scenario Runner - Orchestrates running all story scenarios.
Provides comprehensive testing of all story paths.
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import time
import json
from typing import Dict, List, Type, Optional
from dataclasses import dataclass, field
from fastapi.testclient import TestClient

from main import app
from tests.scenarios.base_scenario import BaseScenario, ScenarioResult, ValidationLevel
from tests.story_validator import validate_story, ValidationReport


@dataclass
class RunnerReport:
    total_scenarios: int
    passed_scenarios: int
    failed_scenarios: int
    total_checkpoints: int
    passed_checkpoints: int
    execution_time: float
    scenario_results: List[ScenarioResult] = field(default_factory=list)
    story_validation: Optional[ValidationReport] = None
    branch_coverage: Dict[str, bool] = field(default_factory=dict)


class ScenarioRunner:
    """Runs all registered scenarios and generates reports."""
    
    def __init__(self, language: str = "FR"):
        self.language = language
        self.client = TestClient(app)
        self.scenarios: List[Type[BaseScenario]] = []
        self.results: List[ScenarioResult] = []
        
    def register_scenario(self, scenario_class: Type[BaseScenario]):
        """Register a scenario to be run."""
        self.scenarios.append(scenario_class)
    
    def register_all_scenarios(self):
        """Discover and register all scenarios from the scenarios package."""
        from tests.scenarios import (
            test_golden_path,
            test_skeptic_path,
            test_protector_path,
            test_betrayer_path,
        )
        
        if hasattr(test_golden_path, 'GoldenPathScenario'):
            self.register_scenario(test_golden_path.GoldenPathScenario)
        if hasattr(test_skeptic_path, 'SkepticPathScenario'):
            self.register_scenario(test_skeptic_path.SkepticPathScenario)
        if hasattr(test_protector_path, 'ProtectorPathScenario'):
            self.register_scenario(test_protector_path.ProtectorPathScenario)
        if hasattr(test_betrayer_path, 'BetrayerPathScenario'):
            self.register_scenario(test_betrayer_path.BetrayerPathScenario)
    
    def run_all(self, validation_level: ValidationLevel = ValidationLevel.NORMAL) -> RunnerReport:
        """Run all registered scenarios."""
        start_time = time.time()
        
        story_report = validate_story(self.language)
        
        for scenario_class in self.scenarios:
            scenario = scenario_class(self.client, self.language)
            result = scenario.run(validation_level)
            self.results.append(result)
        
        execution_time = time.time() - start_time
        
        passed = sum(1 for r in self.results if r.passed)
        failed = len(self.results) - passed
        total_checkpoints = sum(r.checkpoints_total for r in self.results)
        passed_checkpoints = sum(r.checkpoints_passed for r in self.results)
        
        branch_coverage = self._calculate_branch_coverage()
        
        return RunnerReport(
            total_scenarios=len(self.results),
            passed_scenarios=passed,
            failed_scenarios=failed,
            total_checkpoints=total_checkpoints,
            passed_checkpoints=passed_checkpoints,
            execution_time=execution_time,
            scenario_results=self.results,
            story_validation=story_report,
            branch_coverage=branch_coverage
        )
    
    def run_single(self, scenario_name: str, 
                   validation_level: ValidationLevel = ValidationLevel.NORMAL) -> Optional[ScenarioResult]:
        """Run a single scenario by name."""
        for scenario_class in self.scenarios:
            if scenario_class.name == scenario_name:
                scenario = scenario_class(self.client, self.language)
                return scenario.run(validation_level)
        return None
    
    def _calculate_branch_coverage(self) -> Dict[str, bool]:
        """Calculate which story branches have been covered."""
        coverage = {}
        
        for result in self.results:
            coverage[f"scenario_{result.scenario_name}"] = result.passed
            if result.final_ending:
                coverage[f"ending_{result.final_ending}"] = True
        
        return coverage
    
    def generate_report(self, report: RunnerReport, format: str = "text") -> str:
        """Generate a human-readable report."""
        if format == "json":
            return self._generate_json_report(report)
        return self._generate_text_report(report)
    
    def _generate_text_report(self, report: RunnerReport) -> str:
        """Generate text format report."""
        lines = []
        lines.append("=" * 70)
        lines.append("SCENARIO RUNNER REPORT")
        lines.append("=" * 70)
        lines.append("")
        
        lines.append("SUMMARY")
        lines.append("-" * 40)
        lines.append(f"Total Scenarios:    {report.total_scenarios}")
        lines.append(f"Passed:             {report.passed_scenarios}")
        lines.append(f"Failed:             {report.failed_scenarios}")
        lines.append(f"Checkpoints:        {report.passed_checkpoints}/{report.total_checkpoints}")
        lines.append(f"Execution Time:     {report.execution_time:.2f}s")
        lines.append("")
        
        if report.story_validation:
            sv = report.story_validation
            lines.append("STORY VALIDATION")
            lines.append("-" * 40)
            lines.append(f"Valid:              {sv.is_valid}")
            lines.append(f"Narrative Score:    {sv.narrative_score:.1f}/100")
            lines.append(f"Reachable Endings:  {', '.join(sv.reachable_endings)}")
            if sv.issues:
                lines.append(f"Issues:             {len(sv.issues)}")
            if sv.warnings:
                lines.append(f"Warnings:           {len(sv.warnings)}")
            lines.append("")
        
        lines.append("SCENARIO RESULTS")
        lines.append("-" * 40)
        for result in report.scenario_results:
            status = "PASS" if result.passed else "FAIL"
            lines.append(f"[{status}] {result.scenario_name}")
            lines.append(f"       Checkpoints: {result.checkpoints_passed}/{result.checkpoints_total}")
            lines.append(f"       Ending:      {result.final_ending}")
            lines.append(f"       Time:        {result.execution_time:.2f}s")
            
            if result.errors:
                lines.append(f"       Errors:")
                for error in result.errors[:3]:
                    lines.append(f"         - {error[:60]}...")
                if len(result.errors) > 3:
                    lines.append(f"         ... and {len(result.errors) - 3} more")
            lines.append("")
        
        lines.append("BRANCH COVERAGE")
        lines.append("-" * 40)
        for branch, covered in report.branch_coverage.items():
            status = "OK" if covered else "XX"
            lines.append(f"[{status}] {branch}")
        lines.append("")
        
        overall = "PASS" if report.failed_scenarios == 0 else "FAIL"
        lines.append("=" * 70)
        lines.append(f"OVERALL: {overall}")
        lines.append("=" * 70)
        
        return "\n".join(lines)
    
    def _generate_json_report(self, report: RunnerReport) -> str:
        """Generate JSON format report."""
        data = {
            "summary": {
                "total_scenarios": report.total_scenarios,
                "passed": report.passed_scenarios,
                "failed": report.failed_scenarios,
                "checkpoints": {
                    "passed": report.passed_checkpoints,
                    "total": report.total_checkpoints
                },
                "execution_time": report.execution_time
            },
            "story_validation": {
                "is_valid": report.story_validation.is_valid if report.story_validation else None,
                "narrative_score": report.story_validation.narrative_score if report.story_validation else None,
                "issues": report.story_validation.issues if report.story_validation else [],
                "warnings": report.story_validation.warnings[:10] if report.story_validation else []
            },
            "scenarios": [
                {
                    "name": r.scenario_name,
                    "passed": r.passed,
                    "checkpoints_passed": r.checkpoints_passed,
                    "checkpoints_total": r.checkpoints_total,
                    "ending": r.final_ending,
                    "errors": r.errors[:5],
                    "execution_time": r.execution_time
                }
                for r in report.scenario_results
            ],
            "branch_coverage": report.branch_coverage
        }
        return json.dumps(data, indent=2, ensure_ascii=False)


def run_all_scenarios(language: str = "FR", 
                      validation_level: ValidationLevel = ValidationLevel.NORMAL) -> RunnerReport:
    """Convenience function to run all scenarios."""
    runner = ScenarioRunner(language)
    runner.register_all_scenarios()
    return runner.run_all(validation_level)


if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Run story scenario tests")
    parser.add_argument("--language", "-l", default="FR", choices=["FR", "EN"])
    parser.add_argument("--format", "-f", default="text", choices=["text", "json"])
    parser.add_argument("--strict", "-s", action="store_true", help="Use strict validation")
    
    args = parser.parse_args()
    
    level = ValidationLevel.STRICT if args.strict else ValidationLevel.NORMAL
    
    runner = ScenarioRunner(args.language)
    runner.register_all_scenarios()
    report = runner.run_all(level)
    
    print(runner.generate_report(report, args.format))
    
    exit_code = 0 if report.failed_scenarios == 0 else 1
    sys.exit(exit_code)

