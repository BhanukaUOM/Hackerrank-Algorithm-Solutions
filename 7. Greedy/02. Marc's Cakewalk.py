n = int(input())
arr = list(map(int, input().split(' ')))

arr.sort(reverse=True)

res = 0
for i in range(n):
    res += arr[i]*2**i
    
print(res)
