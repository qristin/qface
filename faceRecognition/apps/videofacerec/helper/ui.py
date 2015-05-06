# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created: Sun Jun 15 13:56:44 2014
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        screen = QtGui.QDesktopWidget().screenGeometry() 

        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(screen.width(), screen.height())
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))

        # self.frame = QtGui.QFrame(self.centralwidget)
        # self.frame.setGeometry(QtCore.QRect(200, 0, 4*320, 4*240))
        # self.frame.setFrameShape(QtGui.QFrame.Box)
        # self.frame.setFrameShadow(QtGui.QFrame.Plain)
        # self.frame.setObjectName(_fromUtf8("frame"))

        # self.gridLayout = QtGui.QGridLayout(self.frame)
        # self.gridLayout.setSpacing(10)
        # self.gridLayout.setObjectName(_fromUtf8("gridLayout"))


        self.videoFrame = QtGui.QLabel(self.centralwidget)
        self.videoFrame.setGeometry(QtCore.QRect(500, 0, 2*320, 2*240))
        self.videoFrame.setObjectName(_fromUtf8("videoFrame"))
        #self.gridLayout.addWidget(self.videoFrame,0,0)
        MainWindow.setCentralWidget(self.centralwidget)

        self.label1 = QtGui.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(1300,100, 200, 10))
        self.label1.setText('TEST')

        self.label2 = QtGui.QLabel(self.centralwidget)
        self.label2.setGeometry(QtCore.QRect(1300,200, 200, 10))
        self.label2.setText('TEST')

        self.label3 = QtGui.QLabel(self.centralwidget)
        self.label3.setGeometry(QtCore.QRect(1300,300, 200, 10))
        self.label3.setText('TEST')

        self.label4 = QtGui.QLabel(self.centralwidget)
        self.label4.setGeometry(QtCore.QRect(1300,400, 200, 10))
        self.label4.setText('TEST')

        self.label5 = QtGui.QLabel(self.centralwidget)
        self.label5.setGeometry(QtCore.QRect(1300,500, 200, 10))
        self.label5.setText('TEST')

        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 823, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.videoFrame.setText(QtGui.QApplication.translate("MainWindow", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))

