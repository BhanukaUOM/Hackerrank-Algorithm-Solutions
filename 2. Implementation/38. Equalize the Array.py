from collections import Counter

n = int(input())
arr = list(map(int, input().split(' ')))

print(n - Counter(arr).most_common(1)[0][1])
