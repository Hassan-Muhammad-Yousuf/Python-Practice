f1 = input("Enter File 1: ")
f2 = input("Enter File 2: ")

with open(f1, 'r') as file1, open(f2, 'r') as file2:
    d1 =  file1.readlines() 
    d2 =  file2.readlines() 

with open(f1, 'w') as file1, open(f2, 'w') as file2:
    file1.writelines(d2)
    file2.writelines(d1)

print("Content Changed sucessfully")