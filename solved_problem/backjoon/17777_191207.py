# https://www.acmicpc.net/problem/17777

m = int(input())
s = list(input())
n = int(input())

for i in range (n):
	a = list(map(int, input().split()))
	temp = s[a[0]:a[1]]
	s.insert(a[2], temp)
	s = [y for x in s for y in x]
	if len(s) > M:
		#here
	print(s)
