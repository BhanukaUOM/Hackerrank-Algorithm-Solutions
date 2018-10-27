#!/bin/pyth
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    x = (int(n / 3)) * 3
    y = 0
    while True:
        y = n - x
        if ((int(y / 5)) * 5 != y):
            if (x == 0):
                print("-1")
                break
            x = (int((x - 1) / 3)) * 3
        else:
            print (int(x) * "5" + int(y) * "3")
            break
