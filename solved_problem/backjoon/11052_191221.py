# https://www.acmicpc.net/problem/11052

n = int(input())
pick = 0
pay = 0
remaining_cards = n

price = list(map(int,input().split()))
efficiency = []
for i in range (n):
	efficiency.append(price[i]/(i+1))

while (remaining_cards != 0):
	m = max(efficiency)
	for i in range(len(price)):
		if efficiency[i] == m:
			pick = i + 1

	if pick <= remaining_cards:
		pay += price[pick-1]
		remaining_cards -= pick
	else:
		del price[pick-1]
		del efficiency[pick-1]

print(pay)
