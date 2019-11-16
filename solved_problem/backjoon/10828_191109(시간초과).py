# https://www.acmicpc.net/problem/10828

stack = []
for t in range(int(input())):
	#print(stack)
	command = input().rstrip().split(" ")

	if len(command) == 1:

		if command[0] == 'pop':
			if len(stack) != 0:
				k = stack[-1:]
				print(k[0])
				stack.pop()
			else:
				print("-1")

		elif command[0] == 'size':
			print(len(stack))

		elif command[0] == 'empty':
			if len(stack) == 0:
				print("1")
			else:
				print("0")

		elif command[0] == 'top':
			if len(stack) != 0:
				k = stack[-1:]
				print(k[0])
			else:
				print(-1)

	else:
		if command[0] == 'push':
			stack.append(command[1])
