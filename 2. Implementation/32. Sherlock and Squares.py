from math import *

t = int(input())
for _ in range(t):
    a, b = map(int, input().split(' '))
    
    a = ceil(sqrt(a))
    b = floor(sqrt(b))
    
    print (int(b)-int(a) + 1)
