n = int(input())
arr = list(map(int, input().split(' ')))

arr.sort(reverse=True)
for i in range(n-2):
    if arr[i+2]+arr[i+1]>arr[i]:
        print(arr[i+2],arr[i+1],arr[i])  
        break
    if i==n-3:
        print(-1)
