n = int(input())
s = input()
r = int(input())%26

for i in s:
    if i.isupper():
        print(chr(ord(i)+r) if ord(i)<=ord('Z')-r else chr(ord('A')+r-(ord('Z')+1-ord(i))), end="")
    elif i.islower():
        print(chr(ord(i)+r) if ord(i)<=ord('z')-r else chr(ord('a')+r-(ord('z')+1-ord(i))), end="")
    else:
        print(i, end="")
