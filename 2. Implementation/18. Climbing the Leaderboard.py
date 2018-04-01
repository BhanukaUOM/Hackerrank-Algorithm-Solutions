n = int(input().strip())
scores = list(set(map(int, input().strip().split(' '))))

m = int(input().strip())
alice = list(map(int, input().strip().split(' ')))

scores.append(0)
l = len(scores)

for a in alice:
    while (l > 0) and (a >= scores[l-1]):
        l -= 1
    print(l+1)
