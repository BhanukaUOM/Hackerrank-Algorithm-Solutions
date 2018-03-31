n, k = map(int, input().split(' '))
arr = list(map(int, input().split(' ')))

count = 0
m = [0 for _ in range(k)]

for i in range(n):
    m[arr[i]%k] += 1    
    
count+=(m[0] * (m[0]-1)) //2

for i in range(1, (k+1)//2):
    if i != k-1:
        count += m[i] * m[k-i]

if k%2==0:
    count += (m[k//2] * (m[k//2]-1)) //2
    
print(count)
