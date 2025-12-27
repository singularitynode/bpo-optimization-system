import numpy as np
import matplotlib
matplotlib.use('Agg')  # Headless fix
import matplotlib.pyplot as plt
from src.core.engineering.divine_engineering import DivineEngineering

def plot_sync_trajectory(agents=3, steps=100):
    if agents > 1000:
        # Memory: Subsample
        agents = 1000
    t = np.linspace(0, 10, steps)
    xs = np.random.randn(agents)
    trajectories = np.zeros((steps, agents))
    for i in range(steps):
        coupling = 0.1 * (np.mean(xs) - xs)
        dx = -0.5 * xs + coupling
        xs += 0.1 * dx
        trajectories[i] = xs
    plt.figure(figsize=(8, 6))
    for i in range(min(agents, 5)):  # Plot first 5 for viz
        plt.plot(t, trajectories[:, i], label=f'Agent {i+1}')
    plt.title(f'{agents}-Agent Sync')
    plt.xlabel('Time')
    plt.ylabel('State')
    plt.legend()
    plt.grid(alpha=0.3)
    plt.savefig('sync.png', dpi=150, bbox_inches='tight')
    plt.close()
    return 'sync.png saved'

def plot_scale_summary(agents=100000, steps=100):
    t = np.linspace(0, 10, steps)
    xs_mean = np.random.randn()
    mean_traj = np.zeros(steps)
    for i in range(steps):
        dx_mean = -0.5 * xs_mean
        xs_mean += 0.1 * dx_mean
        mean_traj[i] = xs_mean
    plt.plot(t, mean_traj, linewidth=2)
    plt.title(f'Mean-Field (N={agents})')
    plt.xlabel('Time')
    plt.ylabel('Avg State')
    plt.savefig('scale_sync.png', dpi=150)
    plt.close()
    return 'scale_sync.png saved'