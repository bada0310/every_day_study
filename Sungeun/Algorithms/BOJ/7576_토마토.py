# 7576_토마토 
import sys
input = sys.stdin.readline
from collections import deque

M, N = map(int,input().split())
grid = [list(map(int,input().split())) for _ in range(N)]
# visited = [[False]*M for _ in range(N)]
# 최소 시간 -> bfs

def bfs(start_node):
    max_days = 0
    q = deque(start_node)
    
    while q:
        curr_x , curr_y, d= q.popleft()
        max_days = d

        dir = [(0,1),(1,0),(-1,0),(0,-1)]
        for dx, dy in dir:
            nx, ny = curr_x + dx , curr_y + dy
            if 0<= nx < N and 0<= ny < M:
                if grid[nx][ny] == 0:
                    grid[nx][ny] = grid[curr_x][curr_y] + 1
                    q.append((nx,ny,d+1)) 
                                  
    for row in grid:
        if 0 in row:
            return -1
    return max_days 

tomatoes = [] 
for i in range(N):
    for j in range(M):
        if grid[i][j] == 1:
            tomatoes.append((i, j, 0))
print(bfs(tomatoes))