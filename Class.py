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

# class A:
#     p = 50
#     def __init__(self):
#         A.q = 40
#         del A.p
#     def m1(self):
#         A.r = 30
#         del A.q
#     @classmethod
#     def m2(cls):
#         cls.s = 20
#         del A.r
#     @staticmethod
#     def m3():
#         A.t = 10
#         del A.s
# print(A.__dict__)
# a = A()
# print(A.__dict__)
# a.m1()
# print(A.__dict__)
# a.m2()
# print(A.__dict__)
# a.m3()
# print(A.__dict__)
# a.u = 100
# print(A.__dict__)
# del A.r
# print(A.__dict__)
# del Test.t
# print(Test.__dict__)

# class A:
#     p = 50
# a1 = A()
# del a1.p

# import sys

# class Acc_Hldr:
#     Bank = "HBL"
#     def __init__(self,n, bal = 0.0):
#         self.n = n
#         self.bal = bal
#     def deposite(self, amt):
#         self.bal = self.bal + amt
#         print("Balance", self.bal)
#     def withdraw(self, amt):
#         if amt > self.bal:
#             print("insufficient bal")
#             sys.exit(0)
#         self.bal = self.bal - amt
#         print("Balance", self.bal)
# print(Acc_Hldr.Bank)
# n = input("Enter Name: ")
# ah = Acc_Hldr(n) 
# while True:
#     print('d-Deposite \nw-widthdraw \ne=exit')
#     o = input("Choose the Option: ")
#     if o == 'd' or o == 'D':
#         amt = float(input("Enter Amount: "))
#         ah.deposite(amt)
#     elif o == 'w' or o == 'W':      
#         amt = float(input("Enter Amount: "))
#         ah.withdraw(amt)
#     elif o == 'e' or o =='E':
#         print("Thank you for banking")
#         sys.exit(0)
#     else:
#         print('Please Try Again')

# class Emp:
#     def __init__(self, emp_n, emp_sal):
#         self.emp_n = emp_n
#         self.emp_sal = emp_sal
#     def m1(self):
#         print(self.emp_n)
#         print('Salary', self.emp_sal)
#     def m2(self):
#         if self.emp_sal > 80000:
#             print('GRade Pay 8')
#         elif self.emp_sal > 70000:
#             print('GRade Pay 7')
#         elif self.emp_sal > 60000:
#             print('GRade Pay 6')
#         else: 
#             print('Consolidated')
# n = int(input('Enter Number of employees: '))
# for i in range(n):
#     emp_n = input('Enter Name: ')
#     emp_sal = int(input('Enter Salary: '))
#     e = Emp(emp_n, emp_sal)
#     e.m1()
#     e.m2()
#     print()

# class Book:
#     auth = 3
#     @classmethod
#     def wri(cls, name):
#         print('{} is writing a book with {} authors' .format(name, cls.auth))
# Book.wri('Hassan')

# class A:
#     c = 0
#     def __init__(self):
#         A.c = A.c + 1
#     @classmethod
#     def m1(cls):
#         print("No of object created: ", cls.c)
# a1 = A()
# a2 = A()
# a3 = A()
# a3 = A()
# A.m1()

# class A:
#     @staticmethod
#     def add(a,b):
#         print("Addition", a+b)
#     @staticmethod
#     def mul(a,b):
#         print("Multipilication", a*b)
#     @staticmethod
#     def Avg(a,b):
#         print("Average", (a+b)/2)

# A.add(2,3)
# A.mul(2,3)
# A.Avg(2,3)

# class Emp:
#     def emp_name1(self, emp_n):
#         self.emp_n = emp_n
#     def emp_name2(self):
#         return self.emp_n
#     def emp_sal1(self, emp_s):
#         self.emp_s = emp_s
#     def emp_sal2(self):
#         return self.emp_s
# n1 = int(input("Enter no of Employees: "))
# for i in range(n1):
#     e = Emp()
#     emp_n = input("Enter Name: ")
#     e.emp_name1(emp_n)
#     emp_s = int(input("Enter Salary: "))
#     e.emp_sal1(emp_s)
#     print(e.emp_name2())
#     print(e.emp_sal2())

# class Book:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#     def m(self):
#         print("Book Name: ", self.name)
#         print("Book Price: ", self.price)

# class update:
#     def m2(b):
#         b.price = b.price + 6000
#         b.m()
 
# b1 = Book('ETO', 4000)
# print(b1.m())
# update.m2(b1)