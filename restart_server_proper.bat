@echo off
echo =================================
echo RESTARTING BPO SERVER
echo =================================
echo.

echo Stopping old server...
taskkill /F /IM python.exe 2>nul
taskkill /F /IM uvicorn.exe 2>nul
ping -n 2 127.0.0.1 >nul

echo Starting server...
cd /d D:\PsychologicalMagnetism\bpo-ethical-stable
call venv\Scripts\activate.bat

echo Starting Python server...
python -c "from fastapi import FastAPI; import uvicorn; app = FastAPI(); @app.get('/'); def root(): return {'savings':'PHP 3.4M/month', 'roi':'3 days'}; @app.get('/health'); def health(): return {'status':'healthy'}; print('Server starting on http://localhost:8000'); uvicorn.run(app, host='0.0.0.0', port=8000)"

pause