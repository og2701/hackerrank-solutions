#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    print('Weird' if n%2!=0 or (n>=6 and n<=20) else 'Not Weird')
