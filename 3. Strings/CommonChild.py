# Link to the problem: https://www.hackerrank.com/challenges/common-child/problem

def commonChild(s1, s2, n):
    prev_lcs = [0]*(n+1)
    curr_lcs = [0]*(n+1)
    for c1 in s1:
        curr_lcs, prev_lcs = prev_lcs, curr_lcs
        for i, c2 in enumerate(s2, 1):
            curr_lcs[i] = (
                1 + prev_lcs[i-1] if c1 == c2
                else max(prev_lcs[i], curr_lcs[i-1])
                )
    return curr_lcs[-1]


s1 = input().strip()
s2 = input().strip()
n = len(s1)
result = commonChild(s1, s2, n)
print(result)