from time import sleep
"""
import unicornhat as unicorn
unicorn.set_layout(unicorn.PHAT) # mini hat
unicorn.brightness(0.5)
unicorn.rotation(0)
"""

def interpolate_smoothly(val1, val2, time_change, n_steps):
    interpolation_list = []
    time_step = time_change/n_steps
    print(time_step)
    val_step = (val2 - val1)/time_step
    print(val_step)
    new_val = val1
    while new_val < val2:
        new_val = val1 + val_step
        interpolation_list.append(new_val)
    return interpolation_list


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

    return RGB


def show_colour_on_unicorn(RGB):
    width,height=unicorn.get_shape()
    for y in range(height):
        for x in range(width):
            unicorn.set_pixel(x,y,RGB[0], RGB[1], RGB[2])
    unicorn.show()
    sleep(10)


def glow_fade_on_unicorn(time_tot):
    pass


if __name__ == "__main__":
    hue_to_unicorn("Yellow")