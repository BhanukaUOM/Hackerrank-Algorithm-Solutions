n =int(input())

arr = []

for _ in range(n):
    arr.append(list(input()))
    
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1 or j==n-1 or arr[i][j-1]>=arr[i][j] or arr[i][j+1]>=arr[i][j] or arr[i+1][j]>=arr[i][j] or arr[i-1][j]>=arr[i][j]:
            print(arr[i][j], end="")
        else:
            print("X", end="")
    print()
