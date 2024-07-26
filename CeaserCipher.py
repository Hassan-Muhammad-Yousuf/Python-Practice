#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    result = ""
   
    for char in s:
        if char.islower():  # For lowercase letters
            new_char = chr((ord(char) - ord('a') + k) % 26 + ord('a'))
            result += new_char
        elif char.isupper():  # For uppercase letters
            new_char = chr((ord(char) - ord('A') + k) % 26 + ord('A'))
            result += new_char
        else:  # For non-alphabetic characters
            result += char

    return result
    

if __name__ == '__main__':
    n = int(input().strip())
    s = input().strip()
    k = int(input().strip())
    
    result = caesarCipher(s, k)
    print(result)
