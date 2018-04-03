n, m = map(int, input().split(' '))
arr = list(map(int, input().split(' ')))

c = [0 for _ in range(m)]
count =0

for i in arr:
    c[i%m] += 1
    
if m%2==0:
    count += min(c[0], 1) + min(c[m//2],1)
    for i in range(1, m//2):
        count += max(c[i], c[m-i])
        
else:
    count += min(c[0], 1)
    for i in range(1, (m+1)//2):
        count += max(c[i], c[m-i])

print(count)

#ref: https://www.geeksforgeeks.org/subset-no-pair-sum-divisible-k/
