x1, v1, x2, v2 = map(int, input().split(' '))
for i in range(100000):
    if x1==x2:
        print("YES")
        break
    x1+=v1
    x2+=v2
    if i==99999:
        print("NO")
