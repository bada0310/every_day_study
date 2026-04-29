#17070_파이프 옮기기 
# dir = [(0,1),(1,0),(1,1)]
N = int(input())
grid = [list(map(int,input().split())) for _ in range(N)]
cnt  = 0

def dfs(r,c,dir):
    global cnt 
    if r == N-1 and c == N-1:
        cnt += 1
        return
    if dir == 0 or dir == 2:
        if c+1 < N and grid[r][c+1]==0:
            dfs(r,c+1,0)
    if dir == 1 or dir == 2:
        if r + 1 < N and grid[r+1][c] == 0:
            dfs(r+1,c,1)
    if r+1 < N and c+1 < N:
        if grid[r+1][c+1] == 0 and grid[r][c+1] == 0 and grid[r+1][c]==0:
            dfs(r+1, c+1, 2)

if grid[0][1] == 0:
    dfs(0,1,0)
print(cnt)