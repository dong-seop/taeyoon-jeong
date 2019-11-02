# Samsung SW Academy
# Problem no.1974 (스도쿠 검증)
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PzOCKAigDFAUq&categoryId=AV5PzOCKAigDFAUq&categoryType=CODE

n = int(input())
for i in range(n):
    cnt = 0
    sudoku = [[0]*9 for j in range(9)]
    for j in range(9):
        temp = list(map(int,input().split()))
        for k in range(9):
             sudoku[j][k] = temp[k]



    mult = 1
    for j in range(9):
        for k in range(9):
            mult *= sudoku[j][k]
        if mult != 362880:
            cnt += 1
        mult = 1
        #print("cnt = " + str(cnt))



    mult = 1
    for j in range(9):
        for k in range(9):
            mult *= sudoku[k][j]
        if mult != 362880:
            cnt += 1
        mult = 1
        #print("cnt = " + str(cnt))



    mult = 1
    for h in range(1, 8, 3):
        for w in range(1, 8, 3):
            for j in range(h-1, h+2):
                for k in range(w-1, w+2):
                    mult *= sudoku[j][k]
            if mult != 362880:
                cnt += 1
            mult = 1
        #print("cnt = " + str(cnt))



    if cnt == 0:
        print("#" + str(i+1) + " 1")
    else:
        print("#" + str(i+1) + " 0")
