n, m = map(int, input().split(' '))
arr = list(map(int, input().split(' ')))
arr.sort()

max = arr[0]

if n-arr[m-1]-1>max:
    max = n-arr[m-1]-1

for i in range(m-1):
    if (arr[i+1]-arr[i])//2 > max:
        max = (arr[i+1]-arr[i])//2
        
print(max)
