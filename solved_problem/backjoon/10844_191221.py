# https://www.acmicpc.net/problem/10844

n = int(input())
for i in range (10**n):
	a = str(i)
	a = list(a)
	for j in range (len(a)):
		a[j] = int(a[j])
	#print(i)
	if len(a) == n:
		pass
