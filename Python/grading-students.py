#!/bin/python3

import math
import os
import random
import re
import sys

def gradingStudents(grades):
    results = []
    for i in grades:
        if i >= 38 and i%5 > 2:  
            results.append(i+1 if i%5==4 else i+2)
        else:
            results.append(i)
            
    return results

        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
