#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    s_lst = list(s)
    
    if (s_lst[0].isalpha()) and (s_lst[0].islower()):
        s_lst[0] = s_lst[0].upper()
    
    for i in range(len(s_lst) - 1):
        if (not s_lst[i].isalnum()) and (s_lst[i + 1].isalpha()) and (s_lst[i + 1].islower()):
            s_lst[i + 1] = s_lst[i + 1].upper()
    return "".join(s_lst)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
