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