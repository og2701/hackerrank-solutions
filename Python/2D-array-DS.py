#!/bin/python3

import math
import os
import random
import re
import sys

def hourglassSum(arr):
    results = []
    for i in range(4):
        for j in range(4):
            result = 0
            for k in range(3):
                result += arr[i][j+k]
                result += arr[i+2][j+k]
            results.append(result+arr[i+1][j+1])
    return max(results)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
