from PyQt4 import QtCore, QtGui
import sys
import Form01
import threading
import time
import os

class MyThread(threading.Thread):
    def __init__(self, process):
        super().__init__()
        self.process = process
    def run(self):
        self.process()



app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
UI = Form01.Ui_Form()
UI.setupUi(window)
text = ""
RUN = True


def START():
    global process_TEXT
    global RUN
    RUN = True
    process_TEXT = MyThread(TEXT)
    process_TEXT.start()
    print('process_TEXT =', process_TEXT.is_alive())

def STOP():
    global RUN
    RUN = False
    process_TEXT.daemon
    process_TEXT.join()
    print('process_TEXT =', process_TEXT.is_alive())



QtCore.QObject.connect(UI.pushButton_START,QtCore.SIGNAL("clicked()"), lambda : START())
QtCore.QObject.connect(UI.pushButton_STOP, QtCore.SIGNAL("clicked()"), lambda : STOP())


def TEXT():
    while RUN:
        global text
        images = os.listdir(os.path.abspath(r'images'))
        # text = images[0]
        text = "{}".format(time.time())
        UI.label_TEXT.setText(text)
        # UI.label_TEXT.setPixmap(QtGui.QPixmap(text))
        time.sleep(1)





if __name__ == "__main__":
    window.show()
    sys.exit(app.exec_())



