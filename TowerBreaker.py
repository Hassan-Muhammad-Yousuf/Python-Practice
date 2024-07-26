#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'towerBreakers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#

def towerBreakers(n, m):
    if m == 1 or n % 2 == 0:
        return 2
    else:
        return 1
         

if __name__ == '__main__':
    t = int(input("Enter the number of test cases: "))
    for _ in range(t):
        n, m = map(int, input().strip().split())
        result = towerBreakers(n, m)
        print(result)
