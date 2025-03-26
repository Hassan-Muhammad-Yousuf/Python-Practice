# Enter your code here. Read input from STDIN. Print output to STDOUT
s = ""
stack = []
Q = int(input())

for _ in range(Q):
    q = input().split()
    if q[0] == '1':
        s +=q[1]
        stack.append(q)
    
    elif q[0] == '2':
        k = int(q[1])
        set_del = s[-k:]
        s = s[:-k]
        stack.append([2, set_del])
    
    elif q[0] == '3':
        index = int(q[1]) - 1
        print(s[index])
        
    else:
        last = stack.pop()
        if last[0] == '1':
            val = len(last[1])
            s = s[:-val]
            
        else:
            s += last[1]
            
        
        
    
    