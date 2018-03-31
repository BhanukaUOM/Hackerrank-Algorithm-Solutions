#!/bin/python3

import os
import sys

#
# Complete the countApplesAndOranges function below.
#
def countApplesAndOranges(s, t, a, b, apples, oranges):
    print(sum([1 for x in apple if (x + a) >= s and (x + a) <= t]))
    print(sum([1 for x in orange if (x + b) >= s and (x + b) <= t]))

if __name__ == '__main__':    st = input().split()
    s = int(st[0])
    t = int(st[1])
    ab = input().split()
    a = int(ab[0])
    b = int(ab[1])
    mn = input().split()
    m = int(mn[0])
    n = int(mn[1])
    apple = list(map(int, input().rstrip().split()))
    orange = list(map(int, input().rstrip().split()))
    countApplesAndOranges(s, t, a, b, apple, orange)
