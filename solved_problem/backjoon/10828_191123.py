# https://www.acmicpc.net/problem/10828

import sys

n = sys.stdin.readline()
cmds = sys.stdin.readlines()
stack =[]

size = 0
for cmd in cmds:
    cmd = cmd.rstrip()
    if cmd =='size':
        print(size)
    elif cmd=='pop':
        try:
            print(stack.pop())
            size-=1
        except:
            print('-1')
    elif cmd=='top':
        if(size):
            print(stack[size-1])
        else:
            print('-1')
    elif cmd=='empty':
        if size:
            print('0')
        else:
            print('1')
    else:
        stack.append(int(cmd.split()[1]))
        size+=1
