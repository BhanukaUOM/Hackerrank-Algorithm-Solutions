#!/bin/python3

import math
import os
import random
import re
import sys
#import numpy as np
# Complete the findMedian function below.
def findMedian(arr):
    arr.sort()
    if((len(arr)%2)!=0):
        x=len(arr)//2
        return(arr[x])
    else:
        x=arr[len(arr)//2]+arr[(len(arr)//2)+1]
        return x/2
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = findMedian(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
