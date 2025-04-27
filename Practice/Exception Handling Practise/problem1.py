try:
    with open('pr.txt','w') as file:
        file.write("Hello World")
        file.close()
except IOError:
    print("Error While Writing")
finally:
    print("Operation Complete")

try:
    with open('pr.txt','r') as file:
        c = file.read()
        print(c)
except IOError:
    print("Error While Writing")
finally:
    print("Operation Complete")