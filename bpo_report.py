print("💰 BPO BUSINESS REPORT")
print("="*40)

import sys
sys.path.insert(0, '.')

# Simple import test
try:
    # Test theorem bridge
    from src.services.theorem_bridge import BPOTheoremBridge
    
    bridge = BPOTheoremBridge()
    report = bridge.generate_bpo_report()
    
    print(f"Monthly Savings: {report.get('total_monthly_savings', '₱0')}")
    print(f"ROI: {report.get('roi_days', 0)} days")
    print(f"Efficiency: {report.get('efficiency_gain', '0%')}")
    
    print("\n🎯 System Status: OPERATIONAL")
    print("📊 Access: http://localhost:8000")
    
except ImportError:
    print("Installing packages...")
    import subprocess
    subprocess.run([sys.executable, "-m", "pip", "install", "requests"])
    
    print("\nRetrying...")
    from src.services.theorem_bridge import BPOTheoremBridge
    bridge = BPOTheoremBridge()
    report = bridge.generate_bpo_report()
    print(f"✅ Savings: {report.get('total_monthly_savings', '₱0')}")

input("\nPress Enter...")