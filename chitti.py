# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chitti.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_chitti(object):
    def setupUi(self, chitti):
        chitti.setObjectName("chitti")
        chitti.resize(1124, 824)
        self.centralwidget = QtWidgets.QWidget(chitti)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, -40, 1171, 841))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../../../OneDrive/Desktop/Intercept_Echo_v2-3.5MB-2-1542062294.gif"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(860, 710, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(170, 255, 0);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(980, 710, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 10, 421, 91))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../../../OneDrive/Desktop/ini.gif"))
        self.label_2.setScaledContents(False)
        self.label_2.setObjectName("label_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(630, 0, 256, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.textBrowser.setFont(font)
        self.textBrowser.setStyleSheet("background-color: rgb(170, 255, 0);")
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(880, 0, 241, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.textBrowser_2.setFont(font)
        self.textBrowser_2.setStyleSheet("\n"
"background-color: rgb(170, 255, 0);")
        self.textBrowser_2.setObjectName("textBrowser_2")
        chitti.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(chitti)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1124, 26))
        self.menubar.setObjectName("menubar")
        chitti.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(chitti)
        self.statusbar.setObjectName("statusbar")
        chitti.setStatusBar(self.statusbar)

        self.retranslateUi(chitti)
        QtCore.QMetaObject.connectSlotsByName(chitti)

    def retranslateUi(self, chitti):
        _translate = QtCore.QCoreApplication.translate
        chitti.setWindowTitle(_translate("chitti", "MainWindow"))
        self.pushButton.setText(_translate("chitti", "Run"))
        self.pushButton_2.setText(_translate("chitti", "Terminate"))