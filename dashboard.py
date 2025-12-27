import requests
import json
from datetime import datetime

def get_system_status():
    """Get complete system status"""
    endpoints = {
        'health': 'http://localhost:8000/health',
        'theorems': 'http://localhost:8000/theorems',
        'metrics': 'http://localhost:8000/metrics'
    }
    
    status = {}
    for name, url in endpoints.items():
        try:
            response = requests.get(url, timeout=5)
            status[name] = {
                'status': 'online',
                'data': response.json()
            }
        except:
            status[name] = {'status': 'offline'}
    
    return status

def generate_dashboard():
    """Generate system dashboard"""
    print("="*60)
    print("📊 BPO SYSTEM DASHBOARD")
    print("="*60)
    print(f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    
    status = get_system_status()
    
    # Health
    health = status.get('health', {})
    if health.get('status') == 'online':
        print("✅ SYSTEM HEALTH: ONLINE")
        if 'data' in health:
            print(f"   Savings: {health['data'].get('savings', 'N/A')}")
    else:
        print("❌ SYSTEM HEALTH: OFFLINE")
    
    # Theorems
    theorems = status.get('theorems', {})
    if theorems.get('status') == 'online':
        data = theorems.get('data', {})
        print(f"✅ THEOREMS: {data.get('available', 0)} available")
        print(f"   Status: {data.get('status', 'N/A')}")
    
    print()
    print("🎯 ENDPOINTS:")
    print("   http://localhost:8000/          - System status")
    print("   http://localhost:8000/docs      - API documentation")
    print("   http://localhost:8000/health    - Health check")
    print("   http://localhost:8000/theorems  - Theorem listing")
    print()
    print("💰 BUSINESS IMPACT: PHP 187,500/month savings")
    print("="*60)

if __name__ == "__main__":
    generate_dashboard()