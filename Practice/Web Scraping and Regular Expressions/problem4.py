import re
f1 = open("xz.txt","w")
f1.write("""The quick brown fox jumps over the lazy dog.
There is a cat on the roof.
This line does not have that word.
Another line without it.
In the middle of the night, the stars shine bright.
Theater is an art form.
Gather all the information before the meeting.
""")
f1.close()

f2 = open("xz.txt","r")

for i in f2:
    u =  re.findall(r"\bthe\b",i,re.I)
    if len(u) >= 1:
        print(i.strip())
