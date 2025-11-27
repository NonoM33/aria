#!/bin/bash
# Run all story scenario tests
# Usage: ./run_all_scenarios.sh [--strict] [--json] [--language FR|EN]

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BACKEND_DIR="$(dirname "$SCRIPT_DIR")"

cd "$BACKEND_DIR"

if [ ! -d "venv" ]; then
    echo "Error: Virtual environment not found. Run from backend directory."
    exit 1
fi

source venv/bin/activate

export PYTHONPATH="$BACKEND_DIR:$PYTHONPATH"

echo "========================================"
echo "  SYSTEM_VOID Story Test Suite"
echo "========================================"
echo ""

STRICT=""
FORMAT="text"
LANGUAGE="FR"

while [[ $# -gt 0 ]]; do
    case $1 in
        --strict|-s)
            STRICT="--strict"
            shift
            ;;
        --json|-j)
            FORMAT="json"
            shift
            ;;
        --language|-l)
            LANGUAGE="$2"
            shift 2
            ;;
        *)
            echo "Unknown option: $1"
            exit 1
            ;;
    esac
done

echo "[1/4] Running Story Validator..."
echo "----------------------------------------"
python -c "
from tests.story_validator import validate_story
report = validate_story('$LANGUAGE')
print(f'Valid: {report.is_valid}')
print(f'Narrative Score: {report.narrative_score:.1f}/100')
print(f'Issues: {len(report.issues)}')
print(f'Warnings: {len(report.warnings)}')
if report.issues:
    for issue in report.issues[:3]:
        print(f'  - {issue}')
"
echo ""

echo "[2/4] Running Unit Tests..."
echo "----------------------------------------"
python -m pytest tests/scenarios/ -v --tb=short -q 2>/dev/null || true
echo ""

echo "[3/4] Running Scenario Tests..."
echo "----------------------------------------"
python -c "
from tests.scenario_runner import ScenarioRunner, ValidationLevel
from tests.scenarios.test_golden_path import GoldenPathScenario
from tests.scenarios.test_skeptic_path import SkepticPathScenario
from tests.scenarios.test_protector_path import ProtectorPathScenario
from tests.scenarios.test_betrayer_path import BetrayerPathScenario

runner = ScenarioRunner('$LANGUAGE')
runner.register_scenario(GoldenPathScenario)
runner.register_scenario(SkepticPathScenario)
runner.register_scenario(ProtectorPathScenario)
runner.register_scenario(BetrayerPathScenario)

level = ValidationLevel.STRICT if '$STRICT' else ValidationLevel.NORMAL
report = runner.run_all(level)

print(runner.generate_report(report, '$FORMAT'))
" || true
echo ""

echo "[4/4] Running Branch Coverage..."
echo "----------------------------------------"
python -m pytest tests/scenarios/test_all_branches.py -v --tb=short -q 2>/dev/null || true
echo ""

echo "========================================"
echo "  Test Suite Complete"
echo "========================================"

python -c "
from tests.story_validator import validate_story
report = validate_story('$LANGUAGE')
if report.is_valid and report.narrative_score >= 70:
    print('Overall: PASS')
    exit(0)
else:
    print('Overall: FAIL')
    exit(1)
" 2>/dev/null

exit $?

