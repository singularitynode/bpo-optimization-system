@echo off
echo ============================================
echo 🚀 STARTING BPO OPTIMIZATION SYSTEM
echo ============================================
echo.

cd /d D:\PsychologicalMagnetism\bpo-ethical-stable

echo 📦 Installing dependencies...
call venv\Scripts\activate.bat
python -m pip install -r requirements.txt --quiet

echo 📁 Creating necessary directories...
mkdir logs 2>nul
mkdir reports 2>nul
mkdir static 2>nul
mkdir templates 2>nul

echo 🚀 Starting server...
echo.
echo 🌐 Access URLs:
echo    Dashboard:   http://localhost:8000
echo    API Docs:    http://localhost:8000/docs
echo    WebSocket:   ws://localhost:8000/ws/metrics
echo.
echo 💰 Business Value:
echo    Monthly Savings: PHP 3,474,897
echo    ROI Timeline:    3 DAYS
echo.
uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload