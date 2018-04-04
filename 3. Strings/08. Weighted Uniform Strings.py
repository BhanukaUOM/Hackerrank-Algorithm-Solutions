s = input()
t = int(input())

c = {}
count = 0
prev =''

for i in s:
    if i==prev or prev=='':
        count += 1
    else:
        if prev not in c or c[prev]<count:
            c[prev] = count
        count = 1
    prev = i
       
if prev not in c or c[prev]<count:
        c[prev] = count
        
arr = []
for k, v in c.items():
    for i in range(v):
        arr.append((i+1)*(ord(k)-ord('a')+1))
        
for _ in range(t):
    n = int(input())
    if n in arr:
        print("Yes")
    else:
        print("No")
