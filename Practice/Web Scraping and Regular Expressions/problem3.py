import re
f1 = open("xy.txt","w")
f1.write("""Call me at 9312456789.
My backup number is 7524681350.
The code 1357924680 is a test.
Random digits: 1234567890.
No pairs here: 2468024680.
""")
f1.close()

f2 = open("xy.txt","r")
t = f2.read()


u = re.findall(r"[13579][02468]",t)
print("Matched pair", t)

for i in f2:
    if any(pair in i for pair in u):
        print(i.strip())
        print("matched")
