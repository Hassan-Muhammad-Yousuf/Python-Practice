
import math
import os
import random
import re
import sys



#
# Complete the 'findMedian' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def findMedian(arr):
    arr.sort()
    n = len(arr)
    if n % 2 == 0:
        m1 = arr[n//2]
        m2 = arr[n//2 - 1]
        m = (m1 + m2) / 2
    else:
        m = arr[n//2]
    print(str(m))
    return m

if __name__ == '__main__':
    
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = findMedian(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
