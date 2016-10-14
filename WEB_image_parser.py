import sys, screen
import requests
import re, os
from PyQt4 import QtCore, QtGui, QtDeclarative
from PyQt4.QtCore import QTimer
from PyQt4.QtNetwork import *
import threading
import time

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
UI = screen.Ui_PARSER()
UI.setupUi(window)


path = ''
url = ''
except_url = []
image_size = 500

#http://lamcdn.net/furfurmag.ru/post_image-image/QBna33peHIGsPvZIrVxaEw-wide.jpg
# DATA PREPARATION IN LIST BY URL
def data(url):
    data = []
    if not re.findall(r'(htt.{1,3}://.+?)', url):
        url = "http://" + url

    ROOT_URL = re.findall(r'(^http[s]*://.+\.(ua|com|ru|me|net|io)).*', url)[0]
    page = requests.get(url='{}'.format(url))
    print("url       :",url)
    print("ROOT_URL       :", ROOT_URL)
    #################################################################################
    def images(pattern: str, text: str):
        pattern = pattern
        URLs = re.findall(pattern, text)
        for i in URLs:
            if not re.findall("(^htt.*)", i) and re.findall("(jpg|png|gif|ico)", i):
                print("1  =", i)
                data.append(str(ROOT_URL[0]) + "/" + i)

            elif re.findall("(attachment)", i):
                print("2  =", i)
                data.append(str(ROOT_URL[0]) + "/" + i)

            elif re.findall("(^htt.*jpg|png|gif|ico.*)", i):
                print("3  =", i)
                data.append(i)

            else:
                print("else:    ",i)

    #################################################################################
    RSS_URLs = re.findall(r'.*"(htt.*rss)".*', page.text)
    if RSS_URLs:
        print(RSS_URLs)
        RSS = requests.get(url='{}'.format(RSS_URLs[0]))
        images(r'.*img src\="(.*?)\"', RSS.text)
        images(r'"(htt.{1,3}://.+?)"',RSS.text)

    images(r'.*img src\="(.*?)\"', page.text)
    images(r'"(htt.{1,3}://.+?)"', page.text)
    images(r'src="(/attachment[\w?\.\=]*[0-9]*)"', page.text)

    return set(data)


# SAVE IMAGE BY URL
def save(url: str):
    path = UI.lineEdit_PATH.text() +'/'
    if not os.path.exists(path):
        os.makedirs(path)
    try:
        name = naming(url)
        image = requests.get(url)
        if image.content.__sizeof__() > image_size:
            with open('{}{}'.format(path, name), "wb") as imgfile:
                imgfile.write(image.content)
    except:
        print("can`t save:  ", url)

# NAME IMAGE BY URL
def naming(url: str):
    url_separator = re.split('\/|\?', url)
    type_of_image = re.findall(".*(jpg|png|gif|ico).*", url)
    name_of_image = re.findall('([=a-zA-Z0-9_-]*).*', url_separator[-1])
    if type_of_image:
        return str(name_of_image[0]) + '.' + str(type_of_image[0])
    else:
        return str(name_of_image[0]) + '.' + str("png")

# OPEN DIR
def open_dir():
    if not os.path.exists(os.path.abspath(UI.lineEdit_PATH.text())):
        os.mkdir(os.path.abspath(UI.lineEdit_PATH.text()))
    else:
        pass
    os.startfile(os.path.abspath(UI.lineEdit_PATH.text()))


class programThreadsFor():
    def __init__(self, save, data):
        self._running = None
        self.save = save
        self.data = data
        self.progressBar_value = 0
        self.timer = QTimer()

    def progressBar(self):
        UI.progressBar.setProperty("value", self.progressBar_value)

    def BODY(self):
        self.url = UI.lineEdit_URL.text()
        self.summ = len(self.data(self.url))

        for i in enumerate(self.data(self.url)):
            if self._running == False: break
            self.save(i[1])
            self.progressBar_value = (i[0]/self.summ)*100
        self.progressBar_value = 100

    def START(self):
        self.progressBar_value = 0
        self.timer.timeout.connect(self.progressBar)
        self.timer.start(1000)

        self.url = UI.lineEdit_URL.text()
        if not re.findall(r'(htt.{1,3}://.+?)', self.url):
            self.url = "http://" + self.url

        UI.webView.setUrl(QtCore.QUrl(self.url))
        self._running = True
        self.Thread = threading.Thread(target=lambda: self.BODY())
        self.Thread.start()

    def STOP(self):
        self.timer.stop()
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


tread_parse = programThreadsFor(save, data)
tread_open_dir = programThreads(lambda: open_dir())



QtCore.QObject.connect(UI.pushButton_START,QtCore.SIGNAL("clicked()"), lambda: tread_parse.START())
QtCore.QObject.connect(UI.pushButton_STOP, QtCore.SIGNAL("clicked()"), lambda: tread_parse.STOP())
QtCore.QObject.connect(UI.pushButton_OPEN, QtCore.SIGNAL("clicked()"), lambda: tread_open_dir.START())



if __name__ == '__main__':
    window.show()
    sys.exit(app.exec_())
