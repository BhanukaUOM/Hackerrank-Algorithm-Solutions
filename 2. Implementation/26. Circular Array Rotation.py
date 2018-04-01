n, m, t = map(int, input().split(' '))
arr = list(map(int, input().split(' ')))

for _ in range(t):
    p = int(input())
    print(arr[(p+n-m)%n])
