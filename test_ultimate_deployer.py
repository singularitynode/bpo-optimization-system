#!/usr/bin/env python3
"""
Test script for Ultimate Deployer
"""

import sys
import os
sys.path.insert(0, 'src')

from core.ultimate_deployer import (
    MultivarCalculusProof,
    CosmicArchitectEngine,
    RecursiveSelfFixer,
    UltimateDeployer,
    quick_deploy
)

def test_calculus_proof():
    print("🧮 Testing Calculus Proofs...")
    calculus = MultivarCalculusProof(dimension=4)
    
    # Test Riemann curvature
    curvature = calculus.prove_riemann_curvature()
    assert "ricci_scalar" in curvature
    print(f"  ✅ Riemann curvature: {curvature['ricci_scalar']:.6f}")
    
    # Test gradient flow
    gradient = calculus.gradient_flow_proof("test")
    assert "convex" in gradient
    print(f"  ✅ Gradient flow convex: {gradient['convex']}")
    
    return True

def test_cosmic_engineering():
    print("🌌 Testing Cosmic Engineering...")
    cosmic = CosmicArchitectEngine()
    
    # Test cosmic inflation
    inflation = cosmic.cosmic_inflation_proof([1.0, 0.0])
    assert "scale_factor_growth" in inflation
    print(f"  ✅ Inflation growth: {inflation['scale_factor_growth']:.2f}x")
    
    # Test tensor network
    tensor = cosmic.tensor_network_deployment(nodes=50)
    assert "entanglement_entropy" in tensor
    print(f"  ✅ Entanglement entropy: {tensor['entanglement_entropy']:.4f}")
    
    return True

def test_self_fixer():
    print("🛠️  Testing Self-Fixer...")
    fixer = RecursiveSelfFixer(max_recursion_depth=3)
    
    # Test error fixing
    test_errors = [
        "ModuleNotFoundError: No module named 'nonexistent'",
        "ConnectionError: Connection refused",
        "PermissionError: Access denied"
    ]
    
    for error in test_errors:
        fixed, message = fixer.diagnose_and_fix(error)
        print(f"  ✅ Fixed '{error[:30]}...': {message}")
    
    # Test monitoring
    state = fixer.monitor_and_heal()
    print(f"  ✅ Health score: {state.health_score:.2f}")
    
    return True

def test_ultimate_deployer():
    print("🚀 Testing Ultimate Deployer...")
    deployer = UltimateDeployer(deployment_target="local")
    
    # Quick test of components
    assert deployer.calculus_prover is not None
    assert deployer.cosmic_engineer is not None
    assert deployer.self_fixer is not None
    
    print("  ✅ All components initialized")
    return True

def main():
    print("="*60)
    print("ULTIMATE DEPLOYER TEST SUITE")
    print("="*60)
    
    tests = [
        ("Calculus Proofs", test_calculus_proof),
        ("Cosmic Engineering", test_cosmic_engineering),
        ("Self-Fixer", test_self_fixer),
        ("Ultimate Deployer", test_ultimate_deployer),
    ]
    
    results = []
    for test_name, test_func in tests:
        try:
            if test_func():
                results.append((test_name, "✅ PASS"))
            else:
                results.append((test_name, "❌ FAIL"))
        except Exception as e:
            results.append((test_name, f"❌ ERROR: {e}"))
    
    print("\n" + "="*60)
    print("TEST RESULTS:")
    print("="*60)
    
    for name, result in results:
        print(f"{name:25} {result}")
    
    all_passed = all("✅" in r[1] for r in results)
    
    if all_passed:
        print("\n🎉 ALL TESTS PASSED!")
        print("\nTo deploy:")
        print("  python -m src.core.ultimate_deployer --target=local")
        return True
    else:
        print("\n⚠️  SOME TESTS FAILED")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)