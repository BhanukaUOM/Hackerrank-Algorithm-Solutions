t = int(input())

for _ in range(t):
    n = input()
    c =0
    for i in n:
        if int(i)!=0 and int(n)%int(i)==0:
            c+=1
    print(c)
