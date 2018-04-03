s = input()
counter = [0 for i in range(26)]

for i in s:
    if i.isalpha():
        counter[ord(i.lower())-ord('a')] += 1

print("not pangram" if 0 in counter else "pangram")
