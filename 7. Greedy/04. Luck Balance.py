n, k = map(int, input().split(' '))

luck = 0
important = []
for _ in range(n):
    l, t = map(int, input().split(' '))
    if t==1:
        important.append(l)
    luck += l
    
important.sort(reverse=True)
for i in range(k, len(important)):
    luck -= 2*important[i]
    
print(luck)
