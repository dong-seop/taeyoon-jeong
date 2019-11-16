# https://www.acmicpc.net/problem/9012

for t in range (int(input())):
	a = input()
	b = []
	for c in a:
		#print(c)
		if c == '(':
			b.append(1)
		else:
			if len(b) == 0:
				b.append(2)
				break
			b.pop()
	if len(b) == 0:
		print("YES")
	else:
		print("NO")
