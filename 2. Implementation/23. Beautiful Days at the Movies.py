s, e, d = map(int, input().split(' '))

c = 0
for i in range(s,e+1):
    if (i-int(str(i)[::-1]))%d==0:
        c+=1

print (c)
