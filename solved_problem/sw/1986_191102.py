# Samsung SW Academy
# Problem no.1986 (지그재그 숫자)
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PzOCKAigDFAUq&categoryId=AV5PzOCKAigDFAUq&categoryType=CODE

t = int(input())
for i in range (t):
	n = int(input())
	if n % 2 == 1:
		n = (n+1)/2
	else:
		n = (n/2)*-1
	print("#" + str(i+1) + " " + str(int(n)))
  
