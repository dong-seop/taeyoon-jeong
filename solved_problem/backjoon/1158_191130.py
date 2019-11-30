# https://www.acmicpc.net/problem/1158

from queue import Queue

n, k = list(map(int,input().split()))
a = Queue()
r = Queue()
cnt = 0

for i in range (n):
	a.put(i+1)

while a.qsize() > 1:
	if cnt == k-1:
		r.put(a.queue[0])
		del a.queue[0]
		cnt = 0
	else:
		a.put(a.queue[0])
		del a.queue[0]
		cnt += 1
r.put(a.queue[0])

print("<", end='')
for i in range(r.qsize()-1):
	print(r.queue[i], end='')
	print(", ", end='')
print(r.queue[-1], end='')
print(">", end='')
