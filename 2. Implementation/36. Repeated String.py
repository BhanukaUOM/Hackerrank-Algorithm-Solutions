str = input()
n = int(input())

print ((n//len(str)) * str.count('a') + str[0:n%len(str)].count('a'))
