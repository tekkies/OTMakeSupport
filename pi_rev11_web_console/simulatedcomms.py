import threading
import time

import datetime

class SimulatedComms:

    def __init__(self, socketio):
        self.socketio = socketio
        thread = threading.Thread(target=self.simulator_main, args=(0, 0))
        thread.daemon = True
        thread.start()

    def simulator_main(self, a,b):
        while True:
            time.sleep(3)
            self.socketio.emit('serial', "RX simulated message \"%s\"" % datetime.datetime.now().time())
