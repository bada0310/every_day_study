# 2667_단지번호 붙이기 
# BFS
from collections import deque

N = int(input())
grid = [list(map(int,input().strip())) for _ in range(N)]

# bfs
visited = [[0]*N for _ in range(N)] # 번호 붙여야하기때문에 0 으로 check 
num = 1 # 붙일 번호 (단지 묶음 갯수 )
ans = [] 

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def bfs(r,c):
    visited[r][c] = num
    q = deque([(r,c)])
    count = 1 
    
    while q: 
        cur_r, cur_c= q.popleft()

        for i in range(4):
            nr, nc = cur_r + dx[i], cur_c + dy[i]
            if 0<= nr < N and 0<= nc < N and visited[nr][nc] == 0 and grid[nr][nc]==1:
                visited[nr][nc] = num
                q.append((nr,nc))
                count += 1
    return count 

for i in range(N):
    for j in range(N):
        if grid[i][j] == 1 and visited[i][j] == 0:
            size = bfs(i,j)
            ans.append(size)
            num += 1
ans.sort()
print(len(ans))
for i in ans:
    print(i)
