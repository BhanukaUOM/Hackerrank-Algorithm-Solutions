n = input()
if n[8]=='A':
    if n[0:2] == '12':
        print("00", end="")
        print(n[2:8])
    else:
        print(n[0:8])
else:
    if n[0:2] == '12':
        print("12", end="")
        print(n[2:8])
    else:
        print(12+int(n[0:2]), end="")
        print(n[2:8])
