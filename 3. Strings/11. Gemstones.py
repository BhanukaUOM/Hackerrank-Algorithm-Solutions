t = int(input())

last = set(input())
for _ in range(t-1):
    last = set(input()).intersection(last)
    
print(len(last))    
