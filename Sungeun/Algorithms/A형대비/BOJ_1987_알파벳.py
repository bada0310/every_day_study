#1987_알파벳 

N, M = map(int,input().split())
grid = [input() for _ in range(N)]


visited = [[False]*M for r_ in range(N)]

# dfs ?-> 기록을 확인해야하니 dfs 가 맞음  bfs? -> 최단 거리 일때 
dx = [0,1,0,-1]
dy = [1,0,-1,0]
max_cnt = 0 # max 
past = set([grid[0][0]])
def dfs(r,c,cnt):
    global max_cnt
    max_cnt = max(max_cnt, cnt)

    for i in range(4):
        nr, nc = r + dx[i], c + dy[i]

        if 0<= nr < N and 0<= nc < M:
            if grid[nr][nc] not in past:
                past.add(grid[nr][nc])
                dfs(nr,nc,cnt+1)
                past.remove(grid[nr][nc])
    return max_cnt

dfs(0,0,1)
print(max_cnt)