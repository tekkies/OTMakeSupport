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

    def browser_to_router(self, data):
        self.comms.router_to_board(data)

    def router_to_browser(self, data):
        self.__emit('router_to_browser', data)

    def router_to_browser_echo(self, data):
        self.__emit('Rt', data)


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

@socketio.on('browser_to_router')
def browser_to_router(data):
    global router
    router.browser_to_router(data)

@socketio.on('connect')
def connect():
    global router
    router.connect()




if __name__ == '__main__':
    socketio.run(app)
