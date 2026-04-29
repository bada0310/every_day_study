# 1. 격자 위의 편안한 상태

n, m = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.

board = [[0]*n for _ in range(n)]


dx = [0, 1, 0 , -1]
dy = [1, 0, -1, 0]
for i in range(m):
    answer = 0
    r = points[i][0] - 1
    c = points[i][1] - 1
    if board[r][c] == 0: # 
        board[r][c] = 1
        count = 0
        for k in range(4):
            nr = r + dx[k]
            nc = c + dy[k]
            if 0<= nr < n and 0<= nc <n:
                if board[nr][nc] == 1:
                    count += 1
        
        if count  == 3:
            answer = 1 # 편안한 상태 
    print(answer)



                    
                

    
    

