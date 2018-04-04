t = int(input())

for _ in range(t):
    s = input()
    
    c = 0
    i = 0
    j = 1
    while j < len(s):
        if abs(ord(s[i]) - ord(s[j])) != 1:
            j += 1
            c += 1
        else:
            i = j
            j += 1
    print (c)
