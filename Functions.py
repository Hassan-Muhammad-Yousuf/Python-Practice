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

