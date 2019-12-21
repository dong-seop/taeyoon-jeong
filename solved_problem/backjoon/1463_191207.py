# https://www.acmicpc.net/problem/11656

X = int(input())
dp = [X]
cnt = 0

while True:
    if 1 in dp:
        print(cnt)
        break
    calc = []
    for i in dp:
        if i % 2 == 0:
            calc.append(int(i / 2))
        if i % 3 == 0:
            calc.append(int(i / 3))
        calc.append(i - 1)
    dp = calc
    cnt += 1
