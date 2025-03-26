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



