# https://www.acmicpc.net/problem/9012

for t in range (int(input())):
	a = input()
	b = []
	for c in a:
		if c == '(':
			b.append(1)
		else:
			try:
				b.pop()
			except IndexError:
				b = "IndexError"
				print("NO")
				break
	if len(b) == 0:
		print("YES")
	elif b is not "IndexError":
		print("NO")
