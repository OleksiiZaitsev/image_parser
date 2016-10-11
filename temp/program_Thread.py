import threading
import time
import urllib.request
import re, os

image_size = 500
path = 'sdcard/Pictures'


class programThread():
    def __init__(self, func):
        self.__running = None
        self.func = func
        
    def body_while(self):
        while self.__running:
            self.func()
            
    def start(self):
        self.__running = True
        self.funcThread = threading.Thread(target=
        	                 lambda: self.body_while()
        	                 )
        self.funcThread.start()
        
        
    def stop(self):
        self.__running = False 
        self.funcThread.join()
        
    
def naming(url: str):
    url_separator = re.split('\/|\?', url)
    print(url_separator)
    image  = re.findall(".*(jpg|png|gif|ico).*", url)
    if image:
        name = re.findall('(.*)[.].*', url_separator[-1])
        return str(name[0]) + '.' + str(image[0])
    elif temp:
        return str(url_separator[-1]) + '.' + str(re.findall(".*(jpg|png|gif|ico).*", url)[0])
    elif temp:
        return str(url_separator[-1]) + '.' + str("png")

 
def save(url: str):
    name = naming(url)
    image = urllib.request.urlopen(url)
    if not os.path.exists(path):
        os.mkdir(path)
    if not os.path.exists(path):
        os.makedirs(path)
    with open('{}{}'.format(path, name), "wb") as imgfile:
        imgfile.write(image.content)

   
def myfunc(url):
    url_request = urllib.request.urlopen(url) 
    data = url_request.read()
    pattern = r'.*"(.*jpg|png.*?)".*'
    search = re.findall(pattern, "{}".format(data))
    print(search)
    # if search:
    #     save(search[0])
    #
    
url = r"https://www.pinterest.com"
    
myfunc_Thread = programThread(lambda: myfunc(url))
myfunc_Thread.start()
