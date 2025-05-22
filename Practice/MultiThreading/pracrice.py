# import threading
# print("Current Exec: Thread ",threading.current_thread().getName())

# import threading
# def m1():
#     for i in range(1,5):
#         print("Child Thread")

# t = threading.Thread(target = m1)
# t.start()
# for i in range(1,5):
#     print("Main Thread")

# from threading import *
# class A(Thread):
#     def run(self):
#         for i in range(5):
#             print("Child Class")
# a = A()
# a.start()
# for i  in range(5):
#     print("Main Part")

# from threading import *
# import time
# def m1(n):
#     for i in n:
#         time.sleep(1)
#         print("Double: ",2*i)
# def m2(n):
#     for i in n:
#         time.sleep(1)
#         print("Square: ",i*i)
# n = [2,4]
# b_t = time.time()
# m1(n)
# m2(n)
# print("Total Time: ",time.time()-b_t)


# from threading import *
# import time
# def m1(n):
#     for i in n:
#         time.sleep(1)
#         print("Double: ",2*i)
# def m2(n):
#     for i in n:
#         time.sleep(1)
#         print("Square: ",i*i)
# n = [2,4]
# b_t = time.time()
# t1 = Thread(target=m1,args=(n,))
# t2 = Thread(target=m2,args=(n,))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print("Total Time: ",time.time()-b_t)

# from threading import *
# print(current_thread().getName())
# current_thread().setName("hassan")
# print(current_thread().getName())
# print(current_thread().name)

# from threading import *
# def A():
#     print("Child Thread")
# t = Thread(target=A)
# t.start()
# print("Main Thread ID No:", current_thread().ident)
# print("Child Thread ID No:", t.ident)

# from threading import Thread, current_thread, active_count
# import time

# def A():
#     print(current_thread().name, "\nStart")
#     time.sleep(3)
#     print(current_thread().name, "\nEnd")
#     print("Active Threads", active_count())

# t1 = Thread(target=A, name="Child 1")
# t2 = Thread(target=A, name="Child 2")
# t1.start()
# t2.start()

# print("Active Threads", active_count())
# time.sleep(5)
# print("Active Threads", active_count())

# from threading import Thread, current_thread, active_count,enumerate as en
# import time

# def A():
#     print(current_thread().name, "----> Start")
#     time.sleep(3)
#     print(current_thread().name, "----> End")
#     print("Active Threads", active_count())

# t1 = Thread(target=A, name="Child 1")
# t2 = Thread(target=A, name="Child 2")
# t1.start()
# t2.start()
# l = en()
# for i in l:
#     print("Thread Name:", i.name)
# time.sleep(5)
# l = en()
# for i in l:
#     print("Thread Name:", i.name)

# from threading import Thread, current_thread, active_count
# import time

# def A():
#     print(current_thread().name, "----> Start")
#     time.sleep(3)
#     print(current_thread().name, "----> End")
#     print("Active Threads", active_count())

# t1 = Thread(target=A, name="Child 1")
# t2 = Thread(target=A, name="Child 2")
# t1.start()
# t2.start()
# print(t1.name, "is Alive", t1.is_alive())
# print(t2.name, "is Alive", t2.is_alive())
# time.sleep(5)
# print(t1.name, "is Alive", t1.is_alive())
# print(t2.name, "is Alive", t2.is_alive())

# from threading import *
# import time
# def m1():
#     for i in range(5):
#         print("hassan")
#         time.sleep(2)
# t = Thread(target=m1)
# t.start()
# t.join(5)
# for i in range(2):
#     print("Yousuf")

# from threading import *
# print(current_thread().daemon)
# current_thread().setDaemon(True)

# from threading import Thread
# def m1():
#     print("hassan")
# t =Thread(target=m1)
# print(t.daemon)
# t.setDaemon(True)
# print(t.daemon)

# from threading import *
# import time
# def m1():
#     for i in range(5):
#         print("Child 1")
# time.sleep(2)
# t =Thread(target=m1)
# t.setDaemon(True)
# t.start()
# time.sleep(5)
# print("End Main")