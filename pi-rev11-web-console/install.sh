#!/usr/bin/env bash

function ensure-python3-installed {
    if ! [ -x "$(command -v python3)" ]; then
        sudo apt-get install python3
    fi
}

function ensure-pip3-installed {
    if ! [ -x "$(command -v pip3)" ]; then
        sudo apt-get install python3-pip
    fi
}

function ensure-flask-installed {
	sudo apt-get install python3-flask
}

function ensure-flask-socketio-installed {
	sudo pip3 install flask-socketio
}

ensure-python3-installed
ensure-pip3-installed
ensure-flask-installed
ensure-flask-socketio-installed