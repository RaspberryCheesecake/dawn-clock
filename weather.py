"""
import unicornhat as unicorn
unicorn.setlayout(unicorn.PHAT) # mini hat
unicorn.brightness(0.2)
unicorn.rotation(0)

"""

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

def get_MET_weather_observations(location):
    """ From Andrews Field since that's the closest
    to my geographic location in Cambridge at the moment.
    Andrews Field has site ID 3684"""
    
    API_key = "238ccea7-66bf-44cf-8b14-b0d7b2d787bf"

    query_url = "http://datapoint.metoffice.gov.uk/public/data/val/wxobs/all/json/{0}?res=hourly&key={1}".format(location, API_key)
    response = requests.get(query_url)

    if response.status_code != 200:
        print "I failed with code ".format(response.status_code)

    data = response.json()
    # OK, need to change from unicode before I do the .json() interpretation here - or it doesn't give me my nicely formatted dict
    return data

def extract_temperature(data):
    output = [int(s) for s in data.split() if s.isdigit()]
    return output[0]


def extract_API_temperature(MET_data):
    output=""
    for report in MET_data["SiteRep"]:
        output += report + ","
    return output


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

def hue_to_unicorn(hue):
    """ Take an RGB colour and display it on the Unicorn HAT
    Eg hue =(0, 255, 255)
    """
    if hue == "White":
        RGB = (255, 255, 255)
    elif hue == "Blue":
        RGB = (0, 0, 255)
    elif hue == "Green":
        RGB = (0, 255, 0)
    elif hue == "Yellow":
        RGB = (255, 255, 0)
    elif hue == "Red":
        RGB = (255, 0, 0)
    else return "Error! Try a colour input"
    
    width,height=unicorn.get_shape()
    for y in range(height):
        for x in range(width):
            unicorn.set_pixel(x,y,RGB)
    unicorn.show()


class TestWeatherDisplay(unittest.TestCase):
    def setUp(self):
        self.mock_temp_data = "Baby it's cold outside: 13 degrees C"

    def test_extracting_temperature(self):
        self.assertEqual(extract_temperature(self.mock_temp_data), 13)

    def test_display_temperature(self):
        self.assertEqual(temperature_to_hue(13), "Green")

    def test_extract_temperature(self):
        self.assertEqual("DV,Wx,", extract_API_temperature(get_MET_weather_observations(Andrews_Field)))

    def tearDown(self):
        pass

if __name__ == "__main__":
    #unittest.main()
    hue_to_unicorn("Yellow")


    
