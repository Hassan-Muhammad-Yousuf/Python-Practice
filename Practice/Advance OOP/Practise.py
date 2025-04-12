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