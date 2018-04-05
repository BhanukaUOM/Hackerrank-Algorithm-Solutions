import itertools

t = int(input())

for _ in range(t):
    n = int(input())-1
    a = int(input())
    b = int(input())
    if a>b:
        a,b = b,a

    ans = a*n
    if b==a:        
        print(ans, end=" ")
    else:
        for i in range(n+1):
            print(ans, end=" ")
            ans += b-a
    print()
