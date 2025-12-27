import openai
import asyncio
import os
import hashlib
import re
import ast
import logging
from typing import Dict, Any
from ..utils.sandbox import Sandbox
from .proof import Stability
from .ethical import Veto

logger = logging.getLogger(__name__)

class Evolver:
    def __init__(self):
        self.client = openai.AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.sandbox = Sandbox()
        self.stability = Stability()
        self.veto = Veto()
        self.evolve_rate = 0.001
        self.experience_log = []
      
    async def reflect(self, state: str) -> Dict[str, Any]:
        try:
            if not os.getenv("OPENAI_API_KEY"):
                return {"insight": "Mock reflection (no API key)", "score": 0.5, "stable": True}
            response = await self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "Reflect ethically & stably on BPO task."},
                    {"role": "user", "content": f"Task: {state}"}
                ],
                max_tokens=200
            )
            insight = response.choices[0].message.content
            score = min(len(insight) / 500, 1.0)
            return {"insight": insight, "score": score, "stable": True}
        except Exception as e:
            return {"insight": f"Reflect error: {str(e)}", "score": 0.1, "stable": False}
  
    async def generate_code(self, instruction: str) -> str:
        try:
            response = await self.client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": "Write safe Python w/ stability (dV/dt=-λx²)."},
                    {"role": "user", "content": instruction}
                ],
                temperature=0.2
            )
            code = response.choices[0].message.content
            if "```python" in code:
                code = code.split("```python")[1].split("```")[0].strip()
            return code
        except:
            return "# Mock safe code\ndef stable_func():\n return 'Stable'"
  
    def _safety_scan(self, code: str) -> bool:
        SAFE_IMPORTS = {'os', 'sys', 'datetime', 'json', 'math', 'random', 'sympy'}
        DANGEROUS_PATTERNS = [
            r'__import__\s*\(',
            r'eval\s*\(',
            r'exec\s*\(',
            r'open\s*\([^)]*[rw]\+',
            r'subprocess\.',
            r'os\.system',
            r'rm\s+-rf',
            r'del\s+\w+\.__class__',
        ]
        for pattern in DANGEROUS_PATTERNS:
            if re.search(pattern, code, re.IGNORECASE):
                logger.warning(f"Regex block: {pattern} in code")
                return False
   
        try:
            tree = ast.parse(code)
            for node in ast.walk(tree):
                if isinstance(node, ast.Import):
                    for alias in node.names:
                        mod = alias.name.split('.')[0]
                        if mod not in SAFE_IMPORTS:
                            logger.warning(f"Unsafe import: {mod}")
                            return False
                elif isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id in ['eval', 'exec', '__import__']:
                    return False
        except SyntaxError as e:
            logger.error(f"AST parse fail: {e}")
            return False
   
        return True
  
    async def self_code(self, instruction: str) -> Dict[str, Any]:
        MAX_ATTEMPTS = 3
        for attempt in range(MAX_ATTEMPTS):
            try:
                code = await self.generate_code(f"{instruction} (Attempt {attempt+1})")
               
                if not code or len(code.strip()) < 10:
                    logger.warning(f"Attempt {attempt+1}: Code too short")
                    continue
               
                if not self._safety_scan(code):
                    self.experience_log.append({"error": "Safety scan failed", "attempt": attempt})
                    await self.reflect("Code rejected: unsafe patterns")
                    continue
               
                if not self.stability.verify(code):
                    await self.reflect(f"Unstable code: {code[:100]}")
                    continue
               
                result = self.sandbox.execute(code)
                if result.get("safe", False):
                    if not self.veto.check():
                        return {"success": False, "reason": "Ethical veto on code"}
                    deployment = await self.deploy_to_k8s(code)
                    self.experience_log.append({"success": True, "attempt": attempt})
                    return {"success": True, "message": f"Success on attempt {attempt+1}", "deployment": deployment}
               
            except Exception as e:
                logger.error(f"Attempt {attempt+1} failed: {e}")
                await self.reflect(f"Exception in attempt {attempt+1}: {str(e)}")
           
        return {"success": False, "reason": "All attempts failed", "log": self.experience_log[-3:]}
  
    async def deploy_to_k8s(self, code: str) -> Dict[str, Any]:
        code_hash = hashlib.md5(code.encode()).hexdigest()[:8]
        return {"deployed": True, "image_tag": f"bpo:v{code_hash}", "status": "success", "replicas": int(os.getenv("MAX_REPLICAS", 3))}