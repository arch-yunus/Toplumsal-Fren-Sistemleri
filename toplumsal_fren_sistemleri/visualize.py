"""Visualization helpers for Toplumsal Fren Sistemleri.

Provides simple plotting utilities using matplotlib.
"""
from typing import List, Optional


def plot_speed_history(history: List[List[float]], savepath: Optional[str] = None):
    try:
        import matplotlib.pyplot as plt
    except ImportError as e:
        raise

    # history: list of speed lists per timestep
    if not history:
        raise ValueError("Empty history")

    steps = list(range(1, len(history) + 1))
    n_agents = len(history[0])

    plt.figure(figsize=(8, 4))
    for i in range(n_agents):
        agent_speeds = [history[t][i] for t in range(len(history))]
        plt.plot(steps, agent_speeds, marker='o', label=f'agent_{i}')

    plt.xlabel('Step')
    plt.ylabel('Speed')
    plt.title('Agent speeds over time')
    plt.grid(True)
    plt.legend()

    if savepath:
        plt.savefig(savepath, bbox_inches='tight')
        print(f"Saved plot to {savepath}")
    else:
        plt.show()
