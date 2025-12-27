"""
CORE MODULES INITIALIZATION
Exports all core modules for easy import
"""

# Import all core modules
from .evolve import Evolver
from .proof import Stability
from .ethical import Veto

# Import engineering modules
from .engineering.divine_engineering import DivineEngineering
from .engineering.liquid_engineering import LiquidEngineering

# Import additional modules
from .rigor_proof import RigorProof
from .self_meta import SelfMeta

# Import process theorems
from .process_theorems import run_all_theorems, get_theorem

# Define public API
__all__ = [
    "Evolver",           # AI self-evolution
    "Stability",         # Lyapunov stability proofs
    "Veto",              # Ethical veto system
    "DivineEngineering", # Kuramoto synchronization
    "LiquidEngineering", # Fluid dynamics adaptation
    "RigorProof",        # Mathematical rigor proofs
    "SelfMeta",          # Self-debugging AI
    "run_all_theorems",  # Run all 13 BPO theorems
    "get_theorem",       # Get specific theorem
]

# Version info
__version__ = "2.0.0"
__author__ = "BPO Ethical & Stable Team"
__description__ = "Self-evolving AI with mathematical stability proofs"

def list_modules():
    """List all available core modules"""
    return {
        "ai_evolution": "Evolver - Self-evolving AI code",
        "stability": "Stability - Lyapunov mathematical proofs", 
        "ethics": "Veto - Ethical checking system",
        "synchronization": "DivineEngineering - Kuramoto multi-agent sync",
        "adaptation": "LiquidEngineering - Fluid dynamics adaptation",
        "rigor": "RigorProof - Mathematical rigor verification",
        "self_awareness": "SelfMeta - Self-debugging and learning",
        "theorems": "ProcessTheorems - 13 BPO optimization theorems"
    }

def get_module(module_name: str):
    """Get a specific module by name"""
    modules = {
        "evolver": Evolver,
        "stability": Stability,
        "veto": Veto,
        "divine": DivineEngineering,
        "liquid": LiquidEngineering,
        "rigor": RigorProof,
        "self_meta": SelfMeta,
    }
    
    if module_name.lower() in modules:
        return modules[module_name.lower()]
    else:
        raise ValueError(f"Module '{module_name}' not found. Available: {list(modules.keys())}")