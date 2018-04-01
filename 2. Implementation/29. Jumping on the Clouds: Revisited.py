n, k = map(int, input().split(' '))
arr = list(map(int, input().split(' ')))

power = 100
for i in range(0,n,k):
    power -= 1
    if arr[i]==1:
        power -= 2
print(power)
