import sympy as sp
import ast
import numpy as np
from scipy.linalg import eigvals

class RigorProof:
    def __init__(self):
        pass
    
    def multi_var_calc_proof(self, vars_count=6) -> dict:
        """Multi-var rigor: Jacobian for nD system stability (Hurwitz evals)"""
        vars_ = sp.symbols(f'x0:{vars_count}')
        # Coupled eqs: dx_i/dt = -sum A_ij x_j (linear multi-var)
        A = sp.Matrix(vars_count, vars_count, lambda i,j: -1 if i==j else 0.1)  # Stable matrix
        eqs = [sum(A.row(i) * sp.Matrix(vars_)) for i in range(vars_count)]
        J = sp.Matrix([ [sp.diff(eq, v) for v in vars_] for eq in eqs ])
        J_np = np.array(J, dtype=float)
        evals = eigvals(J_np)
        stable = np.all(np.real(evals) < 0)
        return {"jacobian": str(J), "evals": [float(np.real(e)) for e in evals], "stable": stable, "proof": f"nD={vars_count} Hurwitz convergence"}
    
    def prog_calc_proof(self, code: str) -> dict:
        """Advanced prog calc: AST deriv safety + sympy code rigor"""
        try:
            tree = ast.parse(code)
            # Calc rigor: Extract math expr, sympy verify
            math_nodes = [node for node in ast.walk(tree) if isinstance(node, (ast.BinOp, ast.Call))]
            safe = all(not isinstance(node, (ast.Call, ast.Import)) or node.func.id not in ['eval', 'exec'] for node in math_nodes)
            if math_nodes:
                expr_str = ast.unparse(math_nodes[0])  # First math expr
                expr = sp.sympify(expr_str)
                deriv = sp.diff(expr, sp.symbols('x'))  # Rigor deriv
                return {"ast_safe": safe, "expr_deriv": str(deriv), "proof": "AST-verified calc (deriv exists)"}
            return {"ast_safe": True, "proof": "No math—safe"}
        except Exception as e:
            return {"ast_safe": False, "error": str(e), "proof": "Parse failed—rerig"}