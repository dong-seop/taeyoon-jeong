# https://www.acmicpc.net/problem/10799

string = input()
stack = []
result=0
for i,c in enumerate(string):
	if c=='(':
		stack.append('(')
	else:
		stack.pop()
		if string[i-1]=='(':
			result+=len(stack)
		else:
			result+=1
print(result)
