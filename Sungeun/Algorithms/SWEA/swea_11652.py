from collections import deque
def bfs(x, y, grid, visited):
    q = deque([(x,y,0)])
    visited[x][y] = True
    while q: 
        x, y, count = q.popleft()
        for dx,dy in [(0,1),(1,0),(-1,0),(0,-1)]:
            nx, ny = x + dx , y + dy
            if 0<= nx < N and 0<= ny < N:
                if grid[nx][ny] == '3':
                    return count
                if not visited[nx][ny] and grid[nx][ny] == '0':
                    visited[nx][ny] = True
                    q.append((nx,ny, count+1))
    return 0
        
T = int(input())
for t in range(1, T+1):
    N = int(input())
    grid = [list(input()) for _ in range(N)]
    visited = [[False]* N for _ in range(N)]
    
    found = False
    for r in range(N):
        for c in range(N):
            if grid[r][c] == '2': 
                found = True
                break
        if found:
            break
    
    answer = bfs(r, c, grid, visited)
    print(f'#{t}',answer)
     