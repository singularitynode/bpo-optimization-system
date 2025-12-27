#!/usr/bin/env python3
"""
Quick test to verify bootstrap imports work
"""

import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

def test_imports():
    print("🔧 Testing imports...")
    
    try:
        from core import Evolver, Stability, Veto
        from core import DivineEngineering, LiquidEngineering
        from core import RigorProof, SelfMeta
        from core import run_all_theorems, get_theorem
        
        print("✅ All core imports successful!")
        
        # Test creating instances
        stability = Stability()
        print(f"✅ Stability proof: {stability.lyapunov()['stable']}")
        
        veto = Veto()
        print(f"✅ Veto rate: {veto.check_rate()*100:.1f}%")
        
        return True
        
    except ImportError as e:
        print(f"❌ Import failed: {e}")
        return False

def test_config():
    print("\n🔧 Testing configuration...")
    
    try:
        from config import load_config
        config = load_config()
        print(f"✅ Config loaded: {len(config)} parameters")
        print(f"   Deployment: {'Production' if config.get('aws_access_key') else 'Development'}")
        return True
        
    except Exception as e:
        print(f"❌ Config failed: {e}")
        return False

if __name__ == "__main__":
    print("=" * 60)
    print("BPO SYSTEM IMPORT TEST")
    print("=" * 60)
    
    imports_ok = test_imports()
    config_ok = test_config()
    
    if imports_ok and config_ok:
        print("\n✅ ALL TESTS PASSED - System ready!")
        print("\nNext steps:")
        print("1. python bootstrap.py --validate")
        print("2. python bootstrap.py")
        sys.exit(0)
    else:
        print("\n❌ TESTS FAILED - Check installation")
        sys.exit(1)