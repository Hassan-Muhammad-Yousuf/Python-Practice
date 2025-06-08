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