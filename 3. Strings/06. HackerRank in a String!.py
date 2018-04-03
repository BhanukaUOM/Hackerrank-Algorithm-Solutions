t = int(input())
hack = "hackerrank"

for _ in range(t):
    s = input()
    c = 0
    
    for i in s:
        if i == hack[c]:
            c+=1
        if c==len(hack):
            break
        
    print("YES" if c==len(hack) else "NO")
