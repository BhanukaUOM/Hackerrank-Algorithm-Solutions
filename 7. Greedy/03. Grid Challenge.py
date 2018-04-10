def Solution(arr, n):
    arr[0].sort()
    for i in range(1, n):
        arr[i].sort()
        for j in range(n):
            if arr[i][j]<arr[i-1][j]:
                return "NO"
    return "YES"

            
t = int(input())

for _ in range(t):
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(list(input()))
    
    print(Solution(arr, n))
    
        
