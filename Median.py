
import math
import os
import random
import re
import sys


def findMedian(arr):
    arr.sort()
    n = len(arr)
    if n % 2 == 0:
        # For even length, median is the average of the two middle numbers
        m1 = arr[n // 2]
        m2 = arr[n // 2 - 1]
        m = (m1 + m2) // 2  # Use integer division for exact median
    else:
        # For odd length, median is the middle number
        m = arr[n // 2]
    return m

if __name__ == '__main__':
    # Read the number of integers (not used directly in the function)
    _ = int(input().strip())
    
    # Read the list of integers
    arr = list(map(int, input().rstrip().split()))

    # Find the median
    result = findMedian(arr)

    # Print the result to the console
    print(result)