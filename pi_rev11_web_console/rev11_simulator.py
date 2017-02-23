import threading
import time

import datetime

script_socketio = None

def simulator(a,b):
    while True:
        time.sleep(1)
        script_socketio.emit('serial', "RX simulated message \"%s\"" % datetime.datetime.now().time())

def simulator_start(socketio):
    global script_socketio
    script_socketio = socketio
    t = threading.Thread(target=simulator, args=(0, 0))
    t.daemon = True
    t.start()

