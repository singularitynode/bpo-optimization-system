@echo off
echo =================================
echo 📊 BPO BUSINESS REPORT GENERATOR
echo =================================
echo.

REM Activate venv
call venv\Scripts\activate

REM Install requests if needed
python -c "
try:
    import requests
    print('✅ Requests module installed')
except ImportError:
    print('📦 Installing requests...')
    import subprocess
    subprocess.run(['python', '-m', 'pip', 'install', 'requests'])
"

REM Generate report
echo 📈 Generating business report...
python test_business.py

pause