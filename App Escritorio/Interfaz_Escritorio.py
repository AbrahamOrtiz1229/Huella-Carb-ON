# -*- coding: utf-8 -*-
# Created by: PyQt5 UI code generator 5.15.9
""" 
    Última modificacion 21/06/22
    Porgrama que de interfaz gráfica para escritorio que accede
    a la base de datos y refleja datos como el consumo eleéctrico,
    factor de emisión de carbono, huella de carbono y su promedio
    
    Realizado por Alan Iván Flores Juárez, Ulises Hernández Hernández, 
    Abraham Ortiz Castro y Jesús Alejandro Gómez Bautista

"""

#Librería de interfaz gráfica
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
#Libreria para la Firebase
import pyrebase
#Librería consumo energético
import psutil
import wmi
#Librería de tiempo
import time

#Configuracion de la base de datos Firebase sobre la que trabajamos
config = {
  "apiKey": "AIzaSyBbuUlvoFJ3S6HQrB7NT3GtvKE4IRBcdkw",
  "authDomain": "carbon-footprint-856d0.firebaseapp.com",
  "databaseURL": "https://carbon-footprint-856d0-default-rtdb.firebaseio.com",
  "projectId": "carbon-footprint-856d0",
  "storageBucket": "carbon-footprint-856d0.appspot.com",
  "messagingSenderId": "558213562155",
  "appId": "1:558213562155:web:05da045a6cd89d78d14f6e",
  "measurementId": "G-0GHHHQ93Y4"
  
}
#Inicializacion de firebase
firebase = pyrebase.initialize_app(config)
#Acceso a la firebase
db = firebase.database()

class Ui_MainWindow(object):
    #Creacion de los elementos de la interfaz
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(636, 436)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(200, 20, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setObjectName("title")
        self.lineEdit_1 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_1.setGeometry(QtCore.QRect(20, 140, 211, 41))
        self.lineEdit_1.setObjectName("lineEdit_1")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(200, 70, 47, 13))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(20, 120, 211, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_1.setFont(font)
        self.label_1.setObjectName("label_1")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(390, 140, 211, 41))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(390, 120, 211, 16))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.label_3.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 240, 631, 161))
        self.label.setText("")
        #Ruta de acceso de las imagenes utilizadas
        #Reemplazar para un correcto funcionamiento
        self.label.setPixmap(QtGui.QPixmap(r"C:\Users\...\Hackaton\Diseño_1.jpg")) 
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(430, -20, 211, 111))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(r"C:\Users\...\Hackaton\Imagen_2.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, -30, 161, 141))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap(r"C:\Users\...\Hackaton\ICON_PC.png"))
        
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 190, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(390, 190, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(20, 210, 211, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(390, 210, 211, 31))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(230, 260, 161, 41))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(270, 220, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.label.raise_()
        self.title.raise_()
        self.lineEdit_1.raise_()
        self.label_2.raise_()
        self.label_1.raise_()
        self.lineEdit_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.lineEdit_3.raise_()
        self.lineEdit_4.raise_()
        self.lineEdit_5.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 636, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    #Funcion que establece el texto en la interfaz
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.title.setText(_translate("MainWindow", "PC Carbon Footprint"))
        self.label_1.setText(_translate("MainWindow", "Factor de emisión de Carbono"))
        self.label_3.setText(_translate("MainWindow", "Consumo de Energía"))
        self.label_6.setText(_translate("MainWindow", "Huella de carbono"))
        self.label_7.setText(_translate("MainWindow", "Promedio Total HC"))
        self.pushButton.setText(_translate("MainWindow", "Actualizar"))
        #Obtienen datos de la base de datos y se escriben donde corresponda
        consumo = str(db.child("T-Systems").child("W_Laptop").get().val())
        self.lineEdit_2.setText(str(consumo)+" W")
        emision= str(db.child("T-Systems").child("FactorEmision").get().val())
        self.lineEdit_1.setText(str(emision))
        huella = str(db.child("T-Systems").child("H_Laptop").get().val())
        self.lineEdit_3.setText(str(huella)+" gr CO2")
        huella_prom= str(db.child("T-Systems").child("PromedioHC").get().val())
        self.lineEdit_4.setText(str(huella_prom)+" gr C02")
        #Lógica de la cantidad de consumo
        self.pushButton.clicked.connect(self.actualizar)
        if(float(consumo) > 60):
            self.lineEdit_5.setText("Consumo elevado :C")
        elif(0<=float(consumo)<=60):
            self.lineEdit_5.setText("Consumo adecuado :D")
        else:
            self.lineEdit_5.setText("...")
    #Funcion que actualiza los elementos de la interfaz en base a nuevos datos en Firebase
    def actualizar(self):
        consumo = str(db.child("T-Systems").child("W_Laptop").get().val())
        self.lineEdit_2.setText(str(consumo)+" W")
        emision= str(db.child("T-Systems").child("FactorEmision").get().val())
        self.lineEdit_1.setText(str(emision))
        huella = str(db.child("T-Systems").child("H_Laptop").get().val())
        self.lineEdit_3.setText(str(huella)+" gr CO2")
        huella_prom= str(db.child("T-Systems").child("PromedioHC").get().val())
        self.lineEdit_4.setText(str(huella_prom)+" gr C02")
        #Lógica de la cantidad de consumo
        if(float(consumo) > 60):
            self.lineEdit_5.setText("Consumo elevado :C")
        elif(0<=float(consumo)<=60):
            self.lineEdit_5.setText("Consumo adecuado :D")
        else:
            self.lineEdit_5.setText("...")
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
