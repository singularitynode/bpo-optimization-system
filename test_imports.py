#!/usr/bin/env python3
import sys
import os
sys.path.insert(0, 'src')

def test_import_chain():
    """Test that all modules import correctly"""
    tests = [
        ("Core imports", [
            "from core import Evolver, Stability, Veto",
            "from core import DivineEngineering, LiquidEngineering",
            "from core import RigorProof, SelfMeta",
            "from core import run_all_theorems, get_theorem",
        ]),
        
        ("Engineering imports", [
            "from core.engineering import DivineEngineering, LiquidEngineering",
        ]),
        
        ("Services", [
            "from services.bpo_service import BpoService",
        ]),
        
        ("Utils", [
            "from utils.sandbox import Sandbox",
            "from utils.visualize import plot_sync_trajectory",
        ]),
        
        ("Config", [
            "from config import load_config",
        ]),
    ]
    
    all_passed = True
    for test_name, import_list in tests:
        print(f"\n🔧 Testing: {test_name}")
        for import_stmt in import_list:
            try:
                exec(import_stmt)
                print(f"  ✅ {import_stmt}")
            except Exception as e:
                print(f"  ❌ {import_stmt} -> {e}")
                all_passed = False
    
    return all_passed

if __name__ == "__main__":
    if test_import_chain():
        print("\n✅ ALL IMPORTS WORK!")
    else:
        print("\n❌ SOME IMPORTS FAILED!")
        sys.exit(1)