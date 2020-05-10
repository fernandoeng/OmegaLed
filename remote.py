"""Remote"""

from os import path

import json
import tornado.ioloop
import tornado.websocket
import tornado.web

from models.led_strip import LedStrip


strip = LedStrip(14)

def start():
    """animation"""
    strip.stop_animation()
    print("start_animation")
    strip.start_animation()

def stop():
    """stop"""
    print("stop animation")
    strip.stop_animation()

def change(effects):
    """change"""
    strip.remove_all_effects()

    for effect in effects:
        strip.add_effect_by_name(effect['name'], options=effect['options'])


class MainHandler(tornado.web.RequestHandler): # pylint: disable=W0223
    """MainHandler"""
    def get(self):
        """get"""
        file = open("{}/index.html".format(path.dirname(path.abspath(__file__))), "r")
        self.write(file.read())
        file.close()


class LedStripWebsocket(tornado.websocket.WebSocketHandler): # pylint: disable=W0223
    """LedStripWebsocket"""

    def check_origin(self, origin):
        """check_origin"""
        return True

    def open(self): # pylint: disable=W0221
        """open"""
        print("Websocket Opened")

    def on_message(self, message):
        """on_message"""
        print("LedStripWebsocket")
        print(message)
        data = json.loads(message)

        if data['action'] == 'stop':
            stop()
        if data['action'] == 'start':
            start()
        if data['action'] == 'change':
            if 'effects' in data:
                change(data['effects'])

    def on_close(self):
        """on_close"""
        print("Websocket Closed")


def make_app():
    """Make App"""
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/index", MainHandler),
        (r"/index.html", MainHandler),
        (r"/ledstrip", LedStripWebsocket),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)

    strip.add_effect_by_name("rainbow", options={"hue_end": 60})

    start()

    try:
        tornado.ioloop.IOLoop.current().start()
    finally:
        stop()
