# class External:
#     def __init__(self):
#         print("Outer Class")
    
#     class Inner:
#         def __init__(self):
#             print("Inner Class")
#         def m(self):
#             print("Inner Class Method")

# obj = External()
# In = obj.Inner()
# In.m()
# obj = External().Inner()
# obj.m()

# class Scientist:
#     def __init__(self):
#         self.name = "Dr.Kalam"
#         self.info = self.Info()
#     def m(self):
#         print('Name', self.name)
    
#     class Info:
#         def __init__(self):
#             self.height = 5.7
#             self.weight = 70
#             self.color = "Dark"
#         def m(self):
#             print('Height: {} Weight: {} Color: {}'.format(self.height, self.weight, self.color))
# s = Scientist()
# s.m()
# x = s.info
# x.m()

# class comapny:
#     def __init__(self):
#         self.name = "Hassan"
#         self.doe = self.DOE()
#         self.type = self.Type()
#     def m(self):
#         print(self.name)
#     class DOE:
#         def m1(self):
#             print("m1 method")
#     class Type:
#         def m2(self):
#             print("m2 method")

# c = comapny()
# c.m()
# c.doe.m1()
# c.type.m2()

# import time
# class A:
#     def __init__(self):
#         print("Constructor")
#     def __del__(self):
#         print("Destructor")

# l = [A(), A()]
# del l
# time.sleep(10)
# print("End")

# class parent:
#     def __init__(self):
#         self._a = 2

# class child(parent):
#     def __init__(self):
#         parent.__init__(self)
#         print("Calling protected member of parent class: ")
#         print(self._a)
# c = child()
# p = parent()
# print(p.a)

# # Class P defines some data and behavior
# class P:
#     # Class variable shared by all instances of class P
#     x = 15

#     # Constructor method, runs when a new object is created
#     def __init__(self):
#         # Instance variable unique to each object
#         self.y = 25

#     # A method that prints a message
#     def method1(self):
#         print("P Class Data")

# # Class Q demonstrates composition: it uses an object of class P
# class Q:
#     # Constructor method of class Q
#     def __init__(self):
#         # Creating an object of class P and storing it as an attribute
#         self.p = P()

#     # Method to access data and methods from the composed P object
#     def method2(self):
#         # Accessing class variable x from P through the P object
#         print(self.p.x)
#         # Accessing instance variable y from P
#         print(self.p.y)
#         # Calling a method from class P
#         self.p.method1()

# # Creating an object of class Q
# q = Q()

# # Calling method2 which internally accesses data and behavior from class P
# q.method2()

# # Define class P to store basic person attributes
# class P:
#     def __init__(self, name, eye, color):
#         # Initialize name, eye color, and skin color
#         self.name = name
#         self.eye = eye
#         self.color = color

#     def m1(self):
#         # Display the attributes of the person
#         print("Name: {} Eye: {} Color: {}".format(self.name, self.eye, self.color))


# # Define class C that uses a P object (composition)
# class C:
#     def __init__(self, cname, ear, head):
#         # Initialize class C with its own name, number of ears, and a P class object
#         self.cname = cname
#         self.ear = ear
#         self.head = head  # 'head' is expected to be an object of class P

#     def m2(self):
#         # Display attributes of class C
#         print("Name:", self.cname)
#         print("Ear:", self.ear)
#         print("P Class Information: ")
#         self.head.m1()  # Call m1() method of the P class through the 'head' object


# # Create an object of class P with name, eye color, and skin color
# p = P("Hassan", "Blue", "Fair")

# # Create an object of class C with its own name, number of ears, and pass the P object
# c = C("john", 2, p)

# # Call method m2 of class C to print all related info
# c.m2()

# # Define class AB
# class AB:
#     p = 10  # Class variable (shared among all instances of AB)

#     def __init__(self):
#         self.q = 22  # Instance variable (unique to each object)

#     def method1(self):
#         print("method-1")  # Prints a message when called


# # Define class CD
# class CD:
#     r = 30  # Class variable (shared among all instances of CD)

#     def __init__(self):
#         self.s = 40  # Instance variable (unique to each CD object)

#     def method2(self):
#         print("method-2")  # Prints a message when called

#     def method3(self):
#         # Create an instance of class AB
#         ab = AB()

#         # Access class variable from AB using object
#         print(ab.p)  # Prints 10

#         # Access instance variable from AB object
#         print(ab.q)  # Prints 22

#         # Call method1 of AB
#         ab.method1()  # Prints "method-1"

#         # Access class variable from CD
#         print(CD.r)  # Prints 30

#         # Access instance variable from current CD object
#         print(self.s)  # Prints 40

#         # Call method2 from current CD object
#         self.method2()  # Prints "method-2"

#         # Final print statement
#         print("method - 3")


# # Create an instance of class CD
# cd = CD()

# # Call method3 using CD object
# cd.method3()

# class GOD:
#     p = 10
#     def __init__(self):
#         self.q = 10
#     def method1(self):
#         print("Instance Method - 1")
#     @classmethod
#     def method2(self):
#         print("Instance Method - 2")
#     @staticmethod    
#     def method3():
#         print("Instance Method - 3")

