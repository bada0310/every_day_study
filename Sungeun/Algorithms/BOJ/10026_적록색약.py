# 총 보는 구역의 갯수를 구하는 문제
# 적록 색맹 X: R 구역 B 구역 G 구역 따로 봐야함 
# 적록 색맹 O: R -G 구역, B 구역 따로 봐야함
from collections import deque
dx = [0,1,0,-1]
dy = [1,0,-1,0]

def is_range(r,c):
    return 0<= r < N and 0<= c < N

def bfs_not_blind(r,c):
    q = deque([(r,c)])
    visited[r][c] = True

    while q:
        cr, cc = q.popleft()
        
        for i in range(4):
            nx, ny = cr + dx[i], cc + dy[i]
            if is_range(nx,ny) and not visited[nx][ny]:
                if grid[nx][ny] == color:
                    visited[nx][ny] = True
                    q.append((nx,ny))        

def bfs_blind(r,c):
    q = deque([(r,c)])
    visited2[r][c] = True
    while q:
        cr, cc = q.popleft()
        
        for i in range(4):
            nx, ny = cr + dx[i], cc + dy[i]
            if is_range(nx,ny) and not visited2[nx][ny]:
                if color in ('R', 'G') and grid[nx][ny] in ('R', 'G'):
                    visited2[nx][ny] = True
                    q.append((nx,ny))    
                elif color == 'B' and grid[nx][ny] == 'B':
                    visited2[nx][ny] = True
                    q.append((nx,ny)) 

N = int(input())
grid = [input() for _ in range(N)]
visited = [[False]*N for _ in range(N)]
visited2 = [[False]*N for _ in range(N)]

# global val area_cnt
area_cnt1 = 0
area_cnt2 = 0

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            color = grid[i][j]
            bfs_not_blind(i,j)
            area_cnt1 += 1
for k in range(N):
    for p in range(N):
        if not visited2[k][p]:
            color = grid[k][p]
            bfs_blind(k,p)
            area_cnt2 += 1

print(area_cnt1,area_cnt2)
