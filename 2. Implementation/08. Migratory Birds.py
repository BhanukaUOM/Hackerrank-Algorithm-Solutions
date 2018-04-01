n = int(input())
arr = list(map(int, input().split(' ')))
counter = [0 for _ in range(n)]

for i in arr:
    counter[i] += 1

print(counter.index(max(counter)))
