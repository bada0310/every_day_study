# 최대한 많은 core 를 연결했을때, 전선 길이의 합을 구하고자 한다 

dir = [(0,1),(1,0),(-1,0),(0,-1)]
def is_range(r,c):
    return 0<= r < N and 0<= c < N

def dfs(idx,core_cnt,length):
    global max_core, min_length

    if idx ==len(core): #prunning 
        if core_cnt > max_core:
            max_core = core_cnt
            min_length = length
        elif core_cnt == max_core:
            min_length = min(min_length, length)
        return
    x, y = core[idx]
    for dx, dy in dir:
        nx, ny = x, y
        cnt = 0
        is_possible = True




T = int(input())
for tc in range(1,T+1):
    N = int(input())
    grid = [list(map(int,input().split())) for _ in range(N)]
    core = []
    max_core = 0
    min_length = float('inf')

    for i in range(1,N-1):
        for j in range(1,N-1):
            if grid[i][j] == 1:
                core.append((i,j))
    dfs(0,0,0)


