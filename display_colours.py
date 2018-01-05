from time import sleep
from colour import Color  # python module to do simple colour gradients -or however we want to spell it - color? colour?
from weather import *  # weather.py I wrote myself to fetch weather API info from MET office site

import sys

import unicornhat as unicorn

unicorn.set_layout(unicorn.PHAT) # mini hat
unicorn.brightness(0.5)
unicorn.rotation(0)


# Make these global values to save calculating them each time
white = Color("white")
blue = Color("blue")
green = Color("green")
yellow = Color("yellow")
red = Color("red")

blue_to_white = list(blue.range_to(white, 11))
white_to_green = list(white.range_to(green, 11))
green_to_yellow = list(green.range_to(yellow, 11))
yellow_to_red = list(yellow.range_to(red, 11))

colours_range_total = blue_to_white + white_to_green[1:] + green_to_yellow[1:] + yellow_to_red[1:]
# Got to make sure we get rid of repeated fencepost colours


def temperature_to_hue(temperature):
    if temperature < -10:
        colour_choice = one_range_to_255_range(blue.rgb)
    elif temperature > 30:
        colour_choice = one_range_to_255_range(red.rgb)
    else:
        index = int(temperature) + 10
        colour_choice = one_range_to_255_range(colours_range_total[index].rgb)

    return colour_choice


def hue_to_RGB(hue_name):
    """ Take an RGB colour name and turn it into
    a tuple representation of that colour
    Eg hue_to_RGB("red") = (255, 0, 0)
    """
    colour_tuple = Color(hue_name)
    print(colour_tuple)
    result = one_range_to_255_range(colour_tuple.rgb)
    return result


def one_range_to_255_range(RGB_tuple):
    RGB = []
    for i in range(0, 3):
        result = int(RGB_tuple[i] * 255.0)
        RGB.append(result)
    vals = tuple(RGB)
    return vals


def show_colour_on_unicorn(RGB):
    width,height = unicorn.get_shape()
    for y in range(height):
        for x in range(width):
            unicorn.set_pixel(x,y,RGB[0], RGB[1], RGB[2])
    unicorn.show()


def display_temperature_output_spectrum():
    print("Pooping temperature based rainbows")
    sleep(0.5)
    for i in range(-5, 35):
        sleep(1)
        print("Colour for temperature: {0} deg C".format(i))
        show_colour_on_unicorn(temperature_to_hue(i))
        sleep(1)


def obtain_temperature_and_display_on_unicorn(weather_station, max_bright=0.5,
                                              time_displaying=24.0):
    """
    Get the temperature history from the last few hours & display for user
    """
    weather_observations = get_MET_weather_observations(weather_station)
    latest_temp_history = extract_API_temperatures(weather_observations)
    today_temp = extract_latest_temperature(latest_temp_history)

    bright = 0.1
    increment = max_bright / 24.0

    pause_to_display = time_displaying / 24.0

    for temp in latest_temp_history:
        print("Displaying temperature {}".format(temp))
        show_colour_on_unicorn(temperature_to_hue(temp))
        unicorn.brightness(bright + increment)
        sleep(pause_to_display)


if __name__ == "__main__":
    display_time = float(sys.argv[1])
    max_brightness = float(sys.argv[2])

    Andrews_Field = "3684"
    # Get data from here since it's closest to
    # my geographic location in Cambridge at the moment.
    print("Now displaying on Pi for your viewing pleasure.")
    obtain_temperature_and_display_on_unicorn(weather_station=Andrews_Field,
                                              max_bright=max_brightness,
                                              time_displaying=display_time)
    print("Goodbye!")
