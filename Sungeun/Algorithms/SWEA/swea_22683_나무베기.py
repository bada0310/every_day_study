# 벽뿌2 와 유사해보임
# 전진 좌 우
# 나무 베면  '.' 

from collections import deque
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(r,c):
    global end_x, end_y, min_move 
    q = deque([(r,c,0,0)])
    visited[r][c][0][0] = 1
    
    while q: 
        curr_x, curr_y, curr_dir, broken = q.popleft()
        
        if curr_x == end_x and curr_y == end_y:
            return visited[curr_x][curr_y][curr_dir][broken]-1
        # next_dirs = [curr_dir, (curr_dir+1)%4, (curr_dir+3)%4] # go right left 
        
        left_dir = (curr_dir +3)%4 # left
        if visited[curr_x][curr_y][left_dir][broken] ==0:
            visited[curr_x][curr_y][left_dir][broken] = visited[curr_x][curr_y][curr_dir][broken] + 1
            q.append((curr_x, curr_y, left_dir, broken))
        
        right_dir = (curr_dir + 1)%4 # right
        if visited[curr_x][curr_y][right_dir][broken] ==0:
            visited[curr_x][curr_y][right_dir][broken] = visited[curr_x][curr_y][curr_dir][broken] + 1
            q.append((curr_x, curr_y, right_dir, broken))
            
        nx, ny = curr_x +dx[curr_dir], curr_y+dy[curr_dir]
        
        if 0<= nx <N and 0<= ny < N:
            #not broke
            if grid[nx][ny] != 'T' and visited[nx][ny][curr_dir][broken] ==0:
                visited[nx][ny][curr_dir][broken] = visited[curr_x][curr_y][curr_dir][broken] + 1
                q.append((nx,ny,curr_dir,broken))
        
            # broke 
            elif grid[nx][ny] == 'T' and broken < K and visited[nx][ny][curr_dir][broken+1] == 0:
                visited[nx][ny][curr_dir][broken+1] = visited[curr_x][curr_y][curr_dir][broken] + 1
                q.append((nx, ny, curr_dir, broken+1))
    return -1        
                
        # for nd in next_dirs:
        #     nx, ny = curr_x +dx[nd], curr_y+dy[nd]
        #     if 0<= nx <N and 0<= ny < N:
        #         if grid[nx][ny] != 'T' and visited[nx][ny][nd][broken] ==0:
        #             visited[nx][ny][nd][broken] = visited[curr_x][curr_y][curr_dir][broken] + 1
        #             q.append((nx,ny,nd,broken))
        #         elif grid[nx][ny] == 'T' and broken < K and visited[nx][ny][nd][broken+1] ==0:
        #             visited[nx][ny][nd][broken+1] = visited[curr_x][curr_y][curr_dir][broken] + 1 # broke
        #             q.append((nx,ny,nd,broken+1))        
    
T = int(input())
for tc in range(1,T+1):
    N, K = map(int,input().split()) # 필드의 크기 N과 나무를 벨 수 있는 횟수 K
    grid = [input().strip() for _ in range(N)]
    visited = [[[[0]*(K+1) for _ in range(N)] for _ in range(N)] for _ in range(N)] # grid, dir, broke 
    min_move = 0 # 최소조작 
    
    for i in range(N):
        for j in range(N):
            if grid[i][j] == 'X':
                start_x, start_y = i, j
            elif grid[i][j] == 'Y':
                end_x, end_y = i, j
    ans = bfs(start_x, start_y)
    print(f'#{tc}',ans)
            