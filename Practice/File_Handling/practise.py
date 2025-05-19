# f = open("test.txt",'w')
# print("File Name: ",f.name)
# print("File Mode: ",f.mode)
# print("File Readable: ",f.readable())
# print("File Writeable: ",f.writable())
# print("File close: ",f.closed)
# f.close()
# print("File Closed", f.closed)

# f = open("test.txt","w")
# f.write("Hassan\n")
# f.write("Muhammad\n")
# f.write("Yousuf\n")
# print("Sucessfully write a Data")
# f.close()

# f = open("test.txt","w")
# l = ["Hassan\n","Ali\n","Mahin\n","Vetschau"]
# f.writelines(l)
# print("Sucessfully Written Data")
# f.close()

# f = open("test.txt", "r")
# d = f.read()
# print(d)
# f.close()

# f = open("test.txt", "r")
# l1 = f.readline()
# print(l1,end='')
# l2 = f.readline()
# print(l2,end='')
# l3 = f.readline()
# print(l3,end='')
# f.close()

# f = open("test.txt", "r")
# l = f.readlines()
# for i in l:
#     print(i, end='')
# f.close()

# with open("test.txt", "w") as f:
#     f.write("GISMA\n")
#     f.write("Business\n")
#     f.write("School\n")
#     print("File Closed", f.closed)
# print("File Closed", f.closed)

# f = open("test.txt", "r")
# print(f.tell())
# print(f.read(2))
# print(f.tell())
# print(f.read(3))
# print(f.tell())

# d = "Hassan Muhammad Yousuf"
# f = open("test.txt","w")
# f.write(d)
# with open("test.txt",'r+') as f:
#     t = f.read()
#     print(t)
#     print("Current Cursor Position: ", f.tell())
#     print("After Change the Seek() Position: ")
#     f.seek(7)
#     print("Current Cursor Position: ", f.tell())
#     f.write("| A good being")
#     f.truncate()
#     f.seek(0)
#     t = f.read()
#     print(t)

# import os, sys
# fn = input("Enter File Name: ")
# if os.path.isfile(fn):
#     print("File Here: ", fn)
#     f = open(fn, "r")
# else:
#     print("File Doesnot exist: ", fn)
#     sys.exit(0)
#     print("File Data: ")
# d = f.read()
# print(d)


# import os, sys
# fn = input("Enter File Name: ")
# if os.path.isfile(fn):
#     print("File Here: ", fn)
#     f = open(fn, "r")
# else:
#     print("File Doesnot exist: ", fn)
#     sys.exit(0)
#     print("File Data: ")
# lc = wc = cc = 0
# for i in f:
#     lc = lc + 1
#     cc = cc + len(i)
#     w = i.split()
#     wc = wc+len(w)
# print("Number of Lines: ",lc)
# print("Number of Word Counts: ",wc)
# print("Number of Character Counts: ",cc)


# f1 = open("logo (1).png","rb")
# f2 = open("newpic.jpg","wb")
# bytes = f1.read()
# f2.write(bytes)
# print("New Image with New name: newpic.jpg")

# import csv
# with open("emp.csv", "w", newline='')as f:
#     w = csv.writer(f)
#     w.writerow(["ENO", "ENAME", "ESAL", "EADDR"])
#     n = int(input("Enter Number of Employees: "))
#     for i in range(n):
#         eno = input("Enter Employee Number: ")
#         ename = input("Enter Employee Name: ")
#         esal = input("Enter Employee Salary: ")
#         eadd = input("Enter Employee address: ")
#         w.writerow([eno,ename,esal,eadd])
# print("Employee Data Written into CSV file Sucessfully")

# import csv
# f = open("emp.csv",'r')
# r = csv.reader(f)
# d = list(r)
# print(d)
# for i in d:
#     for j in i:
#         print(j,"\t",end='')
#     print()