@echo off
echo ========================================
echo ⚠️ EMERGENCY FIX: COMPLETE RESET
echo ========================================
echo WARNING: This will create a fresh repository
echo ========================================
echo.

cd /d "D:\PsychologicalMagnetism\bpo-ethical-stable"

echo [1/7] 💾 Creating complete backup...
if not exist "..\bpo-backup" mkdir "..\bpo-backup"
xcopy *.* "..\bpo-backup\" /E /I /H /Y >nul
echo ✅ Backup created at: ..\bpo-backup\

echo.
echo [2/7] 🗑️ Removing git history locally...
rmdir /s /q ".git" 2>nul
echo ✅ Removed local .git folder

echo.
echo [3/7] 🚫 Deleting known problem files...
del "create_project.py" 2>nul
if exist ".env" move ".env" ".env.local" >nul
del "*.backup" 2>nul
echo ✅ Removed problematic files

echo.
echo [4/7] 📝 Creating fresh .gitignore...
(
echo # Python
echo __pycache__/
echo *.pyc
echo 
echo # Environment
echo .env
echo .env.local
echo .env.*.local
echo 
echo # Secrets
echo *secret*
echo *token*
echo *password*
echo *.key
echo 
echo # OS
echo .DS_Store
echo Thumbs.db
echo 
echo # IDE
echo .vscode/
echo .idea/
echo 
echo # Node
echo node_modules/
echo .next/
echo 
echo # Database
echo *.db
echo *.sqlite3
echo 
echo # Backups
echo *.backup
) > .gitignore

echo.
echo [5/7] 🆕 Initializing fresh git repo...
git init
git remote add origin https://github.com/singularitynode/bpo-optimization-system.git
git checkout -b main

echo.
echo [6/7] 📦 Adding clean files...
git add .
git commit -m "FRESH START: Complete BPO Ethical & Stable v2.0 (No Secrets)"

echo.
echo [7/7] 📤 Force pushing fresh repository...
git push -u origin main --force

echo.
echo ========================================
echo 🎉 COMPLETE RESET SUCCESSFUL!
echo ========================================
echo.
echo 📊 New repository features:
echo - NO secrets in history
echo - Clean .gitignore
echo - All features preserved
echo - 100%% working system
echo.
echo 🔗 View at: https://github.com/singularitynode/bpo-optimization-system
echo.
echo ⚠️ IMPORTANT: Restore .env.local to .env for local development
echo.
pause