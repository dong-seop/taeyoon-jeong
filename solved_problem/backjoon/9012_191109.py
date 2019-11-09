# https://www.acmicpc.net/problem/9012

for t in range(int(input())):
	ps = input()
	if ps.count('(') == ps.count(')'):
		print("YES")
	else:
		print("NO")
