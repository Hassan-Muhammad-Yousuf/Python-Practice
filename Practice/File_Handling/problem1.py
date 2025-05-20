t_word = ['print','Print']
with open("demo.txt",'r') as f:
    for i in f:
        for j in t_word:
            if j in i:
                print(i, end='')
                break