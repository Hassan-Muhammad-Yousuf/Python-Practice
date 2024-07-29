#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gridChallenge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY grid as parameter.
#

def gridChallenge(grid):
    sg = [sorted(row) for row in grid]
    
    nr = len(sg)
    nc = len(sg[0])
    for col in range(nc):
        for r in range(1, nr):
            if sg[r][col] < sg[r-1][col]:
                return "NO"
    return "YES"
if __name__ == '__main__':
    # Read the number of test cases
    t = int(input().strip())
    
    # Process each test case
    for _ in range(t):
        n = int(input().strip())  # Read the size of the grid (number of rows)
        
        grid = []
        for _ in range(n):
            grid_item = input().strip()  # Read each row of the grid
            grid.append(grid_item)
        
        # Get the result for the current grid and print it
        result = gridChallenge(grid)
        print(result)
