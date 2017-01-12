from display_colours import *
import unittest

class TestWeatherDisplay(unittest.TestCase):
    def setUp(self):
        pass

    def test_display_temperature(self):
        self.assertEqual(temperature_to_hue(13), "Green")

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()
