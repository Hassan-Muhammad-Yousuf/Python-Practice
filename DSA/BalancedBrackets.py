#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isBalanced(s):
    stack = []
    b = {'{':'}','(':')','[':']'}
    c = {'}':'{',')':'(',']':'['}
    
    for char in s:
        if char in b:
            stack.append(char)
            
        elif char in c:
            if not stack or c[char] != stack.pop():
                return "NO"
                
        else:
            return "NO"
            
    return "YES" if not stack else "NO"
if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        s = input().strip()
        result = isBalanced(s)
        print(result)