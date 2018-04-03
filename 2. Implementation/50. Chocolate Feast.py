for _ in range(int(input())):
    n, c, m = map(int, input().split(' '))
    chocs = n // c
    wraps = chocs
    while wraps >= m:
        chocs += wraps//m
        wraps = wraps//m + wraps%m
    print (chocs)

 """
    Only 1 output worng among all cases?
    Case No. 5, input string is "43203 60 5", my output is "892", right answer is "899" I just want to make sure whether there is a mistake at your end. Kindly check, I've checked plenty of time, If not Kindly explain the case? Much appreciaited.

    #ans:
    43203 / 60 = 720 chocolates ( 3 dollars left and you cannot buy any more chocolate for 3 dollar ) 

    720 / 5 = 144 chocolates ( we can buy 144 chocolates from 720 wrappers ) 

    144 / 5 = 28 chocolates ( we can buy 28 chocolates from 144 wrappers, 4 wrappers left ) 

    (28 + 4 ) / 5 = 6 ( 28 wrappers + 4 wrappers left from 144, we can buy 6 chocolates ) 

    (6 + 2) / 5 = 1 ( 6 wrappers + 2 wrappers left from 32 wrappers, we can buy 1 chocolate ) 


    This sums to 720 + 144 + 28 + 6 + 1 = 899.

"""
