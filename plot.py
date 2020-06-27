##############################################################################
# For copyright and license notices, see LICENSE file in root directory
##############################################################################
import sys

import core
import numpy as np
import pyqtgraph as pg
import serialArd
from PyQt5 import QtCore, QtGui, QtWidgets, uic

pg.setConfigOption('background', '052049')
pg.setConfigOption('leftButtonPan', False)

core= core.Core
class MainWindow(QtWidgets.QDialog):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._ignore_config = []
        self._serial = None
        self._pres1 = 0
        self._pres2 = 0
        self._pip = 20
        self._peep = 6
        self._fr = 14
        self._flow = 0
        self._vol = 99
        self._config_pip = 20
        self._config_peep = 6
        self._config_fr = 14
        self._recruit = False
        self._recruit_on_text = 'STOP RECRUIT'
        self._recruit_off_text = 'RECRUIT'
        self._recruit_timmer = None
        self.serial_setup()
        uic.loadUi(core.path('ui_main.ui'), self)
        self.buttonUpPip.clicked.connect(self.buttonUpPipClicked)
        self.buttonDownPip.clicked.connect(self.buttonDownPipClicked)
        self.buttonUpPeep.clicked.connect(self.buttonUpPeepClicked)
        self.buttonDownPeep.clicked.connect(self.buttonDownPeepClicked)
        self.buttonUpFR.clicked.connect(self.buttonUpFRClicked)
        self.buttonDownFR.clicked.connect(self.buttonDownFRClicked)
        self.buttonRecruit.clicked.connect(self.buttonRecruitClicked)
        self.buttonConfigMode.clicked.connect(self.buttonConfigModeClicked)
        self.stackedWidget.setCurrentIndex(0)
        self.buttonConfigMode.setStyleSheet("background-color: #506380")
        self._recruit_on_stylesheet = "background-color: red"
        self._recruit_off_stylesheet = self.buttonRecruit.styleSheet()
        self.timer = pg.QtCore.QTimer()
        self.timer.timeout.connect(self.serial_read)
        self.myCurve = [0, 0, 0]
        self.chunkSize = 200
        self.split = 100
        self.xAxis = np.arange(self.chunkSize)
        self.data1 = np.zeros((self.chunkSize, 3))
        self.plot(0, self.graphPressure, "P", self.xAxis, self.data1[:, 0])
        self.plot(1, self.graphFlow, "C", self.xAxis, self.data1[:, 1])
        self.myCurve[0].setPen(pg.mkPen('f7a665', width=2))
        self.myCurve[1].setPen(pg.mkPen('5dbfc5', width=2))
        self.pointer = 0
        self.firstCycle = 1
        self.update()

    def show(self, *args, **kwargs):
        res = super().show()
        self.timer.start(10)
        return res

    def serial_setup(self):
        file = core.config['serial_file']
        if file:
            self.serial = serialArd.FileSerial(file)
            return
        port = core.config['serial_port']
        if not port and core.debug:
            core.logger.debug(
                'In debug mode connect to fakeSerial, for force port add '
                '"serial_port" in config.yml')
            self.serial = serialArd.FakeSerial()
            return
        if not port:
            ports = serialArd.serial_ports_get()
            port = serialArd.serial_discovery_port(ports, quick=True)
        if not port:
            print(
                'You must set a "serial_port" value for config file '
                'config.yml')
            sys.exit(-1)
        core.logger.debug('Connect to port "%s"' % port)
        self.serial = serialArd.serial_get(port)
        if not self.serial.is_open:
            raise Exception('Can\'t open serial port %s' % port)
        self.serial.reset_input_buffer()

    def serial_send(self, msg):
        def no_ignore_config():
            if self._ignore_config:
                self._ignore_config.pop(0)

        self._ignore_config.append(1)
        pg.QtCore.QTimer().singleShot(5000, no_ignore_config)

        timer = pg.QtCore.QTimer()
        timer.timeout.connect(self.serial_read)

        core.logger.info('Serial send "%s"' % msg)
        self.serial.write(bytes('%s\r\n' % msg, 'utf8'))
        self.serial.flush()

    def serial_read(self):
        line = self.serial.read_until()
        if not line:
            return
        data = line.strip().decode().split(' ')
        core.logger.debug('Read line: %s' % data)
        # frame: CONFIG pip peep rpm
        if data[0] == 'CONFIG':
            if self._ignore_config:
                core.logger.debug('Ignore config')
                return
            self._config_pip = int(data[1])
            self._config_peep = int(data[2])
            self._config_fr = int(data[3])
            self._fr = int(data[3])
            self.update()
        # frame: DT pres1 pres2 vol flow
        elif data[0] == 'DT':
            self._pres1 = int(data[1])
            self._pres2 = int(data[3])
            # self._vol = int(data[3])
            self._flow = int(data[4])
            self.update()
        # frame: VOL vol
        elif data[0] == 'VOL':
            # self._vol = int(data[1])
            # self.update()
            pass
        # frame: EOC pip peep vol
        elif data[0] == 'EOC':
            self._pip = int(data[1])
            self._peep = int(data[2])
            self._vol = int(data[3])
            self.update()

    def plot(self, chartIndex, widget, title, hour, temperature):
        self.myCurve[chartIndex] = widget.plot(hour, temperature, title=title)
        widget.setXRange(0, self.chunkSize, padding=0)
        if chartIndex == 0:
            widget.setYRange(0, 50)
        else:
            widget.setYRange(-20, 30)
        widget.setMouseEnabled(False, False)
        widget.disableAutoRange()
        widget.showGrid(True, True, 1)

    @property
    def _compliance(self) -> float:
        return self._vol / (self._pip - self._peep)

    def update(self):
        self.configPip.setText(str(self._config_pip))
        self.configPeep.setText(str(self._config_peep))
        self.configFr.setText(str(self._config_fr))
        self.textPip.setText(str(self._pip))
        self.textPeep.setText(str(self._peep))
        self.textFr.setText(str(self._fr))
        self.textVol.setText(str(self._vol))
        self.textComp.setText(str(round(self._compliance, 1)))
        pres = self._pres1
        flow = self._flow
        self.i = self.pointer % (self.chunkSize)
        if self.i == 0 and self.firstCycle == 0:
            tmp = np.empty((self.chunkSize, 3))
            tmp[:self.split] = self.data1[self.chunkSize - self.split:]
            self.data1 = tmp
            self.pointer = self.split
            self.i = self.pointer
        self.data1[self.i, 0] = pres
        self.data1[self.i, 1] = float(flow) / 1000.0
        self.myCurve[0].setData(
            x=self.xAxis[:self.i + 1],
            y=self.data1[:self.i + 1, 0],
            clear=True
        )
        self.myCurve[1].setData(
            x=self.xAxis[:self.i + 1],
            y=self.data1[:self.i + 1, 1],
            clear=True
        )
        QtGui.QApplication.processEvents()
        self.pointer += 1
        if self.pointer >= self.chunkSize:
            self.firstCycle = 0

    def kill_recruit_timmer(self):
        if not self._recruit_timmer:
            return
        self._recruit_timmer.stop()
        self._recruit_timmer.deleteLater()
        self._recruit_timmer = None

    def start_recruit_timmer(self):
        self._recruit_timmer = QtCore.QTimer()
        self._recruit_timmer.timeout.connect(self.recruit_off)
        self._recruit_timmer.setSingleShot(True)
        self._recruit_timmer.start(40000)

    def recruit_on(self):
        self.kill_recruit_timmer()
        self.serial_send('RECRUIT 1')
        self._recruit = True
        self.buttonRecruit.setStyleSheet(self._recruit_on_stylesheet)
        self.buttonRecruit.setText(self._recruit_on_text)
        self.start_recruit_timmer()

    def recruit_off(self):
        self.kill_recruit_timmer()
        self.serial_send('RECRUIT 0')
        self._recruit = False
        self.buttonRecruit.setStyleSheet(self._recruit_off_stylesheet)
        self.buttonRecruit.setText(self._recruit_off_text)

    def buttonUpPipClicked(self):
        if self._config_pip <= 79:
            self._config_pip += 1
        self.update()
        self.serial_send('CONFIG PIP %s' % self._config_pip)

    def buttonDownPipClicked(self):
        if self._config_pip >= 1:
            self._config_pip -= 1
        self.update()
        self.serial_send('CONFIG PIP %s' % self._config_pip)

    def buttonUpPeepClicked(self):
        if self._config_peep < self._config_pip:
            self._config_peep += 1
        self.update()
        self.serial_send('CONFIG PEEP %s' % self._config_peep)

    def buttonDownPeepClicked(self):
        if self._config_peep > 0:
            self._config_peep -= 1
        self.update()
        self.serial_send('CONFIG PEEP %s' % self._config_peep)

    def buttonUpFRClicked(self):
        if self._config_fr < 30:
            self._config_fr += 1
        self.update()
        self.serial_send('CONFIG BPM %s' % self._config_fr)

    def buttonDownFRClicked(self):
        if self._config_fr > 3:
            self._config_fr -= 1
        self.update()
        self.serial_send('CONFIG BPM %s' % self._config_fr)

    def buttonRecruitClicked(self):
        if self._recruit:
            self.recruit_off()
        else:
            self.recruit_on()

    def buttonConfigModeClicked(self):
        if self.buttonConfigMode.isChecked():
            self.stackedWidget.setCurrentIndex(1)
            self.buttonConfigMode.setStyleSheet("background-color: #18a3ac")
        else:
            self.stackedWidget.setCurrentIndex(0)
            self.buttonConfigMode.setStyleSheet("background-color: #506380")


def app():
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())
app()