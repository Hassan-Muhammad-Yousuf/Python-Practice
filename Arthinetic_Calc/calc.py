def addition():
    print("Addition")
    n = float(input("Enter the Number: "))
    t = 0
    ans = 0
    while n != 0:
        ans = ans + n
        t+=1
        n = float(input("Enter another number (0 to calculate): "))
    return [ans, t]
    
def subtration():
    print("Subtraction")
    n = float(input("Enter the Number: "))
    t = 0
    ans = 0
    while n != 0:
        ans = ans - n
        t+=1
        n = float(input("Enter another Number (o to calculate): "))
    return [ans,t]

def multiplication():
    print("Multipilication")
    n = float(input("Enter the Number: "))   
    t = 0
    ans = 1
    while n != 0:
        ans = ans * n
        t += 1
        n = float(input("Enter another Number (o to calculate): "))
    return [ans,t] 

def average():
    an = []
    an = addition()
    t = an[1]
    a = an[0]
    ans = a / t
    return [ans,t]

while True:
    list = []
    print("Enter 'a' for Addition ")
    print("Enter 's' for Substraction")
    print("Enter 'm' for Multipilication ")
    print("Enter 'v' for Average ")
    print("Enter 'q' for quit ")
    c = input(" ")
    if c != 'q':
        if c == 'a':
            list =  addition()
            print("Ans = ", list[0], " total inputs ", list[1])
        elif c == 's':
            list = subtration()
            print("Ans = ", list[0]," total inputs ", list[1])
        elif c == 'm':
            list = multiplication()
            print("Ans = ", list[0]," total inputs ", list[1])
        elif c == 'v':
            list = average()
            print("Ans = ", list[0]," total inputs ", list[1])
        else:
            print("Sorry, Invalid Char")
    else:
        break
