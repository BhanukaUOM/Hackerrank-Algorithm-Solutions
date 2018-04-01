n, k = map(int, input().split(' '))
arr = list(map(int, input().split(' ')))

power = 100
for i in range(0, n, k):
    power -= 1 + arr[i] * 2
    
print(power)
