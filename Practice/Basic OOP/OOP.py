# class python:
#     def __init__(self):
#         self.n = "Hassan"
#         self.r = 25
#     def m1(self):
#         print("Name", self.n)
#         print("Age", self.r)
    
# p = python()
# print(p.m1())

# class Human:
#     def __init__(self, name, pow):
#         self.name = name
#         self.pow = pow

#     def show(self):
#         print(f"Human Name: {self.name}, age: {self.pow}")

# a = Human("Alpha", 30)
# b = Human("Beta", 35)
# a.show()
# b.show()

# class A:
#     def __init__(self):
#         self.d = 20
        
#     def m1(self):
#         self.a = 30

# a = A()
# a.b = 40
# a.m1()
# print(a.__dict__)

# class A:
#     p = 50
#     def n1(self):
#         self.p = 100

# a1 = A()
# a1.n1()
# print(A.p)
# print(a1.p)

# class A:
#     p = 50
#     def __init__(self):
#         self.q = 80

# a1 = A()
# a2 = A()
# print("a1: ",a1.p, a1.q)
# print("a2: ",a2.p, a2.q)
# a1.p = 150
# a1.q = 250
# print("a1: ",a1.p, a1.q)
# print("a2: ",a2.p, a2.q)
# A.p = 350
# a1.q = 450
# print("a1: ",a1.p, a1.q)
# print("a2: ",a2.p, a2.q)

# class A:
#     p = 50
#     def __init__(self):
#         self.q = 80
#     @classmethod
#     def n1(cls):
#         cls.p = 150
#         cls.q = 250
# a1 = A()
# a2 = A()
# a1.n1()
# print(A.p, A.q)
# print(a1.p, a1.q)
# print(a2.p, a2.q)

# class emp:
#     def __init__(self, emp_n, emp_sal):
#         self.emp_n = emp_n
#         self.emp_sal = emp_sal

#     def m1(self):
#         print(self.emp_n)
#         print("Salary: ", self.emp_sal)
#     def m2(self):
#         if self.emp_sal >= 80000:
#             print("Grade Pay 8")  
#         elif self.emp_sal >= 70000:
#             print("Grade Pay 7")        
#         elif self.emp_sal >= 60000:
#             print("Grade Pay 6")
#         else:
#             print("Consolidated")

# n = int(input("Enter Number of Emp: "))
# for i in range(n):
#     emp_n = input("Enter Name: ")  
#     emp_sal = int(input("Enter Salary: "))
#     e = emp(emp_n, emp_sal)
#     e.m1()
#     e.m2()
#     print()

# class Book:
#     auth = 4
#     @classmethod
#     def wri(cls, name):
#         print("{} is writing book  with {} aithors".format(name, cls.auth))
    
# b = Book()
# b.wri('Hassan')
 
# class A:
#     c = 0
#     def __init__(self):
#         A.c = A.c+1
#     @classmethod
#     def m(cls):
#         print('Number of Objects created:', cls.c)
# a1 = A()
# a2 = A()
# a3 = A()
# a4 = A()
# A.m()

# class hassan:
#     @staticmethod
#     def add(a,b):
#         print("addition", a+b)
#     @staticmethod
#     def sub(a,b):
#         print("Subtraction", a-b)
#     @staticmethod
#     def mul(a,b):
#         print("multipilication", a*b)
#     @staticmethod
#     def avg(a,b):
#         print("Average", (a+b)/2)

# hassan.add(2,4)
# hassan.sub(2,4)
# hassan.mul(2,4)
# hassan.avg(2,4)

# class Emp:
#     def setemp_n(self, emp_n):
#         self.emp_n = emp_n
#     def getemp_n(self):
#         return self.emp_n
#     def setemp_sal(self, emp_sal):
#         self.emp_sal = emp_sal
#     def getemp_sal(self):
#         return self.emp_sal
# n1 = int(input("Enter Number of Emp: "))
# for i in range(n1):
#    e = Emp()
#    emp_n = input("Enter Name: ")
#    e.setemp_n(emp_n)
#    emp_sal = int(input("Enter Salary: "))
#    e.setemp_sal(emp_sal)
#    print(e.getemp_n())
#    print('Salar: ', e.getemp_sal())
#    print()     


# class Book:
#     def __init__(self,name,pages,price):
#         self.name = name
#         self.pages = pages
#         self.price = price
#     def m(self):
#         print("Book Name: ",self.name)
#         print("Book Pages: ",self.pages)
#         print("Book Price: ",self.price)

# class update:
#     def m1(b):
#         b.price = b.price + 6000
#         b.m()

# b1 = Book("python", 350, 40000)
# update.m1(b1)


