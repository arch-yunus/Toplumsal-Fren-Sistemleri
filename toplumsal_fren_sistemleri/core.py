"""Core simulation for Toplumsal Fren Sistemleri

This module provides a minimal, easy-to-read agent-based model
where each agent (vehicle) brakes when it is too close to the one ahead.
"""
from typing import List


class SocialBrakeSystem:
    """Simple 1D social braking model.

    Agents are ordered so that index 0 is the leader (front). Positions
    increase in the forward direction. Each follower checks distance to
    the agent ahead and reduces speed if the gap is below `safe_distance`.
    """

    def __init__(self, positions: List[float], speeds: List[float], safe_distance: float = 5.0, brake_amount: float = 0.5):
        if len(positions) != len(speeds):
            raise ValueError("positions and speeds must have the same length")
        # positions: front-most agent at index 0
        self.positions = positions[:]
        self.speeds = speeds[:]
        self.safe_distance = float(safe_distance)
        self.brake_amount = float(brake_amount)

    def step(self, dt: float = 1.0) -> List[float]:
        """Advance the simulation by one time step and return current speeds."""
        n = len(self.speeds)
        new_speeds = self.speeds[:]

        # Followers react to the agent ahead
        for i in range(1, n):
            distance = self.positions[i - 1] - self.positions[i]
            if distance < self.safe_distance:
                # proportional braking: more braking when closer
                reduction = self.brake_amount * (self.safe_distance - distance) / self.safe_distance
                new_speeds[i] = max(0.0, new_speeds[i] - reduction)

        # Update positions using new speeds
        for i in range(n):
            self.positions[i] += new_speeds[i] * dt

        self.speeds = new_speeds
        return list(self.speeds)

    def simulate(self, steps: int, dt: float = 1.0) -> List[List[float]]:
        """Run `steps` simulation steps and return speeds history."""
        history = []
        for _ in range(int(steps)):
            history.append(self.step(dt))
        return history


def create_uniform_road(n: int, spacing: float = 10.0, speed: float = 5.0):
    """Helper: create `n` agents evenly spaced with the same initial speed.

    Returns (positions, speeds) where positions[0] is the leader.
    """
    positions = [i * spacing for i in range(n)]
    # reverse so that index 0 is leader at front
    positions = list(reversed(positions))
    speeds = [float(speed)] * n
    return positions, speeds
