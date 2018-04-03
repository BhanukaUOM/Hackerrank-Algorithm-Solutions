s = input()
sos = ['S', 'O', 'S']

c = 0
for i in range(len(s)):
    if s[i] != sos[i%3]:
        c += 1
        
print(c)
