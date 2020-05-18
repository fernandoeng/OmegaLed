"""Runner Effect"""


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
            "blend": "blend",
            "tail": "tail",
            "acceleration": "acceleration",
        }

        self.running = True

        self.hue = kwargs.get('hue', None)
        self.saturation = kwargs.get('saturation', None)
        self.brightness = kwargs.get('brightness', None)

        self.color = Color(self.hue, self.saturation, self.brightness)

        self.speed = kwargs.get('speed', 1)
        self.size = int(kwargs.get('size', 1))
        self.acceleration = kwargs.get('acceleration', 0)
        self.tail = int(kwargs.get('tail', 1))

        self.start = kwargs.get('start', 0)
        self.end = kwargs.get('end', -1)

        self.edge_bounce = kwargs.get('edge_bounce', True)
        self.repeat = kwargs.get('repeat', True)
        self.forward = kwargs.get('forward', True)

        self.blend = kwargs.get('blend', 'default')

        self.position = kwargs.get('position', 0)
        self.initial_position = self.position

        self.state_time = 0
        self.state = [0] * self.size
        self.tail_state = [0] * self.tail
        self.effects = []
        self.sub_led_strip = LedStrip(self.size)

        if self.position < self.start:
            self.position = self.start

        if self.end > 0 and self.position > self.end:
            self.position = self.end

        if self.tail > 0:
            self.tail_step = 1.0 / self.tail

        if self.tail_step < 0.01:
            self.tail_step = 0.01

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
                in_frame_led_count = self.position_int() - self.start + 1
            else:
                in_frame_led_count = self.size

            while index < in_frame_led_count:
                if (self.position_int() - index) >= self.start and (self.position_int() - index) < self.end:
                    self.set_led((self.position_int() - index), self.sub_led_strip.get_led(index).get_color())
                index = index + 1

            speed_iteration = self.speed * ((self.state_time * self.acceleration) + 1)

            if self.tail > 0:
                tail_brightness = speed_iteration
                tail_index = 1
                tail_size = tail_brightness - self.tail_step
                if tail_brightness > 0 and self.forward:
                    last_color = self.sub_led_strip.get_led(0).get_color()
                    while tail_brightness > 0:
                        tail_brightness = tail_brightness - (self.tail_step * ((tail_index * abs(self.acceleration)) + 1))
                        last_color.set_brightness(tail_brightness)
                        self.set_led((self.position_int() - tail_index), last_color)
                        tail_index = tail_index + 1
                else:
                    tail_brightness = abs(tail_brightness)
                    last_color = self.sub_led_strip.get_led(0).get_color()
                    while tail_brightness > 0:
                        tail_brightness = tail_brightness - (self.tail_step * ((tail_index * abs(self.acceleration)) + 1))
                        last_color.set_brightness(tail_brightness)
                        self.set_led((self.position_int() + tail_index), last_color)
                        tail_index = tail_index + 1

            if self.forward:
                self.position = self.position + speed_iteration
            else:
                self.position = self.position - speed_iteration

            self.state_time = self.state_time + 1

            if self.position_int() > self.end + self.size + self.tail or self.position_int() < self.start - 1 - self.tail:
                self.state_time = 0
                if self.edge_bounce:
                    if self.position < 0:
                        self.forward = True
                    if self.position > self.end + self.size:
                        self.forward = False
                    if self.forward:
                        self.position = 0
                    else:
                        self.position = self.end + self.size
                elif self.repeat:
                    self.position = self.start
                else:
                    self.running = False

    def position_int(self):
        """DocString"""
        return int(self.position)
