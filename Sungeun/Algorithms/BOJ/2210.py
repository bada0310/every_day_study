# 조건 파악 
# 5*5 크기의 숫자판 (0~9)
# 나올수 있는 모든 가짓수를 고려해야함 > dfs


def dfs(r,c,curr_str,cnt):
    if cnt == 6: # pruning
        result.add(curr_str)
        return
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    
    for i in range(4):
        nx, ny = r +dx[i], c +dy[i]
        if 0<= nx < 5 and 0<= ny < 5:
            dfs(nx,ny,curr_str + str(grid[nx][ny]), cnt + 1)
            
            
grid = [list(map(int,input().split())) for _ in range(5)]
result = set()
for i in range(5):
    for j in range(5):
        dfs(i, j, str(grid[i][j]), 1)
print(len(result))