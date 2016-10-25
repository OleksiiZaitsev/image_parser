import sys, UI
import requests
import re, os
from PyQt4 import QtCore, QtGui, QtDeclarative
from PyQt4.QtCore import QTimer
from PyQt4.QtNetwork import *
import threading
import time

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
UI = UI.Ui_PARSER()
UI.setupUi(window)


path = ''
url = ''
except_url = []
image_size = 500

QPixmap_images = ['None','None','None', 'None', 'None']




def Qimages():

    path = os.path.abspath(UI.lineEdit_PATH.text())


    if os.listdir(path):
        global QPixmap_images
        files =[os.path.join(path,i) for i in os.listdir(path)]
        image = os.path.join(path, max(files, key=os.path.getctime))
        QPixmap_images.append(image)

        UI.label_image01.setPixmap(QtGui.QPixmap(r'{}'.format(QPixmap_images[-1])))
        UI.label_image02.setPixmap(QtGui.QPixmap(r'{}'.format(QPixmap_images[-2])))
        UI.label_image03.setPixmap(QtGui.QPixmap(r'{}'.format(QPixmap_images[-3])))
        UI.label_image04.setPixmap(QtGui.QPixmap(r'{}'.format(QPixmap_images[-4])))
        UI.label_image05.setPixmap(QtGui.QPixmap(r'{}'.format(QPixmap_images[-5])))


Qimages_Timer = QTimer()
Qimages_Timer.timeout.connect(Qimages)
Qimages_Timer.start(1000)

# DATA PREPARATION IN LIST BY URL
def data(url):
    data = []
    deep_data = []

    if not re.findall(r'(htt.{1,3}://.+?)', url):
        url = "http://" + url

    ROOT_URL = re.findall(r'(^http[s]*://.+\.(ua|com|ru|me|net|io|to)).*', url)[0]
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
                deep_data.append(i)
                print("deep_data:    ",i)

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

    if UI.checkBox.checkState():
        for i in set(deep_data):
            try:
                deep_URLs = requests.get(url='{}'.format(i))
                images(r'.*img src\="(.*?)\"', deep_URLs.text)
                images(r'"(htt.{1,3}://.+?)"', deep_URLs.text)
                images(r'src="(/attachment[\w?\.\=]*[0-9]*)"', deep_URLs.text)
            except:
                print("404    -",    i)

    return set(data)


# SAVE IMAGE BY URL
def save(url: str):
    path = dir_path_exists() + '\\'
    try:
        name = naming(url)
        image = requests.get(url)
        if image.content.__sizeof__() > int(float(UI.lineEdit_SIZE_value.text())*1e+3):
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

# DIR PATH EXISTS
def dir_path_exists():
    if not os.path.exists(os.path.abspath(UI.lineEdit_PATH.text())):
        if UI.lineEdit_PATH.text() == None:
            UI.lineEdit_PATH.setText('temp')
        os.mkdir(os.path.abspath(UI.lineEdit_PATH.text()))

    else:
        pass
    return str(os.path.abspath(UI.lineEdit_PATH.text()))
# OPEN DIR
def open_dir():
    dir_path_exists()
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

def horizontalSlider_func():
    UI.lineEdit_SIZE_value.setText("{}".format(UI.horizontalSlider.value()))



UI.horizontalSlider.valueChanged.connect(horizontalSlider_func)

QtCore.QObject.connect(UI.pushButton_START,QtCore.SIGNAL("clicked()"), lambda: tread_parse.START())
QtCore.QObject.connect(UI.pushButton_STOP, QtCore.SIGNAL("clicked()"), lambda: tread_parse.STOP())
QtCore.QObject.connect(UI.pushButton_OPEN, QtCore.SIGNAL("clicked()"), lambda: tread_open_dir.START())



if __name__ == '__main__':
    window.show()
    sys.exit(app.exec_())
