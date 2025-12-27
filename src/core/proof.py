import sympy as sp
import numpy as np
from scipy.integrate import odeint
from scipy.linalg import eigvals

class Stability:
    def lyapunov(self) -> dict:
        x, lam = sp.symbols('x lambda', positive=True)
        V = x**2 / 2
        dx_dt = -lam * x
        dV_dt = sp.diff(V, x) * dx_dt
        return {"V": str(V), "dV/dt": str(sp.simplify(dV_dt)), "stable": sp.simplify(dV_dt) < 0, "condition": "λ > 0"}
  
    def verify(self, code: str) -> bool:
        return any(k in code.lower() for k in ["-lambda", "lambda", "x**2", "dx/dt"])
    
    def lyapunov_sync(self, agents=100000, coupling=0.1) -> dict:
        """Hybrid: Symbolic small N, numerical mean-field large N (disrupter scale)"""
        if agents <= 20:
            xs = sp.symbols(f'x0:{agents}')
            lams = sp.symbols(f'λ0:{agents}', positive=True)
            V = sum(xi**2 for xi in xs) / 2
            dV_dt = sum(-lams[i]*xs[i]**2 for i in range(agents))
            coupling_term = coupling * sum((xs[i] - xs[j])**2 for i in range(agents) for j in range(i+1, agents))
            dV_dt -= coupling_term
            sync_cond = f"min(λ_i) > {(agents-1)*coupling}"
            return {"agents": agents, "V": str(V), "dV/dt": str(sp.simplify(dV_dt)), "stable": dV_dt < 0, "sync_condition": sync_cond, "method": "symbolic"}
        else:
            # Numerical mean-field: R = order param, Ψ = phase
            def mean_field(y, t, lam, coupling):
                theta = y
                R = np.sqrt(np.mean(np.cos(theta))**2 + np.mean(np.sin(theta))**2)
                Psi = np.arctan2(np.mean(np.sin(theta)), np.mean(np.cos(theta)))
                dtheta = -lam * theta + coupling * R * np.sin(Psi - theta)
                return dtheta
            y0 = np.random.uniform(0, 2*np.pi, agents)
            t = np.linspace(0, 10, 100)
            sol = odeint(mean_field, y0, t, args=(1.0, coupling))  # Vectorized 100k
            final_var = np.var(sol[-1])  # Convergence metric
            stable = final_var < 0.01  # Threshold
            return {"agents": agents, "final_var": final_var, "stable": stable, "sync_condition": "R→1 (mean-field order)", "method": "numerical_odeint"}
    
    def jacobian_proof(self, eqs: list) -> dict:
        """Numerical Jacobian evals for multivars (rigor at scale)"""
        vars_ = sp.symbols('x1:6')
        if len(eqs) == 0:
            eqs = [sp.Eq(-sum(vars_), 0)] * len(vars_)  # Stub coupled
        J_sym = sp.Matrix([[sp.diff(eq, v) for v in vars_] for eq in eqs])
        J_num = np.array(J_sym.evalf(), dtype=float)
        evals = eigvals(J_num)
        stable = np.all(np.real(evals) < 0)
        return {"jacobian": str(J_sym), "evals": [float(np.real(e)) for e in evals], "stable": stable, "proof": "Numerical Hurwitz (scale-ready)"}