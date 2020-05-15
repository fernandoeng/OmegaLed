"""DocString"""


from generic import GenericEffect
from models.color import Color

class RainbowEffect(GenericEffect):
    """DocString"""
    def __init__(self, **kwargs):
        """DocString"""
        self.name = "rainbow"

        self.options = {
            "speed": "speed",
            "start": "start",
            "end": "start",
            "hue_start": "hue_start",
            "hue_end": "hue_end",
            "forward": "forward",
            "blend": "blend",
        }

        self.state = []

        self.hue_count = 0
        self.hue_step = 0
        self.count = 0

        self.speed = kwargs.get('speed', 1)
        self.hue_start = kwargs.get('hue_start', 0)
        self.hue_end = kwargs.get('hue_end', 360)
        self.start = kwargs.get('start', 0)
        self.end = kwargs.get('end', -1)
        self.forward = kwargs.get('forward', True)
        self.blend = kwargs.get('blend', 'default')


    def reset(self):
        """DocString"""
        self.count = self.end - self.start
        self.hue_count = self.hue_end - self.hue_start
        self.state = [0] * self.count
        self.hue_step = self.hue_count / self.count

        if self.forward:
            index = 0
            while index < self.count:
                self.state[index] = index * self.hue_step + self.hue_start
                index = index + 1
        else:
            index = self.end - 1
            while index >= self.start:
                # self.led_strip.leds[index].on()
                # self.led_strip.leds[index].set_hue(index*self.hue_step )
                self.state[index - self.start] = index * self.hue_step
                index = index - 1

    def iterate(self):
        """DocString"""
        index = 0
        while index < self.count:
            self.state[index] = self.state[index] + int(self.speed)
            if self.blend == 'sum':
                actual_color = self.led_strip.get_led(index).get_color()
                self.led_strip.set_led(position=(index + self.start), state=True, color=Color(self.state[index] + int(actual_color.hue), None, None))
            elif self.blend == 'multiply':
                actual_color = self.led_strip.get_led(index).get_color()
                self.led_strip.set_led(position=(index + self.start), state=True, color=Color(self.state[index] * int(actual_color.hue), None, None))
            else:
                self.led_strip.set_led(position=(index + self.start), state=True, color=Color(self.state[index], None, None))

            index = index + 1
