# Samsung SW Academy
# Problem no.2001 (파리퇴치)
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PzOCKAigDFAUq&categoryId=AV5PzOCKAigDFAUq&categoryType=CODE


for t in range(int(input())):
    n, m = list(map(int,input().split()))
    pari = [[0]*n for j in range(n)]
    for i in range(n):
        temp = list(map(int,input().split()))
        for j in range(n):
             pari[i][j] = temp[j]
    pari_ = [[0]*n for j in range(n)]
    pari_[0][0] = pari[0][0]
    for i in range(n-1):
        pari_[0][i+1] = pari_[0][i] + pari[0][i+1]
    for i in range(n-1):
        pari_[i+1][0] = pari_[i][0] + pari[i+1][0]
    for i in range(n-1):
        for j in range(n-1):
            pari_[i+1][j+1] = pari_[i][j+1] + pari_[i+1][j] - pari_[i][j] + pari[i+1][j+1]
    #print(pari_)

#pari는 해당 칸의 파리의 개수
#pari_는 해당 칸을 포함하여 왼쪽 위에 있는 모든 칸의 파리 합

    max = 0
    for i in range(m-1, n):
        for j in range(m-1, n):
            if i == m-1 and j == m-1:
                #print("a")
                max = pari_[i][j]
            elif i == m-1 and j > m-1:
                #print("b")
                if max < pari_[i][j] - pari_[i][j-m]:
                    max = pari_[i][j] - pari_[i][j-m]
            elif i > m-1 and j == m-1:
                #print("c")
                if max < pari_[i][j] - pari_[i-m][j]:
                    max = pari_[i][j] - pari_[i-m][j]
            else:
                #print("d")
                if max < pari_[i][j] - pari_[i-m][j] - pari_[i][j-m] + pari_[i-m][j-m]:
                    max = pari_[i][j] - pari_[i-m][j] - pari_[i][j-m] + pari_[i-m][j-m]

    print("#" + str(1+t) + " " + str(max))
