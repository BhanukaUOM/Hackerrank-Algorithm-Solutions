def pairs(a,k):
    answer = 0
    s = set(a)
    for v in s:
        if v+k in s:
            answer += 1
    return answer
n,k = map(int, input().split())
b = [int(x) for x in input().split()]
print(pairs(b, k))
