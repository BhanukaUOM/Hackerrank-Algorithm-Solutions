import collections
import itertools

n = int(input())
str = input()

max = 0;

c = collections.Counter(str)
if(len(c)>1):
    for i in itertools.combinations(c, len(c)-2):
        s = str
        for j in i:
            s = s.replace(j, "")
        for i in range(len(s)-1):
            if s[i]==s[i+1]:
                break
            if i==len(s)-2:
                if max<len(s):
                    max = len(s)
print(max)
