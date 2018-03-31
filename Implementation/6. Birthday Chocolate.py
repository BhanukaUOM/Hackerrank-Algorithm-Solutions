n = int(input())
s = [int(x) for x in input().split()]
assert n == len(s)
d, m = map(int, input().split())

r = 0
if n >= m:
    a = sum(s[:m])
    if a == d:
        r += 1
    for j in range(m, n):
        a += s[j] - s[j-m]
        if a == d:
            r += 1
print(r)
