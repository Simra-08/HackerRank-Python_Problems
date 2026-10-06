# Hackerrank Problem : Bill Division
# Description  : To check the divided bill, and produce the excess charge
# if overpriced 

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bonAppetit' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY bill
#  2. INTEGER k
#  3. INTEGER b
#

def bonAppetit(bill, k, b):
    new_bill = list(bill)
    new_bill.remove(new_bill[k])
    
    
    
    count = 0
    for i in new_bill:
        count += i
        
    actual_price = count/2
    
    if actual_price == b:
        print("Bon Appetit")
    else:
        print(int((b-actual_price)))  
        
    
    
    
        
if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
