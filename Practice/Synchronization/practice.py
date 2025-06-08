from threading import *
# import time
# l = Lock()
# def m1(n):
#     l.acquire()
#     for i in range(2):
#         print('Hi: ', end='')
#         time.sleep(2)
#         print(n)
#     l.release()
# t1 = Thread(target = m1, args=['Hassan'])
# t2 = Thread(target = m1, args=['Yousuf'])
# t1.start()
# t2.start()

# l = Lock()
# print("Aquire Lock")
# print(l.acquire())
# print("Again Aquire Lock")
# print(l.acquire())

# l = RLock()
# print("Aquire Lock")
# print(l.acquire())
# print("Again Aquire Lock")
# print(l.acquire())

# from threading import *
# import time
# l = RLock()
# def fact(n):
#     l.acquire()
#     if n == 0:
#         opt = 1
#     else:
#         opt = n*fact(n-1)
#     l.release()
#     return opt
# def opt(n):
#     print("Factorial",n,":",fact(n))
# t1 = Thread(target=opt, args=(3,))
# t2 = Thread(target=opt, args=(5,))
# t1.start()
# t2.start()

# from threading import *
# import time
# s = Semaphore(2)
# def m1(n):
#     s.acquire()
#     for i in range(4):
#         print('Hi :', end='')
#         time.sleep(2)
#         print(n)
#     s.release()
# t1 = Thread(target=m1, args=("Hassan",))
# t2 = Thread(target=m1, args=("Yousuf",))
# t1.start()
# t2.start()

# from threading import *
# s =Semaphore(2)
# s.acquire()
# s.acquire()
# s.release()
# s.release()
# s.release()
# s.release()
# print('end')

# from threading import *
# s =BoundedSemaphore(2)
# s.acquire()
# s.acquire()
# s.release()
# s.release()
# s.release()
# s.release()
# print('end')


# from threading import *
# import time
# def prod():
#     time.sleep(3)
#     print('Producer thread producing items: ')
#     print('Producer thread notifications: ')
#     event.set()
# def cons():
#     print('Consumer thread waiting :')
#     event.wait()
#     print('Consumer thread consuming items :')
# event = Event()
# t1 = Thread(target=prod)
# t2 = Thread(target=cons)
# t1.start()
# t2.start()


# from threading import *
# def cons(c):
#     c.acquire()
#     print('Consumer thread waiting :')
#     c.wait()
#     print('Consumer thread consuming items :')
#     c.release()
# def prod(c):
#     c.acquire()
#     print('Producer thread producing items: ')
#     print('Producer thread notifications: ')
#     c.notify()
#     c.release()
# c = Condition()
# t1 = Thread(target=cons,args=(c,))
# t2 = Thread(target=prod,args=(c,))
# t1.start()
# t2.start()