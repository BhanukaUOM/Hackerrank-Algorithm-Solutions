time = int(input())

value = 3
while time > value:
    time -= value
    value *= 2

print(value - time + 1)
