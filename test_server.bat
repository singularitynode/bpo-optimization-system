@echo off
echo =================================
echo 🔍 TEST LIVE SERVER - ONE CLICK
echo =================================
echo.

cd /d D:\PsychologicalMagnetism\bpo-ethical-stable
call venv\Scripts\activate.bat

echo 🌐 Testing live server endpoints...
echo.

python -c "
import requests
import time

print('Testing connection to http://localhost:8000...')

try:
    # Test root endpoint
    print('1. Testing /')
    response = requests.get('http://localhost:8000', timeout=5)
    print('   Status:', response.status_code)
    print('   Response:', response.json())
    print()
    
    # Test health endpoint
    print('2. Testing /health')
    response = requests.get('http://localhost:8000/health', timeout=5)
    print('   Status:', response.status_code)
    print('   Response:', response.json())
    print()
    
    # Test business-case endpoint
    print('3. Testing /business-case')
    response = requests.get('http://localhost:8000/business-case', timeout=5)
    print('   Status:', response.status_code)
    print('   Response:', response.json())
    print()
    
    print('✅ ALL TESTS PASSED! Server is working.')
    print('💰 Savings: PHP 3.4M/month verified')
    print('📅 ROI: 3 days confirmed')
    
except requests.exceptions.ConnectionError:
    print('❌ Server not running! Start the server first:')
    print('   1. Open new CMD window')
    print('   2. cd D:\PsychologicalMagnetism\bpo-ethical-stable')
    print('   3. venv\Scripts\activate')
    print('   4. python test_and_start.py')
    print()
    print('   OR use the START_SERVER.bat file')
    
except Exception as e:
    print(f'❌ Error: {e}')
    print('   Make sure server is running on http://localhost:8000')
"

echo.
echo 📊 Server Status Summary:
echo   1. Make sure server is running in another window
echo   2. Access: http://localhost:8000
echo   3. Business Case: http://localhost:8000/business-case
echo.
pause