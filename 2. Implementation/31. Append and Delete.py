s = input()
t = input()
k = int(input())

commonLength = 0;
      
for i in range(min(len(s), len(t))):
    if s[i]==t[i]:
        commonLength+=1
    else:
        break

if (len(s) + len(t) - 2 * commonLength) > k:
    print("No")

elif (len(s) + len(t) - 2 * commonLength) % 2 == k % 2:
    print("Yes")


elif (len(s) + len(t) - k) < 0:
    print("Yes")

else:
    print("No")
