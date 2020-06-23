from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

MODO = "Volumen"
RATE = 1
FRECUENCIA = 10
VOL_T = 250
PMAX = 5
PEEP = 0

class Ui_ventConfWindow(object):
    def setupUi(self, ConfigWindow):
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)

        ConfigWindow.setObjectName("ConfigWindow")
        ConfigWindow.resize(800, 450)
        ConfigWindow.setMinimumSize(QtCore.QSize(800, 450))
        ConfigWindow.setMaximumSize(QtCore.QSize(800, 450))

        self.centralwidget = QtWidgets.QWidget(ConfigWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(90, 10, 111, 321))

        #Layout 1
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")

        #Label Modo
        self.ModoLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.ModoLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.ModoLabel.setText("        "+ MODO)
        self.ModoLabel.setObjectName("ModoLabel")
        self.verticalLayout.addWidget(self.ModoLabel)

        #Label Frecuencia
        self.FrecuenciaLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.FrecuenciaLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.FrecuenciaLabel.setText("    "+ str(FRECUENCIA) + " resp/min")
        self.FrecuenciaLabel.setObjectName("FrecuenciaLabel")
        self.verticalLayout.addWidget(self.FrecuenciaLabel)

        #Label P Max
        self.PMaxLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.PMaxLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.PMaxLabel.setText("      "+ str(PMAX) + " cm H2O")
        self.PMaxLabel.setObjectName("PMaxLabel")
        self.verticalLayout.addWidget(self.PMaxLabel)

        #modo anterior boton
        self.antModoButton = QtWidgets.QPushButton(self.centralwidget)
        self.antModoButton.setGeometry(QtCore.QRect(0, 30, 80, 70))
        self.antModoButton.setFont(font)
        self.antModoButton.setObjectName("antModoButton")

        # modo siguiente boton
        self.sigModoButton = QtWidgets.QPushButton(self.centralwidget)
        self.sigModoButton.setGeometry(QtCore.QRect(210, 30, 80, 70))
        self.sigModoButton.setFont(font)
        self.sigModoButton.setObjectName("sigModoButton")

        # - FR boton
        self.menosFRButton = QtWidgets.QPushButton(self.centralwidget)
        self.menosFRButton.setGeometry(QtCore.QRect(0, 140, 80, 70))
        self.menosFRButton.setFont(font)
        self.menosFRButton.setObjectName("menosFRButton")
        self.menosFRButton.clicked.connect(lambda: disminuir(FRECUENCIA,"FRECUENCIA"))  # accion al tocar el boton

        # + FR boton
        self.masFRButton = QtWidgets.QPushButton(self.centralwidget)
        self.masFRButton.setGeometry(QtCore.QRect(210, 140, 80, 70))
        self.masFRButton.setFont(font)
        self.masFRButton.setObjectName("masFRButton")
        self.masFRButton.clicked.connect(lambda: aumentar(FRECUENCIA,"FRECUENCIA")) #accion al tocar el boton

        # - PMax boton
        self.menosPMaxButton = QtWidgets.QPushButton(self.centralwidget)
        self.menosPMaxButton.setGeometry(QtCore.QRect(0, 250, 80, 70))
        self.menosPMaxButton.setFont(font)
        self.menosPMaxButton.setObjectName("menosPMaxButton")
        self.menosPMaxButton.clicked.connect(lambda: disminuir(PMAX,"PMAX"))  # accion al tocar el boton

        # + PMax boton
        self.masPMaxButton = QtWidgets.QPushButton(self.centralwidget)
        self.masPMaxButton.setGeometry(QtCore.QRect(210, 250, 80, 70))
        self.masPMaxButton.setFont(font)
        self.masPMaxButton.setObjectName("masPMaxButton")
        self.masPMaxButton.clicked.connect(lambda: aumentar(PMAX, "PMAX"))  # accion al tocar el boton


        #layout 2
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(590, 10, 121, 321))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        # Label Rate
        self.RateLabel = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.RateLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.RateLabel.setText("           1:"+ str(RATE))
        self.RateLabel.setObjectName("RateLabel")
        self.verticalLayout_2.addWidget(self.RateLabel)

        # Label Vol Tidal
        self.VolTLabel = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.VolTLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.VolTLabel.setText("        "+ str(VOL_T)+" mL")
        self.VolTLabel.setObjectName("VolTLabel")
        self.verticalLayout_2.addWidget(self.VolTLabel)

        #Label PEEP
        self.PEEPLabel = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.PEEPLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.PEEPLabel.setText("      "+ str(PEEP) + " cm H2O")
        self.PEEPLabel.setObjectName("PEEPLabel")
        self.verticalLayout_2.addWidget(self.PEEPLabel)

        # - Rate boton
        self.menosRateButton = QtWidgets.QPushButton(self.centralwidget)
        self.menosRateButton.setGeometry(QtCore.QRect(500, 30, 80, 70))
        self.menosRateButton.setFont(font)
        self.menosRateButton.setObjectName("menosRateButton")
        self.menosRateButton.clicked.connect(lambda: disminuir(RATE, "RATE"))  # accion al tocar el boton

        # + Rate boton
        self.masRateButton = QtWidgets.QPushButton(self.centralwidget)
        self.masRateButton.setGeometry(QtCore.QRect(720, 30, 80, 70))
        self.masRateButton.setFont(font)
        self.masRateButton.setObjectName("masRateButton")
        self.masRateButton.clicked.connect(lambda: aumentar(RATE, "RATE"))  # accion al tocar el boton

        # - Vol Tidal Boton
        self.menosVolTButton = QtWidgets.QPushButton(self.centralwidget)
        self.menosVolTButton.setGeometry(QtCore.QRect(500, 140, 80, 70))
        self.menosVolTButton.setFont(font)
        self.menosVolTButton.setObjectName("menosVolTButton")
        self.menosVolTButton.clicked.connect(lambda: disminuir(VOL_T, "VOL_T"))  # accion al tocar el boton

        # + Vol Tidal boton
        self.masVolTButton = QtWidgets.QPushButton(self.centralwidget)
        self.masVolTButton.setGeometry(QtCore.QRect(720, 140, 80, 70))
        self.masVolTButton.setFont(font)
        self.masVolTButton.setObjectName("masVolTButton")
        self.masVolTButton.clicked.connect(lambda: aumentar(VOL_T, "VOL_T"))  # accion al tocar el boton

        # - PEEP boton
        self.menosPEEPButton = QtWidgets.QPushButton(self.centralwidget)
        self.menosPEEPButton.setGeometry(QtCore.QRect(500, 250, 80, 70))
        self.menosPEEPButton.setFont(font)
        self.menosPEEPButton.setObjectName("menosPEEPButton")
        self.menosPEEPButton.clicked.connect(lambda: disminuir(PEEP, "PEEP"))  # accion al tocar el boton

        # + PEEP boton
        self.masPEEPButton = QtWidgets.QPushButton(self.centralwidget)
        self.masPEEPButton.setGeometry(QtCore.QRect(720, 250, 80, 70))
        self.masPEEPButton.setFont(font)
        self.masPEEPButton.setObjectName("masPEEPButton")
        self.masPEEPButton.clicked.connect(lambda: aumentar(PEEP, "PEEP"))  # accion al tocar el boton

        # Label titulo modo y rate
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(310, 30, 171, 70))

        #Cambio fuente para labels
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setWeight(75)

        # Label Modo y Rate
        self.label.setFont(font)
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setObjectName("label")

        # Label titulo Frecuencia y Vol T
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(310, 140, 171, 70))
        self.label_2.setFont(font)
        self.label_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_2.setObjectName("label_2")

        # Label titulo P.Max y PEEP
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(310, 250, 171, 70))
        self.label_3.setFont(font)
        self.label_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_3.setObjectName("label_3")

        # Aplicar cambios boton
        self.aplicaCambiosButton = QtWidgets.QPushButton(self.centralwidget)
        self.aplicaCambiosButton.setGeometry(QtCore.QRect(270, 330, 111, 61))
        self.aplicaCambiosButton.setObjectName("aplicaCambiosButton")
        self.aplicaCambiosButton.clicked.connect(mostrarAdvertencia)

        # Cerrar boton
        self.cerrarButton = QtWidgets.QPushButton(self.centralwidget)
        self.cerrarButton.setGeometry(QtCore.QRect(400, 330, 111, 61))
        self.cerrarButton.setObjectName("cerrarButton")
        self.cerrarButton.clicked.connect(lambda: cerrar(ConfigWindow))#accion para cerrar la ventana

        ConfigWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ConfigWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        ConfigWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ConfigWindow)
        self.statusbar.setObjectName("statusbar")
        ConfigWindow.setStatusBar(self.statusbar)
        self.retranslateUi(ConfigWindow)
        QtCore.QMetaObject.connectSlotsByName(ConfigWindow)


    def retranslateUi(self, ConfigWindow):
        _translate = QtCore.QCoreApplication.translate
        ConfigWindow.setWindowTitle(_translate("ConfigWindow", "ConfigWindow"))
        self.antModoButton.setText(_translate("ConfigWindow", "<"))
        self.menosFRButton.setText(_translate("ConfigWindow", "-"))
        self.menosPMaxButton.setText(_translate("ConfigWindow", "-"))
        self.sigModoButton.setText(_translate("ConfigWindow", ">"))
        self.masFRButton.setText(_translate("ConfigWindow", "+"))
        self.masPMaxButton.setText(_translate("ConfigWindow", "+"))
        self.menosRateButton.setText(_translate("ConfigWindow", "-"))
        self.masPEEPButton.setText(_translate("ConfigWindow", "+"))
        self.menosVolTButton.setText(_translate("ConfigWindow", "-"))
        self.menosPEEPButton.setText(_translate("ConfigWindow", "-"))
        self.masRateButton.setText(_translate("ConfigWindow", "+"))
        self.masVolTButton.setText(_translate("ConfigWindow", "+"))
        self.aplicaCambiosButton.setText(_translate("ConfigWindow", "Aplicar Cambios"))
        self.cerrarButton.setText(_translate("ConfigWindow", "Cerrar"))
        self.label.setText(_translate("ConfigWindow", "Modo                        Rate"))
        self.label_2.setText(_translate("ConfigWindow", "Frecuencia             Vol T"))
        self.label_3.setText(_translate("ConfigWindow", "P Max                      PEEP"))

