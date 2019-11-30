# https://www.acmicpc.net/problem/10845

import sys

n = sys.stdin.readline()
cmds = sys.stdin.readlines()
a = []
size = 0

for cmd in cmds:
	cmd = cmd.rstrip()
	#print(a)

	if cmd == 'pop':
		try:
			print(a[0])
			del a[0]
			size -= 1
		except IndexError:
			print(-1)

	elif cmd == 'size':
		print(size)

	elif cmd == 'empty':
		if size:
			print(0)
		else:
			print(1)

	elif cmd == 'front':
		try:
			print(a[0])
		except IndexError:
			print(-1)

	elif cmd == 'back':
		try:
			print(a[len(a) - 1])
		except IndexError:
			print(-1)

	else:
		#print(cmd)
		a.append(int(cmd.split()[1]))
		size+=1
		
