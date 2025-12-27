#!/usr/bin/env python3
import os
import sys

CRITICAL_FILES = [
    # Root files
    ".env",
    "docker-compose.yml",
    "Dockerfile",
    "requirements.txt",
    "bootstrap.py",
    "init_db.sql",
    "deploy.sh",
    
    # Core backend
    "src/main.py",
    "src/config.py",
    
    # Core modules
    "src/core/__init__.py",
    "src/core/evolve.py",
    "src/core/proof.py",
    "src/core/ethical.py",
    "src/core/rigor_proof.py",
    "src/core/self_meta.py",
    "src/core/process_theorems.py",
    
    # Engineering
    "src/core/engineering/__init__.py",
    "src/core/engineering/divine_engineering.py",
    "src/core/engineering/liquid_engineering.py",
    
    # Services & Utils
    "src/services/bpo_service.py",
    "src/utils/sandbox.py",
    "src/utils/visualize.py",
    
    # Frontend
    "frontend/package.json",
    "frontend/next.config.js",
    "frontend/src/app/page.tsx",
    "frontend/src/components/Dashboard.tsx",
    
    # Infrastructure
    "terraform/main.tf",
    "terraform/variables.tf",
    "helm/Chart.yaml",
    "helm/values.yaml",
    "helm/templates/deployment.yaml",
    
    # Tests
    "tests/test_core.py",
    "tests/test_engineering.py",
]

def check_files():
    missing = []
    for file_path in CRITICAL_FILES:
        if not os.path.exists(file_path):
            missing.append(file_path)
    
    if missing:
        print("❌ MISSING FILES:")
        for file in missing:
            print(f"   - {file}")
        return False
    else:
        print("✅ All critical files present")
        return True

if __name__ == "__main__":
    if check_files():
        sys.exit(0)
    else:
        sys.exit(1)