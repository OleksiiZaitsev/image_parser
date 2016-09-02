import sys
from PyQt4 import QtCore, QtGui, QtDeclarative
from PyQt4.QtNetwork import *
from PyQt4.QtWebKit import QWebView,QWebPage
import requests
import re
import random
import os


path = r'images/'
image_size = 10000
url = ''
except_url = []



# URL CLEANER
def except_cleaner(except_url, url):
    clean_url = set()

    for i in except_url:
        pattern = re.findall(r'(^ht.{0,25}\/{2}.{1,50}:?\/{0,10}.{0,150}) *', i)
        if pattern:
            clean_url.add(i)
    cleaned_url = list(clean_url)

    for i in cleaned_url:
        if i == url:
            cleaned_url.remove(i)

        elif re.findall('(rss)', i):
            rss = i
            cleaned_url.remove(i)
            cleaned_url.insert(0,rss)

    return cleaned_url


# CREATED DICT OF FILES IN DIR "{NAME:SIZE}"
def ls(path):
    """RETURN DICT OF FILES {NAME:SIZE}"""

    items = {}
    files = os.listdir(path)

    for i in files:
        items['{}'.format(i)] = os.path.getsize(path + i)
    return items


# SEARCH FILES FROM THE DICT WITH SAME SIZE
def search_for_clean(ls, size):
    """RETURN LIST OF NAMES FOR DELETE"""

    garbage = []

    for i in ls.items():
        if i[1] == size:
            garbage.append(i[0])
    return garbage[1:]


# CLEAN FILES FROM THE DICT WITH SAME SIZE
def garbage_collector(path):
    items = ls(path)

    for size in items.values():

        for i in search_for_clean(items, size):
            if os.path.exists(path + i):
                print('# CLEAN FILES FROM THE DIR WITH SAME SIZE :', path + i)
                os.remove(path + i)
            else:
                pass


# DATA PREPARATION IN LIST BY URL
def data(url):
    page = requests.get(url='{}'.format(url))
    encoding = page.encoding  # GET PAGE CODE

    if encoding == None:
        encoding = 'UTF-8'
        data = r'{}'.format(page.text.encode(encoding=encoding))
        return data.split('"')  # SPLIT DATA BY THE '"' AND RETURN
    else:
        data = r'{}'.format(page.text.encode(encoding=encoding))
        return data.split('"')  # SPLIT DATA BY THE '"' AND RETURN


# SAVE IMAGE BY URL AND DEF NAME()
def save(url, name, path = 'images/'):
    image = requests.get(url)

    if not os.path.exists(path):
        os.mkdir(path)

    if image.content.__sizeof__() > image_size:
        with open('{}{}'.format(path, name), "wb") as imgfile:
            imgfile.write(image.content)

    # CLEAN FILES FROM THE DICT WITH SAME SIZE
    garbage_collector(path)


# NAME IMAGE BY URL
def name(url):
    split_name = re.split('\/|\-|\?', url)
    search_name = re.findall('(\w+.jpg|\w.png)', '{}'.format(split_name))

    if len(search_name) > 0:
        return str(random.randint(0,500)) + '_' + search_name[0]
    else:
        if re.findall('jpg', '{}'.format(split_name)):
            return str(random.randint(0,500)) + '_' + '.jpg'
        elif re.findall('png', '{}'.format(split_name)):
            return str(random.randint(0,500)) + '_' + '.png'
        elif re.findall('ico', '{}'.format(split_name)):
            return str(random.randint(0,500)) + '_' + '.ico'
        elif re.findall('gif', '{}'.format(split_name)):
            return str(random.randint(0,500)) + '_' + '.gif'


# SEARCH THE TEXT
def search(data):
    for i in except_cleaner(data, url):
        print(i)
        pattern = 'src\=|.{0,10}(h.{0,25}\/{2}.{1,50}:?\/{0,10}.{0,150}(.png|.jpg|.ico|.JPG|.gif)) *'
        image = re.findall('.png.*|.jpg.*|.ico.*|.JPG.*|.gif.*', i)
        purified = re.search(pattern, i)

        if purified and image:
            #print(purified.group(1))
            if purified.group(1) != None:
                save(purified.group(1), name(purified.group(1)))

        elif re.match('\/\/.+', i):
            except_url.append("{}{}".format('http:', i))

        elif re.match('https|http.+', i):
            except_url.append("{}".format(i))


# START THE PROGRAM
def start():
    while True:
        for i in except_url:
            print(i)
            try:
                print('=========================', except_url)
                search(data(i))
            except:
                print('This site can’t be reached')


# PyQt UI
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
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("D:/MyPython/image_parser-master/icons/wallpaperfolder.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
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
        self.declarativeView.setStyleSheet(_fromUtf8("background-image: url(D:/MyPython/image_parser-master/icons/wallpaperfolder.jpg);"))
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
        image_size = 10000
        url = self.lineEdit.text()

        search(data(url))
        start()


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = Ui_image_parser_QObject()
    ex.show()
    sys.exit(app.exec_())
