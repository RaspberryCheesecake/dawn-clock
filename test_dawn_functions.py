from display_colours import sigmoid_curve
import unittest


class TestDawn(unittest.TestCase):
    def test_sigmoid_behaviour(self):
        self.assertAlmostEqual(sigmoid_curve(-6), 0, delta=0.01)  # converges
        self.assertAlmostEqual(sigmoid_curve(6), 1, delta=0.01)
        self.assertEqual(sigmoid_curve(0), 0.5)  # halfway point


if __name__ == "__main__":
    unittest.main()