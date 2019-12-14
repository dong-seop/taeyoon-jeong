# https://www.acmicpc.net/problem/11655

a = input()
a = list(a)
for i in range (len(a)):
	a[i] = ord(a[i])
for i in range (len(a)):
	if 65 <= a[i] <= 90 or 97 <= a[i] <= 122:
		a[i] += 13
		if 91 <= a[i] <= 104 or 123 <= a[i]:
			a[i] -= 26
for i in range (len(a)):
	a[i] = chr(a[i])
	print(a[i], end='')
