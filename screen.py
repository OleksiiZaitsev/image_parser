# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'screen.ui'
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
        PARSER.resize(1624, 1527)
        PARSER.setMinimumSize(QtCore.QSize(0, 0))
        self.LAYOUT = QtGui.QGridLayout(PARSER)
        self.LAYOUT.setObjectName(_fromUtf8("LAYOUT"))
        self.gridLayout_MAIN = QtGui.QGridLayout()
        self.gridLayout_MAIN.setSpacing(15)
        self.gridLayout_MAIN.setObjectName(_fromUtf8("gridLayout_MAIN"))
        self.gridLayout_ROOT = QtGui.QGridLayout()
        self.gridLayout_ROOT.setObjectName(_fromUtf8("gridLayout_ROOT"))
        self.pushButton_STOP = QtGui.QPushButton(PARSER)
        self.pushButton_STOP.setObjectName(_fromUtf8("pushButton_STOP"))
        self.gridLayout_ROOT.addWidget(self.pushButton_STOP, 1, 6, 1, 1)
        self.label_TEXT_URL = QtGui.QLabel(PARSER)
        self.label_TEXT_URL.setObjectName(_fromUtf8("label_TEXT_URL"))
        self.gridLayout_ROOT.addWidget(self.label_TEXT_URL, 1, 0, 1, 1)
        self.label_TEXT_PATH = QtGui.QLabel(PARSER)
        self.label_TEXT_PATH.setObjectName(_fromUtf8("label_TEXT_PATH"))
        self.gridLayout_ROOT.addWidget(self.label_TEXT_PATH, 4, 0, 1, 1)
        self.pushButton_START = QtGui.QPushButton(PARSER)
        self.pushButton_START.setObjectName(_fromUtf8("pushButton_START"))
        self.gridLayout_ROOT.addWidget(self.pushButton_START, 1, 5, 1, 1)
        self.webView = QtWebKit.QWebView(PARSER)
        self.webView.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.webView.setObjectName(_fromUtf8("webView"))
        self.gridLayout_ROOT.addWidget(self.webView, 2, 0, 1, 7)
        self.pushButton_OPEN = QtGui.QPushButton(PARSER)
        self.pushButton_OPEN.setObjectName(_fromUtf8("pushButton_OPEN"))
        self.gridLayout_ROOT.addWidget(self.pushButton_OPEN, 4, 6, 1, 1)
        self.lineEdit_PATH = QtGui.QLineEdit(PARSER)
        self.lineEdit_PATH.setObjectName(_fromUtf8("lineEdit_PATH"))
        self.gridLayout_ROOT.addWidget(self.lineEdit_PATH, 4, 1, 1, 5)
        self.lineEdit_URL = QtGui.QLineEdit(PARSER)
        self.lineEdit_URL.setObjectName(_fromUtf8("lineEdit_URL"))
        self.gridLayout_ROOT.addWidget(self.lineEdit_URL, 1, 1, 1, 4)
        self.gridLayout_MAIN.addLayout(self.gridLayout_ROOT, 2, 0, 1, 1)
        self.LAYOUT.addLayout(self.gridLayout_MAIN, 0, 0, 1, 1)

        self.retranslateUi(PARSER)
        QtCore.QMetaObject.connectSlotsByName(PARSER)

    def retranslateUi(self, PARSER):
        PARSER.setWindowTitle(_translate("PARSER", "WEB IMAGE PARSER", None))
        self.pushButton_STOP.setText(_translate("PARSER", "STOP", None))
        self.label_TEXT_URL.setText(_translate("PARSER", "URL:", None))
        self.label_TEXT_PATH.setText(_translate("PARSER", "PATH:", None))
        self.pushButton_START.setText(_translate("PARSER", "START", None))
        self.pushButton_OPEN.setText(_translate("PARSER", "OPEN", None))
        self.lineEdit_PATH.setText(_translate("PARSER", "None", None))
        self.lineEdit_URL.setText(_translate("PARSER", "https://", None))

from PyQt4 import QtWebKit
