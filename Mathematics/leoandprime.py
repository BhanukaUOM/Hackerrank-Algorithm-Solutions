#https://www.hackerrank.com/challenges/leonardo-and-prime/problem
def gcd(a,b):
	if b==0:
		return a
	return gcd(b,a%b)
q=int(input())
for i in range(0,q):
	n=int(input())
	if n<2:
		print(0)
		continue
	prod=int(1)
	ans=int(0)
	for j in range(2,n+1):
		if gcd(prod,j)==1:
			prod*=j
			if prod<=n:
				ans+=1
			else:
				break
	print(ans)
