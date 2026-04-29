# CTR_등산로 공사
# 깎을때 조건 확인필요
# 가장 높은 봉우리들은 깎을 수 없다 .
# 깎을 수 있는 높이 조절 가능 
# 깎아도 grid[nr][nc] 의 옾이는 적어도 1이상이어야 한다. (0 이면 안됌)

N , K = map(int,input().split())
grid = [list(map(int,input().split())) for _ in range(N)]
top = max(max(row) for row in grid)
highest = []
for i in range(N):
    for j in range(N):
        if grid[i][j] == top:
            highest.append((i,j))

# 가장 최고봉 찾기 
dx = [0,1,0,-1]
dy = [1,0,-1,0]
max_dist = 0
visited = [[False]*N for _ in range(N)]
def dfs(r,c,K,D):
    global max_dist
    max_dist = max(max_dist,D)

    for i in range(4):
        nr, nc = r + dx[i], c + dy[i]
        if 0<= nr < N and 0<= nc < N and not visited[nr][nc]:
            if grid[nr][nc] < grid[r][c]:
                visited[nr][nc] = True
                dfs(nr,nc,K,D+1)
                visited[nr][nc] = False

            elif K > 0: # 땅을 팠을 때
                if (nr,nc) not in highest:
                    depth = max(0,grid[nr][nc] -grid[r][c] + 1)
                    if depth <= K and grid[nr][nc]-depth >= 1:  # 최소 높이 1 
                        ori_height = grid[nr][nc]
                        
                        grid[nr][nc] -= depth
                        visited[nr][nc] = True

                        dfs(nr,nc,K-depth,D+1)
                        visited[nr][nc] = False
                        grid[nr][nc] = ori_height

for hr, hc in highest:
    visited[hr][hc] = True
    dfs(hr,hc,K,1) # 시작점도 1로 계산 
    visited[hr][hc] =False

print(max_dist)
