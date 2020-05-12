# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interfazControlador.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class Ui_MenuRespirador(object):
    def setupUi(self, MenuRespirador):
        MenuRespirador.setObjectName("MenuRespirador")
        MenuRespirador.resize(800, 480)
        MenuRespirador.setMinimumSize(QtCore.QSize(800, 400))
        MenuRespirador.setMaximumSize(QtCore.QSize(800, 402))

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("logo-tec.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap("logo-tec.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        MenuRespirador.setWindowIcon(icon)
        MenuRespirador.setWindowOpacity(2.0)
        MenuRespirador.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)

        self.centralwidget = QtWidgets.QWidget(MenuRespirador)
        self.centralwidget.setObjectName("centralwidget")

        self.graficasLabel = QtWidgets.QLabel(self.centralwidget)
        self.graficasLabel.setGeometry(QtCore.QRect(10, 0, 781, 221))
        self.graficasLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.graficasLabel.setText("")
        self.graficasLabel.setObjectName("graficasLabel")

        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(90, 250, 595, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        #Boton de modo
        self.ModoButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ModoButton.sizePolicy().hasHeightForWidth())
        self.ModoButton.setSizePolicy(sizePolicy)
        self.ModoButton.setObjectName("ModoButton")
        self.horizontalLayout.addWidget(self.ModoButton)
        self.ModoButton.clicked.connect(clickModo) #accion al hacer click

        #Boton de Frecuencia Respiratoria
        self.FRButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.FRButton.sizePolicy().hasHeightForWidth())
        self.FRButton.setSizePolicy(sizePolicy)
        self.FRButton.setObjectName("FRButton")
        self.horizontalLayout.addWidget(self.FRButton)
        self.FRButton.clicked.connect(clickFR)  # accion al hacer click

        #Boton de Volumen Tidal
        self.VolTButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.VolTButton.sizePolicy().hasHeightForWidth())
        self.VolTButton.setSizePolicy(sizePolicy)
        self.VolTButton.setObjectName("VolTButton")
        self.horizontalLayout.addWidget(self.VolTButton)
        self.VolTButton.clicked.connect(clickVT)  # accion al hacer click

        #Boton de rate (inspiracion:Espiracion)
        self.rateButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rateButton.sizePolicy().hasHeightForWidth())
        self.rateButton.setSizePolicy(sizePolicy)
        self.rateButton.setObjectName("rateButton")
        self.horizontalLayout.addWidget(self.rateButton)
        self.rateButton.clicked.connect(mostrarAdvertencia)  # accion al hacer click

        #Boton PEEP
        self.PEEPButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PEEPButton.sizePolicy().hasHeightForWidth())
        self.PEEPButton.setSizePolicy(sizePolicy)
        self.PEEPButton.setObjectName("PEEPButton")
        self.horizontalLayout.addWidget(self.PEEPButton)
        self.PEEPButton.clicked.connect(clickPEEP)  # accion al hacer click

        #Boton PMax
        self.PmaxButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PmaxButton.sizePolicy().hasHeightForWidth())
        self.PmaxButton.setSizePolicy(sizePolicy)
        self.PmaxButton.setObjectName("PmaxButton")
        self.horizontalLayout.addWidget(self.PmaxButton)
        self.PmaxButton.clicked.connect(clickPMax)  # accion al hacer click

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
        self.ModoButton.setText(_translate("MenuRespirador", "Modo"))
        self.FRButton.setText(_translate("MenuRespirador", "FR"))
        self.VolTButton.setText(_translate("MenuRespirador", "Volumen Tidal"))
        self.rateButton.setText(_translate("MenuRespirador", "I:E"))
        self.PEEPButton.setText(_translate("MenuRespirador", "PEEP"))
        self.PmaxButton.setText(_translate("MenuRespirador", "Pmax"))

def mostrarAdvertencia():
    msg = QMessageBox()
    msg.setWindowTitle("Advertencia")
    msg.setText("Esta seguro(a) que desea cambiar el rate?")
    msg.setIcon(QMessageBox.Warning)
    msg.setStandardButtons(QMessageBox.Ok|QMessageBox.Cancel)
    msg.setDefaultButton(QMessageBox.Cancel)
    msg.buttonClicked.connect(clickAdvertencia)
    x = msg.exec_()

def clickAdvertencia(i):
    if i.text() == "OK":
        print("El rate fue cambiado")
    elif i.text() == "Cancel":
        print("Se cancelo el cambio de rate")

def clickModo():
    print("Click en modo")

def clickFR():
    print("Click FR")

def clickVT():
    print("Click Volumen tidal")

def clickRate():
    print("Click Rate")

def clickPEEP():
    print("Click PEEP")

def clickPMax():
    print("Click PMax")

if __name__== "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MenuRespirador()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())