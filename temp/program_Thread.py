import threading
import time


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
        
def myfunc(text):
    print(text)
    
    
myfunc_Thread1 = programThread(lambda: myfunc(1))
    
myfunc_Thread2 = programThread(lambda: myfunc(2))

myfunc_Thread1.start()
myfunc_Thread2.start()
time.sleep(1)
myfunc_Thread2.stop()
myfunc_Thread1.stop()
    

        