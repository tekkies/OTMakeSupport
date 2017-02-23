#!/usr/bin/env python3

import sys

from flask import Flask
from flask_socketio import SocketIO, send, emit

from simulatedcomms import SimulatedComms

app = Flask(__name__, static_url_path='')
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def root():
    return app.send_static_file('index.html')

@socketio.on('command')
def handle_message(data):
    global router
    router.command(data)

@socketio.on('connect')
def connect():
    global router
    router.connect()


class Router:

    def __init__(self, socketio):
        self.socketio = socketio

    def register_comms(self, comms):
        self.comms = comms

    def connect(self):
        print "Browser connected"

    def command(self, data):
        comms.tx(data)

    def emit(self, type, data):
        self.socketio.emit(type, data)

    def tx_confirm(self, data):
        self.emit('tx', data)


if __name__ == '__main__':
    global router
    router = Router(socketio)
    if sys.argv.__contains__('--start-simulator'):
        comms = SimulatedComms(router)
    socketio.run(app)
