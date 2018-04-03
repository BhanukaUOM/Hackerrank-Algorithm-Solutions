n = int(input())
arr = list(map(int, input().split(' ')))

c = 0
for i in range(n-1):
    if arr[i]%2!=0:
        arr[i] += 1
        arr[i+1] += 1
        c += 2

if arr[n-1]%2==0:
    print(c)
else:
    print("NO")
