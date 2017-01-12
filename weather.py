"""
import unicornhat as unicorn
unicorn.set_layout(unicorn.PHAT) # mini hat
unicorn.brightness(0.5)
unicorn.rotation(0)
"""

from time import sleep
import requests
import json
import unittest

Andrews_Field = "3684" # Get data from here since it's closest to
# my geographic location in Cambridge at the moment.

def get_MET_weather_observations(location):
    """ From the UK MET Office website documentation:
    Example: to obtain observations for a specified location at all available times in XML format:
    For json:
    http://datapoint.metoffice.gov.uk/public/data/val/wxobs/all/json/[LocationID]?res=hourly&key=<API key>
    Or for XML data return:
    http://datapoint.metoffice.gov.uk/public/data/val/wxobs/all/xml/[LocationID]?res=hourly&key=<API key>
    """
    API_key = "238ccea7-66bf-44cf-8b14-b0d7b2d787bf"

    query_url = "http://datapoint.metoffice.gov.uk/public/data/val/wxobs/all/json/{0}?res=hourly&key={1}".format(location, API_key)
    response = requests.get(query_url)

    if response.status_code != 200:
        print("I failed with code ".format(response.status_code))

    data = response.json()
    # OK, need to change from unicode before I do the .json() interpretation -
    # or it doesn't give me my nicely formatted dict... what's going on??
    #print(json.dumps(data, sort_keys=True, indent=4))
    return data

def extract_temperature(data):
    output = [int(s) for s in data.split() if s.isdigit()]
    return output[0]


def extract_API_temperature(MET_data):
    output=""
    temp_strings = MET_data["SiteRep"]["DV"]["Location"]["Period"]
    print(temp_strings[0])
    temp_rep = temp_strings[0]["Rep"]
    print(temp_rep)
    temp_rep2 = temp_rep[0]["T"]
    print(temp_rep2)
    return temp_rep2


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
    else:
        return "Not a colour I know, try another"
    
    width,height=unicorn.get_shape()
    for y in range(height):
        for x in range(width):
            unicorn.set_pixel(x,y,RGB[0], RGB[1], RGB[2])
    unicorn.show()

    sleep(5)


if __name__ == "__main__":
    hue_to_unicorn("Yellow")


    
