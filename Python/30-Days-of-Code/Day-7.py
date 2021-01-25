#!/bin/python3

import math
import os
import random
import re
import sys

def reverseList(arr):
    return arr[::-1]

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    print(' '.join(str(i) for i in reverseList(arr)))
