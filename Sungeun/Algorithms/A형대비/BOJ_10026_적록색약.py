# 10026_적록색약
# R_G 

dx = [0,1,0,-1]
dy = [1,0,-1,0]
# bfs 
from collections import deque

def not_colorblind(r,c):
    q = deque([(r,c)])
    visited_not[r][c] = True

    while q:
        cur_r, cur_c = q.popleft()
        for i in range(4):
            nr, nc = cur_r + dx[i], cur_c + dy[i]
            if 0<= nr < N and 0<= nc < N:
                if not visited_not[nr][nc] and grid[nr][nc] == grid[cur_r][cur_c]:
                    visited_not[nr][nc] = True
                    q.append((nr,nc))

def colorblind(r,c):
    q = deque([(r,c)])
    visited[r][c] = True

    while q:
        cur_r, cur_c = q.popleft()
        for i in range(4):
            nr, nc = cur_r + dx[i], cur_c + dy[i]
            if 0<= nr < N and 0<= nc < N:
                if grid[cur_r][cur_c] in ['R', 'G']:
                    if not visited[nr][nc] and grid[nr][nc] in ['R', 'G']:
                        visited[nr][nc]= True
                        q.append((nr,nc))
                else:
                    if not visited[nr][nc] and grid[nr][nc] == grid[cur_r][cur_c]:
                        visited[nr][nc] = True
                        q.append((nr,nc))

N = int(input())
grid = [list(input()) for _ in range(N)]
cnt_non = 0 # non color blind
cnt = 0  # color blind 
visited_not = [[False]*N for _ in range(N)]
visited = [[False]*N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if not visited_not[i][j]:
            not_colorblind(i,j)
            cnt_non += 1

        if not visited[i][j]:
            colorblind(i,j)
            cnt += 1

print(cnt_non, cnt)
