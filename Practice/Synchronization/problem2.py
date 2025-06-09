from threading import *
import time
l = RLock()
def outer():
    l.acquire()
    print("Enter Outer Func")
    iner()
    l.release()
def iner():
    l.acquire()
    print("Enter Inner Func")
    l.release()
def rec(n):
    l.acquire()
    if n == 0:
        print("Base Case")
    else:
        print("Recursive Func", n)
        rec(n-1)
    l.release()
t1 = Thread(target=outer)
t2 = Thread(target=rec, args=(3,))

t1.start()
t2.start()
t1.join()
t2.join()
print("Main Thread Finished")