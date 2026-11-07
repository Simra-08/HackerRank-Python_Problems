# Hackerrank Problem : Electronics Shop
# Description : To purchase the max amount of keyboard and drives to match the budget 


#!/bin/python3

import os
import sys

#
# Complete the getMoneySpent function below.
#
def getMoneySpent(keyboards, drives, b):
    
    list_1 = []
    
    list_ok = []
    
    
    for i in range (n):
        for j in range (m):
            
            list_1.append(keyboards[i]+drives[j])
            
    list_2 = sorted(list_1,reverse=True)
    
    for i in list_2:
        if i<=b:
            return i
    return -1        
            
            
    
    
    
    
            
              
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    #
    # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
    #

    moneySpent = getMoneySpent(keyboards, drives, b)

    fptr.write(str(moneySpent) + '\n')

    fptr.close()
