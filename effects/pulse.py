"""Breathing effect"""


from generic import GenericEffect
from models.color import Color

class PulseEffect(GenericEffect):
    """DocString"""
    def __init__(self, **kwargs):
        """DocString"""
        self.name = "pulse"

        self.options = {
            "speed": "speed",
            "start": "start",
            "end": "start",
            "blend": "blend",
            "pulse": "pulse",
            "hue": "hue",
            "saturation": "saturation",
            "brightness": "brightness",
            "size": "size",
            "spread": "spread",
            "acceleration": "acceleration",
            "fill": "fill",
        }

        self.enable = True
        self.state = 0
        self.position = 0

        self.speed = kwargs.get('speed', 0.25)
        self.start = kwargs.get('start', 0)
        self.end = kwargs.get('end', -1)
        self.forward = kwargs.get('forward', True)
        self.blend = kwargs.get('blend', 'default')

        self.pulse = kwargs.get('pulse', None)
        self.spread = kwargs.get('spread', 7)
        self.acceleration = kwargs.get('acceleration', 0)
        self.fill = kwargs.get('fill', False)
        self.size = kwargs.get('size', 1)
        self.hue = kwargs.get('hue', 0)
        self.saturation = kwargs.get('saturation', None)
        self.brightness = kwargs.get('brightness', None)
        self.color = Color(self.hue, self.saturation, self.brightness)

    def reset(self):
        """DocString"""
        self.count = self.end - self.start

        if self.pulse is None:
            self.pulse = int((self.end - self.start)/2)

        if self.pulse > self.end - self.start:
            self.pulse = self.end - self.start

        self.pulse_start = self.pulse

    def iterate(self):
        """DocString"""


        if self.fill:
            index = int(self.pulse_start - self.position)
            while index < int(self.pulse_start + self.position):
                self.set_led(index, self.color)
                index = index + 1
        else:
            self.set_led(int(self.pulse_start + self.position), self.color)
            self.set_led(int(self.pulse_start - self.position), self.color)


        self.position = self.position + self.speed * ((self.state * self.acceleration) + 1)
        self.state = self.state + 1

        if self.position < 0 or self.position > self.spread:
            self.position = 0
            self.state = 0

    def position_int(self):
        """DocString"""
        return int(self.position)
