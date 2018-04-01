n = int(input())
str = input()

count = 0
res = 0

for i in str:
    if i=="U":
        count += 1
        if count==0:
            res+=1
    if i=="D":
        count -= 1
        
print (res)
