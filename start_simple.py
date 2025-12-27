import sys
sys.path.insert(0, '.')

# Quick test
try:
    from src.services.theorem_bridge import BPOTheoremBridge
    print("✅ Theorem Bridge loaded")
    
    bridge = BPOTheoremBridge()
    report = bridge.generate_bpo_report()
    print(f"💰 Savings: {report['total_monthly_savings']}")
    
    # Start server
    from src.main import app
    import uvicorn
    
    print("\n🚀 Starting server...")
    print("📊 http://localhost:8000")
    print("📚 http://localhost:8000/docs")
    
    uvicorn.run(app, host="0.0.0.0", port=8000)
    
except Exception as e:
    print(f"❌ Error: {e}")
    print("\n📦 Installing packages...")
    import subprocess
    subprocess.run([sys.executable, "-m", "pip", "install", "fastapi", "uvicorn", "numpy"])
    
    print("\n🔄 Retrying...")
    from src.main import app
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)