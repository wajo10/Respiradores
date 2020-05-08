##############################################################################
# For copyright and license notices, see LICENSE file in root directory
##############################################################################
import datetime
import glob
import os
import sys
import threading
import time

import serial
import serial.tools.list_ports


def serial_ports_get():
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')
    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result

def get_ports():
    ports = list(serial.tools.list_ports.comports())
    for p in ports:
        if "Arduino" in p.description:
            return p[0]
        else:
            pass
    return "No Arduinos were found"
def serial_port_frames_get(port, timeout=3):
    def test(frames, port):
        with serial.Serial(port, timeout=0.1) as s:
            frames.append(s.read_until())

    frames = []
    thread = threading.Thread(target=test, args=[frames, port])
    thread.daemon = True
    thread.start()
    time.sleep(timeout)
    threading.currentThread().ident
    return frames


def serial_discovery_port(ports, quick = False):
    result = []
    for port in ports:
        frames = serial_port_frames_get(port)
        if frames and any(['DT' in str(f) for f in frames]):
            result.append(port)
            if quick:
                return [port]
    return result


def serial_get(port):
    return serial.Serial(port=port, baudrate=115200, timeout=0.1)

class FakeSerial:
    def __init__(self):
        self._waiting = True

    @property
    def in_waiting(self):
        return self._waiting

    def is_open(self):
        return True

    def read(self, size):
        pass

    def read_until(self, chr='\n'):
        pass

    def write(self, byte):
        pass

    def flush(self):
        pass


