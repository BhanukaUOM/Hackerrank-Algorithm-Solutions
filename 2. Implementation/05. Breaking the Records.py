n = int(input())
arr = list(map(int, input().split(' ')))

max = arr[0]
min = arr[0]
maxc=0
minc=0

for i in arr:
    if i>max:
        maxc += 1
        max = i
    if i<min:
        minc += 1
        min = i
print(maxc, minc)
