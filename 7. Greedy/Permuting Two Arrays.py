#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the twoArrays function below.
def twoArrays(k, A, B):
    A.sort()
    B=sorted(B,reverse=True)
    x=0

    

    for i in range  (len(A)):
        if A[i]+B[i]>=k:
            x=x+1
            
    if x==len(A):
        return "YES"
    else:
        return "NO"
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        A = list(map(int, input().rstrip().split()))

        B = list(map(int, input().rstrip().split()))

        result = twoArrays(k, A, B)

        fptr.write(result + '\n')

    fptr.close()
