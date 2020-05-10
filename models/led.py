"""DocString"""
from models.color import Color

class Led:
    """DocString"""
    def __init__(self):
        """DocString"""
        self.state = False
        self.hex_color = [1, 1, 1]
        self.color = Color(0, 1, 1)
        self.hue = 0
        self.saturation = 100
        self.brightness = 100

    def set_color(self, color):
        """DocString"""
        # self.hex_color = color
        if color.hue is not None:
            self.color.hue = color.hue
        if color.saturation is not None:
            self.color.saturation = color.saturation
        if color.brightness is not None:
            self.color.brightness = color.brightness

    def get_color(self):
        """DocString"""
        return self.color

    def get_rgb_color(self):
        """DocString"""
        self.hex_color = self.color.get_rgb_color()
        return self.hex_color

    def set_hue(self, hue):
        """DocString"""
        self.hue = hue % 360

    def get_hue(self):
        """DocString"""
        return self.hue

    def set_saturation(self, saturation):
        """DocString"""
        self.color.saturation = saturation % 360

    def get_saturation(self):
        """DocString"""
        return self.color.saturation

    def set_brightness(self, brightness):
        """DocString"""
        if brightness > 1:
            self.color.brightness = 1
            return
        if brightness < 0:
            self.color.brightness = 0
            return

        self.color.brightness = brightness

    def get_brightness(self):
        """DocString"""
        return self.color.brightness

    def turn(self, state):
        """DocString"""
        self.state = state

    def turn_on(self):
        """DocString"""
        self.turn(True)

    def turn_off(self):
        """DocString"""
        self.turn(False)

    def hex_string(self):
        """DocString"""
        hex_color_string = ""
        if self.state:
            self.hex_color = self.get_rgb_color()
            for hex_string in self.hex_color:
                hex_color_string = hex_color_string + chr(int(hex_string*255))
        else:
            hex_color_string = chr(0)+chr(0)+chr(0)
        return hex_color_string
