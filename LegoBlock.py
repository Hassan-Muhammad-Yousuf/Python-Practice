#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'legoBlocks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#
Mod = 10**9+7

def legoBlocks(n, m):
    rw = [0] * (m+1)
    rw[0] = 1
   
    for i in range(1, m+1):
        rw[i] = rw[i-1]
        if i > 1:
            rw[i] = (rw[i] + rw[i-2]) % Mod
        if i > 2:
            rw[i] = (rw[i] + rw[i-3]) % Mod 
        if i > 3:
            rw[i] = (rw[i] + rw[i-4]) % Mod
            
    tw = [pow(rw[i], n, Mod) for i in range(m+1)]
    
    vw = [0] * (m+1)
    for width in range(1, m+1):
        vw[width] = tw[width]
        for j in range(1, width):
            vw[width]= (vw[width] - (vw[j] * tw[width - j])) % Mod
    return vw[m]

if __name__ == '__main__':
    t = int(input().strip())

    results = []
    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])
        m = int(first_multiple_input[1])

        result = legoBlocks(n, m)
        results.append(result)

    for result in results:
        print(result)
