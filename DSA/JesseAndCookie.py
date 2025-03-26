#!/bin/python3

import math
import os
import random
import re
import sys
from heapq import heapify, heappop, heappush

#
# Complete the 'cookies' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY A
#

def cookies(k, A):
    heapify(A)
    r = 0
    
    while True:
        x = heappop(A)
        
        if x >= k:
            return r
        if A:
            y = heappop(A)
            s = x + 2 * y
            heappush(A, s)
            r += 1
        
        
        else:
            return -1
        
    
    

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])
    A = list(map(int, input().rstrip().split()))

    # Call the function and print the result
    result = cookies(k, A)
    print(result)
