#!/bin/python3

import os
import sys


def timeConversion(s):
    am_pm = s[-2:];
    s = s.replace(am_pm,'').split(':')
    if am_pm == "PM":
        s[0] = str(24-abs(int(s[0])-12))
    s[0] = '00' if s[0] == '12' and am_pm == 'AM' else s[0]
    s[0] = '12' if s[0] == '24' and am_pm == 'PM' else s[0]
    return ':'.join(s)

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
