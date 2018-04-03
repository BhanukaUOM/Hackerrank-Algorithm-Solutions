for _ in range(int(input())):
    n, c, m = map(int, input().split(' '))
    chocs = n // c
    wraps = chocs
    while wraps >= m:
        chocs += wraps//m
        wraps = wraps//m + wraps%m
    print (chocs)
