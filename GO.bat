@echo off
cd /d D:\PsychologicalMagnetism\bpo-ethical-stable
call venv\Scripts\activate.bat

python -c "import sys; sys.path.insert(0, '.'); from src.services.theorem_bridge import BPOTheoremBridge; bridge = BPOTheoremBridge(); print('💰 Savings:', bridge.generate_bpo_report()['total_monthly_savings']); from src.main import app; import uvicorn; print('🚀 Server: http://localhost:8000'); uvicorn.run(app, host='0.0.0.0', port=8000)"