import threading
import time

import datetime
import queue


class SimulatedComms:



    def __init__(self, router):
        self.router = router
        self.receive_queue = queue.Queue()
        router.register_comms(self)
        thread = threading.Thread(target=self.simulator_main, args=(0, 0))
        thread.daemon = True
        thread.start()

    def simulate_command(self, data):
        upper_data = data.upper()
        if(upper_data == "I"):
            self.on_rx("ID TH IS IS AF AK EI D")

    def tx(self, data):
        self.router.on_tx(data)
        self.receive_queue.put(data)
        #self.simulate_command(data)

    def on_rx(self, data):
        self.router.on_rx(data)

    def simulator_main(self, a,b):
        self.simulation_test_wake_command_prompt()

    def simulate_command_prompt(self):
        loop = 0
        while True:
            time.sleep(1)
            if (loop % 10 == 0):
                self.on_rx("Fake simulated message \"%s\"" % datetime.datetime.now().time())
            else:
                self.on_rx("")
                self.on_rx(">")
            loop = loop + 1


    def simulation_test_wake_command_prompt(self):
        loop = 0
        while True:
            if not self.receive_queue.empty():
                rx = self.receive_queue.get_nowait()
                self.simulate_command_prompt()
            time.sleep(0.1)

