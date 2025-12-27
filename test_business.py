import sys
sys.path.insert(0, '.')

print("="*50)
print("🎯 BPO BUSINESS INSIGHTS")
print("="*50)

try:
    from src.services.theorem_bridge import BPOTheoremBridge
    
    bridge = BPOTheoremBridge()
    
    # Get optimization report
    report = bridge.generate_bpo_report({
        'monthly_cost': 1000000,
        'agent_count': 50,
        'calls_per_month': 12000
    })
    
    print(f"💰 Monthly Savings: {report.get('total_monthly_savings', '₱0')}")
    print(f"📊 ROI Days: {report.get('roi_days', 0)}")
    print(f"🚀 Efficiency Gain: {report.get('efficiency_gain', '0%')}")
    
    # Implementation roadmap
    print("\n📅 IMPLEMENTATION ROADMAP:")
    for phase in report.get('implementation_roadmap', []):
        print(f"  Phase: {phase.get('focus', 'N/A')}")
        print(f"    Duration: {phase.get('duration', 'N/A')}")
        print(f"    Expected Savings: {phase.get('expected_savings', '₱0')}")
        print()
    
except ImportError as e:
    print(f"❌ Error: {e}")
    print("\n📦 Installing packages...")
    import subprocess
    subprocess.run([sys.executable, "-m", "pip", "install", "requests"])
    
    print("\n🔄 Retrying...")
    from src.services.theorem_bridge import BPOTheoremBridge
    bridge = BPOTheoremBridge()
    report = bridge.generate_bpo_report()
    print(f"✅ Savings: {report.get('total_monthly_savings', '₱0')}")

input("\nPress Enter to exit...")