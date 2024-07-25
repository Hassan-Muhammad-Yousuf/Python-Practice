import math
import os
import random
import re
import sys

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a):
    r = 0
    for i in a:
        r ^= i
    return r

if __name__ == '__main__':
    # Prompt user for input
    input_string = input("Enter a list of integers separated by spaces: ")

    # Convert the input string into a list of integers
    a = list(map(int, input_string.split()))

    # Find the lonely integer
    result = lonelyinteger(a)

    # Print the result to the console
    print(result)
