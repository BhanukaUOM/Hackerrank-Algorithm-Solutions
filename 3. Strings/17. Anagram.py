t = int(input())

for _ in range(t):
    s = input()
    n = len(s)
    
    if n%2!=0:
        print(-1)
    else:
        c = 0
        c1 = [0 for i in range(26)]
        c2 = [0 for i in range(26)]

        for i in s[:n//2]:
            c1[ord(i)-ord('a')] += 1
         
        for i in s[n//2:]:
            c2[ord(i)-ord('a')] += 1
        
        for i in range(26):
            if c1[i]>c2[i]:
                c += c1[i]-c2[i]
                
        print(c)
