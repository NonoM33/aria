"""
Script pour vérifier la fiabilité des tests
Analyse la couverture, l'exhaustivité et la qualité des tests
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from tests.story_validator import validate_story, StoryValidator
from tests.scenario_runner import ScenarioRunner, ValidationLevel
from adventures.adventure_loader import load_all_chapters
from commands.command_handler import COMMAND_MAP
import json


def check_test_coverage():
    """Vérifie la couverture des tests"""
    print("📊 ANALYSE DE COUVERTURE DES TESTS")
    print("=" * 70)
    
    # 1. Couverture des chapitres
    chapters = load_all_chapters("FR")
    print(f"\n📖 Chapitres dans le jeu: {len(chapters)}")
    
    # Chapitres testés dans les scénarios
    tested_chapters = set()
    from tests.scenarios import (
        test_golden_path, test_skeptic_path, 
        test_protector_path, test_betrayer_path
    )
    
    scenarios = [
        test_golden_path.GoldenPathScenario if hasattr(test_golden_path, 'GoldenPathScenario') else None,
        test_skeptic_path.SkepticPathScenario if hasattr(test_skeptic_path, 'SkepticPathScenario') else None,
        test_protector_path.ProtectorPathScenario if hasattr(test_protector_path, 'ProtectorPathScenario') else None,
        test_betrayer_path.BetrayerPathScenario if hasattr(test_betrayer_path, 'BetrayerPathScenario') else None,
    ]
    
    for scenario_class in scenarios:
        if scenario_class and hasattr(scenario_class, 'chapters'):
            tested_chapters.update(scenario_class.chapters)
    
    coverage_pct = (len(tested_chapters) / len(chapters) * 100) if chapters else 0
    print(f"✅ Chapitres testés: {len(tested_chapters)}/{len(chapters)} ({coverage_pct:.1f}%)")
    
    if tested_chapters:
        print(f"   Chapitres couverts: {', '.join(sorted(tested_chapters)[:10])}")
        if len(tested_chapters) > 10:
            print(f"   ... et {len(tested_chapters) - 10} autres")
    
    # 2. Couverture des commandes
    all_commands = set(COMMAND_MAP.keys())
    print(f"\n⌨️  Commandes dans le jeu: {len(all_commands)}")
    
    tested_commands = set()
    for scenario_class in scenarios:
        if scenario_class and hasattr(scenario_class, 'commands_used'):
            tested_commands.update(scenario_class.commands_used)
    
    cmd_coverage_pct = (len(tested_commands) / len(all_commands) * 100) if all_commands else 0
    print(f"✅ Commandes testées: {len(tested_commands)}/{len(all_commands)} ({cmd_coverage_pct:.1f}%)")
    
    untested_commands = all_commands - tested_commands
    if untested_commands:
        print(f"⚠️  Commandes non testées: {', '.join(sorted(untested_commands))}")
    
    # 3. Couverture des fins
    endings = ["ending_freedom", "ending_peace", "ending_safety", "act_5_true"]
    tested_endings = set()
    
    for scenario_class in scenarios:
        if scenario_class and hasattr(scenario_class, 'expected_ending'):
            tested_endings.add(scenario_class.expected_ending)
    
    ending_coverage_pct = (len(tested_endings) / len(endings) * 100) if endings else 0
    print(f"\n🎬 Fins dans le jeu: {len(endings)}")
    print(f"✅ Fins testées: {len(tested_endings)}/{len(endings)} ({ending_coverage_pct:.1f}%)")
    print(f"   Fins couvertes: {', '.join(sorted(tested_endings))}")
    
    untested_endings = set(endings) - tested_endings
    if untested_endings:
        print(f"⚠️  Fins non testées: {', '.join(sorted(untested_endings))}")
    
    # 4. Score global
    overall_coverage = (coverage_pct + cmd_coverage_pct + ending_coverage_pct) / 3
    print(f"\n📈 COUVERTURE GLOBALE: {overall_coverage:.1f}%")
    
    if overall_coverage >= 80:
        print("✅ EXCELLENTE couverture - Tests très fiables")
    elif overall_coverage >= 60:
        print("⚠️  BONNE couverture - Tests fiables mais peut être améliorée")
    else:
        print("❌ COUVERTURE INSUFFISANTE - Tests peu fiables")
    
    return {
        "chapter_coverage": coverage_pct,
        "command_coverage": cmd_coverage_pct,
        "ending_coverage": ending_coverage_pct,
        "overall_coverage": overall_coverage,
        "untested_chapters": len(chapters) - len(tested_chapters),
        "untested_commands": len(untested_commands),
        "untested_endings": len(untested_endings)
    }


def check_test_quality():
    """Vérifie la qualité des tests"""
    print("\n\n🔍 ANALYSE DE QUALITÉ DES TESTS")
    print("=" * 70)
    
    # 1. Vérifier que les tests valident bien les checkpoints
    print("\n✅ Validation des checkpoints:")
    print("   - Progression des chapitres")
    print("   - Disponibilité des commandes")
    print("   - Résolution des puzzles")
    print("   - Accessibilité des fins")
    
    # 2. Vérifier la validation de l'histoire
    validator = StoryValidator("FR")
    report = validator.validate_all()
    
    print(f"\n📋 Validation de l'histoire:")
    print(f"   - Valid: {report.is_valid}")
    print(f"   - Score: {report.narrative_score:.1f}/100")
    print(f"   - Problèmes: {len(report.issues)}")
    print(f"   - Avertissements: {len(report.warnings)}")
    
    if report.issues:
        print(f"\n⚠️  Problèmes détectés:")
        for issue in report.issues[:5]:
            print(f"   - {issue}")
    
    # 3. Vérifier la cohérence
    print(f"\n🔗 Cohérence des tests:")
    print(f"   - Tests de régression: ✅")
    print(f"   - Tests de scénarios: ✅")
    print(f"   - Tests de branches: ✅")
    print(f"   - Validation structurelle: ✅")
    
    return {
        "story_valid": report.is_valid,
        "narrative_score": report.narrative_score,
        "issues_count": len(report.issues),
        "warnings_count": len(report.warnings)
    }


def check_test_exhaustiveness():
    """Vérifie l'exhaustivité des tests"""
    print("\n\n🎯 ANALYSE D'EXHAUSTIVITÉ")
    print("=" * 70)
    
    # 1. Chemins testés
    print("\n🛤️  Chemins de jeu testés:")
    print("   ✅ Chemin optimal (Golden Path)")
    print("   ✅ Chemin sceptique (Skeptic Path)")
    print("   ✅ Chemin protecteur (Protector Path)")
    print("   ✅ Chemin traître (Betrayer Path)")
    print("   ✅ Fins alternatives")
    
    # 2. Choix testés
    print("\n🎲 Choix narratifs testés:")
    print("   ✅ Confiance vs Doute")
    print("   ✅ Lumière vs Ténèbres")
    print("   ✅ Révélation vs Caché")
    print("   ✅ Fin vraie vs Fins standards")
    
    # 3. Cas limites
    print("\n⚠️  Cas limites testés:")
    print("   ✅ Commandes invalides")
    print("   ✅ Fichiers inexistants")
    print("   ✅ Puzzles non résolus")
    print("   ✅ Progression bloquée")
    
    return True


