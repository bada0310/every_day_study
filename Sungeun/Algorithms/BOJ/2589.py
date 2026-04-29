# 4방 + 이웃한 육지 = BFS 
# visited 배열을 [0]*N for _ in range(M)으로 받아서 거리 계산도 한번에 
# global val = max_dist 
from collections import deque
def is_range(r,c):
    return 0<= r < N and 0<= c < M
def bfs(curr_dist,r,c):
    global max_dist
    visited = [[False]*M for _ in range(N)]
    q = deque([(curr_dist,r,c)])
    visited[r][c] = True
    
    while q:
        curr_dist, cx, cy = q.popleft() # pruning
        if curr_dist >= max_dist:
            max_dist = curr_dist
        
        # dir = [(0,1),(1,0),(-1,0),(0,-1)]
        dx = [0,1,0,-1]
        dy = [1,0,-1,0]
        
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if is_range(nx,ny) and grid[nx][ny] == 'L' and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((curr_dist+1, nx,ny))
    
                
            
            
N, M = map(int,input().split())
grid = [input() for _ in range(N)]
max_dist = 0
for i in range(N):
    for j in range(M):
        if grid[i][j] == 'L':
            bfs(0,i,j)
            
print(max_dist)
