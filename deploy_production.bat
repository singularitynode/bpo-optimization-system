@echo off
echo =================================
echo 🚀 BPO PRODUCTION DEPLOYMENT
echo =================================
echo.

REM Stop existing server
echo 🛑 Stopping existing services...
taskkill /F /IM python.exe 2>nul
taskkill /F /IM uvicorn.exe 2>nul

REM Start fresh
echo 📦 Starting production server...
call venv\Scripts\activate

REM Create production .env if not exists
if not exist ".env.production" (
    echo ⚙️ Creating production environment...
    echo # PRODUCTION SETTINGS > .env.production
    echo API_PORT=8000 >> .env.production
    echo DEBUG=False >> .env.production
    echo SECRET_KEY=generated-production-key >> .env.production
)

REM Start with production settings
echo 🚀 Starting server (production mode)...
python -c "
import sys
sys.path.insert(0, '.')
from src.main import app
import uvicorn
uvicorn.run(app, host='0.0.0.0', port=8000, log_level='info')
"

pause