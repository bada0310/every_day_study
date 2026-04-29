# 2804
# 크로스워드 만들기
# 단어 A= 가로 배열 , B= 세로 배열 
# A 와 B 가 일치하는 '철자'를 찾음 >  그 열에 따라 B를 배열 
# > 그 행에 따라 A를 배열(A는 B 몇번째 단어인지 따라 영향받아 배열 )

A, B = map(str, input().split())  # BANANA PIDZAMA
n, m = len(A), len(B) # int
matrix = [['.']*n for _ in range(m)] 
for i in range(n):
    if A[i] in B:
        row = i
        col = B.index(A[i])
        break
    
for i in range(m):
    matrix[i][row] = B[i] # row 를 B로 바꾸기
for i in range(n):
    matrix[col][i] = A[i] # col 을 A로 바꾸기 
    
for i in matrix:
    print(''.join(i))