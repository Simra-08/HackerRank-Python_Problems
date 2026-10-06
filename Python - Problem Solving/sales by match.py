# Hackerrank Problem : Sales by Match
# Description : To find out the number of pairs that can be obtained from single
# colored sock

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    freq = {}
    
    for x in ar:
        if x in freq:
            freq[x] += 1
        else:
            freq[x] = 1
     
    count = 0       
    for key in freq:
        count += freq[key]//2
        
    return count
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
