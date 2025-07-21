# import re
# count = 0
# p = re.compile("pq")
# m = p.finditer("pqpqpqpq")
# for m1 in m:
#     count += 1
#     print(m1.start(),'-->',m1.end(),'-->',m1.group())
# print("Number of occurrences: ",count)

# import re
# count = 0

# m = re.finditer("pq","pqpqpqpq")
# for m1 in m:
#     count += 1
#     print(m1.start(),'-->',m1.end(),'-->',m1.group())
# print("Number of occurrences: ",count)

# import re
# m = re.finditer("[adk]","a5d@k8z")
# for i in m:
#     print(i.start(),"--->",i.group())

# import re
# m = re.finditer("[^adk]","a5d@k8z")
# for i in m:
#     print(i.start(),"--->",i.group())

# import re
# m = re.finditer("[d-p]","a5d@k8mz")
# for i in m:
#     print(i.start(),"--->",i.group())

# import re
# m = re.finditer("[1-8]","a5d@k8z")
# for i in m:
#     print(i.start(),"--->",i.group())

# import re
# m = re.finditer("[a-zA-Z0-9]","a5d@k8z")
# for i in m:
#     print(i.start(),"--->",i.group())

# import re
# m = re.finditer("[^a-zA-Z0-9]","a5d@k8z")
# for i in m:
#     print(i.start(),"--->",i.group())


# import re 
# m = re.finditer("\S","a5d@6k#8mz")
# for i in m:
#     print(i.start(),"---->",i.group())


# import re 
# m = re.finditer("\d","a5d@6k#8mz")
# for i in m:
#     print(i.start(),"---->",i.group())


# import re 
# m = re.finditer("\D","a5d@6k#8mz")
# for i in m:
#     print(i.start(),"---->",i.group())

# import re 
# m = re.finditer("\w","a5d@6k#8mz")
# for i in m:
#     print(i.start(),"---->",i.group())

# import re 
# m = re.finditer("\W","a5d@6k#8mz")
# for i in m:
#     print(i.start(),"---->",i.group())

# import re 
# m = re.finditer(".","a5d@6k#8mz")
# for i in m:
#     print(i.start(),"---->",i.group())

# import re 
# m = re.finditer("\s","a5d @6k# 8mz")
# for i in m:
#     print(i.start(),"---->",i.group())

# import re 
# m = re.finditer("p","pqppqqpppqq")
# for i in m:
#     print(i.start(),"---->",i.group())

# import re 
# m = re.finditer("p+","pqppqqpppqq")
# for i in m:
#     print(i.start(),"---->",i.group())

# import re 
# m = re.finditer("p*","pqppqqpppqq")
# for i in m:
#     print(i.start(),"---->",i.group())

# import re 
# m = re.finditer("p{2}","pqppqqpppqq")
# for i in m:
#     print(i.start(),"---->",i.group())

# import re 
# m = re.finditer("p{2,3}","pqppqqpppqq")
# for i in m:
#     print(i.start(),"---->",i.group())

# import re 
# s = input("Enter Pattern: ")
# m =  re.match(s,'pqrstuvw')
# if m != None:
#     print("Match Begning")
#     print("start Index: ",m.start(),"End Index",m.end())
# else:
#     print("Not Matched")

# import re 
# s = input("Enter Pattern: ")
# m =  re.fullmatch(s,'pqrstuvw')
# if m != None:
#     print("Matched")
#     # print("start Index: ",m.start(),"End Index",m.end())
# else:
#     print("Not Matched")

# import re 
# s = input("Enter Pattern: ")
# m =  re.search(s,'pqrstuvw')
# if m != None:
#     print("Match Pattern")
#     print("start Index: ",m.start(),"End Index",m.end())
# else:
#     print("Not Matched")

# import re 
# l = re.findall("[0-9]","d5s4a6s8d1a3")
# print(sorted(l))

# import re
# i = re.finditer("[a-z]","b5v9d4pz1")
# for m in i:
#     print(m.start(),"--->",m.group())

# import re
# i = re.subn("[a-z]","$","b5v9d4pz1")
# print(i)
# print("String",i[0])
# print("REplacement",i[1])

# import re 
# s = re.split(",","Hassan,Yousuf")
# print(s)
# for i in s:
#     print(i)

# import re
# l = re.split("\.","www.google.com")
# for i in l:
#     print(i)

# import re 
# s = "Mr Hassan Muhamad Yousuf"
# r = re.search("^Hassan",s)
# if r != None:
#     print("Start by Hassan")
# else:
#     print("Not Start by Hassan")

# import re 
# s = "Hassan Muhamad Yousuf"
# r = re.search("Yousuf$",s)
# if r != None:
#     print("End by Hassan")
# else:
#     print("Not End by Hassan")

# import re 
# s = "Hassan Muhamad Yousuf"
# r = re.search("yousuf$",s,re.IGNORECASE)
# if r != None:
#     print("End by Hassan")
# else:
#     print("Not End by Hassan")

# import re 
# n = input("Enter Number: ")
# m = re.fullmatch("[9-2]\d{9}",n)
# if m != None:
#     print("Valid Cell Number") 
# else:
#     print("Invalid Cell Number")

# import re
# f1 = open("abc.txt","r")
# f2 = open("xyz.txt","w")
# for l in f1:
#     l1 = re.findall("[7-9]\d{9}",l)
#     for n in l1:
#         f2.write(n+"\n")
#         print("Extracted all contact numbers")
# f1.close()
# f2.close()

import re, urllib
import urllib.request

# s = "google scholar".split()
# print(s)
# for i in s:
#     print("Search",i)
#     u = urllib.request.urlopen("http://"+i+".com")
#     t = u.read()
#     title = re.findall("<title>.*</title>",str(t),re.I)
#     print(title[0])

# u = urllib.request.urlopen("http://www.mnnit.ac.in/index.php/contact-us")
# t = u.read()
# num = re.findall("[0-9-]{7}[0-9-]+",str(t),re.I)
# for n in num:
#     print(n)

# s = input("Enter E-Mails: ")
# m = re.fullmatch("\w[a-zA-Z0-9_.]*@gmail[.]com",s)
# if m != None:
#     print("Valid")
# else:
#     print("Invalid")


# s = input("Vehical Number: ")
# m = re.fullmatch("KC[019][0-9][A-Z]{2}\d{4}",s)
# if m != None:
#     print("Valid")
# else:
#     print("InValid")