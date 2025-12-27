#!/usr/bin/env python3
"""
Fix for aioredis compatibility issue on Python 3.12
"""

import os
import sys

def fix_main_py():
    """Update main.py to use modern redis instead of aioredis"""
    
    main_py_path = "src/main.py"
    
    if not os.path.exists(main_py_path):
        print(f"❌ {main_py_path} not found!")
        return False
    
    with open(main_py_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace the problematic import
    old_import = "import aioredis\nfrom redis import Redis"
    new_import = "import redis.asyncio as aioredis\nfrom redis import Redis"
    
    if old_import in content:
        content = content.replace(old_import, new_import)
        print("✅ Updated aioredis import to use redis.asyncio")
    else:
        # Try alternative pattern
        content = content.replace("import aioredis", "import redis.asyncio as aioredis")
        print("✅ Replaced aioredis import")
    
    # Save the file
    with open(main_py_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return True

if __name__ == "__main__":
    print("🛠️  Fixing aioredis compatibility for Python 3.12...")
    
    # Step 1: Uninstall old aioredis
    print("\n1. Uninstalling old aioredis...")
    os.system(f"{sys.executable} -m pip uninstall aioredis -y")
    
    # Step 2: Install modern redis
    print("\n2. Installing modern redis library...")
    os.system(f"{sys.executable} -m pip install redis>=5.0.0")
    
    # Step 3: Update main.py
    print("\n3. Updating main.py imports...")
    if fix_main_py():
        print("\n🎉 Fix applied successfully!")
        print("\nNow run: python src/main.py")
    else:
        print("\n⚠️  Could not update main.py automatically.")
        print("Please manually change 'import aioredis' to 'import redis.asyncio as aioredis'")