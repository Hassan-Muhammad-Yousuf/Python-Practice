import emp,pickle
f = open("emp1.dat",'rb')
print("Emp Details: ")
while True:
    try: 
        obj = pickle.load(f)
        obj.display()
    except EOFError:
        print("All employees Completed")
        break
f.close()