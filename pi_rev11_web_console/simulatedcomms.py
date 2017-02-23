import threading
import time

import datetime

class SimulatedComms:

    def __init__(self, router):
        self.router = router
        router.register_comms(self)
        thread = threading.Thread(target=self.simulator_main, args=(0, 0))
        thread.daemon = True
        thread.start()

    def tx(self, data):
        self.router.emit('serial', "TX " + data)

    def on_rx(self, data):
        self.router.emit('serial', "RX " + data)

    def simulator_main(self, a,b):
        while True:
            time.sleep(3)
            self.on_rx("simulated message \"%s\"" % datetime.datetime.now().time())

