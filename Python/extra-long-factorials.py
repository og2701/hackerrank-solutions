#!/bin/python3

import math
import os
import random
import re
import sys

def extraLongFactorials(n):
    factorial = 1
    for i in range(1,n+1):
        factorial = factorial * i
    print(factorial)
if __name__ == '__main__':
    n = int(input())

    extraLongFactorials(n)
