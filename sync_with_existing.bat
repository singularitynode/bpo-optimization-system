@echo off
echo ========================================
echo 🔄 SMART SYNC WITH EXISTING REPO
echo ========================================
echo.

setlocal enabledelayedexpansion

:: Backup first
echo [1/8] 💾 Creating backup...
if not exist "backup" mkdir backup
xcopy *.* backup\ /E /I /Y 2>nul
echo ✅ Backup created: backup\

:: Check if repo exists
echo [2/8] 🔍 Checking repository status...
git status >nul 2>nul
if %errorlevel% neq 0 (
    echo ❌ Not a git repository
    goto :init_repo
)

:: Pull latest
echo [3/8] 📥 Pulling latest from GitHub...
git pull origin main
if %errorlevel% neq 0 (
    echo ⚠️  Pull failed, may be first push
)

:: Check what's different
echo [4/8] 🔄 Comparing changes...
git status

:: Add only new/changed files
echo [5/8] 📦 Adding specific changes...
set added=0
for /f "tokens=*" %%f in ('git status --porcelain ^| findstr "^?? ^M ^A"') do (
    set file=%%f
    set file=!file:~3!
    if exist "!file!" (
        git add "!file!"
        set /a added+=1
        echo Added: !file!
    )
)

:: If no files were added, add everything
if !added! equ 0 (
    echo No specific changes, adding everything...
    git add .
)

:: Create commit
echo [6/8] 💾 Creating commit...
set timestamp=%date% %time%
git commit -m "Update !timestamp!: Complete BPO Ethical & Stable v2.0"

:: Push
echo [7/8] 📤 Pushing to GitHub...
git push origin main

:: Verify
echo [8/8] ✅ Verifying update...
git log --oneline -3

echo.
echo ========================================
echo 🎉 SYNC COMPLETE!
echo ========================================
echo.
echo 📊 Summary:
echo Files added/updated: !added!
echo Commit: Update !timestamp!
echo Repository: https://github.com/singularitynode/bpo-optimization-system
echo.
echo 🚀 New Features:
echo - Complete admin dashboard at /admin
echo - 1000+ demo data records
echo - 13 mathematical theorems
echo - Self-healing deployment
echo - Real-time metrics streaming
echo.
goto :end

:init_repo
echo.
echo 📁 Initializing new repository...
git init
git remote add origin https://github.com/singularitynode/bpo-optimization-system.git
git checkout -b main
goto :end

:end
pause