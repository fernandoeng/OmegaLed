"""DocString"""


class GenericEffect:
    """DocString"""
    def __init__(self):
        self.led_strip = None
        self.speed = 1
        self.start = 0
        self.end = -1

    def iterate(self):
        """DocString"""

    def reset(self):
        """DocString"""

    def set_speed(self, speed):
        """DocString"""
        self.speed = speed

    def get_speed(self):
        """DocString"""
        return self.speed

    @staticmethod
    def get_effect_by_name(effect_name, **kwargs):
        """DocString"""
        effect = None

        print("get_effect_by_name")
        print(kwargs)

        if effect_name == 'rainbow':
            from effects.rainbow import RainbowEffect
            effect = RainbowEffect(**kwargs)
        elif effect_name == 'runner':
            from effects.runner import RunnerEffect
            effect = RunnerEffect(**kwargs)

        return effect

    def atatch_led_strip(self, led_strip):
        """DocString"""
        self.led_strip = led_strip
        if self.end < 0:
            self.end = self.led_strip.size()

        self.reset()
