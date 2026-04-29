N, M = map(int,input().split())
edges = [tuple(map(int, input().split())) for _ in range(M)]
grid = [[0]*M for _ in range(N)]

for x, y in edges:
    grid[x-1][y-1] = 5 # 0-based
dirs = [(1,0),(0,1),(0,-1)] # 좌우 반전은 존재 계속 하강 
def is_range(r,c):
    return 0<= r< N or 0<= c < M

def dfs(x, y):
    nx, ny = x + 1, y
    if is_range(nx,ny) and grid[nx][ny] ==5:
        if ny != N-1:
            ny = ny+1 # 대부분은 우하향으로 이동 
        elif ny == N-1: 
            ny = ny-1 # 오른쪽 벽일때만 고려
                
            
