# https://www.acmicpc.net/problem/17777

m = int(input())
s = list(input())
n = int(input())

import sys

for i in range (n):
	a = map(int, sys.stdin.readline())
	temp = s[a[0]:a[1]]
	s.insert(a[2], temp)
	s = [y for x in s for y in x]
	if len(s) > m:
		s = s[0:m]
	#print(s)
for i in range(len(s)):
    print(s[i], end='')
