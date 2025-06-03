
# def rev(a):
#     char = list(a)

#     left = 0
#     right = len(char) - 1
#     while left < right:
#         char[left],char[right] = char[right],char[left]

#         left += 1
#         right -= 1
#     return ''.join(char)
# print(rev('leetcode'))
        
def rev2(text):
    if not text or not isinstance(text, str) or len(text) < 2:
        return "Validation error" 
    
    backward = []
    total = len(text) - 1
    for i in range(total , -1, -1):
        backward.append(text[i])
    print(backward)
    return ''.join(backward)
print(rev2('Hi Hassan'))
