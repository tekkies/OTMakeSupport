import threading
import time

import datetime
import queue


class SimulatedComms:



    def __init__(self, router):
        self.router = router
        self.from_browser = queue.Queue()
        router.register_comms(self)
        self.live = True
        self.thread = threading.Thread(target=self.simulator_main, args=(0, 0))
        self.thread.daemon = True
        self.thread.start()

    def close(self):
        self.live = False

    def simulate_command(self, data):
        upper_data = data.upper()
        if(upper_data == "I"):
            self.on_rx("ID TH IS IS AF AK EI D")

    def router_to_board(self, data):
        self.from_browser.put(data)
        self.router.router_to_browser_echo(data)

    def on_rx(self, data):
        self.router.router_to_browser(data)

    def simulator_main(self, a,b):
        self.simulation_test_wake_command_prompt()

    def simulate_command_prompt(self):
        loop = 0
        while self.live:
            time.sleep(1)
            if (loop % 10 == 0):
                self.on_rx('=F0%@22CE;X0;T16 10 W0 48 F2 54 W255 0 F255 0;S6 6 18 e;C5;{"@":"12ab","vC|%":0,"L":0,"B|cV":321}')
            else:
                self.on_rx("")
                self.on_rx(">")
            loop = loop + 1


    def simulation_test_wake_command_prompt(self):
        loop = 0
        while self.live:
            if not self.from_browser.empty():
                rx = self.from_browser.get_nowait()
                self.simulate_command_prompt()
            time.sleep(0.1)

