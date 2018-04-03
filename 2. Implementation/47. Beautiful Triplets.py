n, d = map(int, input().split(' '))
arr = list(map(int, input().split(' ')))

c=0

for j in range(n):
    if arr[j]+d in arr and arr[j]+2*d in arr:
        c+=1
                
print(c)
