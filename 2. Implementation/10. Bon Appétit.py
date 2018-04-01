n, k = map(int, input().split(' '))
arr = list(map(int, input().split(' ')))
b = int(input())

print("Bon Appetit" if b-(sum(arr)-arr[k])//2==0 else b-(sum(arr)-arr[k])//2)
