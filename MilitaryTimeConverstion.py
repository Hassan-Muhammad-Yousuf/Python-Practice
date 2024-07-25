#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    if (s[-2:] == "AM"): 
        if (s[:2] == "12"):
            return "00" + s[2:-2]
        else:
            return s[:-2]
    else:
        h = int(s[:2])
        if (h<12):
            h += 12
        return str(h)+s[2:-2]

if __name__ == '__main__':
    # Safely get output path from environment variable or use a default
    output_path = os.environ.get('OUTPUT_PATH', 'output.txt')

    # Read the input time string
    s = input().strip()

    # Convert time
    result = timeConversion(s)

    # Write the result to the output file
    with open(output_path, 'w') as fptr:
        fptr.write(result + '\n')

    # Print the result to the console (for local testing)
    print(result)
