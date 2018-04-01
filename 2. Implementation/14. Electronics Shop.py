n, k, m = map(int, input().split(' '))
keyboard = list(map(int, input().split(' ')))
mouse = list(map(int, input().split(' ')))


max = -1
for i in mouse:
    for j in keyboard:
        if i+j<=n and i+j>max:
            max = i+j
    
print(max)
