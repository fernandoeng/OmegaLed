"""DocString"""


class GenericEffect:
    """DocString"""
    def __init__(self):
        self.name = "generic"

        self.options = {
            "speed": "speed",
            "start": "start",
            "end": "start",
        }

        self.led_strip = None
        self.speed = 1
        self.start = 0
        self.end = -1
        self.count = 0
        self.blend = 'default'

    def iterate(self):
        """DocString"""

    def reset(self):
        """DocString"""
        self.count = self.end - self.start

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
        elif effect_name == 'static':
            from effects.static import StaticEffect
            effect = StaticEffect(**kwargs)
        elif effect_name == 'breathing':
            from effects.brightbreathing import BrighbreathingEffect
            effect = BrighbreathingEffect(**kwargs)
        elif effect_name == 'pulse':
            from effects.pulse import PulseEffect
            effect = PulseEffect(**kwargs)

        return effect

    def set_led(self, index, color, state=True):
        """Generic set Led"""
        if self.start <= index < self.end:
            try:
                self.led_strip.get_led(index).blend(color, self.blend)
                self.led_strip.get_led(index).turn(state)
            except Exception as e:
                print("failt to set led at index {} {}".format(index,str(e)))

    def atatch_led_strip(self, led_strip):
        """Generic Atach led strip"""
        self.led_strip = led_strip
        if self.end < 0:
            self.end = self.led_strip.size()

        self.reset()

    def to_json(self):
        """To Json"""
        result = {
            "name": self.name,
            "options" : {}
        }

        for option in self.options:
            if type(getattr(self, option)) is not object:
                result['options'][option] = getattr(self, option)

        return result
