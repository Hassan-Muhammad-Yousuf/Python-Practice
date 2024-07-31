q = int(input("Enter number of queries: ").strip())

s1 = []
s2 = []

for i in range(q):
    t = list(input(f"Enter query {i+1}: ").strip().split())
    
    if t[0] == '1':
        s1.append(t[1])
        print(f"Enqueued {t[1]}")

    elif t[0] == '2':
        if not s2:
            while s1:
                s2.append(s1.pop())
        if s2:
            dequeued = s2.pop()
            print(f"Dequeued {dequeued}")
        else:
            print("Queue is empty. Cannot dequeue.")

    elif t[0] == '3':
        if not s2:
            while s1:
                s2.append(s1.pop())
        if s2:
            print(f"Front of the queue: {s2[-1]}")
        else:
            print("Queue is empty. Nothing to show.")

# Print the remaining values in the queue
print("Remaining values in the queue:")
if not s2:
    while s1:
        s2.append(s1.pop())

if s2:
    while s2:
        print(s2.pop(), end=' ')
    print()
else:
    print("Queue is empty.")
