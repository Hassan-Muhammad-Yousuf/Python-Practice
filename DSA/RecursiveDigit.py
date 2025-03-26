#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

def superDigit(n, k):
    ds= sum(int(i)for i in n)
    
    p = ds * k
    while p >= 10:
        p = sum(int(i) for i in str(p))
    return p
      

if __name__ == '__main__':
    # Read input values
    first_multiple_input = input().strip().split()
    n = first_multiple_input[0]
    k = int(first_multiple_input[1])
    
    # Compute result
    result = superDigit(n, k)
    
    # Print the result
    print(result)
    

