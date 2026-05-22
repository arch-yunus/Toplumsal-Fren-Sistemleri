import unittest

from toplumsal_fren_sistemleri.core import SocialBrakeSystem, create_uniform_road


class TestSocialBrakeSystem(unittest.TestCase):
    def test_simulation_runs_and_nonnegative(self):
        positions, speeds = create_uniform_road(4, spacing=5.0, speed=8.0)
        system = SocialBrakeSystem(positions, speeds, safe_distance=6.0, brake_amount=0.5)
        history = system.simulate(steps=5, dt=1.0)

        self.assertEqual(len(history), 5)
        for step_speeds in history:
            for s in step_speeds:
                self.assertGreaterEqual(s, 0.0)

    def test_followers_slow_when_leader_stops(self):
        # leader at index 0 will stop immediately
        positions = [30.0, 20.0, 10.0]
        speeds = [0.0, 10.0, 10.0]
        system = SocialBrakeSystem(positions, speeds, safe_distance=12.0, brake_amount=2.0)
        history = system.simulate(steps=3, dt=1.0)

        # followers should reduce speed from initial
        self.assertTrue(history[0][1] <= 10.0)
        self.assertTrue(history[0][2] <= 10.0)


if __name__ == "__main__":
    unittest.main()
