n = int(input())
for i in range(n):
    p = int(input())
    #print(p%5)
    if p%5>2 and p>37:
        print(p+(5-p%5))
    else:
        print(p)
