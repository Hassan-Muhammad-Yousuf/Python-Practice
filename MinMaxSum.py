import math
import os
import random
import re
import sys



def miniMaxSum(arr):
    arr.sort()
    
    min_sum = sum(arr[:n - 1])
    max_sum = sum(arr[-n + 1:])

    print("Min Sum ",min_sum,"Max_Sum ", max_sum)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
