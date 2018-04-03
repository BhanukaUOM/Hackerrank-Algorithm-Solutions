from math import sqrt, ceil

str = input()
n = len(str)

for i in range(ceil(sqrt(n))):
    for j in range(ceil(sqrt(n))):
        if j * ceil(sqrt(n)) + i < n:
            print(str[j * ceil(sqrt(n)) + i], end="")
    print(end=" ")
