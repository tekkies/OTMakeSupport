#!/usr/bin/env python3

import sys

from flask import Flask
from flask_socketio import SocketIO, send, emit

from simulatedcomms import SimulatedComms
from serialcomms import SerialComms


class Router:

    def __init__(self, socketio):
        self.socketio = socketio
        self.comms = None

    def register_comms(self, comms):
        self.comms = comms

    def connect(self):
        if self.comms != None:
            self.__emit('port_changed', self.comms.port)
        print("Browser connected")

    def browser_to_router(self, data):
        self.comms.router_to_board(data)

    def router_to_browser(self, data):
        self.__emit('router_to_browser', data)

    def router_to_browser_echo(self, data):
        self.__emit('router_to_browser_echo', data)

    def port_change(self, port):
        if self.comms != None:
            self.comms.close()
        if port == "simulator":
            self.comms = SimulatedComms(router)
        else:
            self.comms = SerialComms(router, port)
        self.__emit('port_changed', port)


    def __emit(self, type, data):
        self.socketio.emit(type, data)

def init():
    print("Init pi_rev11_web_console")
    global router
    router = Router(socketio)


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

@socketio.on('port_change')
def browser_to_router(port):
    global router
    router.port_change(port)


@socketio.on('connect')
def connect():
    global router
    router.connect()




if __name__ == '__main__':
    socketio.run(app)
