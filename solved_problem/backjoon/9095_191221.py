# https://www.acmicpc.net/problem/9095

for i in range (int(input())):
	n = int(input())
	a = [1, 2, 4]
	for i in range (n-1):
		a.append(a[i] + a[i+1] + a[i+2])
	print(a[len(a)-3])
