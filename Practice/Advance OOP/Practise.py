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