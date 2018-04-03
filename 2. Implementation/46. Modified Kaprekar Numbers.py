s = int(input())
e = int(input())

c =0

if s<=1:
    print(1, end=" ")
    c+=1

if s<=9:
    print(9, end=" ")
    c+=1

for i in range(max(s,10), e+1):
    p = i*i
    pstr = str(p)
    
    if i == int(pstr[0:len(pstr)//2]) + int(pstr[len(pstr)//2:]):
        print(i, end=" ")
        c+=1
if c==0:
    print("INVALID RANGE")