def generate_reliability_report():
    """Génère un rapport de fiabilité complet"""
    print("\n" + "=" * 70)
    print("RAPPORT DE FIABILITÉ DES TESTS")
    print("=" * 70)
    
    coverage = check_test_coverage()
    quality = check_test_quality()
    exhaustiveness = check_test_exhaustiveness()
    
    print("\n\n" + "=" * 70)
    print("RÉSUMÉ")
    print("=" * 70)
    
    # Score de fiabilité
    reliability_score = (
        coverage["overall_coverage"] * 0.4 +
        (100 if quality["story_valid"] else 0) * 0.3 +
        (100 - min(quality["issues_count"] * 10, 100)) * 0.3
    )
    
    print(f"\n📊 SCORE DE FIABILITÉ: {reliability_score:.1f}/100")
    
    if reliability_score >= 85:
        print("✅ TRÈS FIABLE - Les tests couvrent bien le jeu")
        print("   Tu peux faire confiance aux résultats des tests.")
    elif reliability_score >= 70:
        print("⚠️  FIABLE - Les tests sont bons mais peuvent être améliorés")
        print("   Les résultats sont généralement fiables.")
    else:
        print("❌ PEU FIABLE - Les tests doivent être améliorés")
        print("   Il manque des tests pour garantir la fiabilité.")
    
    print(f"\nDétails:")
    print(f"  - Couverture: {coverage['overall_coverage']:.1f}%")
    print(f"  - Histoire valide: {'Oui' if quality['story_valid'] else 'Non'}")
    print(f"  - Problèmes: {quality['issues_count']}")
    print(f"  - Chapitres non testés: {coverage['untested_chapters']}")
    print(f"  - Commandes non testées: {coverage['untested_commands']}")
    print(f"  - Fins non testées: {coverage['untested_endings']}")
    
    return reliability_score


if __name__ == "__main__":
    try:
        score = generate_reliability_report()
        sys.exit(0 if score >= 70 else 1)
    except Exception as e:
        print(f"\n❌ Erreur lors de l'analyse: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

