"""DocString"""

import threading
from time import sleep

from led import Led
from effects.generic import GenericEffect

class LedStrip:
    """DocString"""
    def __init__(self, size):
        """DocString"""
        self.animation_thread = None
        self.leds = []
        self.effects = []
        self.running = False
        self.animation_speed = 30
        self.frames_per_second = 1.0 / self.animation_speed
        self.background_color = None
        index = 0
        while index < size:
            self.leds.append(Led())
            index = index + 1

    def size(self):
        """DocString"""
        return len(self.leds)

    def update(self):
        """DocString"""
        ledchain0 = ""
        for led in self.leds:
            ledchain0 = ledchain0 + led.hex_string()
        device_file = open("/dev/ledchain0", "w")
        device_file.write(ledchain0)
        device_file.close()

    def turn_all(self, state=False):
        """DocString"""
        for led in self.leds:
            led.turn(state)

    def turn_all_on(self):
        """DocString"""
        self.turn_all(True)

    def turn_all_off(self):
        """DocString"""
        self.turn_all(False)

    def set_brightness(self, brightness=1):
        """DocString"""
        if 0 < brightness < 100:
            for led in self.leds:
                led.set_brightness(brightness)

    def fill_color(self, color):
        """DocString"""
        for led in self.leds:
            led.set_color(color)

    def set_animation_speed(self, animation_speed):
        """DocString"""
        if animation_speed > 0:
            self.animation_speed = animation_speed
            self.frames_per_second = 1.0 / self.animation_speed

    def get_animation_speed(self):
        """DocString"""
        print(self.frames_per_second)
        return self.animation_speed

    def set_background_color(self, color):
        """DocString"""
        self.background_color = color

    def get_background_color(self):
        """DocString"""
        return self.background_color

    def start_animation(self):
        """DocString"""
        self.animation_thread = threading.Thread(target=self.animation_loop)
        self.animation_thread.start()

    def stop_animation(self):
        """DocString"""
        self.running = False
        sleep(self.frames_per_second)

    def animation_loop(self):
        """DocString"""
        self.running = True

        while self.running:
            self.iterate()
            self.update()
            sleep(self.frames_per_second)

    def iterate(self):
        """DocString"""
        if self.background_color is not None:
            self.fill_color(self.background_color)

        for effect in self.effects:
            effect.iterate()

    def remove_all_effects(self):
        """DocString"""
        self.effects = []

    def add_effect_by_name(self, effect_name, **kwargs):
        """DocString"""
        options = kwargs.get('options', None)

        effect = GenericEffect.get_effect_by_name(effect_name, **options)

        if effect is not None:
            if isinstance(effect, GenericEffect):
                effect.atatch_led_strip(self)
                self.effects.append(effect)

    def add_effect(self, effect):
        """DocString"""
        if isinstance(effect, Generic_effect):
            effect.atatch_led_strip(self)
            self.effects.append(effect)

    def get_effects(self):
        """Return the dict with all effects"""
        return self.effects

    def get_led(self, index):
        """DocString"""
        if 0 <= index < self.size():
            return self.leds[index]
        return None

    def set_led(self, **kwargs):
        """DocString"""
        position = kwargs.get('position')
        color = kwargs.get('color')
        state = kwargs.get('state')

        if position is None:
            print("no led position!")
            print(position)
            return

        if color:
            self.set_led_color(position, color)
        if state:
            self.set_led_state(position, state)

    def set_led_color(self, position, color):
        """DocString"""
        if 0 <= position < self.size():
            self.leds[position].set_color(color)

    def set_led_brightness(self, position, brightness):
        """DocString"""
        if 0 <= position < self.size():
            self.leds[position].set_brightness(brightness)

    def set_led_state(self, position, state):
        """DocString"""
        if 0 <= position < self.size():
            self.leds[position].turn(state)


    def to_json(self):
        """To Json"""
        result = {
            "size": self.size(),
            "running": self.running,
            "animation_speed": self.animation_speed,
            "frames_per_second": self.frames_per_second,
            "background_color": self.background_color,
        }

        return result
