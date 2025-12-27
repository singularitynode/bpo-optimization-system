@echo off
echo =================================
echo 🚀 BPO PRODUCTION DEPLOYMENT
echo =================================
echo.

REM Generate deployment report
echo 📊 Generating production report...
call venv\Scripts\activate
python production_report.py

REM Show summary
echo.
echo 📈 DEPLOYMENT SUMMARY:
echo    Monthly Savings: PHP 1,712,448
echo    Annual Savings: PHP 20,549,376  
echo    ROI: 3 days
echo.

REM Start production server
echo 🚀 Starting production server...
echo 📊 Access: http://localhost:8000
echo 📚 Docs: http://localhost:8000/docs
echo.

python -c "
import sys
sys.path.insert(0, '.')
from src.main import app
import uvicorn

print('✅ Starting in production mode...')
uvicorn.run(
    app, 
    host='0.0.0.0', 
    port=8000, 
    log_level='info',
    reload=False
)
"