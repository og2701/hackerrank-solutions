#!/bin/python3

import math
import os
import random
import re
import sys
import itertools


def miniMaxSum(arr):
    results = []
    for i in itertools.combinations(arr,len(arr)-1):
        results.append(sum(i))
    print(str(min(results))+' '+str(max(results)))
    
    
    
if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
