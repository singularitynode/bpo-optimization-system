# Create test env check
cat > check_env.py << 'EOF'
import os

REQUIRED_VARS = [
    "OPENAI_API_KEY",
    "POSTGRES_PASSWORD", 
    "REDIS_PASSWORD",
    "JWT_SECRET"
]

def check_env():
    print("🔐 Checking environment variables...")
    
    # Check if .env exists
    if not os.path.exists(".env"):
        print("❌ .env file missing")
        return False
    
    # Load .env
    with open(".env", "r") as f:
        content = f.read()
    
    issues = []
    for var in REQUIRED_VARS:
        if f"{var}=" not in content:
            issues.append(f"Missing: {var}")
        elif "your-" in content.split(f"{var}=")[1].split("\n")[0]:
            issues.append(f"Using placeholder: {var}")
    
    if issues:
        print("❌ Issues found:")
        for issue in issues:
            print(f"   - {issue}")
        return False
    
    print("✅ Environment variables configured")
    return True

if __name__ == "__main__":
    import sys
    sys.exit(0 if check_env() else 1)
EOF

python check_env.py