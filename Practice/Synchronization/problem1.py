from threading import *
import time

l = Lock()

def m1(n):
    l.acquire()
    try:
        for i in range(3):
            print(f"Hi from {n}")
            time.sleep(1)
    finally:
        l.release()

def m2(m):
    for i in range(3):
        print(f"By from {m}")
        time.sleep(0.5)

t1 = Thread(target=m1, args=('Hassan',)) 
t2 = Thread(target=m1, args=('Yousuf',)) 
t3 = Thread(target=m2, args=('BNan',)) 

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

print("Main thread finished")
