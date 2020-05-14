"""DocString"""


from generic import GenericEffect
from models.color import Color

class StaticEffect(GenericEffect):
    """DocString"""
    def __init__(self, **kwargs):
        """DocString"""
        self.name = "static"

        self.options = {
            "hue": "hue",
            "start": "start",
            "end": "start"
        }

        self.start = kwargs.get('start', 0)
        self.end = kwargs.get('end', -1)
        self.hue = kwargs.get('hue', True)
        self.count = 0

        try:
            self.hue = int(self.hue) % 360
        except Exception as error:
            print(error)

    def reset(self):
        """DocString"""
        self.count = self.end - self.start

    def iterate(self):
        """DocString"""
        index = 0
        while index < self.count:
            self.led_strip.set_led(position=(index + self.start), state=True, color=Color(self.hue, None, None))
            index = index + 1
