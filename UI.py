# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import subprocess

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, -90, 631, 331))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.horizontal.setGeometry(QtCore.QRect(60, 260, 171, 91))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Medium")
        font.setPointSize(14)
        self.horizontal.setFont(font)
        self.horizontal.setObjectName("horizontal")
        self.Projectile = QtWidgets.QPushButton(self.centralwidget)
        self.Projectile.setGeometry(QtCore.QRect(270, 260, 221, 91))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Medium")
        font.setPointSize(14)
        self.Projectile.setFont(font)
        self.Projectile.setObjectName("Projectile")
        self.rotation = QtWidgets.QPushButton(self.centralwidget)
        self.rotation.setGeometry(QtCore.QRect(510, 260, 211, 91))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Medium")
        font.setPointSize(14)
        self.rotation.setFont(font)
        self.rotation.setObjectName("rotation")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)



        self.horizontal.clicked.connect(self.hori)

        self.rotation.clicked.connect(self.rot)



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Mecanical Simulation"))
        self.horizontal.setText(_translate("MainWindow", "Horizontal plane"))
        self.Projectile.setText(_translate("MainWindow", "Projectile(not available)"))
        self.rotation.setText(_translate("MainWindow", "Rotation"))

    def hori(self):
        new_gui = subprocess.Popen(["python",'horizontalui.py'])

    def rot(self):
    	new_gui = subprocess.Popen(["python",'rotationui.py'])



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

