# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MS.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setWindowTitle("")
        MainWindow.setAutoFillBackground(False)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Title = QtWidgets.QLabel(self.centralwidget)
        self.Title.setGeometry(QtCore.QRect(150, -20, 591, 221))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight SemiConde")
        font.setPointSize(28)
        self.echelle = QtWidgets.QLabel(self.centralwidget)
        self.echelle.setGeometry(QtCore.QRect(270, 400, 591, 221))
        self.echelle.setFont(font)
        self.echelle.setObjectName("echelle")

        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight SemiConde")
        font.setPointSize(48)

        self.Title.setFont(font)
        self.Title.setObjectName("Title")
        self.MASS = QtWidgets.QLabel(self.centralwidget)
        self.MASS.setGeometry(QtCore.QRect(30, 140, 191, 121))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI Semilight")
        font.setPointSize(48)
        self.MASS.setFont(font)
        self.MASS.setObjectName("MASS")
        self.mass = QtWidgets.QLineEdit(self.centralwidget)
        self.mass.setGeometry(QtCore.QRect(190, 190, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.mass.setFont(font)
        self.mass.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
        self.mass.setText("1")
        self.mass.setObjectName("mass")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(250, 180, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.V0 = QtWidgets.QLabel(self.centralwidget)
        self.V0.setGeometry(QtCore.QRect(30, 240, 161, 81))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI Semilight")
        font.setPointSize(48)
        self.V0.setFont(font)
        self.V0.setObjectName("V0")
        self.v0 = QtWidgets.QLineEdit(self.centralwidget)
        self.v0.setGeometry(QtCore.QRect(130, 270, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.v0.setFont(font)
        self.v0.setObjectName("v0")
        self.v0.setText("0")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(190, 260, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.FORCE1 = QtWidgets.QLabel(self.centralwidget)
        self.FORCE1.setGeometry(QtCore.QRect(370, 140, 191, 121))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI Semilight")
        font.setPointSize(48)
        self.FORCE1.setFont(font)
        self.FORCE1.setObjectName("FORCE1")
        self.force1 = QtWidgets.QLineEdit(self.centralwidget)
        self.force1.setGeometry(QtCore.QRect(560, 190, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.force1.setFont(font)
        self.force1.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
        self.force1.setText("0")
        self.force1.setObjectName("force1")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(640, 180, 41, 51))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.FORCE2 = QtWidgets.QLabel(self.centralwidget)
        self.FORCE2.setGeometry(QtCore.QRect(360, 210, 211, 121))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI Semilight")
        font.setPointSize(36)
        self.invalid = QtWidgets.QLabel(self.centralwidget)
        self.invalid.setGeometry(QtCore.QRect(240, 240, 400, 200))
        self.invalid.setStyleSheet("color:red;")
        self.invalid.setFont(font)
        self.invalid.setObjectName("FORCE2")

        font = QtGui.QFont()
        font.setFamily("Leelawadee UI Semilight")
        font.setPointSize(48)
        self.FORCE2.setFont(font)
        self.FORCE2.setObjectName("FORCE2")
        self.force2 = QtWidgets.QLineEdit(self.centralwidget)
        self.force2.setGeometry(QtCore.QRect(560, 260, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.force2.setFont(font)
        self.force2.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
        self.force2.setText("0")
        self.force2.setObjectName("force2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(640, 250, 41, 51))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.run = QtWidgets.QPushButton(self.centralwidget)
        self.run.setGeometry(QtCore.QRect(230, 390, 271, 91))

        self.run.clicked.connect(self.clicked)

        font = QtGui.QFont()
        font.setPointSize(48)
        self.run.setFont(font)
        self.run.setObjectName("run")
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



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.Title.setText(_translate("MainWindow", "horizontal simulation"))
        self.MASS.setText(_translate("MainWindow", "Mass:"))
        self.invalid.setText(_translate("MainWindow", ""))
        self.label.setText(_translate("MainWindow", "KG"))
        self.V0.setText(_translate("MainWindow", "V0:"))
        self.label_2.setText(_translate("MainWindow", "M/S"))
        self.FORCE1.setText(_translate("MainWindow", "Force1:"))
        self.label_3.setText(_translate("MainWindow", "N"))
        self.FORCE2.setText(_translate("MainWindow", "Force2:"))
        self.label_4.setText(_translate("MainWindow", "N"))
        self.run.setText(_translate("MainWindow", "Simulate"))
        self.echelle.setText(_translate("MainWindow", "1m = 4pixels"))



    def clicked(self):


        import horizontalsim
        try:
            m = float(self.mass.text())
            v0 = float(self.v0.text())
            f1 = float(self.force1.text())
            f2 = float(self.force2.text())
            f = f1 + f2
            self.invalid.setText("")
            main.play(f,m,v0)
            
        except:
            self.invalid.setText("Invalid input")


            

        

        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

