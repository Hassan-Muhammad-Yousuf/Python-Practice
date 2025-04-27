# print("Frist-1")
# print(10/0)
# print("Second-2")

# print("Frist-1")
# try:
#     print(10/0)
# except ZeroDivisionError as z:
#     print("Exception:",z)

# print("Second-2")

# try:
#     a = int(input("Enter Var-1: "))
#     b = int(input("Enter Var-2: "))
#     print(a/b)
# except ZeroDivisionError as z:
#     print("Exception 1", z)
# except ArithmeticError as a:
#     print("Exception 2", a)
# except ValueError as e:
#     print("Exception 3",e)

# try:
#     a = int(input("Enter Var-1: "))
#     b = int(input("Enter Var-1: "))
#     print(a/b)
# except (ZeroDivisionError, ValueError) as msg:
#     print("Invalid: ", msg)

# try:
#     a = int(input("Enter Var-1: "))
#     b = int(input("Enter Var-1: "))
#     print(a/b)
# except Exception as e:
#     print("Invalid: ", e)

# try:
#     print("try")
#     print(10/0)
# except ZeroDivisionError as e:
#     print("error", e)
# finally:
#     print("pass")

# try:
#     print("try")
#     print(10/0)
# except NameError as e:
#     print("error", e)
# finally:
#     print("pass")

# try:
#     print("a: No error")
#     print(10/0)  # <-- Error at b
# except:
#     print("d: Handling error but new error occurs")
#     print(10/0)  # <-- New error at d
# finally:
#     print("e: Always executes")
#     print("f: Also always executes")  # Depends if e crashes


# try:
#     print("outer try block")
#     # print(20/0)
#     try:
#         print("inner try block")
#         print(10/0)
#     except ZeroDivisionError:
#         print("Inner Except Block")
#     finally:
#         print("Inner finally block")
# except:
#     print("outer except block")
# finally:
#     print("outer finally block")