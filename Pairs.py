#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'pairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def pairs(k, arr):
    n = set(arr)
    c = 0
    
    for i in arr:
        if i + k in n: 
            c += 1
        if i - k in n:
            c += 1
        n.remove(i)
    return c
if __name__ == '__main__':
    first_multiple_input = input("Enter n and k: ").rstrip().split()

    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])

    arr = list(map(int, input("Enter the array elements: ").rstrip().split()))

    result = pairs(k, arr)

    print("Number of pairs:", result)
