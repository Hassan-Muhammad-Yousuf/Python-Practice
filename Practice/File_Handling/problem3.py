with open("emp1.txt",'r') as f:
    s_count = 0
    for i in f:
        s_count += 1
f.close()
print("Number of records found", s_count)
