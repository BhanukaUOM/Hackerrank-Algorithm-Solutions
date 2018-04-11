dp = {}

def ways(n, arr, l):
    global dp
    c = 0
    if n==0:
        return 1
    elif n>0:
        if (n,l) not in dp:
            for i in arr:
                if i>=l:
                    c += ways(n-i, arr, i)
            dp[(n,l)] = c
        return dp[(n,l)]
    else:
        return 0
    
n, m = map(int, input().split(' '))
arr = list(map(int, input().split(' ')))
print(ways(n, arr, 0))