# class Moster(GOD):
#     pass

# m = Moster()
# print(m.p)
# print(m.q)
# m.method1()
# m.method2()
# m.method3()

# class computer():
#     def __init__(self, gen, name):
#         self.name = name
#         self.gen = gen
#     def m1(self):
#         print("method m1")
# class Mobile(computer):
#     def __init__(self, gen, name, var, price):
#         super().__init__(gen, name)
#         self.var = var
#         self.price = price
#     def m2(self):
#         print("method m2")
#     def m3(self):
#         print("Name: ",self.name)
#         print("Gen: ",self.gen)
#         print("Ver: ",self.var)
#         print("Price: ",self.price)

# m = Mobile(5, "Apple", 12.0, 100000)
# m.m1()
# m.m2()
# m.m3()

# class Man:
#     def __init__(self,n,h,c):
#         self.n = n
#         self.h = h
#         self.c = c
#     def m1(self):
#         print("Name: {} Height: {} Color: {}".format(self.n,self.h,self.c))

# class Woman:
#     def __init__(self,n,s):
#         self.n = n
#         self.s = s
#     def m2(self):
#         print("Method - 2")

# class Kid(Woman):
#     def __init__(self, n, s, g, a):
#         super().__init__(n, s)
#         self.g = g
#         self.a = a
#     def m3(self):
#         print("Method - 3")
#     def m4(self):
#         print("Name: ", self.n)
#         print("Status: ", self.s)
#         print("Gender: ", self.g)

#         print("Man Class info:")
#         self.a.m1()

# m = Man("Hassan", "6ft", "Brown")
# k = Kid("Mahin", "divorced", "non-binary", m)
# k.m2()
# k.m3()
# k.m4()

# class Faculty:
#     def __init__(self, name, dept):
#         self.name = name
#         self.dept = dept

# class Student(Faculty):
#     def __init__(self, name, dept, sub):
#         super().__init__(name, dept)
#         self.sub = sub
#     def __str__(self):
#         return 'Name: {}\nDepartment: {}\nSubject: {}'.format(self.name,self.dept,self.sub)
    
# s = Student('Hassan', 'SE', 'Python')

# print(s)

# class A(B):
#     pass
# class B(A):
#     pass

# class A: pass
# class B(A): pass
# class C(A): pass
# class D(B, C): pass
# print(A.mro())
# print(B.mro())
# print(C.mro())
# print(D.mro())

# class Human:
#     def __init__(self,name,gender):
#         self.name = name
#         self.gender = gender
#     def method(self):
#         print("Name :",self.name)
#         print("Gender :",self.gender)
# class Author(Human):
#     def __init__(self, name, gender,title, price):
#         super().__init__(name, gender)
#         self.title = title
#         self.price = price
#     def method(self):
#         super().method()
#         print("title :",self.title)
#         print("price :",self.price)

# a = Author("Hassan","Male","Book",20000)
# a.method()

# class Parent:
#     var1 = 18
#     def __init__(self):
#         self.b=10
#     def m1(self):
#         print("m1")
#     @classmethod
#     def m2(cls):
#         print("class m2")
#     @staticmethod
#     def m3():
#         print("Static Method")
# class Child(Parent):
#     var1 = 50
#     def __init__(self):
#         self.var2 = 100
#         super().__init__()
#         print(super().var1)
#         super().m1()
#         super().m2()
#         super().m3()
# c = Child()

# class One:
#     var1 = 12
#     def __init__(self):
#         self.var2 = 28
# class Two(One):
#     def m(self):
#         print(super().var1)
#         print(self.var2)
# t = Two()
# t.m()

# class Parent:
#     def __init__(self):
#         print("Constructor")
#     def m1(self):
#         print("Instance Method")
#     @classmethod
#     def m2(cls):
#         print("Class Method")
#     @staticmethod
#     def m3():
#         print("Static Method")

# class child(Parent):
#     def __init__(self):
#         super().__init__()
#         super().m1()
#         super().m2()
#         super().m3()
#     def m1(self):
#         super().__init__()
#         super().m1()
#         super().m2()
#         super().m3()
# c = child()
# c.m1()

# class Parent:
#     def __init__(self):
#         print("Constructor")
#     def m1(self):
#         print("Instance Method")
#     @classmethod
#     def m2(cls):
#         print("Class Method")
#     @staticmethod
#     def m3():
#         print("Static Method")
# class Child(Parent):
#     @classmethod
#     def m(cls):
#         # super(Child,cls).__init__(cls)
#         # super(Child,cls).m1(cls)
#         i = cls()
#         i.m1()
#         super().m2()
#         super().m3()
# Child.m()

# class Parent:
#     def __init__(self):
#         print("Constructor")
#     def m1(self):
#         print("Instance Method")
#     @classmethod
#     def m2(cls):
#         print("Class Method")
#     @staticmethod
#     def m3():
#         print("Static Method")
# class Child(Parent):
#     @staticmethod
#     def m():
#         # super(Child, Child).m1() #invalid
#         i = Parent()
#         i.m1()
#         super(Child, Child).m2()
#         super(Child, Child).m3()   
# Child.m()

