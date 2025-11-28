#!/bin/bash
# Script rapide pour vérifier que le jeu est terminable sans bugs

cd "$(dirname "$0")"

echo "╔════════════════════════════════════════════════════════════════════╗"
echo "║          VÉRIFICATION COMPLÈTE DU JEU SYSTEM_VOID                  ║"
echo "╚════════════════════════════════════════════════════════════════════╝"
echo ""

if [ ! -d "venv" ]; then
    echo "❌ Erreur: Environnement virtuel non trouvé"
    exit 1
fi

source venv/bin/activate

echo "📋 [1/3] Tests de régression..."
echo "─────────────────────────────────────────────────────────────────────"
python -m pytest tests/test_regression.py -v --tb=short -q
REGRESSION_EXIT=$?
echo ""

echo "📖 [2/3] Validation de l'histoire..."
echo "─────────────────────────────────────────────────────────────────────"
python -c "
from tests.story_validator import validate_story
report = validate_story('FR')
print(f'✅ Valid: {report.is_valid}')
print(f'📊 Score narratif: {report.narrative_score:.1f}/100')
print(f'⚠️  Problèmes: {len(report.issues)}')
print(f'⚠️  Avertissements: {len(report.warnings)}')
if report.issues:
    print('\n🔴 Problèmes détectés:')
    for issue in report.issues[:5]:
        print(f'   - {issue}')
if not report.is_valid:
    exit(1)
"
STORY_EXIT=$?
echo ""

echo "🎮 [3/3] Tests de scénarios complets..."
echo "─────────────────────────────────────────────────────────────────────"
python -m pytest tests/scenarios/ -v --tb=short -q
SCENARIOS_EXIT=$?
echo ""

echo "🔍 [BONUS] Vérification de la fiabilité des tests..."
echo "─────────────────────────────────────────────────────────────────────"
python verify_tests_reliability.py
RELIABILITY_EXIT=$?
echo ""

echo "╔════════════════════════════════════════════════════════════════════╗"
echo "║                          RÉSULTAT FINAL                            ║"
echo "╚════════════════════════════════════════════════════════════════════╝"

if [ $REGRESSION_EXIT -eq 0 ] && [ $STORY_EXIT -eq 0 ] && [ $SCENARIOS_EXIT -eq 0 ]; then
    echo "✅ TOUS LES TESTS SONT PASSÉS - Le jeu est terminable sans bugs !"
    exit 0
else
    echo "❌ CERTAINS TESTS ONT ÉCHOUÉ - Vérifiez les erreurs ci-dessus"
    exit 1
fi

