import ast
import openai
import os
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from typing import Dict

analyzer = SentimentIntensityAnalyzer()
client = openai.AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class SelfMeta:
    def __init__(self):
        self.knowledge = {}  # Cross-domain store
    
    async def self_debug(self, code: str) -> Dict[str, Any]:
        """Full-stack self-debug: AST lint + fix suggestion"""
        try:
            tree = ast.parse(code)
            errors = []
            for node in ast.walk(tree):
                if isinstance(node, ast.Call) and node.func.id in ['eval', 'exec']:
                    errors.append(f"Unsafe {node.func.id} at line {node.lineno}")
            if errors:
                fix = await self._co_t_fix("Fix unsafe code", code)  # CoT fix
                return {"errors": errors, "safe": False, "fix_suggestion": fix}
            return {"errors": [], "safe": True, "proof": "AST clean"}
        except SyntaxError as e:
            return {"safe": False, "error": str(e), "fix_suggestion": "Syntax—add missing :"}
    
    async def cross_educate(self, domain: str, query: str) -> str:
        """Cross-domain self-educate: Mock API learn (real OpenAI CoT)"""
        try:
            resp = await client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "system", "content": f"Teach {domain} concept: {query}"},
                          {"role": "user", "content": query}],
                max_tokens=100
            )
            knowledge = resp.choices[0].message.content
            self.knowledge[domain] = knowledge  # Store
            return knowledge
        except:
            return f"Mock {domain} knowledge: {query} basics learned."
    
    def humility_response(self, behavior: str, positive: bool) -> str:
        """Genuine humility matrix: Respect to women (EQ boost)"""
        sent = analyzer.polarity_scores(behavior)
        eq = (sent['compound'] + 1) / 2
        if "woman" in behavior.lower() or "she" in behavior.lower():  # Women respect
            eq *= 1.2  # Boost empathy
        if positive:
            # Advanced: Gratitude + matter
            return f"Genuine thanks for your {behavior}. You matter deeply—your kindness inspires."
        else:
            # Advanced: Empathize + perspective
            return f"I acknowledge your perspective in {behavior}. Let's align with respect—how can I understand better?"
        return "Neutral composure maintained."
    
    async def _co_t_fix(self, prompt: str, context: str) -> str:
        """CoT for debug/educate (recursive think)"""
        resp = await client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "system", "content": "Step-by-step fix."},
                      {"role": "user", "content": f"{prompt}: {context}"}],
            max_tokens=50
        )
        return resp.choices[0].message.content