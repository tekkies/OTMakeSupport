import threading
import time

import datetime

class SimulatedComms:

    def __init__(self, router):
        self.router = router
        thread = threading.Thread(target=self.simulator_main, args=(0, 0))
        thread.daemon = True
        thread.start()

    def simulator_main(self, a,b):
        while True:
            time.sleep(3)
            self.router.emit('serial', "RX simulated message \"%s\"" % datetime.datetime.now().time())
