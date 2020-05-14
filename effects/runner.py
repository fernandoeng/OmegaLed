"""DocString"""


from generic import GenericEffect
from models.color import Color
from models.led_strip import LedStrip

class RunnerEffect(GenericEffect):
    """DocString"""
    def __init__(self, **kwargs):
        """DocString"""
        self.name = "runner"

        self.options = {
            "speed": "speed",
            "size": "size",
            "start": "start",
            "end": "start",
            "hue": "hue",
            "saturation": "saturation",
            "brightness": "brightness",
            "forward": "forward",
            "edge_bounce": "edge_bounce",
            "repeat": "repeat",
            "position": "position",
            "effects": "effects",
        }

        self.running = True

        self.hue = kwargs.get('hue', None)
        self.saturation = kwargs.get('saturation', None)
        self.brightness = kwargs.get('brightness', None)

        self.color = kwargs.get('color', Color(self.hue, self.saturation, self.brightness))

        self.speed = kwargs.get('speed', 1)
        self.size = int(kwargs.get('size', 1))
        self.start = kwargs.get('start', 0)
        self.end = kwargs.get('end', -1)

        self.edge_bounce = kwargs.get('edge_bounce', True)
        self.repeat = kwargs.get('repeat', True)
        self.forward = kwargs.get('forward', True)

        self.position = kwargs.get('position', 0)
        self.initial_position = self.position

        self.state = [0] * self.size
        self.effects = []
        self.sub_led_strip = LedStrip(self.size)

        if self.position < self.start:
            self.position = self.start

        if self.end > 0 and self.position > self.end:
            self.position = self.end

        try:
            self.hue = int(self.hue) % 360
        except Exception as error:
            print(error)

    def add_effect(self, effect):
        """DocString"""
        if isinstance(effect, GenericEffect):
            effect.atatch_led_strip(self.sub_led_strip)
            self.effects.append(effect)

    def iterate(self):
        """DocString"""
        if self.running:
            self.sub_led_strip.fill_color(self.color)

            for effect in self.effects:
                effect.iterate()

            index = 0
            in_frame_led_count = 1

            if (self.position_int() - self.start) < self.size:
                in_frame_led_count = self.position_int() - self.start
            else:
                in_frame_led_count = self.size

            while index < in_frame_led_count:
                if (self.position_int() - index) > self.start and (self.position_int() - index) < self.end:
                    self.led_strip.set_led(position=(self.position_int() - index), state=True, color=self.sub_led_strip.get_led(index).get_color())
                    # print(self.sub_led_strip.get_led(index).get_color())
                index = index + 1

            if self.forward:
                self.position = self.position + self.speed
            else:
                self.position = self.position - self.speed

            if self.position > self.end + self.size or self.position < self.start:
                if self.edge_bounce:
                    self.forward = not self.forward

                    if self.forward:
                        self.position = self.position + self.speed
                    else:
                        self.position = self.position - self.speed
                elif self.repeat:
                    self.position = self.start
                    # self.position = self.initial_position
                else:
                    self.running = False

    def position_int(self):
        """DocString"""
        return int(self.position)
