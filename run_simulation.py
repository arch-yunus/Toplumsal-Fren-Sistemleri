"""Small runner for the SocialBrakeSystem example.

Usage: python run_simulation.py
"""
import argparse
from toplumsal_fren_sistemleri.core import SocialBrakeSystem, create_uniform_road


def main():
    parser = argparse.ArgumentParser(description="Run social braking simulation")
    parser.add_argument("--n", type=int, default=5, help="number of agents")
    parser.add_argument("--spacing", type=float, default=8.0, help="initial spacing")
    parser.add_argument("--speed", type=float, default=10.0, help="initial speed")
    parser.add_argument("--safe", type=float, default=6.0, help="safe distance")
    parser.add_argument("--brake", type=float, default=1.0, help="brake amount")
    parser.add_argument("--steps", type=int, default=12, help="simulation steps")
    parser.add_argument("--dt", type=float, default=0.5, help="time step dt")
    parser.add_argument("--plot", action="store_true", help="plot results (requires matplotlib)")
    parser.add_argument("--save", type=str, default=None, help="save plot to file (png)")
    args = parser.parse_args()

    positions, speeds = create_uniform_road(n=args.n, spacing=args.spacing, speed=args.speed)
    system = SocialBrakeSystem(positions, speeds, safe_distance=args.safe, brake_amount=args.brake)

    history = system.simulate(steps=args.steps, dt=args.dt)

    for t, spds in enumerate(history, start=1):
        print(f"Step {t:2d}: speeds = {[round(s,2) for s in spds]}")

    if args.plot:
        try:
            from toplumsal_fren_sistemleri.visualize import plot_speed_history

            plot_speed_history(history, savepath=args.save)
        except Exception as e:
            print("Plotting failed:", e)


if __name__ == "__main__":
    main()
