#!/usr/bin/env python3
import time

import datetime

import sys
from flask import Flask, request, send_from_directory, copy_current_request_context
from flask_socketio import SocketIO, send, emit
import threading

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
    print "Browser connected"


if __name__ == '__main__':
    if sys.argv.__contains__('--start-simulator'):
        simulator = SimulatedComms(socketio)
        simulator.simulator_start()
    socketio.run(app)

	