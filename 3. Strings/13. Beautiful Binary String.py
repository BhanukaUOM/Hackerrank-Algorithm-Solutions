n = int(input())
s = input()

c = 0
i = 0
while i<len(s)-2:
    if s[i:i+3] == "010":
        c += 1
        i += 2
    i += 1
    
print (c)
