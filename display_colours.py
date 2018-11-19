from time import sleep
from colour import Color  # module to do simple colour gradients

import sys
import math

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


def sigmoid_curve(x, L=1, k=1, x0=0):
    """
    The so-called 'Logistic' function
    https://en.wikipedia.org/wiki/Logistic_function

    It starts out increasing rapidly and slowly levels off to a constant.
    Dawn behaves this way.

    :param x: input
    :param L: Curve y maximum
    :param k: controls slope
    :param x0: Midpoint of curve
    :return: f(x)
    """
    return L/(1 + math.e**(-1 * k*(x - x0)))


def display_dawn_sigmoid(dawn_duration_mins=30.0):
    x = -6  # close enough approx to 0 start

    sleep_pause_sec = 1
    sec_per_step = dawn_duration_mins * 60 / 12.0  # ~ 12 steps in the sigmoid

    increment_x = sleep_pause_sec / sec_per_step
    yellow_to_white = list(yellow.range_to(white, 12))

    while x < 6:
        brightness = sigmoid_curve(x)
        unicorn.brightness(brightness)
        # We want dawn to shade from yellow into a bright white
        colour_choice = one_range_to_255_range(yellow_to_white[int(x) + 6].rgb)
        show_colour_on_unicorn(colour_choice)
        sleep(sleep_pause_sec)
        x += increment_x  # And increment brightness

    print("It's a new dawn, it's a new day.")


def show_colour_on_unicorn(RGB):
    """ Display an (R, G, B) value on the Unicorn Hat """
    width,height = unicorn.get_shape()
    for y in range(height):
        for x in range(width):
            unicorn.set_pixel(x, y, RGB[0], RGB[1], RGB[2])
    unicorn.show()


if __name__ == "__main__":
    import unicornhat as unicorn

    unicorn.set_layout(unicorn.PHAT)  # mini hat
    unicorn.rotation(0)

    dawn_duration_min = float(sys.argv[1])

    print("Now dawning on Pi for your viewing pleasure.")
    display_dawn_sigmoid(dawn_duration_min)
    print("Goodbye!")
