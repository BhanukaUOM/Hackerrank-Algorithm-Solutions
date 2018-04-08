n, m = map(int, input().split(' '))

arr = list(map(int, input().split(' ')))
arr.sort()

count = 0
i = 0
while i<n:
    j = i
    
    while(j<n and arr[j]<=arr[i]+m):
        j += 1
    j -= 1
    i = j
    count += 1
    
    while(i<n and arr[i]<=arr[j]+m):
        i += 1
    
print(count)
