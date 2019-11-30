# https://www.acmicpc.net/problem/10866

deque = []

for i in range (int(input())):
	command = list(input().split())
	#print(deque) #

	# push_front X
	if command[0] == 'push_front':
		deque = [command[1]] + deque

	# push_back X
	if command[0] == 'push_back':
		deque.append(command[1])

	# pop_front
	if command[0] == 'pop_front':
		try:
			print(deque[0])
			del deque[0]
		except IndexError:
			print(-1)

	# pop_back
	if command[0] == 'pop_back':
		try:
			print(deque[-1])
			del deque[-1]
		except IndexError:
			print(-1)

	# size
	if command[0] == 'size':
		print(len(deque))

	# empty
	if command[0] == 'empty':
		if len(deque) == 0:
			print(1)
		else:
			print(0)

	# front
	if command[0] == 'front':
		try:
			print(deque[0])
		except IndexError:
			print(-1)

	# back
	if command[0] == 'back':
		try:
			print(deque[-1])
		except IndexError:
			print(-1)
