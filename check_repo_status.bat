@echo off
echo ========================================
echo 🔍 CHECKING GITHUB REPOSITORY STATUS
echo ========================================
echo.

:: Check git
where git >nul 2>nul
if %errorlevel% neq 0 (
    echo ❌ Git not installed
    goto :install_git
)

cd /d "D:\PsychologicalMagnetism\bpo-ethical-stable" 2>nul
if %errorlevel% neq 0 (
    echo ❌ Wrong directory
    echo Current: %cd%
    echo Expected: D:\PsychologicalMagnetism\bpo-ethical-stable
    pause
    exit /b 1
)

echo [1/4] 📊 Checking local files...
dir | find "File(s)" || echo No files found

echo.
echo [2/4] 🔗 Checking GitHub connection...
git remote -v
if %errorlevel% neq 0 (
    echo ❌ Not connected to GitHub
    goto :connect_github
)

echo.
echo [3/4] 🔄 Checking differences with GitHub...
echo Local changes not yet pushed:
git status --porcelain

echo.
echo [4/4] 📈 Repository statistics...
echo Total files: & dir /s /b | find /c ":" >nul 2>nul && echo See above || echo Cannot count
echo File size: & for /f %%i in ('dir /s ^| find "File(s)"') do echo %%i

echo.
echo ========================================
echo ✅ REPOSITORY READY FOR UPDATE
echo ========================================
echo.
goto :end

:install_git
echo.
echo 📥 Please install Git for Windows:
echo https://gitforwindows.org/
pause
exit /b 1

:connect_github
echo.
echo 🔗 Connect to GitHub with:
echo git remote add origin https://github.com/singularitynode/bpo-optimization-system.git
pause
exit /b 1

:end
pause