import threading
import time

import datetime

class Simuator:

    def __init__(self, socketio):
        self.socketio = socketio

    def simulator_main(self, a,b):
        while True:
            time.sleep(1)
            self.socketio.emit('serial', "RX simulated message \"%s\"" % datetime.datetime.now().time())

    def simulator_start(self):
        t = threading.Thread(target=self.simulator_main, args=(0, 0))
        t.daemon = True
        t.start()

