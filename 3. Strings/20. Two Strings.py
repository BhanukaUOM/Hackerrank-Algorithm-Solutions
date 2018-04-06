from collections import Counter as c

t = int(input())

for _ in range(t):
    s1 = set(input())
    s2 = set(input())
    
    if len(s1 & s2)==0:
        print("NO")
    else:
        print("YES")
