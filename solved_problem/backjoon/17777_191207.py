# https://www.acmicpc.net/problem/17777

import sys

m = int(sys.stdin.readline())
s = list(sys.stdin.readline())
n = int(sys.stdin.readline())


a = sys.stdin.readlines()
for i in range (n):
	a[i] = a[i].split()

for i in range (n):
	temp = s[int(a[i][0]):int(a[i][1])]
	s.insert(int(a[i][2]), temp)
	s = [y for x in s for y in x]
	if len(s) > m:
		s = s[0:m]
	#print(s)
for i in range(len(s)):
    print(s[i], end='')
