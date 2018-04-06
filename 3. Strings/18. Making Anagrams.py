s1 = input()
s2 = input()

c1 = [0 for i in range(26)]
c2 = [0 for i in range(26)]
c = 0

for i in s1:
    c1[ord(i)-ord('a')] += 1
    
for i in s2:
    c2[ord(i)-ord('a')] += 1

for i in range(26):
    c += abs(c1[i]-c2[i])

print(c)
