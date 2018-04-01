n = int(input())
arr = list(map(int, input().split(' ')))

counter = [0 for i in range(101)]
max = 0

for i in arr:
    counter[i] += 1
    
for i in range(98):
    if counter[i]+counter[i+1]>max:
        max = counter[i]+counter[i+1]
    
print (max)
