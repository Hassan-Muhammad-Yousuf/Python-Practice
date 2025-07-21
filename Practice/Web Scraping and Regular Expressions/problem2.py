import re
f1 = open("abc.txt","w")
f1.write("""Apple is a fruit. 
    This line does not have the letter.
    A new project starts today.
    banana is yellow.
    ALWAYS aim high.
    no uppercase here.
    Amazing things happen every day.
    """)
f1.close()

f2 = open("abc.txt","r")
for i in f2:
    if "A" in i:
        print(i.strip())
    else:
        None
f2.close()