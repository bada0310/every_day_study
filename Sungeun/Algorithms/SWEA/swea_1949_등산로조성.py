from collections import deque
# dfs ->> is_range(r,c) 필수 
def is_range(r,c):
    return 0<= r < N and 0<= c< N
 
def dfs(r,c,chance, length):
    global max_length
    max_length = max(max_length, length)
 
    dir = [(0,1),(1,0),(0,-1),(-1,0)]
    for dx, dy in dir:
        nx, ny = r + dx, c + dy
        if is_range(nx,ny) and not visited[nx][ny]:
 
            if grid[nx][ny] < grid[r][c]: #낮은길
                visited[nx][ny] = True
                dfs(nx,ny, chance,length + 1)
                visited[nx][ny] = False
 
            elif chance == 1 and grid[nx][ny] -K < grid[r][c]:
                visited[nx][ny] = True
                ori_top = grid[nx][ny]
                grid[nx][ny] = grid[r][c] -1
 
                dfs(nx,ny,0,length+1)
                visited[nx][ny] = False
                grid[nx][ny] = ori_top
             
         
T = int(input())
 
for t in range(1,T+1):
    N , K = map(int,input().split())
    grid = [list(map(int,input().split())) for _ in range(N)]
    top = max(max(row) for row in grid)
    visited = [[False]*N for _ in range(N)] 
 
    highest = []
    for i in range(N):
        for j in range(N):
            if grid[i][j] == top:
                highest.append((i,j))
 
    max_length =0
    for hr, hc in highest:
        visited[hr][hc] = True
        dfs(hr, hc, 1, 1) # chance -= 1
        visited[hr][hc] =False # 백트래킹 
    print(f'#{t}', max_length)