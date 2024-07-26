#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'flippingMatrix' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
#

def flippingMatrix(matrix):
    
    n = len(matrix)
    ms = 0
    for i in range(n // 2):
        for j in range(n // 2):
            tl = matrix[i][j]
            tr = matrix[i][n-j-1]
            bl = matrix[n-i-1][j]
            br = matrix[n-i-1][n-j-1]
            
            ms += max(tl , tr , bl , br)
            
    return ms

if __name__ == '__main__':
    q = int(input("Enter the number of queries: ").strip())
    for q_itr in range(q):
        n = int(input("Enter the size n: ").strip())
        matrix = []
        print("Enter the matrix:")
        for _ in range(2 * n):
            matrix.append(list(map(int, input().rstrip().split())))
        result = flippingMatrix(matrix)
        print(result)