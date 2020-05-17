"""Static Color"""


from generic import GenericEffect
from models.color import Color

class StaticEffect(GenericEffect):
    """DocString"""
    def __init__(self, **kwargs):
        """DocString"""
        self.name = "static"

        self.options = {
            "hue": "hue",
            "brightness": "brightness",
            "saturation": "saturation",
            "start": "start",
            "end": "start",
            "blend": "blend"
        }

        self.start = kwargs.get('start', 0)
        self.end = kwargs.get('end', -1)
        self.hue = kwargs.get('hue', True)
        self.saturation = kwargs.get('saturation', None)
        self.brightness = kwargs.get('brightness', None)
        self.blend = kwargs.get('blend', 'default')
        self.count = 0

        self.color = Color(self.hue, self.saturation, self.brightness)

        try:
            self.hue = int(self.hue) % 360
        except Exception as error:
            print(error)

    def iterate(self):
        """DocString"""
        index = 0
        while index < self.count:
            self.set_led((index + self.start), self.color)
            index = index + 1
