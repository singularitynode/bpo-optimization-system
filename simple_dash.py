print("="*50)
print("📊 BPO SYSTEM DASHBOARD")
print("="*50)

import sys
sys.path.insert(0, '.')

try:
    from src.services.theorem_bridge import BPOTheoremBridge
    bridge = BPOTheoremBridge()
    report = bridge.generate_bpo_report()
    
    print(f"💰 Monthly Savings: {report.get('total_monthly_savings', '₱0')}")
    print(f"📊 ROI: {report.get('roi_days', 0)} days")
    print(f"🚀 Efficiency: {report.get('efficiency_gain', '0%')}")
    
    print("\n✅ SYSTEM OPERATIONAL")
    print("🌐 http://localhost:8000")
    print("📚 http://localhost:8000/docs")
    
except Exception as e:
    print(f"❌ Error: {e}")
    print("Run: python -m pip install requests")

print("="*50)
input("Press Enter to exit...")