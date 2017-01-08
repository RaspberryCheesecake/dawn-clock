# import unicornhat as unicorn
# unicorn.setlayout(unicorn.PHAT) # mini hat

import requests
import json
import unittest



""" From the UK MET Office website documentation:

You would like a complete list of the observations for
a specified location at each available time-step.
In this case you specify the location ID explicitly in the location field.
Example: to obtain observations for a specified location at all available times in XML format:

For json:
http://datapoint.metoffice.gov.uk/public/data/val/wxobs/all/json/[LocationID]?res=hourly&key=<API key>
Or for XML data return:
http://datapoint.metoffice.gov.uk/public/data/val/wxobs/all/xml/[LocationID]?res=hourly&key=<API key>


"""

Andrews_Field = "3684"

def get_weather_observations(location):
    """ From Andrews Field since that's the closest
    to my geographic location in Cambridge at the moment.
    Andrews Field has site ID 3684"""
    API_key = "238ccea7-66bf-44cf-8b14-b0d7b2d787bf"

    query_url = "http://datapoint.metoffice.gov.uk/public/data/val/wxobs/all/json/{0}?res=hourly&key={1}".format(location, API_key)
    print query_url
    response = requests.get(query_url)
    print response

    if response.status_code != 200:
        print "I failed with code ".format(response.status_code)

    data = response.json()
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

    def test_weather_obs_retrieve(self):
        self.assertEqual("tiddlybing", get_weather_observations(Andrews_Field))

    def tearDown(self):
        pass

if __name__ == "__main__":
    #unittest.main()
    data = get_weather_observations(Andrews_Field)
    print data


    
