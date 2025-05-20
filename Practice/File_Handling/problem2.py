f1 = input("Enter 1st File name: ")
f2 = input("Enter 2nd File name: ")

with open(f1, 'r') as file1, open(f2, 'r') as file2:
    l_n = 1
    equal = True
    while True:
       l1 = file1.readline()
       l2 = file2.readline()
       if not l1 and not l2:
            break
       elif l1 != l2:
           print("Difference Found in line: ",l_n)
           print("File1: ",l1.strip())
           print("File2: ",l2.strip())
           equal = False
           
       l_n += 1
    if equal:
        print("identical")
