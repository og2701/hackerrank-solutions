#!/bin/python3

import math
import os
import random
import re
import sys

def diagonalDifference(arr):

    x = len(arr)
    l2r = sum(arr[i][i] for i in range(x))
    r2l = sum(arr[i][-i+x-1] for i in range(x))
    return abs(l2r-r2l)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
