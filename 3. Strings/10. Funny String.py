t = int(input())

for _ in range(t):
    s = input()
    n = len(s)
    
    for i in range(n-1):
        if abs(ord(s[i])-ord(s[i+1])) != abs(ord(s[n-i-1])-ord(s[n-i-2])):
            print("Not Funny")
            break
        if i==n-2:
            print("Funny")
