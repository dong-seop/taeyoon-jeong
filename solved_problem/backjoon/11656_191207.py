a = input()
b = []
for i in range (len(a)):
	b.append(a)
	a = a[1:1001]
b.sort()
for i in range (len(b)):
	print(b[i])
