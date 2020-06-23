from PyQt5 import QtCore, QtGui, QtWidgets
from ventConf import *


class Ui_MenuRespirador(object):
    frecuencia = 10
    def prueba(self):
        frecuencia = 10
        self.labelFR.setText("Frecuencia\nRespiratoria:\n\n       "+str(frecuencia))


    def ventanaConfiguracion(self):
        self.ventanaConfig = QtWidgets.QMainWindow()
        self.ui = Ui_ventConfWindow()
        self.ui.setupUi(self.ventanaConfig)
        self.ventanaConfig.show()

    def setupUi(self, MenuRespirador):
        #dimensiones ventana principal
        MenuRespirador.setObjectName("MenuRespirador")
        MenuRespirador.resize(800, 450)
        MenuRespirador.setMinimumSize(QtCore.QSize(800, 450))
        MenuRespirador.setMaximumSize(QtCore.QSize(800, 450))

        #icono
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("logo-tec.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap("logo-tec.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        MenuRespirador.setWindowIcon(icon)
        MenuRespirador.setWindowOpacity(2.0)
        MenuRespirador.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)

        self.centralwidget = QtWidgets.QWidget(MenuRespirador)
        self.centralwidget.setObjectName("centralwidget")
        self.graficasLabel = QtWidgets.QLabel(self.centralwidget)
        self.graficasLabel.setGeometry(QtCore.QRect(10, 0, 551, 391))
        self.graficasLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.graficasLabel.setText("")
        self.graficasLabel.setObjectName("graficasLabel")

        #boton configuracion
        self.ConfigButton = QtWidgets.QPushButton(self.centralwidget)
        self.ConfigButton.setGeometry(QtCore.QRect(570, 320, 101, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.ConfigButton.setFont(font)
        self.ConfigButton.setObjectName("ConfigButton")
        self.ConfigButton.clicked.connect(self.ventanaConfiguracion) #Abre la ventana de configuracion al hacer click

        #boton Encendido/Apagado
        self.OnOffButton = QtWidgets.QPushButton(self.centralwidget)
        self.OnOffButton.setGeometry(QtCore.QRect(690, 320, 101, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.OnOffButton.setFont(font)
        self.OnOffButton.setObjectName("OnOffButton")
        self.OnOffButton.clicked.connect(self.prueba)

        #layout de labels
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(570, 10, 221, 291))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        #label Modo
        self.labelModo = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.labelModo.setFont(font)
        self.labelModo.setAutoFillBackground(True)
        self.labelModo.setFrameShape(QtWidgets.QFrame.Panel)
        self.labelModo.setObjectName("labelModo")
        self.gridLayout.addWidget(self.labelModo, 0, 0, 1, 1)

        #label Frecuencia respiratoria
        self.labelFR = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.labelFR.setFont(font)
        self.labelFR.setAutoFillBackground(True)
        self.labelFR.setFrameShape(QtWidgets.QFrame.Panel)
        self.labelFR.setObjectName("labelFR")
        self.gridLayout.addWidget(self.labelFR, 1, 0, 1, 1)

        #label Volumen Tidal
        self.labelVolT = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.labelVolT.setFont(font)
        self.labelVolT.setAutoFillBackground(True)
        self.labelVolT.setFrameShape(QtWidgets.QFrame.Panel)
        self.labelVolT.setObjectName("labelVolT")
        self.gridLayout.addWidget(self.labelVolT, 1, 1, 1, 1)

        #label Rate Inspiracion : Espiracion
        self.labelRate = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.labelRate.setFont(font)
        self.labelRate.setAutoFillBackground(True)
        self.labelRate.setFrameShape(QtWidgets.QFrame.Panel)
        self.labelRate.setObjectName("labelRate")
        self.gridLayout.addWidget(self.labelRate, 0, 1, 1, 1)

        #label Presion Maxima
        self.labelPMax = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.labelPMax.setFont(font)
        self.labelPMax.setAutoFillBackground(True)
        self.labelPMax.setFrameShape(QtWidgets.QFrame.Panel)
        self.labelPMax.setObjectName("labelPMax")
        self.gridLayout.addWidget(self.labelPMax, 2, 0, 1, 1)

        #label PEEP
        self.labelPEEP = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.labelPEEP.setFont(font)
        self.labelPEEP.setAutoFillBackground(True)
        self.labelPEEP.setFrameShape(QtWidgets.QFrame.Panel)
        self.labelPEEP.setObjectName("labelPEEP")
        self.gridLayout.addWidget(self.labelPEEP, 2, 1, 1, 1)

        MenuRespirador.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MenuRespirador)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MenuRespirador.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MenuRespirador)
        self.statusbar.setObjectName("statusbar")
        MenuRespirador.setStatusBar(self.statusbar)

        self.retranslateUi(MenuRespirador)
        QtCore.QMetaObject.connectSlotsByName(MenuRespirador)

    def retranslateUi(self, MenuRespirador):
        _translate = QtCore.QCoreApplication.translate
        MenuRespirador.setWindowTitle(_translate("MenuRespirador", "Control Respirador"))
        self.ConfigButton.setText(_translate("MenuRespirador", "Configuracion"))
        self.OnOffButton.setText(_translate("MenuRespirador", "On/Off"))
        self.labelModo.setText(_translate("MenuRespirador", "Modo:\n"""))
        self.labelFR.setText(_translate("MenuRespirador", "Frecuencia\nRespiratoria:\n"))
        self.labelVolT.setText(_translate("MenuRespirador", "Volumen\n""Tidal:\n"))
        self.labelRate.setText(_translate("MenuRespirador", "Rate:\n"))
        self.labelPMax.setText(_translate("MenuRespirador", "Presion\nMaxima:\n"))
        self.labelPEEP.setText(_translate("MenuRespirador", "PEEP:\n"))


if __name__== "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MenuRespirador()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())