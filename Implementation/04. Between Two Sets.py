n = input()
a = list(map(int, input().split(' ')))
b = list(map(int, input().split(' ')))
count=0
res=0

for num in range(max(a), min(b)+1):
    count=0
    
    for i in a:
        if num%i==0:
            count+=1
            
    for i in b:
        if i%num==0:
            count+=1
            
    if count==len(a)+len(b):
        res+=1
        
print(res)
