t = int(input())

for _ in range(t):
    n, m = map(int, input().split(' '))
    arr = []
    for _ in range(n):
        arr.append(list(input()))
    
    sn, sm = map(int, input().split(' '))
    a = []
    for _ in range(sn):
        a.append(list(input()))
    ans = True
    
    for i in range(n-sn):
        if ans:
            for j in range(m-sm):
                if a == [arr[z][j:j+sm] for z in range(i,i+sn)]:
                    print("YES")
                    ans = False
                    break
    if ans:
        print("NO")
