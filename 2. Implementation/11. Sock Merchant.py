from collections import Counter

n = int(input())
arr = list(map(int, input().split(' ')))

c = Counter(arr)

res = 0

for i in c:
    res += c[i]//2
print(res)
