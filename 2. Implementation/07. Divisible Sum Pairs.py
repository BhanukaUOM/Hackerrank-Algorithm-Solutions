n, k = map(int, input().split(' '))
arr = list(map(int, input().split(' ')))

count = 0
m = [0 for _ in range(k)]

for i in range(n):
    m[arr[i]%k] += 1    
    
count+=(m[0] * (m[0]-1)) //2

for i in range(1, (k+1)//2):
    count += m[i] * m[k-i]

if k%2==0:
    count += (m[k//2] * (m[k//2]-1)) //2
    
print(count)

"""
The idea is that you separate elements into buckets depending on their mod k. For example, you have the elements: 
1 3 2 6 4 5 9 and k = 3

   mod 3 == 0 : 3 6 9
   mod 3 == 1 : 1 4
   mod 3 == 2 : 2 5

Now, you can make pairs like so: Elements with mod 3 == 0 will match with elements with (3 - 0) mod k = 0, so other elements in the mod 3 == 0 list, like so:

(3, 6) (3, 9) (6, 9)

There will be n * (n - 1) / 2 such pairs, where n is length of the list, because the list is the same and i != j. Elements with mod 3 == 1 will match with elements with (3 - 1) mod k = 2, so elements in the mod 3 == 2 list, like so:

(1, 2) (1, 5) (4, 2) (4, 5)

There will be n * k such elements, where n is the length of the first list, and k of the second.

Because you don't need to print the actual pairs, you need to store only the number of elements in each list.
"""
