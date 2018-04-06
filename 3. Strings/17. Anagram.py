from collections import Counter as c

t = int(input())

for _ in range(t):
    s = input()
    n = len(s)
    
    if n%2!=0:
        print(-1)
    else:                
        print(sum((c(s[:n//2])-c(s[n//2:])).values()))
