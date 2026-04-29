# 입력받는법 
n, m = map(int,input().split()) # row = n col = m
matrix_a = [list(map(int,input().split())) for _ in range(n)] 
matrix_b = [list(map(int,input().split())) for _ in range(n)]

matrix_total = [[matrix_a[i][j] + matrix_b[i][j] for j in range(m)] for i in range(n)]
#이 함수 로직 풀이
# matrix_total = matrix_a + matrix_b
# matrix_total = []
# for i in range(n):
#     row = []
#     for j in range(m):
#         row.append(matrix_a[i][j] + matrix_b[i][j])
#     matrix_total.append(row) 

# 출력 부분
for row in  matrix_total:
    print(*row)

# 풀이 2 zip()
# result = [[c+d for c, d in zip(a,b)] for a, b in zip(grid1, grid2)]
	# 모든 행렬의 원소에 대해서 같은 index에 위치한 원소들을 더한다 
	# 2중 for문으로 엮인 부분을 zip(a, b) 로 묶어서 
	