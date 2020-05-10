"""DocString"""


from generic import GenericEffect

class BrighbreathingEffect(GenericEffect):
    """DocString"""
    def __init__(self, **kwargs):
        """DocString"""
        self.enable = True

        self.speed = kwargs.get('speed', 0.01)

        self.min_brightness = kwargs.get('min_brightness', 0.0)
        self.max_brightness = kwargs.get('max_brightness', 1.0)

        self.start = kwargs.get('start', 0)
        self.end = kwargs.get('end', -1)
        self.forward = kwargs.get('forward', True)
        self.brightness = kwargs.get('brightness', 1.0)

        if self.min_brightness > 1:
            self.min_brightness = 1

        if self.min_brightness < 0:
            self.min_brightness = 0

        if self.max_brightness > 1:
            self.max_brightness = 1

        if self.max_brightness < 0:
            self.max_brightness = 0

        if self.brightness < self.min_brightness:
            self.brightness = self.min_brightness

        if self.brightness > self.max_brightness:
            self.brightness = self.max_brightness

    def iterate(self):
        """DocString"""
        if self.forward:
            self.brightness = self.brightness + self.speed
        else:
            self.brightness = self.brightness - self.speed

        if self.brightness > self.max_brightness or self.brightness < self.min_brightness:
            self.forward = not self.forward
            if self.forward:
                self.brightness = self.brightness + self.speed
            else:
                self.brightness = self.brightness - self.speed

        if self.enable:
            index = self.start
            while index < self.end:
                # self.led_strip.leds[index].set_brightness(self.brightness)

                self.led_strip.set_led_brightness(index, self.brightness)
                index = index + 1

    def position_int(self):
        """DocString"""
        return int(self.position)
