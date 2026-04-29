from collections import deque
def bfs(r,c):
    q =deque([(r,c)])
    visited[r][c] = True

    while q:
        curr_x, curr_y = q.popleft()
        
        dir  = [(0, 1),(1,0),(-1,0),(0,-1)]
        for dx ,dy in dir:
            nx, ny = curr_x + dx, curr_y + dy
            if 0<= nx < N and 0<= ny < M:
                if grid[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] =True
                    q.append((nx,ny))

T = int(input())
for t in range(1, T+1):
    M, N, K = map(int,input().split())
    grid = [[0]*M for _ in range(N)]
    
    for _ in range(K):
        y, x = map(int,input().split())
        grid[x][y] = 1
    cnt = 0  
    visited = [[False]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if grid[i][j] == 1 and not visited[i][j]:
                bfs(i,j)
                cnt += 1
    print(cnt)