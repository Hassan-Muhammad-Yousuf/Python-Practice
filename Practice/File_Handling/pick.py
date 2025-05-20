import emp,pickle

f = open("emp1.dat","wb")
n = int(input("Enter Number of Employees: "))
for i in range(n):
    eno = int(input("Enter Employee Number: "))
    ename = input("Enter Employee Name: ")
    esal = float(input("Enter Emp Sal: "))
    eaddr = input("Enter Emp Address: ")
e = emp.Emp(eno,ename,esal,eaddr)
pickle.dump(e,f)
print("Emp obj Pickeled Sucessfully")