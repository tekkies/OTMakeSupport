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
        self.router.on_tx(data)

    def on_rx(self, data):
        self.router.on_rx(data)

    def simulator_main(self, a,b):
        while True:
            time.sleep(1)
            #self.on_rx("simulated message \"%s\"" % datetime.datetime.now().time())
            self.on_rx("")
            self.on_rx(">")

