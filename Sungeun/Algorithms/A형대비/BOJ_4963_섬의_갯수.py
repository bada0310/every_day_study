# 4963_섬의 갯수 
# bfs
dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]

from collections import deque
def island(r,c):
    q = deque([(r,c)])
    visited[r][c] = True

    while q:
        cur_r, cur_c = q.popleft()
        for i in range(8):
            nr, nc = cur_r + dx[i], cur_c + dy[i]
            if 0<= nr < N and 0<= nc <M and grid[nr][nc] == 1 and not visited[nr][nc]:
                visited[nr][nc]= True
                q.append((nr,nc))
while True:
    # line = input().split()
    # if not line: break
    
    M, N = map(int,input().split()) #너비 # 높이
    if M == 0 and N == 0:
        break

    grid = [list(map(int,input().split())) for _ in range(N)]
    visited = [[False]*M for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(M):
            if grid[i][j] == 1 and not visited[i][j]:
                island(i,j)
                cnt += 1
    print(cnt)


