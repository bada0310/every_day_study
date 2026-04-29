from collections import deque
N ,M = map(int,input().split())
grid = [list(map(int,input())) for _ in range(N)]
visited= [[[0]*2 for _ in range(M)] for _ in range(N)] #dist and visited check # x, y, 거리 

def bfs(r,c):
    q = deque([(r,c,0)])
    visited[r][c][0] = 1
    
    while q:
        curr_x, curr_y, broken = q.popleft()
        dx, dy = [0,1,0,-1],[1,0,-1,0]
        if curr_x == N-1 and curr_y == M-1:
            return visited[curr_x][curr_y][broken] # val 은 거리 
        
        for i in range(4):
            nx, ny = curr_x + dx[i], curr_y + dy[i]
            if 0<= nx < N and 0<= ny < M:
                if grid[nx][ny] == 0 and visited[nx][ny][broken] == 0: # no wall 
                    visited[nx][ny][broken] = visited[curr_x][curr_y][broken] +1 
                    q.append((nx, ny, broken))
                        
                elif grid[nx][ny] == 1 and broken == 0 and visited[nx][ny][1] == 0: # yes wall + no broken
                    visited[nx][ny][1] = visited[curr_x][curr_y][broken] +1 
                    q.append((nx, ny, 1))
    return -1

print(bfs(0,0))