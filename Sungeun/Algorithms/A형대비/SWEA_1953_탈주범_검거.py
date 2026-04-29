# swea_1953_탈주범 검거 
pipe_dict = {
    1:[0,1,2,3],
    2:[1,3],
    3:[0,2],
    4:[0,3],
    5:[0,1],
    6:[1,2],
    7:[2,3]
}

from collections import deque
dx = [0,1,0,-1] # 우 하 좌 상 
dy = [1,0,-1,0]
def bfs(r,c):
    global cnt
    q = deque([(r,c,1)])
    visited[r][c] = True
    cnt += 1
    
    while q:
        cr, cc , time = q.popleft()
        if time >= L:
            continue
        for d in pipe_dict[grid[cr][cc]]:
            nr, nc = cr + dx[d], cc + dy[d]
            if 0<= nr < N  and 0<= nc < M and not visited[nr][nc] and grid[nr][nc] != 0:
                next_pipe = grid[nr][nc]
                
                opposite_d = (d+2)%4
                
                if opposite_d in pipe_dict[next_pipe]:
                    visited[nr][nc] = True
                    q.append((nr,nc,time+1))
                    cnt += 1              

T = int(input())
for tc in range(1,T+1):
    N, M, R, C, L = map(int,input().split())
    grid = [list(map(int,input().split())) for _ in range(N)]
    visited = [[False]*M for _ in range(N)]
    cnt = 0
    bfs(R,C)
    print(f'#{tc}',cnt)