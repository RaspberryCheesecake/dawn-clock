from display_colours import *
import unittest

class TestDisplay(unittest.TestCase):
    def setUp(self):
        pass

    def test_display_temperature(self):
        self.assertEqual(temperature_to_hue(13), "Green")

    def test_interpolation_works(self):
        self.assertEqual(interpolate_smoothly(0.2, 0.5, 1, 4), [0.2, 0.3, 0.4, 0.5])

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()
