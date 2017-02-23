# pi-rev11-web-console

An asynchronous web interface to probe a REV11 stats hub when directly connected to a Raspberry Pi

## Plan
* [ ] Configure Raspberry Pi on-board serial port for connection to a stats hub
* [ ] Set up a lightweight web server on the Pi
* [ ] Build a simple web page to allow commands to be sent to the stats hub
* [ ] Any messages received on the serial port should be immediately displayed on the web page

## Overview

Built on python3, flask, SocketIO

## Setup

1. [Reconfigure serial port UART0 on the Pi](#Reconfigure serial port UART0 on the Pi)

## Reconfigure serial port UART0 on the Pi

Before we can access serial port UART0 from our code, we need reconfigure the Pi so it does not claim UART0 at boot up as a serial console shell.

See section [RaspberryPi Serial - Setting up the Pi](https://github.com/opentrv/OTWiki/wiki/RaspberryPi-Serial#setting-up-the-pi) in the wiki.
