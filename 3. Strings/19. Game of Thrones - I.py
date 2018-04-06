from collections import Counter as c

s = input()

count = c(s)
odd = 0

for i in count:
    if count[i]%2==1:
        odd += 1
        
if (len(s)%2==0 and odd==0) or (len(s)%2==1 and odd==1):
    print("YES")
else:
    print("NO")
