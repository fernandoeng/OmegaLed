"""Remote"""

from os import path

import uuid
import time
import json
import tornado.ioloop
import tornado.websocket
import tornado.web

from models.led_strip import LedStrip
from models.color import Color


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

    for key in clients:
        print(clients[key].uuid)
        clients[key].send_led_strip_info()

    json.dump(effects, open("./effect.store", "w"))

clients = {}


class MainHandler(tornado.web.RequestHandler): # pylint: disable=W0223
    """MainHandler"""
    def get(self):
        """get"""
        file = open("{}/index.html".format(path.dirname(path.abspath(__file__))), "r")
        self.write(file.read())
        file.close()


class LedStripWebsocket(tornado.websocket.WebSocketHandler): # pylint: disable=W0223
    """LedStripWebsocket"""

    def simple_init(self):
        """ Initialize Socket """
        self.last = time.time()
        self.stop = False
        self.uuid = uuid.uuid1()

    def check_origin(self, origin):
        """check_origin"""
        return True

    def send_led_strip_info(self):
        """check_origin"""

        result = {}

        result['ledstrip'] = strip.to_json()

        effects = strip.get_effects()

        result['effects'] = []
        for effect in effects:
            result['effects'].append(effect.to_json())

        result_json = "{}"

        try:
            result_json = json.dumps(result)
        except Exception as error:
            print(error)

        self.write_message(u"{}".format(result_json))


    def open(self): # pylint: disable=W0221
        """open"""
        print("Websocket Opened")
        self.simple_init()

        clients[self.uuid] = self

        self.send_led_strip_info()

        self.loop = tornado.ioloop.PeriodicCallback(self.keep_alive, 1000)
        self.loop.start()

    def keep_alive(self):
        """Keep alive"""
        if time.time() - self.last > 10:
            self.write_message(u'{"message":"keep Alive"}')
            self.last = time.time()

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
                self.write_message(u'{"message":"Changes done!"}')

    def on_close(self):
        """on_close"""
        print("Websocket Closed")
        try:
            self.loop.stop()
            del clients[self.uuid]
        except KeyError:
            print("Could not remove {}".format(self.uuid))
        except Exception:
            print("Exception {}".format(self.uuid))


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

    try:
        effects = json.load(open("./effect.store", "r"))
        change(effects)
    except Exception as error:
        print('Could not load from file, error: {}',format(error))
        strip.add_effect_by_name("rainbow", options={"hue_end": 60})

    strip.set_background_color(Color(0,0,0))

    start()

    try:
        tornado.ioloop.IOLoop.current().start()
    finally:
        stop()
