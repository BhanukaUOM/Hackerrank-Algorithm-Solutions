import math

# All 3x3 Magic Squares
magic = [
             [
                 [8,1,6],
                 [3,5,7],
                 [4,9,2]
             ],
             [
                 [4,3,8],
                 [9,5,1],
                 [2,7,6]
             ],
             [
                 [2,9,4],
                 [7,5,3],
                 [6,1,8]
             ],
             [
                 [6,7,2],
                 [1,5,9],
                 [8,3,4]
             ],
             [
                 [6,1,8],
                 [7,5,3],
                 [2,9,4]
             ],
             [
                 [8,3,4],
                 [1,5,9],
                 [6,7,2]
             ],
             [
                 [4,9,2],
                 [3,5,7],
                 [8,1,6]
             ],
             [
                 [2,7,6],
                 [9,5,1],
                 [4,3,8]
             ]
        ]

arr = []
for i in range(3):
    arr.append(list(map(int, input().split(' '))))

min = 99999

for z in magic:
    c=0
    for i, j in zip(arr,z):
        for x, y in zip(i,j):
            c += int(math.fabs(x-y))
    if c<min:
        min = c
    
print (min)

#Reference: https://mindyourdecisions.com/blog/2015/11/08/how-many-3x3-magic-squares-are-there-sunday-puzzle/