# class Man:
#     def m1(self):
#         print("Man")
# class Woman:
#     def m1(self):
#         print("Woman")
# class Boy:
#     def m1(self):
#         print("Boy")
# class Kid:
#     def m1(self):
#         print("Kid")
# def fun(x):
#     x.m1()
# l = [Man(),Woman(),Boy(),Kid()]
# for x in l:
#     fun(x)

# class Man:
#     def m1(self):
#         print("Man")
# class Woman:
#     def m2(self):
#         print("Woman")

# def fun(x):
#     x.m1()

# m = Man()
# fun(m)
# w = Woman()
# fun(w)


# class Man:
#     def m1(self):
#         print("Man")
# class Woman:
#     def m2(self):
#         print("Woman")
# class Boy:
#     def m3(self):
#         print("Boy")

# def fun(x):
#     if hasattr(x, 'm1'):
#         x.m1()
#     elif hasattr(x, 'm2'):
#         x.m2()
# m = Man()
# fun(m)
# w= Woman()
# fun(w)
# b = Boy()
# fun(b)

# class Boy:
#     def __init__(self,toys):
#         self.toys = toys
#     def __add__(self,var):
#         return self.toys+var.toys
# b1 = Boy(40)
# b2 = Boy(50)
# print(b1 + b2)

# class Worker:
#     def __init__(self,name,sal):
#         self.name = name
#         self.sal = sal
#     def __gt__(self,var):
#         return self.sal>var.sal
#     def __le__(self,var):
#         return self.sal<=var.sal
# w1 = Worker("A",10000)
# w2 = Worker("B",20000)
# print(w1>w2)
# print(w1<w2)
# print(w1<=w2)
# print(w1>=w2)

# class A:
#     def __init__(self,sal):
#         self.sal = sal
#     def __mul__(self,var):
#         return self.sal*var.days
# class B:
#     def __init__(self,days):
#         self.days = days
# a = A(500)
# b = B(27)
# print("Total Amount : ", a*b)

# class A:
#     def m(self):
#         print("no args")
#     def m(self,x):
#         print("1 args")
#     def m(self,x,y):
#         print("2 args")

# a = A()
# # a.m()
# # a.m(4)
# a.m(4,5)

# class Arth:
#     def sum(self, x = None, y = None, z = None):
#         if x!= None and y!= None and z!= None:
#             print('3 args:',x+y+z)
#         elif x!= None and y!= None:
#             print('2 args:',x+y)
#         else:
#             print('default')
# a = Arth()
# a.sum(3,4)
# a.sum(3,4,5)
# a.sum(5)

# class Arth:
#     def sum(self, *x):
#         s = 0
#         for i in x:
#             s = s + i
#         print('sum', s)
# a = Arth()
# a.sum()
# a.sum(2,5)
# a.sum(2,3,4)
# a.sum(8)
# a.sum()

# class Arth:
#     def __init__(self):
#         print('No-Args Constr')
#     def __init__(self,x):
#         print('1-Args Constr')
#     def __init__(self,x,y):
#         print('2-Args Constr')

# # a = Arth()
# # a = Arth(4)
# a = Arth(3,4)

# class Arth:
#     # def __init__(self, x = None,y = None,z = None):
#     def __init__(self,*x):
#         print('Constr')

# a = Arth()
# a = Arth(1)
# a = Arth(2,3)
# a = Arth(2,3,4)

# class A:
#     def m1(self):
#         print(" A Class m1")
#     def m2(self):
#         print(" A Class m2")
# class B(A):
#     def m2(self):
#         print(" B Class m2")
# a = B()
# a.m1() 
# a.m2() 

# class A:
#     def m1(self):
#         print(" A Class m1")
#     def m2(self):
#         print(" A Class m2")
# class B(A):
#     def m2(self):
#         super().m2()
#         print(" B Class m2")
# class C(B):
#     def m2(self):
#         super().m2()
#         print(" C Class m2")
# a = C()
# a.m1() 
# a.m2() 

# class Parent:
#     def __init__(self,name):
#         self.name = name

# class Child(Parent):
#     def __init__(self, name,dept):
#         super().__init__(name)
#         self.dept = dept
#     def m(self):
#         print('Name :',self.name)
#         print('Department  :',self.dept)

# c1 = Child("Hassan", "Beng")
# c1.m()
# c2 = Child("Mahin", "BSC")
# c2.m()

from abc import *
# class abst(ABC):
#     pass
# a = abst()

# class abst:
#     @abstractmethod
#     def m(self):
#         print('Abstract')
# a = abst()
# a.m()

# class A(ABC):
#     @abstractmethod
#     def m(self):
#         pass
# class B(A): pass

# v = B()

# class A:
#     @abstractmethod
#     def m(self):
#         self
# class B(A):
#     def m(self):
#         return 'B Class m'
# class C(A):
#     def m(self):
#         return 'C Class m'

# b = B()
# print(b.m())
# c = C()
# print(c.m())