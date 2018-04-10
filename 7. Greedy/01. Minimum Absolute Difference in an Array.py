n = int(input())
arr = list(map(int, input().split(' ')))
arr.sort()

mini = 999999
for i in range(n-1):
    mini = min(mini, abs(arr[i]-arr[i+1]))
    
print(mini)
