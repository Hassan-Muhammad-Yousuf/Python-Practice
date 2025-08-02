# Brute Force
def firstRecurringCharacter(input):
    min_s = len(input)
    f_r = None
    
    for i in range(len(input)): 
        for j in range(i + 1, len(input)):
            if input[i] == input[j]:
                if j < min_s:
                    min_s = j
                    f_r = input[i]
                   
    return f_r

call = firstRecurringCharacter([2, 5, 5, 1, 2, 3, 5, 1, 2, 4])
print(call)

#Hash Table
def firstRecurringCharacter2(input):
    map = {}
    for i in range(len(input)):
        if input[i] in map:
            return input[i]
        else:
            map[input[i]] = i
    return None

call = firstRecurringCharacter2([2, 5, 5, 1, 2, 3, 5, 1, 2, 4])
print(call)