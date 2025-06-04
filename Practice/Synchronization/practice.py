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

l = RLock()
print("Aquire Lock")
print(l.acquire())
print("Again Aquire Lock")
print(l.acquire())

