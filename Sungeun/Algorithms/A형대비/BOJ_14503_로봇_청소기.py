# 14503_로봇청소기 
# 반시계 방향으로 90 도 돈다 
# 1은벽 
N, M = map(int,input().split())
r, c, dir = map(int,input().split())
grid = [list(map(int,input().split())) for _ in range(N)]
visited = [[False]*M for _ in range(N)]
# dirs = [(-1,0),(0,1),(1,0),(0,-1)] # 북 동 남 서 
dx = [-1,0,1,0]
dy = [0,1,0,-1]

total_clean = 0
def dfs(r,c,d):
    global total_clean
    if grid[r][c] == 0 and not visited[r][c]:
        visited[r][c] = True
        total_clean += 1

    for _ in range(4):
        d = (d + 3) %4
        nr, nc = r + dx[d], c + dy[d]
            
        if 0<= nr < N and 0<= nc < M:
            if grid[nr][nc] == 0 and not visited[nr][nc]:
                dfs(nr,nc,d)
                return
            
    br, bc = r-dx[d], c-dy[d]
    if 0<= br < N and 0<= bc < M and grid[br][bc] != 1:
        dfs(br,bc,d)
    else:
        return

dfs(r,c,dir)
print(total_clean)
