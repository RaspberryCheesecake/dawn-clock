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

def extract_temperature_data(data):
    output = [int(s) for s in data.split() if s.isdigit()]
    return output[0]


def display_temperature_on_pi(temperature):
    if type(temperature) != float:
        print "Don't mess me around!"

    if temperature < 0:
        print "White"
    elif 0 < temperature < 10:
        print "Blue"
    elif 10 < temperature < 20:
        print "Green"
    elif 20 < temperature < 30:
        print "Yellow"
    elif temperature > 30:
        print "Red"

class TestWeatherDisplay(unittest.TestCase):
    def setUp(self):
        self.mock_temp_data = "Baby it's cold outside: 13 degrees C"

    def test_extracting_temperature(self):
        self.assertEqual(extract_temperature_data(self.mock_temp_data), 13)

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()


    
