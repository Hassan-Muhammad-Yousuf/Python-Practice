# class A:
#     "Document String"
# print(A.__doc__)
# help(A)

# class test:
#     def __init__(self):
#         self.n = "Hassan"
#         self.m = 25
#     def y(self):
#         print("Name", self.n)
#         print("Age", self.m)

# p = test()
# print(p.y())

# class A:
#     def __init__(self, n):
#         self.n = n
#     def m(self):
#         print("Name:", self.n)
# a = A("Hassan")
# a.m()

# class A:
#     def __init__(self):
#         print("Constructor")
#     def b(self):
#         print("method")

# a = A()
# a.b()

# class test:
#     def __init__(self, a,b):
#         self.a = a
#         self.b =b
#     def m(self):
#         print("Name: {}\nId: {}".format(self.a, self.b))

# t = test("Hassan", 10202)
# t.m()

# class A:
#     def __init__(self):
#         self.n = "hassan"
#         self.m = "yousuf"
# a = A()
# print(a.__dict__)

# class A:
#     def __init__(self):
#         self.a = 100
#     def m(self):
#         self.b =200
# x = A()
# x.m()
# print(x.__dict__)

# class A:
#     def __init__(self):
#         self.n = 10
#     def x(self):
#         self.m = 20

# a = A()
# a.x()
# a.c = 30
# print(a.__dict__)

# class A:
#     def __init__(self):
#         self.n = 10
#         self.m = 20
#     def x(self):
#         print(self.n)
#         print(self.m)
# a = A()
# a.x()
# a.o = 30
# print(a.n, a.m, a.o)

# class A:
#     def __init__(self):
#         self.p = 2
#         self.q = 3
#         self.r = 4
#     def m(self):
#         del self.p
# a = A()
# print(a.__dict__)
# a.m()
# print(a.__dict__)
# del a.r
# print(a.__dict__)

# class A:
#     def __init__(self):
#         self.p = 2
#         self.q = 3
#         self.r = 4
# a1 = A()
# a2 = A()
# del a2.p
# print(a1.__dict__)
# print(a2.__dict__)

# class A:
#     p = 20
#     def __init__(self):
#         self.q = 10
# a1 = A()
# a2 = A()
# print("a1: ", a1.p, a1.q)
# print("a2: ", a2.p, a2.q)
# A.p = 200
# a1.q = 300
# print("a1: ", a1.p, a1.q)
# print("a2: ", a2.p, a2.q)

# class A:
#     p = 2
#     def __init__(self):
#         A.q = 3
#     def p1(self):
#         A.r = 4
#     @classmethod
#     def p2(cls):
#         cls.s = 5
#         A.t = 6
#     @staticmethod
#     def p3():
#         A.u = 7
# print(A.__dict__)
# a = A()
# print(A.__dict__)
# a.p1()
# print(A.__dict__)
# A.p2()
# print(A.__dict__)
# A.p3()
# print(A.__dict__)
# A.v =  8
# print(A.__dict__)

# class A:
#     p = 50
#     def __init__(self):
#         print(self.p)
#         print(A.p)
#     def n1(self):
#         print(self.p)
#         print(A.p)
#     @classmethod
#     def n2(cls):
#         print(cls.p)
#         print(A.p)
#     @staticmethod
#     def n3():
#         print(A.p)

# a = A()
# print(A.p)
# print(a.p)
# a.n1()
# a.n2()
# a.n3()

# class A:
#     p = 50
#     @classmethod
#     def n1(cls):
#         cls.p = 100
#     @staticmethod
#     def n2():
#         A.p = 200

# print(A.p)    
# A.n1()
# print(A.p)
# A.n2()
# print(A.p)

# class A:
#     p = 50
#     def __init__(self):
#         self.q=80
#     def n1(self):
#         self.p = 100
#         self.q = 200

# a1 = A()
# a2 = A()
# a1.n1()
# print(a1.p, a1.q)
# print(a2.p, a2.q)

# class A:
#     p = 50
#     def __init__(self):
#         self.q = 80
#     @classmethod
#     def n1(cls):
#         cls.p =150
#         cls.q =250
# a1 = A()
# a2 = A()
# a1.n1()
# print(a1.p,a1.q)
# print(a2.p,a2.q)
# print(A.p,A.q)