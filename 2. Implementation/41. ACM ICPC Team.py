n, m = map(int, input().split(' '))
arr = []

max = 0
count = 0

for _ in range(n):
    arr.append(int(input(), 2))

for i in range(n):
    for j in range(i+1, n):
        if (bin(arr[i] | arr[j])).count('1') == max:
            count += 1
            
        elif (bin(arr[i] | arr[j])).count('1') > max:
            max = (bin(arr[i] | arr[j])).count('1')
            count = 1
    
print (max)
print (count)
