n = int(input())
arr = list(map(int, input().split(' ')))

while min(arr)<1000:
    c = 0
    m = min(arr)
    for i in range(n):
        if arr[i]<2000:
            c+=1
        if arr[i] - m == 0:
            arr[i] = 999999
        arr[i] -= m
    print(c)
