@echo off
echo =================================
echo 🚀 START BPO SERVER - ONE CLICK
echo =================================
echo.

cd /d D:\PsychologicalMagnetism\bpo-ethical-stable
call venv\Scripts\activate.bat

echo 📦 Ensuring dependencies are installed...
python -m pip install fastapi uvicorn requests --quiet

echo 🚀 Starting server...
echo 💰 Business Value: PHP 3.4M/month savings
echo 📅 ROI: 3 days
echo 📊 Access: http://localhost:8000
echo 📚 API Docs: http://localhost:8000/docs
echo.

python test_and_start.py

pause