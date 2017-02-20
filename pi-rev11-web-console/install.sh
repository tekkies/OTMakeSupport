#!/usr/bin/env bash

function ensure-flask-installed {
    if ! [ -x "$(command -v flask)" ]; then
        echo 'Installing flask now...' >&2
        sudo apt-get install python3-flask
    fi
}

function ensure-flask-installed {
	sudo apt-get install python3
}

ensure-python3-installed
ensure-flask-installed