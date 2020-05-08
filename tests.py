from PyQt5 import QtWidgets, QtCore, QtGui
import pyqtgraph as pg
import sys  # We need sys so that we can pass argv to QApplication
import os
from random import randint
import numpy as np

import serialArd
import serial, time
#self.port = serialArd.get_ports()
port = "COM13"
arduino = serial.Serial(port, 9600, timeout=1.0)
time.sleep(1)

### START QtApp #####
app = QtGui.QApplication([])            # you MUST do this once (initialize things)
####################

win = pg.GraphicsWindow(title="Grafica Arduino") # creates a window

p = win.addPlot(title="Grafica 1")  # creates empty space for the plot in the window
curve = p.plot(pen=(0,255,0))                        # create an empty "plot" (a curve to plot)
windowWidth = 500                       # width of the window displaying the curve
x = list(range(100))  # 100 time points
y = [randint(0, 1) for _ in range(100)]  # 100 data points         # create array that will contain the relevant time series
ptr = -windowWidth                      # set first x position

win.nextRow()

p2 = win.addPlot(title="Grafica 2")  # creates empty space for the plot in the window
curve2 = p2.plot(pen=(0,0,255))                        # create an empty "plot" (a curve to plot)                     # width of the window displaying the curve
x2 = list(range(100))  # 100 time points
y2 = [randint(0, 1) for _ in range(100)]  # 100 data points         # create array that will contain the relevant time series
ptr2 = -windowWidth                      # set first x position

# Realtime data plot. Each time this function is called, the data display is updated
def update():
    global curve, ptr, x,y, curve2, ptr2, x2,y2, arduino
    x = x[1:]  # Remove the first y element.
    x.append(x[-1] + 1)  # Add a new value 1 higher than the last.
    y = y[1:]  # Remove the first
    data = leer(arduino)
    y.append(data[0])  # Add a new random value.
    curve.setData(x, y)  # Update the data.

    x2 = x2[1:]  # Remove the first y element.
    x2.append(x2[-1] + 1)  # Add a new value 1 higher than the last.
    y2 = y2[1:]  # Remove the first
    y2.append(data[1])  # Add a new random value.
    curve2.setData(x2, y2)  # Update the data.

    QtGui.QApplication.processEvents()    # you MUST process the plot now

timer = QtCore.QTimer()
timer.timeout.connect(update)
timer.start(5)

def leer(arduino):
    dato = (arduino.readline().decode())
    dato = dato.split(",")
    print(dato)
    return int(dato[0]),int(dato[1])

## Start Qt event loop unless running in interactive mode or using pyside.
if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()