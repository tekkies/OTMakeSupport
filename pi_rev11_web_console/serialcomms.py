import threading
import time
import serial

import datetime

class SerialComms:

    def __init__(self, router):
        self.router = router

        self.ser = serial.Serial(
            port="/dev/serial0",
            baudrate=4800,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
            timeout=10
        )

        router.register_comms(self)
        thread = threading.Thread(target=self.simulator_main, args=(0, 0))
        thread.daemon = True
        thread.start()

    def tx(self, data):
        self.ser.write(bytes(data+"\n", 'utf-8'))
        self.router.on_tx(data)

    def on_rx(self, data):
        self.router.on_rx(data)

    def simulator_main(self, a,b):
        while True:
            rx = self.ser.readline()
            print("ser.readline()")
            print(rx)
            rx = str(rx)
            print(rx)
            self.on_rx(rx)

