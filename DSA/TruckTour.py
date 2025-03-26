#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'truckTour' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY petrolpumps as parameter.
#

def truckTour(petrolpumps):
    s = pit = 0
    p = len(petrolpumps)
    a,d = zip(*petrolpumps)
    for i in range(p):
        pit += a[i] - d[i]
        
        if pit < 0:
            s = i + 1
            pit = 0
            
    return s

if __name__ == '__main__':
    t = int(input().strip())  # Read the number of test cases

    for _ in range(t):
        n = int(input().strip())  # Read the number of petrol pumps
        petrolpumps = [list(map(int, input().rstrip().split())) for _ in range(n)]
        result = truckTour(petrolpumps)
        print(result)  # Print the result to the console
