import math

t = int(input())
for _ in range(t):
    c=0
    s, e = map(int, input().split(' '))
    s = math.ceil(math.sqrt(s))
    for i in range(s, e):
        if i*i>e:
            break
        c+=1
            
    print(c)
