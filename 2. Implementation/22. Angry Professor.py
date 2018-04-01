t = int(input())
for _ in range(t):
    n, k = map(int, input().split(' '))
    arr = list(map(int, input().split(' ')))
    
    c = 0
    for i in arr:
        if i<=0:
            c+=1
    print("YES" if c<k else "NO")
