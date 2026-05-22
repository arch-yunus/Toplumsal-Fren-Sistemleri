"""Small runner for the SocialBrakeSystem example.

Usage: python run_simulation.py
"""
from toplumsal_fren_sistemleri.core import SocialBrakeSystem, create_uniform_road


def main():
    positions, speeds = create_uniform_road(n=5, spacing=8.0, speed=10.0)
    system = SocialBrakeSystem(positions, speeds, safe_distance=6.0, brake_amount=1.0)

    history = system.simulate(steps=12, dt=0.5)

    for t, speeds in enumerate(history, start=1):
        print(f"Step {t:2d}: speeds = {[round(s,2) for s in speeds]}")


if __name__ == "__main__":
    main()
