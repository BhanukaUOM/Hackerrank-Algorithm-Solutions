n, k = map(int, input().split(' '))
arr = list(map(int, input().split(' ')))

count = 0
page = 1

for i in arr:
    for j in range(1, i+1):
        if(page == j):
            count += 1
        if ((j % k == 0 ) or j == i):
            page += 1
        
print(count)
