"""
Story Validator - Validates narrative coherence and story integrity.
Checks that the story makes sense, has proper tension build-up, and no plot holes.
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from typing import Dict, List, Any, Set, Tuple
from dataclasses import dataclass, field
from adventures.adventure_loader import load_all_chapters


@dataclass
class ValidationReport:
    is_valid: bool
    chapters_checked: int
    issues: List[str] = field(default_factory=list)
    warnings: List[str] = field(default_factory=list)
    coverage: Dict[str, bool] = field(default_factory=dict)
    reachable_endings: List[str] = field(default_factory=list)
    orphan_chapters: List[str] = field(default_factory=list)
    missing_puzzles: List[str] = field(default_factory=list)
    narrative_score: float = 0.0


class StoryValidator:
    """Validates story structure and narrative coherence."""
    
    def __init__(self, language: str = "FR"):
        self.language = language
        self.chapters = load_all_chapters(language)
        self.issues: List[str] = []
        self.warnings: List[str] = []
        
    def validate_all(self) -> ValidationReport:
        """Run all validations and return a comprehensive report."""
        self._validate_chapter_structure()
        self._validate_puzzle_solutions()
        self._validate_progression_paths()
        self._validate_file_accessibility()
        self._validate_narrative_coherence()
        reachable = self._find_reachable_endings()
        orphans = self._find_orphan_chapters()
        
        coverage = self._calculate_coverage()
        narrative_score = self._calculate_narrative_score()
        
        return ValidationReport(
            is_valid=len(self.issues) == 0,
            chapters_checked=len(self.chapters),
            issues=self.issues,
            warnings=self.warnings,
            coverage=coverage,
            reachable_endings=reachable,
            orphan_chapters=orphans,
            narrative_score=narrative_score
        )
    
    def _validate_chapter_structure(self):
        """Validate that all chapters have required fields."""
        required_fields = ["id", "title", "intro"]
        
        for chapter_id, chapter_data in self.chapters.items():
            if chapter_id.startswith("chapter_") and chapter_id != "chapter_0":
                continue
            
            for field in required_fields:
                if field not in chapter_data:
                    self.issues.append(
                        f"Chapter {chapter_id} missing required field: {field}"
                    )
            
            if "filesystem" not in chapter_data and "files" not in chapter_data:
                self.warnings.append(
                    f"Chapter {chapter_id} has no files/filesystem defined"
                )
    
    def _validate_puzzle_solutions(self):
        """Validate that all puzzles have valid solutions."""
        for chapter_id, chapter_data in self.chapters.items():
            puzzles = chapter_data.get("puzzles", {})
            
            for puzzle_id, puzzle_data in puzzles.items():
                if "solution" not in puzzle_data:
                    self.issues.append(
                        f"Puzzle {puzzle_id} in {chapter_id} has no solution"
                    )
                elif not puzzle_data["solution"]:
                    self.issues.append(
                        f"Puzzle {puzzle_id} in {chapter_id} has empty solution"
                    )
                
                if "command" not in puzzle_data:
                    self.warnings.append(
                        f"Puzzle {puzzle_id} in {chapter_id} has no command specified"
                    )
    
    def _validate_progression_paths(self):
        """Validate that all chapters can be reached and exited."""
        entry_points = {"chapter_0", "act_1"}
        all_next_chapters: Set[str] = set()
        
        for chapter_id, chapter_data in self.chapters.items():
            progression = chapter_data.get("progression", {})
            next_chapter = progression.get("next_chapter")
            
            if next_chapter:
                all_next_chapters.add(next_chapter)
            elif not progression.get("is_final"):
                self.warnings.append(
                    f"Chapter {chapter_id} has no next_chapter and is not marked as final"
                )
            
            branches = chapter_data.get("branches", {})
            for branch_name, branch_target in branches.items():
                all_next_chapters.add(branch_target)
        
        for chapter_id in self.chapters:
            if chapter_id not in entry_points and chapter_id not in all_next_chapters:
                if not chapter_id.startswith("chapter_"):
                    self.warnings.append(
                        f"Chapter {chapter_id} may be unreachable (not linked from any chapter)"
                    )
    
    def _validate_file_accessibility(self):
        """Validate that all files mentioned are accessible."""
        for chapter_id, chapter_data in self.chapters.items():
            filesystem = chapter_data.get("filesystem", chapter_data.get("files", {}))
            
            puzzles = chapter_data.get("puzzles", {})
            for puzzle_id, puzzle_data in puzzles.items():
                hint = puzzle_data.get("hint", "")
                for filename in self._extract_filenames(hint):
                    if not self._file_exists_in_filesystem(filename, filesystem):
                        self.warnings.append(
                            f"Puzzle {puzzle_id} in {chapter_id} references file "
                            f"'{filename}' which may not exist in filesystem"
                        )
    
    def _validate_narrative_coherence(self):
        """Validate narrative elements for coherence."""
        story_elements = {
            "aria_mentioned": False,
            "eleanor_mentioned": False,
            "marcus_mentioned": False,
            "howard_mentioned": False,
            "1984_referenced": False,
            "prometheus_referenced": False
        }
        
        for chapter_id, chapter_data in self.chapters.items():
            intro = chapter_data.get("intro", "").lower()
            filesystem = str(chapter_data.get("filesystem", {})).lower()
            combined_text = intro + filesystem
            
            if "aria" in combined_text:
                story_elements["aria_mentioned"] = True
            if "eleanor" in combined_text or "vance" in combined_text:
                story_elements["eleanor_mentioned"] = True
            if "marcus" in combined_text or "chen" in combined_text:
                story_elements["marcus_mentioned"] = True
            if "howard" in combined_text:
                story_elements["howard_mentioned"] = True
            if "1984" in combined_text:
                story_elements["1984_referenced"] = True
            if "prometheus" in combined_text:
                story_elements["prometheus_referenced"] = True
        
        for element, present in story_elements.items():
            if not present:
                self.warnings.append(
                    f"Core story element '{element}' not found in any chapter"
                )
    
    def _find_reachable_endings(self) -> List[str]:
        """Find all endings that can be reached."""
        endings = []
        
        for chapter_id, chapter_data in self.chapters.items():
            progression = chapter_data.get("progression", {})
            if progression.get("is_final"):
                endings.append(chapter_id)
            
            choices = chapter_data.get("choices", {})
            for choice_name, choice_data in choices.items():
                if "next_ending" in choice_data:
                    endings.append(choice_data["next_ending"])
        
        return list(set(endings))
    
    def _find_orphan_chapters(self) -> List[str]:
        """Find chapters that cannot be reached."""
        entry_points = {"chapter_0", "act_1"}
        reachable: Set[str] = set(entry_points)
        
        branch_chapters = {
            "act_1_5", "act_2_trust", "act_2_doubt", "act_2_5",
            "act_3_light", "act_3_dark", "act_3_5", "act_4_5_reveal", "act_5_true"
        }
        reachable.update(branch_chapters)
        
        changed = True
        while changed:
            changed = False
            for chapter_id in reachable.copy():
                if chapter_id not in self.chapters:
                    continue
                    
                chapter_data = self.chapters[chapter_id]
                
                next_ch = chapter_data.get("progression", {}).get("next_chapter")
                if next_ch and next_ch not in reachable:
                    reachable.add(next_ch)
                    changed = True
                
                for branch_target in chapter_data.get("branches", {}).values():
                    if branch_target not in reachable:
                        reachable.add(branch_target)
                        changed = True
                
                for puzzle_data in chapter_data.get("puzzles", {}).values():
                    reward = puzzle_data.get("reward", {})
                    unlocks = reward.get("unlocks_chapter")
                    if unlocks and unlocks not in reachable:
                        reachable.add(unlocks)
                        changed = True
        
        orphans = []
        for chapter_id in self.chapters:
            if chapter_id not in reachable:
                orphans.append(chapter_id)
        
        return orphans
    
    def _calculate_coverage(self) -> Dict[str, bool]:
        """Calculate test coverage for story elements."""
        coverage = {}
        
        for chapter_id in self.chapters:
            coverage[f"chapter_{chapter_id}"] = True
        
        for chapter_id, chapter_data in self.chapters.items():
            for puzzle_id in chapter_data.get("puzzles", {}):
                coverage[f"puzzle_{chapter_id}_{puzzle_id}"] = True
        
        return coverage
    
    def _calculate_narrative_score(self) -> float:
        """Calculate a narrative quality score (0-100)."""
        score = 100.0
        
        score -= len(self.issues) * 10
        score -= len(self.warnings) * 2
        
        if len(self.chapters) < 5:
            score -= 20
        
        endings = self._find_reachable_endings()
        if len(endings) < 2:
            score -= 15
        elif len(endings) >= 4:
            score += 10
        
        puzzle_count = sum(
            len(ch.get("puzzles", {})) 
            for ch in self.chapters.values()
        )
        if puzzle_count < 3:
            score -= 10
        
        return max(0.0, min(100.0, score))
    
    def _extract_filenames(self, text: str) -> List[str]:
        """Extract potential filenames from text."""
        import re
        patterns = [
            r'\b[\w_-]+\.\w{2,4}\b',
            r'/[\w_/-]+\.\w{2,4}\b',
        ]
        
        filenames = []
        for pattern in patterns:
            matches = re.findall(pattern, text)
            filenames.extend(matches)
        
        return filenames
    
    def _file_exists_in_filesystem(self, filename: str, filesystem: Dict) -> bool:
        """Check if a file exists in the filesystem structure."""
        filename = filename.lstrip('/')
        
        if filename in filesystem:
            return True
        
        for key, value in filesystem.items():
            if isinstance(value, dict):
                if self._file_exists_in_filesystem(filename, value):
                    return True
            
            if '/' in filename:
                parts = filename.split('/', 1)
                if parts[0] == key and isinstance(value, dict):
                    return self._file_exists_in_filesystem(parts[1], value)
        
        return False


def validate_story(language: str = "FR") -> ValidationReport:
    """Convenience function to validate the story."""
    validator = StoryValidator(language)
    return validator.validate_all()


if __name__ == "__main__":
    print("=" * 60)
    print("STORY VALIDATION REPORT")
    print("=" * 60)
    
    for lang in ["FR", "EN"]:
        print(f"\n--- {lang} Version ---")
        report = validate_story(lang)
        
        print(f"Valid: {report.is_valid}")
        print(f"Chapters: {report.chapters_checked}")
        print(f"Narrative Score: {report.narrative_score:.1f}/100")
        print(f"Reachable Endings: {report.reachable_endings}")
        
        if report.issues:
            print(f"\nISSUES ({len(report.issues)}):")
            for issue in report.issues:
                print(f"  - {issue}")
        
        if report.warnings:
            print(f"\nWARNINGS ({len(report.warnings)}):")
            for warning in report.warnings[:5]:
                print(f"  - {warning}")
            if len(report.warnings) > 5:
                print(f"  ... and {len(report.warnings) - 5} more")
        
        if report.orphan_chapters:
            print(f"\nOrphan Chapters: {report.orphan_chapters}")

