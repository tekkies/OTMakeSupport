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

@socketio.on('serial')
def handle_message(data):
    emit('serial', "TX " + data)

@socketio.on('json')
def handle_json(json):
    send(json, json=True)

@socketio.on('my event')
def handle_my_custom_event(json):
    emit('my response', json)


@socketio.on('connect')
def connect():
    global router
    router.connect()


class Router:

    def __init__(self, socketio):
        self.socketio = socketio

    def connect(self):
        print "Browser connected"


if __name__ == '__main__':
    global router
    router = Router(socketio)
    if sys.argv.__contains__('--start-simulator'):
        simulator = SimulatedComms(socketio)
        simulator.simulator_start()
    socketio.run(app)

	