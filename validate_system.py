#!/usr/bin/env python3
import os
import sys
import importlib.util

def check_python_files():
    print("🔍 Checking Python syntax...")
    python_files = []
    for root, dirs, files in os.walk("src"):
        for file in files:
            if file.endswith(".py"):
                python_files.append(os.path.join(root, file))
   
    errors = []
    for py_file in python_files:
        try:
            spec = importlib.util.spec_from_file_location("module", py_file)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
        except Exception as e:
            errors.append(f"{py_file}: {str(e)}")
   
    if errors:
        print("❌ Syntax errors found:")
        for err in errors:
            print(f" - {err}")
        return False
    print("✅ All Python files syntax OK")
    return True

def check_imports():
    print("🔍 Testing imports...")
    test_imports = [
        ("fastapi", "FastAPI"),
        ("openai", "AsyncOpenAI"),
        ("sqlalchemy", "create_engine"),
        ("jose", "jwt"),
        ("sympy", "symbols"),
    ]
   
    for module, obj in test_imports:
        try:
            exec(f"from {module} import {obj}")
            print(f"✅ {module}.{obj}")
        except ImportError as e:
            print(f"❌ Failed to import {module}.{obj}: {e}")
            return False
    return True

def check_env_template():
    print("🔍 Checking .env.example...")
    with open(".env.example", "r") as f:
        content = f.read()
   
    required = [
        "OPENAI_API_KEY=",
        "POSTGRES_PASSWORD=",
        "REDIS_PASSWORD=",
        "JWT_SECRET=",
        "POSTGRES_URL=",
        "REDIS_URL=",
    ]
   
    missing = []
    for req in required:
        if req not in content:
            missing.append(req)
   
    if missing:
        print(f"❌ Missing in .env.example: {missing}")
        return False
   
    print("✅ .env.example complete")
    return True

def main():
    print("=" * 60)
    print("BPO SYSTEM VALIDATION")
    print("=" * 60)
   
    checks = [
        ("Python syntax", check_python_files),
        ("Imports", check_imports),
        (".env template", check_env_template),
    ]
   
    results = []
    for name, check_func in checks:
        print(f"\n{name}:")
        try:
            if check_func():
                results.append((name, "✅ PASS"))
            else:
                results.append((name, "❌ FAIL"))
        except Exception as e:
            results.append((name, f"❌ ERROR: {e}"))
   
    print("\n" + "=" * 60)
    print("VALIDATION RESULTS:")
    print("=" * 60)
   
    all_pass = True
    for name, result in results:
        print(f"{name:20} {result}")
        if "❌" in result:
            all_pass = False
   
    if all_pass:
        print("\n✅ SYSTEM VALIDATION PASSED")
        print("\nNext steps:")
        print("1. cp .env.example .env")
        print("2. Edit .env with real values")
        print("3. pip install -r requirements.txt")
        print("4. python bootstrap.py")
    else:
        print("\n❌ SYSTEM VALIDATION FAILED")
        print("Fix the issues above before proceeding.")
        sys.exit(1)

if __name__ == "__main__":
    main()