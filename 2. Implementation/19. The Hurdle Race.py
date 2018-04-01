n, k = map(int, input().split(' '))
arr = list(map(int, input().split(' ')))

print ("0" if max(arr)-k<=0 else max(arr)-k)
