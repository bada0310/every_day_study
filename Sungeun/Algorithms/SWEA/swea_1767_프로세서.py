# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV4suNtaXFEDFAUf

dir = [(0,1),(1,0),(-1,0),(0,-1)]

def is_range(x,y):
    return 0<= x < N and 0<= y < N

def dfs(idx, core_cnt, length):
    global max_core, min_length
    # 모든 코어를 다 탐색했다면 return 
    if idx == len(cores):
        if core_cnt > max_core:
            max_core = core_cnt
            min_length = length
        elif core_cnt == max_core:
            min_length = min(min_length,length)
        return
    
    x, y = cores[idx]
    for dx, dy in dir:
        nx, ny = x, y
        cnt = 0
        is_possible = True
        
        while True:
            nx += dx
            ny += dy
            if not is_range(nx,ny):
                break
            if grid[nx][ny] != 0: # 이미 전선이 깔려져 있으면 
                is_possible = False 
                break
            cnt += 1
    
        if is_possible:
            fill_x, fill_y = x,y 
            for _ in range(cnt):
                fill_x += dx
                fill_y += dy
                grid[fill_x][fill_y] = 2
            
            dfs(idx+1, core_cnt+1, length+cnt)
            fill_x, fill_y = x, y
            for _ in range(cnt):  # back tracking 
                fill_x += dx
                fill_y += dy
                grid[fill_x][fill_y] = 0 
                 
    dfs(idx+1, core_cnt, length)            

T = int(input())

for t in range(1,T+1):
    N = int(input())
    grid = [list(map(int,input().split())) for _ in range(N)]
    cores = []
    max_core = 0 # count max_core
    min_length = float('inf') # total min_length 
    
    for i in range(1,N-1):
        for j in range(1,N-1):
            if grid[i][j] == 1:
                cores.append((i,j))
    
    dfs(0,0,0)
    print(f'#{t}',min_length)