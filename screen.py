# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'image_parser.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_PARSER(object):
    def setupUi(self, PARSER):
        PARSER.setObjectName(_fromUtf8("PARSER"))
        PARSER.resize(975, 1170)
        self.LAYOUT = QtGui.QGridLayout(PARSER)
        self.LAYOUT.setObjectName(_fromUtf8("LAYOUT"))
        self.gridLayout_MAIN = QtGui.QGridLayout()
        self.gridLayout_MAIN.setSpacing(15)
        self.gridLayout_MAIN.setObjectName(_fromUtf8("gridLayout_MAIN"))
        self.gridLayout_ROOT = QtGui.QGridLayout()
        self.gridLayout_ROOT.setObjectName(_fromUtf8("gridLayout_ROOT"))
        self.lineEdit_URL = QtGui.QLineEdit(PARSER)
        self.lineEdit_URL.setObjectName(_fromUtf8("lineEdit_URL"))
        self.gridLayout_ROOT.addWidget(self.lineEdit_URL, 0, 1, 1, 3)
        self.label_TEXT_URL = QtGui.QLabel(PARSER)
        self.label_TEXT_URL.setObjectName(_fromUtf8("label_TEXT_URL"))
        self.gridLayout_ROOT.addWidget(self.label_TEXT_URL, 0, 0, 1, 1)
        self.pushButton_STOP = QtGui.QPushButton(PARSER)
        self.pushButton_STOP.setObjectName(_fromUtf8("pushButton_STOP"))
        self.gridLayout_ROOT.addWidget(self.pushButton_STOP, 0, 5, 1, 1)
        self.pushButton_START = QtGui.QPushButton(PARSER)
        self.pushButton_START.setObjectName(_fromUtf8("pushButton_START"))
        self.gridLayout_ROOT.addWidget(self.pushButton_START, 0, 4, 1, 1)
        self.lineEdit_PATH = QtGui.QLineEdit(PARSER)
        self.lineEdit_PATH.setObjectName(_fromUtf8("lineEdit_PATH"))
        self.gridLayout_ROOT.addWidget(self.lineEdit_PATH, 3, 1, 1, 5)
        self.label_TEXT_PATH = QtGui.QLabel(PARSER)
        self.label_TEXT_PATH.setObjectName(_fromUtf8("label_TEXT_PATH"))
        self.gridLayout_ROOT.addWidget(self.label_TEXT_PATH, 3, 0, 1, 1)
        self.IMAGE = QtGui.QLabel(PARSER)
        self.IMAGE.setFrameShape(QtGui.QFrame.NoFrame)
        self.IMAGE.setFrameShadow(QtGui.QFrame.Plain)
        self.IMAGE.setMidLineWidth(0)
        self.IMAGE.setScaledContents(True)
        self.IMAGE.setObjectName(_fromUtf8("IMAGE"))
        self.gridLayout_ROOT.addWidget(self.IMAGE, 2, 0, 1, 6)
        self.gridLayout_MAIN.addLayout(self.gridLayout_ROOT, 2, 0, 1, 1)
        self.LAYOUT.addLayout(self.gridLayout_MAIN, 0, 0, 1, 1)

        self.retranslateUi(PARSER)
        QtCore.QMetaObject.connectSlotsByName(PARSER)

    def retranslateUi(self, PARSER):
        PARSER.setWindowTitle(_translate("PARSER", "PARSER", None))
        self.label_TEXT_URL.setText(_translate("PARSER", "URL:", None))
        self.pushButton_STOP.setText(_translate("PARSER", "STOP", None))
        self.pushButton_START.setText(_translate("PARSER", "START", None))
        self.label_TEXT_PATH.setText(_translate("PARSER", "PATH:", None))
        self.IMAGE.setText(_translate("PARSER", "TextLabel", None))

