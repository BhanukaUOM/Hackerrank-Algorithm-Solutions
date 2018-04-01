from math import *

t = input()
for _ in range(t):
    a, b = map(int, input().split(' '))
    
    a = ceil(sqrt(a))
    b = floor(sqrt(b))
    
    print int(b-a) + 1
