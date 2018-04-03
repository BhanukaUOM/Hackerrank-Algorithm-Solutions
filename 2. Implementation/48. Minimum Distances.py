n = int(input())
arr = list(map(int, input().split(' ')))

m = 99999

for i in range(n):
    for j in range(i+1, n):
        if arr[i] == arr[j]:
            m = min(j-i, m)
            
print(-1 if m==99999 else m)
