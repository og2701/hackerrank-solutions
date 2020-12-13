#!/bin/python3

import math
import os
import random
import re
import sys
from bisect import bisect_left


def longestIncreasingSubsequence(arr):
    x=[0 for i in range(len(arr)+1)]
    x[0] = arr[0]
    length = 1
    for i in range(1,len(arr)):
        if arr[i] < x[i]:
            x[0] = arr[i]
        
        elif arr[i] > x[length-1]:
            x[length] = arr[i]
            length += 1
        
        else:
            a = bisect_left(x[:length],arr[i])
            x[a] = arr[i]
            
    return length
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    result = longestIncreasingSubsequence(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
