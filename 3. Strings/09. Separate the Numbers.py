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

    
    """ 
    Best:
    
    Our approach is to use brute force. We'll begin with the first, smallest number that can be made from the input string. We'll see if the next number that can be made from the input string is one greater than it, and if it is we'll create the next number in the sequence and again compare it. If at any moment our sequence fails to meet the conditions necessary we'll start back over at the beginning of the input string and create a new beginning to the sequence using a larger first number.
"""
