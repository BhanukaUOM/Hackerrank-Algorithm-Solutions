t = int(input())
for _ in range(t):
    n, k = map(int, input().split(' '))
    arr = list(map(int, input().split(' ')))
    arr.sort()
    
    print("YES" if arr[k-1]>0 else "NO")
