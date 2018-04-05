t = int(input())

for _ in range(t):
    n = input()
    
    beautiful = False
    
    i=1
    while i<len(n):
        k = 0
        last = -1
        j = 0
        while j<len(n):
            s = n[j:j+i+k]
            if j==0:
                first = s
            if s[0] == '0' or (last+1 != int(s) and last != -1):
                break
            if int(s)%9 ==0 and (int(s)+1) % 10 == 0:
                k += 1
                j -= 1
            last = int(s)
            
            if j+i+k>=len(n):
                beautiful = True  
                F = first
            j += i+k
        i+=1
            
    print("YES " + F if beautiful else "NO")
