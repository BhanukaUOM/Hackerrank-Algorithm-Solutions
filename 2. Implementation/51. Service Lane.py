n, t = map(int, input().split(' '))
arr = list(map(int, input().split(' ')))

for _ in range(t):
    s, e = map(int, input().split(' '))
    print(min(arr[s:e+1]))
