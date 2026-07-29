import threading
import time
lock=threading.lock()



def  work(name):
  if lock:
    for i in range(1,6):
      print(name,i)
      time.sleep(1)
#   print("threading is running")
t1=threading.thread(target=work)#creates a thread
t2=threading.thread(target=work)
t1.start()
t2.start()
t1.join()
t2.join()



