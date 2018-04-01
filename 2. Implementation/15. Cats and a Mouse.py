t = int(input())

for _ in range(t):
    x, y, z = map(int, input().split(' '))
    print("Cat A" if abs(z - x) < abs(z - y) else "Cat B" if abs(z - x) > abs(z - y) else "Mouse C")