# funcion para aumentar la variable deseada
# num: numero inicial de la variable
# variable: indica que variable global se desea modificar
def aumentar(num, variable):
    global FRECUENCIA, RATE, VOL_T, PEEP, PMAX

    if (variable == "FRECUENCIA"):
        if (num >= 10 and num < 30):
            FRECUENCIA = num + 1
            ui.FrecuenciaLabel.setText("    " + str(FRECUENCIA) + " resp/min")

    elif (variable == "RATE"):
        if (num >= 1 and num < 5):
            RATE = num + 1
            ui.RateLabel.setText("           1:" + str(RATE))

    elif (variable == "VOL_T"):
        if (num >= 250 and num < 800):
            VOL_T = num + 50
            ui.VolTLabel.setText("        " + str(VOL_T) + " mL")

    elif (variable == "PEEP"):
        if (num >= 0 and num < 25):
            PEEP = num + 1
            ui.PEEPLabel.setText("      " + str(PEEP) + " cm H2O")

    elif (variable == "PMAX"):
        if (num >= 5 and num < 40):
            PMAX = num + 1
            ui.PMaxLabel.setText("      " + str(PMAX) + " cm H2O")

# funcion para disminuir la variable deseada
# num: numero inicial de la variable
# variable: indica que variable global se desea modificar
def disminuir(num, variable):
    global FRECUENCIA, RATE, VOL_T, PEEP, PMAX

    if (variable == "FRECUENCIA"):
        if (num > 10 and num <= 30):
            FRECUENCIA = num - 1
            ui.FrecuenciaLabel.setText("    " + str(FRECUENCIA) + " resp/min")

    elif (variable == "RATE"):
        if (num > 1 and num <= 5):
            RATE = num - 1
            ui.RateLabel.setText("           1:" + str(RATE))

    elif (variable == "VOL_T"):
        if (num > 250 and num <= 800):
            VOL_T = num - 50
            ui.VolTLabel.setText("        " + str(VOL_T) + " mL")

    elif (variable == "PEEP"):
        if (num > 0 and num <= 25):
            PEEP = num - 1
            ui.PEEPLabel.setText("      " + str(PEEP) + " cm H2O")

    elif (variable == "PMAX"):
        if (num > 5 and num <= 40):
            PMAX = num - 1
            ui.PMaxLabel.setText("      " + str(PMAX) + " cm H2O")

# Cerrar la ventana de configuracion
def cerrar(ConfigWindow):
    ConfigWindow.close()

#Mensaje de advertencia para
def mostrarAdvertencia():
    msg = QMessageBox()
    msg.setWindowTitle("Advertencia")
    msg.setText("Esta seguro(a) que aplicar estos cambios?")
    msg.setIcon(QMessageBox.Warning)
    msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    msg.setDefaultButton(QMessageBox.Cancel)
    msg.buttonClicked.connect(clickAdvertencia)
    x = msg.exec_()


def clickAdvertencia(i):
    if i.text() == "OK":
        print("Cambios aplicados")
        print("Frecuencia: " + str(FRECUENCIA))
        print("P Max: " + str(PMAX))
        print("PEEP: " + str(PEEP))
        print("Vol Tidal: " + str(VOL_T))
        print("RATE: 1:" + str(RATE))

    elif i.text() == "Cancel":
        print("Los cambios no fueron aplicados")


if __name__== "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ConfigWindow = QtWidgets.QMainWindow()
    ui = Ui_ventConfWindow()
    ui.setupUi(ConfigWindow)
    ConfigWindow.show()
    sys.exit(app.exec_())