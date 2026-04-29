#  answer = 첫 줄에 빙산이 분리되는 최초의 시간(년)
# bfs
# 시물레이션 + 그래프 탐색 
from collections import deque

N ,M  = map(int,input().split())
grid = [list(map(int,input().split())) for _ in range(N)]
dir =  [(0,1),(1,0),(-1,0),(0,-1)]
time = 0
 
while True:
    visited =[[False]*M for _ in range(N)]
    chunk = 0 # 덩어리 
    
    for i in range(N):
        for j in range(M):
            if grid[i][j] >0 and not visited[i][j]:
                chunk += 1
                # bfs
                q = deque([(i,j)])
                visited[i][j] = True
                
                while q:
                    x, y = q.popleft()
                    for dx, dy in dir:
                        nx,ny = x + dx , y + dy
                        if 0<= nx < N and 0<= ny < M:
                            if grid[nx][ny] > 0 and not visited[nx][ny]:
                                visited[nx][ny] = True
                                q.append((nx,ny))
    # 분기점 
    if chunk >= 2:
        print(time)
        break
    if chunk == 0:
        print(0)
        break

    to_melt = []
    for i in range(N):
        for j in range(M):
            if grid[i][j] > 0:
                sea_cnt = 0
                for dx, dy in dir:
                    nx, ny = i +dx, j + dy
                    if 0<= nx < N and 0<= ny < M:
                        if grid[nx][ny] == 0:
                            sea_cnt += 1
                            
                if sea_cnt >0:
                    to_melt.append((i,j, sea_cnt))
                    
    for i, j, d in to_melt:
        grid[i][j] -= d
        if grid[i][j] < 0:
            grid[i][j] = 0 # 음수면 0으로 보정
            
    # one cycle over 
    time += 1

