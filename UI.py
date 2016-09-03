import sys
from parser_PyQt import *
from PyQt4 import QtCore, QtGui, QtDeclarative
from PyQt4.QtNetwork import *
from PyQt4.QtWebKit import QWebView,QWebPage


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


class Ui_image_parser_QObject(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)

    def setupUi(self, image_parser_QObject):
        image_parser_QObject.setObjectName(_fromUtf8("image_parser_QObject"))
        image_parser_QObject.resize(532, 587)
        image_parser_QObject.setMaximumSize(QtCore.QSize(532, 587))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("icons/wallpaperfolder.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        image_parser_QObject.setWindowIcon(icon)
        image_parser_QObject.setWindowOpacity(1.0)
        self.horizontalLayout = QtGui.QHBoxLayout(image_parser_QObject)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.declarativeView = QtDeclarative.QDeclarativeView(image_parser_QObject)
        self.declarativeView.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.declarativeView.sizePolicy().hasHeightForWidth())
        self.declarativeView.setSizePolicy(sizePolicy)
        self.declarativeView.setMinimumSize(QtCore.QSize(0, 0))
        self.declarativeView.setMaximumSize(QtCore.QSize(512, 512))
        self.declarativeView.setSizeIncrement(QtCore.QSize(0, 0))
        self.declarativeView.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.declarativeView.setAutoFillBackground(True)
        self.declarativeView.setStyleSheet(_fromUtf8("background-image: url(icons/wallpaperfolder.jpg);"))
        self.declarativeView.setFrameShape(QtGui.QFrame.Box)
        self.declarativeView.setFrameShadow(QtGui.QFrame.Sunken)
        self.declarativeView.setRubberBandSelectionMode(QtCore.Qt.ContainsItemBoundingRect)
        self.declarativeView.setObjectName(_fromUtf8("declarativeView"))
        self.verticalLayout.addWidget(self.declarativeView)
        self.lineEdit = QtGui.QLineEdit(image_parser_QObject)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.verticalLayout.addWidget(self.lineEdit)
        self.pushButton_GET_IMAGES = QtGui.QPushButton(image_parser_QObject)
        self.pushButton_GET_IMAGES.setObjectName(_fromUtf8("pushButton_GET_IMAGES"))
        self.verticalLayout.addWidget(self.pushButton_GET_IMAGES)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.retranslateUi(image_parser_QObject)
        QtCore.QMetaObject.connectSlotsByName(image_parser_QObject)

    def retranslateUi(self, image_parser_QObject):
        image_parser_QObject.setWindowTitle(_translate("image_parser_QObject", "image_parser", None))
        self.pushButton_GET_IMAGES.setText(_translate("image_parser_QObject", "GET IMAGES", None))
        self.pushButton_GET_IMAGES.clicked.connect(self.GET_IMAGES)

    def GET_IMAGES(self):
        url = self.lineEdit.text()
        image_size = 100000
        search(data(url))
        start()


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = Ui_image_parser_QObject()
    ex.show()
    sys.exit(app.exec_())
