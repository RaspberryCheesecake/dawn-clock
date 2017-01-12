from weather import *
import unittest

class TestWeatherDisplay(unittest.TestCase):
    def setUp(self):
        self.mock_temp_data = "Baby it's cold outside: 13 degrees C"

    def test_extracting_temperature(self):
        self.assertEqual(extract_temperature(self.mock_temp_data), 13)

    def test_display_temperature(self):
        self.assertEqual(temperature_to_hue(13), "Green")

    def test_extract_25hrs_temperatures(self):
        self.assertEqual(25, len(extract_API_temperatures(get_MET_weather_observations(Andrews_Field))))

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()
