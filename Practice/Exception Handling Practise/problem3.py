try: 
    a = int(input("Enter the Number: "))
    if a >= 0:
        print("Number: ",a)
    else:
        raise ValueError("Negative Numbers are Not allowed")
except ValueError as e:
    print("Error: ", e)