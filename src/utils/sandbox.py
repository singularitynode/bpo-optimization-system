import ast
import builtins

class Sandbox:
    SAFE_MODULES = ['math', 'json', 'datetime', 're', 'collections', 'itertools']
    UNSAFE_KEYWORDS = ['__', 'eval', 'exec', 'import', 'open', 'os.', 'sys.', 'subprocess']
  
    def execute(self, code: str) -> dict:
        try:
            for keyword in self.UNSAFE_KEYWORDS:
                if keyword in code:
                    return {"safe": False, "error": f"Unsafe keyword: {keyword}"}
          
            ast.parse(code)
          
            safe_globals = {
                '__builtins__': {
                    k: v for k, v in builtins.__dict__.items()
                    if not k.startswith('_') and k not in ['exec', 'eval', 'compile', '__import__']
                }
            }
          
            for mod_name in self.SAFE_MODULES:
                try:
                    module = __import__(mod_name)
                    safe_globals[mod_name] = module
                except ImportError:
                    pass
          
            exec(code, safe_globals, {})
          
            if 'result' in safe_globals:
                result = safe_globals['result']
                return {"safe": True, "result": result}
          
            return {"safe": True, "result": "Code executed successfully"}
          
        except SyntaxError as e:
            return {"safe": False, "error": f"Syntax error: {str(e)}"}
        except Exception as e:
            return {"safe": False, "error": f"Execution error: {str(e)}"}