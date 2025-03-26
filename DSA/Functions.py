# def root(n):
#    print('Square',n,':',n*n)
#
# root(100)

# def add(a,b):
#    return a+b
# print(add(7,15))

# def evenodd(n):
#    if n%2 == 0:
#        print(n, 'is even')
#    else:
#        print(n, 'is odd')
# evenodd(9)

# def fact(n):
#     r = 1
#     while n>=1:
#         r = r*n
#         n = n-1
#     return r
# for i in range(1, 6):
#     print('factorial', i,  ", ", fact(i))

# def mth(a,b):
#     sum = a + b 
#     sub = a - b
#     return sum, sub
# n2,n1 = mth(3,5)
# print('Addition :',n2)
# print('Subtracton :',n1)

# def calc(a,b):
#     sum = a + b
#     sub = a - b
#     mul = a * b
#     div = a / b

#    return sum, sub, mul, div

# c = calc(2,3)
# for i in c:
#     åprint('output:', i)

# def test(*n):
#     s = 0
#     for i in n:
#         s = s + i
#     print('Addition :', s)
# test(10)
# test(10, 11)
# test(10, 11, 12)
# test(10, 11, 12, 13)

# def test(a ,*s , n):
#     print(a)
#     for i in s:
#         print(i)
#     print(n)
# test("A", 1, "B", 2 , n = 9999)

# def test(**n):
#     for i,j in n.items():
#         print(i, "=", j)
# test(a = 2, b = 4, c= 6, d = "Hassan")

# def fact(n):
#     if n == 0:
#         r = 1
#     else:
#         r = n * fact(n-1)
#     return r
# print("factorial", fact(99))

# l = lambda n:n*n
# print("Square", l(3))

# l = lambda a,b : a+b
# print("Addition", l(20,30))

# l = lambda a,b: a if a>b else b
# print("Biggest", l(20,30))

# def test(n):
#     if n%2==0:
#         return True
#     else:
#         return False
    
# l = [0,2,3,6,2,3,30]
# l1 = list(filter(test, l))
# print(l1)

# l = [0,2,4,1,5,2,3,7,4,5,7]
# l1 =  sorted(list(filter(lambda a: a % 2 == 0, l)))
# print(l1)
# l2 = list(filter(lambda a: a % 2 != 0, l))
# print(l2)

# l = [11,22,33,44]
# def test(a):
#     return 2*a
# l1 = list(map(test, l))
# print(l1)

# l = [11,22,33,44]
# l1= list(map(lambda a : a*2 ,l))
# l2= list(map(lambda a : a*a ,l))
# print(l1)
# print(l2)

# l1 = [11,22,33,44]
# l2 = [1,2,3,4]
# l3 = list(map(lambda x,y: x*y, l1,l2))
# print(l3)

# from functools import *
# l = [1,2,3,4,5]
# r =reduce(lambda a,b: a+b, l)
# print(r)


# r1 = reduce(lambda x,y: x*y, range(1,50))
# print(r1)

# def test():
#     print("test() function is started")
#     def test1():
#         print("test1() function execution")
#     print("test func() is calling test1()")
#     test1()
# test()

# def test():
#     print("test() function is started")
#     def test1():
#         print("test1() function execution")
#     print("test func() is returning test1()")
#     return test1
# l = test()
# l()
# l()
# l()
# l()

# def test(fun):
#     def wrap(n):
#         if n == 'Hassan':
#             print("This is Hassan")
#         else:
#             fun(n)
#     return wrap

# @test
# def test1(n):
#     print(n, "Welcome")

# test1("Xyz")
# test1("Zyx")
# test1("Hassan")

# def test(fun):
#     def wrap(n):
#         if n == 'Hassan':
#             print("This is Hassan")
#         else:
#             fun(n)
#     return wrap


# def test1(n):
#     print(n, "Welcome")

# m = test(test1)
# test1("Xyz")
# test1("Zyx")
# m("Hassan")

# def mul(fun):
#     def wrap(x,y):
#         print("num 1 =", x,"num 2 =",y)
#         if x== 0  or y == 0:
#             print("Answer is zero")
#         else:
#             return fun(x,y)
#     return wrap
# @mul
# def multi(x,y):
#     return x*y

# print(multi(10,20))
# print(multi(0,20))
# print(multi(10,0))

# def stdec(fun):
#     def wrap():
#         print("Student Name")
#         print("Student Subject")
#         print("Student Package")
#         fun()
#     return wrap

# def test():
#     print("Company Name")

# r = stdec(test)
# r()

# def d1(fun):
#     def wrap1():
#         f = fun()
#         return f*f
#     return wrap1
# def d2(fun):
#     def wrap1():
#         f = fun()
#         return 3*f
#     return wrap1

# @d1
# @d2
# def final():
#     return 5

# print(final())

# def m():
#     yield 'P'
#     yield 'Q'
#     yield 'R'

# n = m()
# print(type(n))
# print(next(n))
# print(next(n))
# print(next(n))

# def m(n):
#     print('num')
#     while n>0:
#         yield n
#         n = n-1
# v = m(10)
# for i in v:
#     print(i)

# def m(n):
#     n1 = 0
#     print('num')
#     while n>=n1:
#         yield n1
#         n1 = n1+1
# v = m(10)
# for i in v:
#     print(i)

# def fib():
#     x,y = 0,1
#     while True:
#         yield x
#         x,y = y, x+y
    
# for i in fib():
#     if i >=30:
#         break
#     print(i)

# def factors(n):
#     f = []
#     for i in range(1, int(n**0.5)+1):
#         if n%1 == 0:
#             f.append(i)
#             if i != n // i:
#                 f.append(n // i)
#     return sorted(f)

# num = int(input("Enter Number"))
# print("Factors of:  ", num, "is", factors(num))

# def db(n):
#     binary = ""
#     while n > 0:
#         rem = n % 2
#         binary = str(rem) + binary
#         n = n // 2
#     return binary

# num = int(input("Enter Number: "))
# print("Binary Number of:" , num, "is ", db(num))

# def gv():
#     yield 1
#     yield 2
#     yield 3
#     yield 4
#     yield 5

# gen = gv()

# for i in gen:
#     print(i)

# def ca(n1, n2 , op):
#     if op == "add":
#         r = n1 + n2
#         return r
#     elif op == "sub":
#         r = n1 - n2
#         return r
#     else: 
#         return "Invalid"
    
# num1 = int(input("Enter Number 1:"))
# num2 = int(input("Enter Number 2:"))
# oper = input("Enter operation add or sub:")

# result = ca(num1, num2, oper)
# print(result)

# n = 12
# def m(p):
#     j = n+p
#     return j

# o = m(5)
# print(o)