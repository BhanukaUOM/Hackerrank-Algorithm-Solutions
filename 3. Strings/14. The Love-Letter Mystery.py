t = int(input())

for _ in range(t):
    s = input()
    n = len(s)
    
    c = 0
    for i in range(n//2):
        c += abs(ord(s[i]) - ord(s[n-i-1]))
    
    print(c)
