import sys, screen
import requests
import re, os
from PyQt4 import QtCore, QtGui, QtDeclarative
from PyQt4.QtNetwork import *
import threading

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
UI = screen.Ui_PARSER()
UI.setupUi(window)


path = ''
url = ''
except_url = []
image_size = 500


# DATA PREPARATION IN LIST BY URL
def data(url):
    page = requests.get(url='{}'.format(url))
    main_url = re.findall('(htt.*\..{1,4})\/.*', url)[0]
    data = []
    if re.findall(r"\.zbrushcentral\.", url):  # www.zbrushcentral.com
        zbrushcentral_search_pattern = r'.*img src\="(.*?)\"'
        zbrushcentral_links = re.findall(zbrushcentral_search_pattern, page.text)

        for i in zbrushcentral_links:
            if not re.findall("(^htt.*)", i):
                data.append(main_url + '/' + i)
            elif re.findall("(^htt.*jpg$|png$|gif$|ico$)", i):
                data.append(i)

        return data

# SAVE IMAGE BY URL
def save(url: str):
    path = UI.lineEdit_PATH.text() +'/'
    name = naming(url)
    image = requests.get(url)
    if not os.path.exists(path):
        os.mkdir(path)
    if image.content.__sizeof__() > image_size:
        with open('{}{}'.format(path, name), "wb") as imgfile:
            imgfile.write(image.content)

# NAME IMAGE BY URL
def naming(url: str):
    name = re.split('\/|\?', url)
    print(name)
    image_type = re.findall('(jpg|png|gif|\.ico)', name[-1])
    if image_type:
        name = re.findall('(.*)[.].*', name[-1])
        return str(name[0]) + '.' + str(image_type[0])
    else:
        return str(name[-1]) + '.' + str("png")

# OPEN DIR
def open_dir():
    if not os.path.exists(os.path.abspath(UI.lineEdit_PATH.text())):
        os.mkdir(os.path.abspath(UI.lineEdit_PATH.text()))
    else:
        pass
    os.startfile(os.path.abspath(UI.lineEdit_PATH.text()))


class programThreadsWhile():
    def __init__(self, save, data):
        self._running = None
        self.save = save
        self.data = data

    def BODY(self):
        self.url = UI.lineEdit_URL.text()
        for i in self.data(self.url):
            if self._running == False: break
            self.save(i)


    def START(self):
        self._running = True
        self.Thread = threading.Thread(target=lambda: self.BODY())
        self.Thread.start()

    def STOP(self):
        self.Thread.daemon
        self._running = False
        self.Thread.join()
        print('=== END ===')

class programThreads():
    def __init__(self, func):
        self.func = func

    def START(self):
        self.Thread = threading.Thread(target=lambda: self.func())
        self.Thread.start()


tread_parse = programThreadsWhile(save, data)
tread_open_dir = programThreads(lambda: open_dir())



QtCore.QObject.connect(UI.pushButton_START,QtCore.SIGNAL("clicked()"), lambda: tread_parse.START())
QtCore.QObject.connect(UI.pushButton_STOP, QtCore.SIGNAL("clicked()"), lambda: tread_parse.STOP())

QtCore.QObject.connect(UI.pushButton_OPEN, QtCore.SIGNAL("clicked()"), lambda: tread_open_dir.START())



if __name__ == '__main__':
    window.show()
    sys.exit(app.exec_())
