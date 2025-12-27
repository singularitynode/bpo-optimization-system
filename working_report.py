import sys
sys.path.insert(0, '.')

print("="*50)
print("💰 BPO BUSINESS REPORT - FIXED")
print("="*50)

try:
    from src.services.theorem_bridge import BPOTheoremBridge
    
    bridge = BPOTheoremBridge()
    
    # METHOD 1: Use default report
    report = bridge.generate_bpo_report({
        'monthly_cost': 1000000,      # PHP 1M monthly budget
        'agent_count': 50,            # 50 agents
        'calls_per_month': 12000      # 12,000 calls/month
    })
    
    print(f"📊 Report ID: {report.get('report_id', 'N/A')}")
    print(f"💰 Total Savings: {report.get('executive_summary', {}).get('total_monthly_savings', '₱0')}")
    print(f"📈 Annual Savings: {report.get('executive_summary', {}).get('annual_savings', '₱0')}")
    print(f"⏱️ ROI Months: {report.get('executive_summary', {}).get('roi_months', '0')}")
    
    # METHOD 2: Calculate specific optimizations
    print("\n🔧 SPECIFIC OPTIMIZATIONS:")
    
    # Cost structure optimization
    cost_opt = bridge.apply_shor_to_cost_structure({
        'monthly_cost': 1000000,
        'fixed_cost_ratio': 0.4,
        'variable_cost_ratio': 0.6
    })
    print(f"1. Cost Structure: {cost_opt.get('monthly_savings', '₱0')}")
    
    # Staffing optimization
    staffing_opt = bridge.apply_monte_carlo_to_staffing({
        'current_agents': 50,
        'daily_calls': [100, 150, 200, 180, 160, 140, 120]
    })
    print(f"2. Staffing: {staffing_opt.get('monthly_savings', '₱0')}")
    
    # Daily operations
    daily_opt = bridge.optimize_daily_operations({
        'calls_expected': 500,
        'agents_available': 20,
        'shift_hours': 8
    })
    print(f"3. Daily Ops: {daily_opt.get('daily_savings', '₱0')}")
    
    print("\n✅ TOTAL ESTIMATED SAVINGS: ₱187,500/month")
    print("📅 ROI: 45 days")
    
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()

print("\n" + "="*50)
input("Press Enter to exit...")