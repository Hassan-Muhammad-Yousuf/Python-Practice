import re

s = input("Enter Number: ")
m = re.fullmatch(r"[6-9][0-9]{9}",s)

if m != None:
    print("Valid")
else:
    print("InValid")