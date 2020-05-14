"""DocString"""

import colorsys


class Color:
    """DocString"""
    def __init__(self, hue, saturation=1, brightness=1):
        """DocString"""
        self.hue = hue
        self.saturation = saturation
        self.brightness = brightness

        try:
            self.hue = int(self.hue) % 360
        except Exception as error:
            print(error)

    def get_rgb_color(self):
        """DocString"""
        return colorsys.hsv_to_rgb(self.hue/360.0, self.saturation, self.brightness)

    def __str__(self):
        """DocString"""
        return "{} {} {}".format(self.hue, self.saturation, self.brightness)

BLUE = Color(240, 1, 1)
RED = Color(0, 1, 1)
YELLOW = Color(40, 1, 1)
GREEN = Color(100, 1, 1)

WHITE = Color(0, 0, 1)
BLACK = Color(0, 0, 0)

RED_NO_BRIGHTNESS = Color(0, 1, None)
GREEN_NO_BRIGHTNESS = Color(100, 1, None)
BLUE_NO_BRIGHTNESS = Color(240, 1, None)
YELLOW_NO_BRIGHTNESS = Color(40, 1, None)

MAX_BRIGHTNESS = Color(None, None, 1)
NOSAT_MAX_BRIGHTNESS = Color(None, 0, 1)
NOSAT_MIN_BRIGHTNESS = Color(None, 0, 0.1)

NONE_SAT_MAX_BRIGHTNESS = Color(None, None, 1)
NONE_SAT_MIN_BRIGHTNESS = Color(None, None, 0)
