# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Form01.ui'
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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(986, 541)
        self.verticalLayoutWidget = QtGui.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 971, 521))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem)
        self.pushButton_START = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushButton_START.setObjectName(_fromUtf8("pushButton_START"))
        self.verticalLayout.addWidget(self.pushButton_START)
        self.label_TEXT = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_TEXT.setText(_fromUtf8(""))
        self.label_TEXT.setScaledContents(True)
        self.label_TEXT.setAlignment(QtCore.Qt.AlignCenter)
        self.label_TEXT.setObjectName(_fromUtf8("label_TEXT"))
        self.verticalLayout.addWidget(self.label_TEXT)
        self.pushButton_STOP = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushButton_STOP.setObjectName(_fromUtf8("pushButton_STOP"))
        self.verticalLayout.addWidget(self.pushButton_STOP)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.pushButton_START.setText(_translate("Form", "START", None))
        self.pushButton_STOP.setText(_translate("Form", "STOP", None))

