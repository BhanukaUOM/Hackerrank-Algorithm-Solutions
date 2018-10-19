n = int(input())
s = [int(x) for x in input().split()]
assert n == len(s)
d, m = map(int, input().split())

count = 0
for i in range(0,n):
    total = sum(s[i:m+i])
    if total == d:
        count+=1
 
print(count)
