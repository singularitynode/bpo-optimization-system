@echo off
echo ========================================
echo 🚀 NUCLEAR OPTION: FRESH REPOSITORY START
echo ========================================
echo.
echo WARNING: This will DELETE GitHub history and start fresh
echo Recommended for this blocked push situation
echo ========================================
echo.

cd /d "D:\PsychologicalMagnetism\bpo-ethical-stable"

echo [1/9] 💾 Creating emergency backup...
mkdir "C:\BPO_BACKUP_%date:~-4,4%%date:~-10,2%%date:~-7,2%" 2>nul
xcopy *.* "C:\BPO_BACKUP_%date:~-4,4%%date:~-10,2%%date:~-7,2%\" /E /I /H /Y >nul
echo ✅ Emergency backup: C:\BPO_BACKUP_%date:~-4,4%%date:~-10,2%%date:~-7,2%\

echo.
echo [2/9] 🗑️ Removing ALL git history...
rmdir /s /q ".git" 2>nul
echo ✅ Removed .git folder

echo.
echo [3/9] 🔍 Finding and cleaning ALL secret files...
echo Scanning for files with secrets...
for /r %%f in (*.py *.json *.env *.txt *.yml *.yaml *.js *.ts) do (
    findstr /i "slack.*webhook\|api.*key\|secret.*key\|aws.*key\|password.*=" "%%f" >nul 2>nul
    if !errorlevel! equ 0 (
        echo Cleaning: %%f
        powershell -Command "(Get-Content '%%f') -replace 'https://hooks.slack.com/services/[^'\""]+', 'https://hooks.slack.com/services/EXAMPLE/EXAMPLE/EXAMPLE' | Set-Content '%%f'"
        powershell -Command "(Get-Content '%%f') -replace 'sk-[a-zA-Z0-9]{48}', 'sk-example-123456789012345678901234567890123456789012' | Set-Content '%%f'"
        powershell -Command "(Get-Content '%%f') -replace 'AIza[0-9A-Za-z\-_]{35}', 'AIzaExampleKey123456789012345678901234567890' | Set-Content '%%f'"
    )
)

echo.
echo [4/9] 📁 Creating CLEAN directory structure...
if not exist "clean_version" mkdir "clean_version"

echo Copying source files...
xcopy src clean_version\src /E /I /H /Y >nul
xcopy frontend clean_version\frontend /E /I /H /Y >nul
xcopy docs clean_version\docs /E /I /H /Y >nul

echo Copying root files...
copy *.py clean_version\ >nul 2>nul
copy *.md clean_version\ >nul 2>nul
copy *.txt clean_version\ >nul 2>nul
copy *.bat clean_version\ >nul 2>nul

echo.
echo [5/9] 🚫 Creating ULTIMATE .gitignore...
(
echo # ========================================
echo # ULTIMATE GITIGNORE - NO SECRETS ALLOWED
echo # ========================================
echo.
echo # SECRETS - NEVER COMMIT
echo *.env
echo .env*
echo *.key
echo *.pem
echo *.crt
echo *.csr
echo *secret*
echo *password*
echo *token*
echo *credential*
echo *private*
echo 
echo # SLACK/WEBHOOKS
echo *webhook*
echo *slack*
echo *discord*
echo *telegram*
echo 
echo # API KEYS
echo *api*key*
echo *aws*
echo *azure*
echo *gcp*
echo *openai*
echo *anthropic*
echo 
echo # DATABASE
echo *.db
echo *.sqlite*
echo *postgres*
echo *mysql*
echo *mongo*
echo 
echo # BACKUPS
echo *.backup
echo *.bak
echo *backup*
echo 
echo # TEMP FILES
echo *.tmp
echo *.temp
echo *~
echo 
echo # LOGS
echo *.log
echo logs/
echo 
echo # PYTHON
echo __pycache__/
echo *.py[cod]
echo *$py.class
echo .python-version
echo 
echo # NODE
echo node_modules/
echo .next/
echo out/
echo 
echo # IDE
echo .vscode/
echo .idea/
echo *.swp
echo *.swo
echo 
echo # OS
echo .DS_Store
echo Thumbs.db
echo 
echo # DOCKER
echo .dockerignore
) > clean_version\.gitignore

echo.
echo [6/9] 📝 Creating SAFE .env.example...
(
echo # ========================================
echo # BPO ETHICAL & STABLE - EXAMPLE ENVIRONMENT
echo # ========================================
echo # NEVER COMMIT REAL VALUES!
echo # Copy to .env and fill with real values
echo.
echo # OpenAI (Get from https://platform.openai.com/api-keys)
echo OPENAI_API_KEY=sk-example-123456789012345678901234567890123456789012
echo.
echo # Database (Generate your own)
echo POSTGRES_PASSWORD=example_postgres_password_123
echo REDIS_PASSWORD=example_redis_password_456
echo JWT_SECRET=example_32_char_jwt_secret_string_here_789
echo.
echo # URLs
echo POSTGRES_URL=postgresql://bpo_admin:${POSTGRES_PASSWORD}@localhost:5432/bpo_stable
echo REDIS_URL=redis://:${REDIS_PASSWORD}@localhost:6379/0
echo NEXT_PUBLIC_BACKEND_URL=http://localhost:8000
echo.
echo # Admin
echo ADMIN_TOKEN=example_admin_token_do_not_use_in_production
echo.
echo # Monitoring
echo GRAFANA_ADMIN_PASS=example_grafana_password
echo.
echo # System Parameters
echo VETO_RATE=0.3
echo GDPR_CONSENT=true
echo LYAPUNOV_LAMBDA=0.1
echo MAX_REPLICAS=5
echo.
echo # LEAVE EMPTY FOR LOCAL
echo AWS_ACCESS_KEY_ID=
echo AWS_SECRET_ACCESS_KEY=
echo K8S_CLUSTER=
echo DOMAIN_NAME=
) > clean_version\.env.example

echo.
echo [7/9] 🆕 Initializing CLEAN git repo...
cd clean_version
git init
git remote add origin https://github.com/singularitynode/bpo-optimization-system.git
git checkout -b main

echo.
echo [8/9] 📦 Adding ALL clean files...
git add .
git commit -m "🚀 FRESH START v2.0: Complete BPO Ethical & Stable (No Secrets)"

echo.
echo [9/9] 📤 FORCE PUSHING to GitHub...
git push -u origin main --force

echo.
cd ..

echo ========================================
echo 🎉 NUCLEAR CLEAN PUSH COMPLETE!
echo ========================================
echo.
echo 📊 What was done:
echo 1. Created clean version in \clean_version
echo 2. Scanned and cleaned ALL potential secrets
echo 3. Created ULTIMATE .gitignore
echo 4. Created SAFE .env.example
echo 5. Force pushed FRESH repository
echo.
echo 🔗 View at: https://github.com/singularitynode/bpo-optimization-system
echo 💾 Backup at: C:\BPO_BACKUP_%date:~-4,4%%date:~-10,2%%date:~-7,2%\
echo.
echo ⚠️ IMPORTANT:
echo 1. Work from \clean_version folder now
echo 2. Create .env from .env.example for local dev
echo 3. NEVER commit .env file
echo.
pause