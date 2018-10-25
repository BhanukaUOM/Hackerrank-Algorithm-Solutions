# Link to the problem: https://www.hackerrank.com/challenges/dynamic-programming-classics-the-longest-common-subsequence/problem

table = list()

def calculate_lcs(a, b, n, m):
	if table[n][m]:
		return table[n][m]
	tmp = list()
	if n == 0 or m == 0:
		return tmp
	if a[n] == b[m]:
		tmp.append(a[n])
		tmp.extend(calculate_lcs(a, b, n-1, m-1))
	else:
		p = calculate_lcs(a, b, n-1, m)
		q = calculate_lcs(a, b, n, m-1)
		if len(p) > len(q):
			tmp.extend(p)
		else:
			tmp.extend(q)
	table[n][m] = tmp[:]
	return tmp

def main():
	global table
	n, m = list(map(int, input().strip().split()))
	for i in range(n+1):
		tmp = list()
		for j in range(m+1):
			tmp.append(0)
		table.append(tmp)
	a = [None] + list(map(str, input().strip().split()))
	b = [None] + list(map(str, input().strip().split()))
	res = calculate_lcs(a, b, n, m)
	res.reverse()
	print(' '.join(res))

if __name__ == '__main__':
	main()