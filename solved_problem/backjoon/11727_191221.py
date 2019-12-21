n = int(input())
a = [1]
for i in range (n-1):
	if i % 2 == 0:
		a.append(a[i] * 2 + 1)
	else:
		a.append(a[i] * 2 - 1)
print(a[len(a)-1] % 10007)
