# Hackerrank Problem : Picking Numbers
# Description : To pickout out the max subset where the atmost difference is 1


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#


def pickingNumbers(a):
    freq = {}
    
    for i in a:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    
    max_count = 0
    for n in freq:
        count = freq[n] + freq.get(n+1,0) 
        max_count = max(max_count, count)
        
    return max_count         
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
