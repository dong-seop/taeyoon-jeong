# https://www.acmicpc.net/problem/10799

a = input()
a = list(a)
res = 0

for i in range(len(a)-1):
	#print(a[i:])
	if len(a[i:]) <= 1:
		break
	elif a[i] == '(' and a[i+1] == ')':
		a[i] = 'q'
		del a[i+1]

#print(a)
while '(' in  a:
	if a[-1] == 'q':
		del a[-1]
	if a[1] == 'q':
		del a[1]

	else:
		stack = []
		for i in range (len(a)):
			#print()
			#print(a)
			#print(stack)
			#print()
			if a[i] == '(':
				stack.append('(')
			elif a[i] == ')':
				stack.pop()
				if len(stack) == 0:
					res += 1
					for j in range (1, i):
						if a[j] == 'q':
							res += 1
					del a[i], a[1]
					break
	#print(a)
print(res)
