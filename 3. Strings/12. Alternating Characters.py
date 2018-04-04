t = int(input())

for _ in range(t):
    s = input()
    
    c = 0
    for i in range(len(s)-1):
        if abs(ord(s[i]) - ord(s[i+1])) != 1:
            c += 1
    print (c)
