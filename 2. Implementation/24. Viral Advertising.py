n = int(input())

if n==1:
    print(2)
else:
    ans = 2
    count = 2
    for i in range(n-1):
        ans = (ans * 3) // 2
        count += ans
print (count)
