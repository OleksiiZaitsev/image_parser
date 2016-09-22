import sys, screen
import requests
import re, os
from PyQt4 import QtCore, QtGui, QtDeclarative
from PyQt4.QtNetwork import *
import threading

app = QtGui.QApplication(sys.argv)
app.setWindowIcon(QtGui.QIcon('icon.jpg'))

window = QtGui.QWidget()
UI = screen.Ui_PARSER()
UI.setupUi(window)


path = ''
url = ''
except_url = []
image_size = 50000
stop = False


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'



# URL CLEANER
def except_cleaner(except_url, url):
    clean_url = set()
    for i in except_url:
        pattern = re.findall(r'(^ht.{0,25}\/{2}.{1,50}:?\/{0,10}.{0,150}) *', i)
        if pattern:
            if re.findall('\\\\', url):
                clean_url.add(i[:-2])
                print(url)
            clean_url.add(i)
    cleaned_url = list(clean_url)
    for i in cleaned_url:
        print(i)
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
def save(url, name, path):
    image = requests.get(url)
    if not os.path.exists(path):
        os.mkdir(path)
    if image.content.__sizeof__() > image_size:
        with open('{}{}'.format(path, name), "wb") as imgfile:
            imgfile.write(image.content)


    # CLEAN FILES FROM THE DICT WITH SAME SIZE
    #garbage_collector(path)


# NAME IMAGE BY URL
def name(url):
    split_name = re.split('\/|\?', url)
    name = re.findall('\/?(([a-zA-Z0-9\-\_\@]*)\.?(jpg|png|gif|ico|avi|mp4))', '{}'.format(split_name))
    type = re.findall('(jpg|png|gif|ico|avi|mp4)', '{}'.format(split_name))
    if type:
        return str(str('{}'.format(name[0][1]) + '.' + '{}'.format(type[0])))


# SEARCH THE TEXT
def search(data, ):
    for i in except_cleaner(data, url):
        if stop != True:
            print(i)
            pattern = 'src\=|.{0,10}(h.{0,25}\/{2}.{1,50}:?\/{0,10}.{0,150}(.png|.jpg|.ico|.JPG|.gif)) *'
            image = re.findall('.png.*|.jpg.*|.ico.*|.JPG.*|.gif.*', i)
            purified = re.search(pattern, i)
            if purified and image:
                #print(purified.group(1))
                if purified.group(1) != None:
                    save(purified.group(1), name(purified.group(1)), path)


            elif re.match('\/\/.+', i):
                except_url.append("{}{}".format('http:', i))
            elif re.match('https|http.+', i):
                except_url.append("{}".format(i))
        else:
            break

# STOP THE PROGRAM
def STOP():
    del except_url[:]
    print(os.path.abspath(UI.lineEdit_PATH.text()))
    global stop
    stop = True
    print('=== END ===')



# START THE PROGRAM
def START():
    global stop
    stop = False
    while True:
        for i in except_url:


            if stop != True:
                try:
                    print(bcolors.WARNING + 'EXCEPT URL: ', except_url)
                    search(data(i))

                except:
                    print('This site can’t be reached')
            else:
                break


def GET_IMAGES(url):
    global path
    UI.webView.setUrl(QtCore.QUrl(url))
    path = UI.lineEdit_PATH.text() +'/'
    p1 = threading.Thread(target=lambda: search(data(url)), )
    p2 = threading.Thread(target=START, )
    p1.start()
    p2.start()

def OPEN():
    if not os.path.exists(os.path.abspath(UI.lineEdit_PATH.text())):
        os.mkdir(os.path.abspath(UI.lineEdit_PATH.text()))
    else:
        pass
    print(os.path.abspath(UI.lineEdit_PATH.text()))
    os.startfile(os.path.abspath(UI.lineEdit_PATH.text()))


QtCore.QObject.connect(UI.pushButton_START,QtCore.SIGNAL("clicked()"),
                       lambda: GET_IMAGES(UI.lineEdit_URL.text(),))

QtCore.QObject.connect(UI.pushButton_STOP, QtCore.SIGNAL("clicked()"),
                       lambda:STOP())

QtCore.QObject.connect(UI.pushButton_OPEN, QtCore.SIGNAL("clicked()"),
                       lambda:OPEN())



if __name__ == '__main__':
    UI.webView.setUrl(QtCore.QUrl('https://www.artstation.com/'))
    window.show()
    sys.exit(app.exec_())