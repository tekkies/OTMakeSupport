#!/usr/bin/env python3

import sys

from flask import Flask
from flask_socketio import SocketIO, send, emit

from simulatedcomms import SimulatedComms
from serialcomms import SerialComms

class Router:

    def __init__(self, socketio):
        self.socketio = socketio

    def register_comms(self, comms):
        self.comms = comms

    def connect(self):
        print("Browser connected")

    def tx(self, data):
        self.comms.tx(data)

    def on_tx(self, data):
        self.__emit('tx', data)

    def on_rx(self, data):
        self.__emit('rx', data)

    def __emit(self, type, data):
        self.socketio.emit(type, data)

def init():
    print("Init pi_rev11_web_console")
    global router
    router = Router(socketio)
    if sys.argv.__contains__('--start-simulator'):
        comms = SimulatedComms(router)
    else:
        comms = SerialComms(router)

app = Flask(__name__, static_url_path='')
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)
init()

@app.route('/')
def root():
    return app.send_static_file('index.html')

@socketio.on('tx')
def tx(data):
    global router
    router.tx(data)

@socketio.on('connect')
def connect():
    global router
    router.connect()




if __name__ == '__main__':
    socketio.run(app)
