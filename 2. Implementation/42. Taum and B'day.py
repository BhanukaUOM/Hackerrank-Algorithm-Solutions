t = int(input())

for _ in range(t):
    b, w = map(int, input().split(' '))
    Cb, Cw, Cc = map(int, input().split(' '))
    if Cb+Cc<Cw:
        print(Cb*b + (Cb+Cc)*w)
    elif Cw+Cc<Cb:
        print(Cw*w + (Cw+Cc)*b)
    else:
        print(Cw*w + Cb*b)
