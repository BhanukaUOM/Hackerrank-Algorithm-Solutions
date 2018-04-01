n = int(input())
arr = list(map(int, input().split(' ')))

c = -1
i = 0

while i < n:
    if i < n-2 and arr[i+2] == 0: i += 1
    c += 1
    i += 1
    
print(c)
