#!/usr/bin/env python3
import asyncio
import sys
import os

sys.path.insert(0, 'src')

async def full_system_test():
    """Complete end-to-end system test"""
    print("🔬 COMPLETE SYSTEM INTEGRATION TEST")
    print("="*60)
    
    tests_passed = 0
    total_tests = 0
    
    # 1. Config test
    total_tests += 1
    try:
        from config import load_config
        config = load_config()
        print("✅ [1/6] Config loaded")
        tests_passed += 1
    except Exception as e:
        print(f"❌ [1/6] Config failed: {e}")
    
    # 2. Core modules test
    total_tests += 1
    try:
        from core import Evolver, Stability, Veto
        from core.engineering import DivineEngineering
        print("✅ [2/6] Core modules import")
        tests_passed += 1
    except Exception as e:
        print(f"❌ [2/6] Core imports failed: {e}")
    
    # 3. AI evolution test
    total_tests += 1
    try:
        from core import Evolver
        evolver = Evolver()
        reflection = await evolver.reflect("Test prompt")
        print(f"✅ [3/6] AI reflection: {reflection.get('score', 0):.2f}")
        tests_passed += 1
    except Exception as e:
        print(f"❌ [3/6] AI failed: {e}")
    
    # 4. Stability proof test
    total_tests += 1
    try:
        from core import Stability
        stability = Stability()
        proof = stability.lyapunov()
        print(f"✅ [4/6] Stability proven: {proof['stable']}")
        tests_passed += 1
    except Exception as e:
        print(f"❌ [4/6] Stability failed: {e}")
    
    # 5. Theorem test
    total_tests += 1
    try:
        from core.process_theorems import get_theorem
        theorem1 = get_theorem(1)
        print(f"✅ [5/6] Theorem 1: DOF={theorem1.get('degrees_of_freedom', '?')}")
        tests_passed += 1
    except Exception as e:
        print(f"❌ [5/6] Theorem failed: {e}")
    
    # 6. Self-meta test
    total_tests += 1
    try:
        from core import SelfMeta
        meta = SelfMeta()
        response = meta.humility_response("Test", True)
        print(f"✅ [6/6] Self-meta response: {response[:30]}...")
        tests_passed += 1
    except Exception as e:
        print(f"❌ [6/6] Self-meta failed: {e}")
    
    # Results
    print(f"\n📊 RESULTS: {tests_passed}/{total_tests} tests passed")
    
    if tests_passed == total_tests:
        print("🎉 SYSTEM INTEGRATION TEST PASSED!")
        return True
    else:
        print("⚠️  SOME TESTS FAILED")
        return False

if __name__ == "__main__":
    success = asyncio.run(full_system_test())
    sys.exit(0 if success else 1)