arr = list(map(int, input().split(' ')))
str = input()

m =0

for i in str:
    m = max(arr[ord(i)-97], m)
    
print (m*len(str))
