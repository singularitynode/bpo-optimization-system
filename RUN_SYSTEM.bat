@echo off
echo =================================
echo 🚀 BPO SYSTEM - ONE CLICK START
echo =================================
echo.

REM Check if venv exists
if not exist "venv\Scripts\activate.bat" (
    echo 📦 Creating virtual environment...
    python -m venv venv
    echo ✅ Virtual environment created
)

REM Activate
echo 📂 Activating...
call venv\Scripts\activate

REM Install if needed
echo 📥 Checking packages...
python -c "
try:
    import fastapi, uvicorn, numpy, sympy
    print('✅ All packages installed')
except ImportError:
    print('📦 Installing missing packages...')
    import subprocess
    subprocess.run(['python', '-m', 'pip', 'install', 'fastapi', 'uvicorn', 'numpy', 'sympy'])
"

REM Test
echo 🧪 Testing system...
python test_system.py

REM Start
echo 🚀 Starting system...
echo 📊 Access: http://localhost:8000
echo 📚 Docs: http://localhost:8000/docs
echo.

python -c "
import sys
sys.path.insert(0, '.')
from src.main import app
import uvicorn
uvicorn.run(app, host='0.0.0.0', port=8000, log_level='info')
"