#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthday function below.
def birthday(s, d, m):
    solutions = 0
    total = 0
    if len(s) == 1 and s[0] == d:
        return 1
    for i in range(0, (len(s) + 1) - m):
        for j in range(i, i+m):
            total += s[j]
        if total == d:
            solutions += 1
        total = 0
    return solutions

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
