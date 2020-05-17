"""DocString"""

import colorsys


class Color:
    """DocString"""
    def __init__(self, hue, saturation=1, brightness=1):
        """DocString"""
        self.hue = None
        self.saturation = None
        self.brightness = None

        self.set_hue(hue)
        self.set_saturation(saturation)
        self.set_brightness(brightness)

    def get_rgb_color(self):
        """Get RGB color"""
        result = colorsys.hsv_to_rgb(self.hue/360.0, self.saturation, self.brightness)
        return result

    def set_hue(self, hue):
        """Set hue, min 0 max 360"""
        if hue is not None:
            self.hue = hue % 360
            if self.hue < 0:
                self.hue = 0 - self.hue

    def get_hue(self):
        """Get hue"""
        return self.hue

    def set_brightness(self, brightness):
        """DocString"""
        if brightness is not None:
            self.brightness = brightness
            if self.brightness < 0:
                self.brightness = 0
            elif self.brightness > 1:
                self.brightness = 1

    def set_saturation(self, saturation):
        """DocString"""
        if saturation is not None:
            self.saturation = saturation
            if self.saturation < 0:
                self.saturation = 0
            elif self.saturation > 1:
                self.saturation = 1

    def set_color(self, color):
        """Set led color"""
        if color.hue and color.hue is not None:
            self.set_hue(color.hue)

    def blend_sum_color(self, color):
        """Blend color with hue sum"""
        if color.hue and color.hue is not None:
            self.set_hue(self.hue + color.hue)
        # if color.brightness and color.brightness is not None:
        #     self.brightness = self.brightness + color.brightness
        # if color.saturation and color.saturation is not None:
        #     self.saturation = self.saturation + color.saturation

    def __str__(self):
        """DocString"""
        return "hue: {} Sat: {} Bri: {}".format(self.hue, self.saturation, self.brightness)

    def to_json(self):
        """DocString"""
        return "{ 'hue': {}, 'saturation': {}, 'brightness': {} }".format(self.hue, self.saturation, self.brightness)

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
