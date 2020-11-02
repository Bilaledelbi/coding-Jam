# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rotationyi.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.run = QtWidgets.QPushButton(self.centralwidget)
        self.run.setGeometry(QtCore.QRect(290, 380, 271, 111))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(28)
        self.run.setFont(font)
        self.run.setObjectName("run")

        self.run.clicked.connect(self.clicked)
        
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(270, 20, 241, 101))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.title.setFont(font)
        self.title.setObjectName("title")
        self.teta0 = QtWidgets.QLabel(self.centralwidget)
        self.teta0.setGeometry(QtCore.QRect(250, 130, 91, 71))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(36)
        self.teta0.setFont(font)
        self.teta0.setObjectName("teta0")
        self.av0 = QtWidgets.QLineEdit(self.centralwidget)
        self.av0.setGeometry(QtCore.QRect(350, 150, 81, 51))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(36)
        self.av0.setFont(font)
        self.av0.setText("0")
        self.av0.setObjectName("av0")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(440, 140, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(36)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.force1 = QtWidgets.QLabel(self.centralwidget)
        self.force1.setGeometry(QtCore.QRect(40, 220, 171, 81))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(36)
        self.force1.setFont(font)
        self.force1.setObjectName("force1")
        self.f1 = QtWidgets.QLineEdit(self.centralwidget)
        self.f1.setGeometry(QtCore.QRect(190, 250, 71, 41))
        self.f1.setText("0")
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(20)
        self.f1.setFont(font)
        self.f1.setObjectName("f1")
        self.force2 = QtWidgets.QLabel(self.centralwidget)
        self.force2.setGeometry(QtCore.QRect(510, 230, 171, 81))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(36)
        self.force2.setFont(font)
        self.force2.setObjectName("force2")
        self.f2 = QtWidgets.QLineEdit(self.centralwidget)
        self.f2.setGeometry(QtCore.QRect(660, 250, 71, 41))
        self.f2.setText("0")
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(20)
        self.f2.setFont(font)
        self.f2.setObjectName("f2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(330, 500, 188, 39))
        self.label_2.setStyleSheet("color:red;")
        self.label_2.setObjectName("label_2")
        self.circle = QtWidgets.QRadioButton(self.centralwidget)
        self.circle.setGeometry(QtCore.QRect(350, 260, 82, 17))
        self.circle.setChecked(True)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.circle.setFont(font)
        self.circle.setObjectName("circle")
        self.rectangle = QtWidgets.QRadioButton(self.centralwidget)
        self.rectangle.setGeometry(QtCore.QRect(350, 290, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.rectangle.setFont(font)
        self.rectangle.setObjectName("rectangle")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(350, 340, 181, 20))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color:red")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.distr = QtWidgets.QLabel(self.centralwidget)
        self.distr.setGeometry(QtCore.QRect(50, 280, 171, 81))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(10)
        self.distr.setFont(font)
        self.distr.setObjectName("distr")
        self.dr1 = QtWidgets.QLineEdit(self.centralwidget)
        self.dr1.setGeometry(QtCore.QRect(180, 310, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(8)
        self.dr1.setFont(font)
        self.dr1.setText("1")
        self.dr1.setObjectName("dr1")
        self.dr2 = QtWidgets.QLineEdit(self.centralwidget)
        self.dr2.setGeometry(QtCore.QRect(670, 310, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(8)
        self.dr2.setFont(font)
        self.dr2.setText("1")
        self.dr2.setObjectName("dr2")
        self.distr2 = QtWidgets.QLabel(self.centralwidget)
        self.distr2.setGeometry(QtCore.QRect(540, 280, 121, 81))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(10)
        self.distr2.setFont(font)
        self.distr2.setObjectName("distr2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(260, 240, 81, 51))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(36)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(730, 240, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(36)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
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
        MainWindow.setWindowTitle(_translate("MainWindow", "Rotation"))
        self.run.setText(_translate("MainWindow", "Simulate"))
        self.title.setText(_translate("MainWindow", "Rotation"))
        self.teta0.setText(_translate("MainWindow", "θ`0: "))
        self.label.setText(_translate("MainWindow", "Rad/s"))
        self.force1.setText(_translate("MainWindow", "force1:"))
        self.force2.setText(_translate("MainWindow", "force2:"))
        self.label_2.setText(_translate("MainWindow", "note: the diametere is always equal 2m \n"
		"and the rectangle dimenions are \n"
		"width = 1m/height = 2m"))
        self.circle.setText(_translate("MainWindow", "circle"))
        self.rectangle.setText(_translate("MainWindow", "Rectangle"))
        self.distr.setText(_translate("MainWindow", "distance from center:"))
        self.distr2.setText(_translate("MainWindow", "distance from center:"))
        self.label_4.setText(_translate("MainWindow", "N"))
        self.label_5.setText(_translate("MainWindow", "N"))


    def clicked(self):
        import rotation
        F = []
        d = []
        fault = 0

        try:
            self.label_3.setText("")
            tetas0 = float(self.av0.text())
            fo1 = float(self.f1.text())
            fo2 = float(self.f2.text())
            dr1 = float(self.dr1.text())
            dr2 = float(self.dr2.text())
            d.append(dr1)
            d.append(dr2)
            if(dr1 > 1 or dr2 > 1 or dr1 == 0 or dr2 == 0):
                fault = ""
            int(fault)        
            F.append(fo1)
            F.append(fo2)
            if(self.circle.isChecked()):
                i = (3.4 * (1)/4)
                fault = 0
            elif(self.rectangle.isChecked()):
                i = 0.66
                fault = 0
            else:
                fault = "a"

            int(fault)
            rotation.play(tetas0, F, i, d)
                

        except:
            self.label_3.setText("invalid input")
            del rotation



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

