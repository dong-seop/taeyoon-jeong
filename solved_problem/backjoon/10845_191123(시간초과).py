# https://www.acmicpc.net/problem/10845

#import sys
# n = sys.stdin.readline()
# cmds = sys.stdin.readlines()

a = []
for i in range(int(input())):
	b = list(input().split())
	
	if b[0] == 'push':
		a.append(b[1])

	elif b[0] == 'pop':
		try:
			print(a[0])
			del a[0]
		except IndexError:
			print(-1)

	elif b[0] == 'size':
		print(len(a))

	elif b[0] == 'empty':
		if len(a) == 0:
			print(1)
		else:
			print(0)

	elif b[0] == 'front':
		try:
			print(a[0])
		except IndexError:
			print(-1)

	elif b[0] == 'back':
		try:
			print(a[len(a) - 1])
		except IndexError:
			print(-1)
