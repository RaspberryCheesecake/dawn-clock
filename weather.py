# import unicornhat as unicorn
# unicorn.setlayout(unicorn.PHAT) # mini hat

import requests
import json
import unittest

def get_weather_forecast():
    response = requests.get("url.json")

    if response.status_code != 200:
        print "I failed with code ".format(response.status_code)

    data = response.json
    return data

def extract_temperature(data):
    output = [int(s) for s in data.split() if s.isdigit()]
    return output[0]


def temperature_to_hue(temperature):
    if temperature < 0:
        return "White"
    elif 0 < temperature < 10:
        return "Blue"
    elif 10 < temperature < 20:
        return "Green"
    elif 20 < temperature < 30:
        return "Yellow"
    elif temperature > 30:
        return "Red"


class TestWeatherDisplay(unittest.TestCase):
    def setUp(self):
        self.mock_temp_data = "Baby it's cold outside: 13 degrees C"

    def test_extracting_temperature(self):
        self.assertEqual(extract_temperature(self.mock_temp_data), 13)

    def test_display_temperature(self):
        self.assertEqual(temperature_to_hue(13), "Green")

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()


    
